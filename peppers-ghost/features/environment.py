import behave_webdriver
import os

def before_all(context):
    headless = os.getenv('HEADLESS', 'false').lower() == 'true'
    context.behave_driver = behave_webdriver.Chrome(headless=headless)

def after_all(context):
    context.behave_driver.quit()