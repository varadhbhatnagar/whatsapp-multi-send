from selenium import webdriver
from time import sleep
from welper.util import get_project_root
from os import sep
from loguru import logger
from datetime import datetime
from selenium.common.exceptions import WebDriverException
from typing import Iterator

driver = webdriver.Firefox()
logger.info('Web driver created')


def launch_whatsapp_web() -> bool:
    """
    Launches WhatsApp Web
    :return: True if succeeds, False otherwise
    """
    driver.get("https://web.whatsapp.com")
    logger.info("Waiting for whatsapp web to load")
    sleep(12)
    for attempt in range(0, 3):
        try:
            script_path = str(
                get_project_root()) + sep + 'wapi.js'
            with open(script_path, 'r') as script_file:
                script = script_file.read()
            driver.execute_script(script)
            sleep(15)  # in order to let javascript object get ready
            logger.info('Connected to Web.WhatsApp: Success')
            return True
        except:
            logger.info('Connecting to Web.WhatsApp: Attempt #' +
                        str(attempt) + ' failed')
            sleep(20)
            continue
    return False

def send_text_message(contact: str, msg: str) -> bool:
    """
    :param msg: text message to send
    :param contact: contact to send the message to
    """
    contact = str(contact) + '@c.us'
    try:
        driver.execute_script(
            ''' window.WAPI.sendMessageToIDUnknown(arguments[0], arguments[1]) ''',
            contact, msg)
        return True
    except WebDriverException as we:
        logger.critical("Failed to send message to contact " + we.msg)
        return False