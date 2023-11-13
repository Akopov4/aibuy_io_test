from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from behave import fixture, use_fixture


class WebdriverManager:
    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.driver = None

    def get_webdriver_instance(self):
        if self.browser_name.lower() == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif self.browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox(GeckoDriverManager.install())
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")
        return self.driver

    def quit(self):
        if self.driver is not None:
            self.driver.quit()





def before_all(context,scenario):
    browser_name = getattr(context, 'browser', 'chrome')
    context.web_driver_manager = WebdriverManager(browser_name)
    context.browser = context.web_driver_manager.get_webdriver_instance()
    context.browser.maximize_window()
    context.browser.get('https://aibuy.io/')

def after_all(context):
    context.browser.quit()