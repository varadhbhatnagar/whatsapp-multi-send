from flask import Flask, flash, redirect, render_template, request
from welper.web_interface import send_text_message
from welper import web_interface
from loguru import logger

app = Flask(__name__)

logger.add("logs/wappy_{time}.log")

@app.route("/home")
def hello_world():
    return render_template('home.html')


@app.route('/form_submit', methods=['POST'])
def form_submit():
    contacts = [x.strip() for x in request.form['contacts'].split(',')]
    message = request.form['message']

    success = 0
    for contact in contacts:
        if(valid_contact(contact)):
            success += send_text_message(contact, message)
    logger.success("Sent {} Reply Messages to the User".format(success))
    return redirect('home')


def valid_contact(contact):
    return True

res = web_interface.launch_whatsapp_web()
if res:
    logger.info("Good to go!")
else:
    logger.critical(":(")