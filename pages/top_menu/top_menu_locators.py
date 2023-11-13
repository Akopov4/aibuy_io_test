from selenium.webdriver.common.by import By


class TopMenuLocators:
    TOP_LOGO = (By.XPATH, '//div[@data-elementor-type="header"]//img[contains(@class,"large")]')
    TOP_MENU_ITEMS = (By.XPATH, '//a[contains(@class,"ekit-menu-nav-link")]')
    TOP_MENU_ITEM = (By.XPATH, '//a[contains(@class,"ekit-menu-nav-link")][text()="{}"]/..')
    SUB_MENU = (By.XPATH, '//ul[@class="elementor-nav-menu"]/ancestor::section')
    SUB_MENU_ITEM = (By.XPATH, '//nav[contains(@class,"elementor-nav-menu--main")]//li/a[text()={}]/..')
    SUB_MENU_ITEMS_TEXT =(By.XPATH, '//nav[contains(@class,"elementor-nav-menu--main")]//li/a]')
    SUB_HEADINGS = (By.XPATH, '//h2[contains(@class,"elementor-heading") and  text()="{}"]')
    DROP_DOWN = (By.XPATH,'//div[@class="elementskit-megamenu-panel"]')
    DROP_DOWN_TEXT = (By.XPATH,'//ul[@class="elementor-icon-list-items"]//span')
