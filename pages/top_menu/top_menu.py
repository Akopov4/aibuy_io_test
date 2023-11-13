from pages.base_page import BasePage
from .top_menu_locators import TopMenuLocators
from typing import List


class TopMenu(BasePage):
    def __int__(self, browser):
        self.browser = browser

    def get_text_of_top_menu_items(self) -> List[str]:
        menu_items = self.find_elements(*TopMenuLocators.TOP_MENU_ITEMS)
        text_of_menu_items = []
        for item in menu_items:
            text_of_menu_items.append(self.get_text_of_element(item))
        return text_of_menu_items

    def click_on_item(self, item_text: str):
        item_locator = self.get_parametrized_locator(TopMenuLocators.TOP_MENU_ITEM, [item_text])
        self.click(*item_locator)

    def get_color_of_sub_menu(self) -> str:
        self.wait_until_element_is_visible(*TopMenuLocators.SUB_MENU)
        css_property = self.get_css_property(TopMenuLocators.SUB_MENU, 'background-image')
        return css_property

    def get_sub_menu_items_text(self)->List[str]:
        sub_menu_item_text = []
        sub_menu_items= self.find_elements(*TopMenuLocators.SUB_MENU_ITEMS_TEXT)
        for item in sub_menu_items:
            sub_menu_item_text.append(item.text)
        return  sub_menu_item_text

    def click_on_sub_menu_item(self, item:str):
        locator = self.get_parametrized_locator(TopMenuLocators.SUB_MENU_ITEM,[item])
        self.wait_until_element_is_visible(*locator)

    def is_sub_heading_visible(self, heading:str):
        locator = self.get_parametrized_locator(TopMenuLocators.SUB_HEADINGS,[heading])
        assert  self.is_element_visible(*locator)

    def is_industries_drop_down_visible(self):
        self.is_element_visible(*TopMenuLocators.DROP_DOWN)

    def get_text_of_drop_down_items(self,locator:str):
        items_text = self.get_text_from_drop_down(*locator)
        return  items_text
