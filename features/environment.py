from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from behave import fixture, use_fixture


@fixture()
def browser(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.maximize_window()
    yield context.browser
    context.browser.quit()


@fixture()
def open_home_page(context):
    context.browser.get('https://aibuy.io/')


def before_all(context):
    use_fixture(browser,context)


def before_scenario(context,scenario):
    use_fixture(open_home_page,context)
