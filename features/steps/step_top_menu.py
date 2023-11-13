from behave import given, when, then
from pages.top_menu.top_menu import TopMenu
from pages.top_menu.top_menu_locators import TopMenuLocators
from typing import List

@given('Home page is loaded')
def is_top_logo_loaded(context):
    context.top_menu = TopMenu(context.browser)
    context.top_menu.is_element_visible(*TopMenuLocators.TOP_LOGO)


@then('Home, Solutions, Industries, Patents,News are present in the TOP Menu')
def are_top_menu_items(context):
    item_text = []
    text_to_verify = ['home', 'solutions', 'industries', 'patents', 'news']
    for text in context.top_menu.get_text_of_top_menu_items():
        item_text.append(text.lower())
    assert all([text in item_text for text in text_to_verify])


@when('Click on item Solution in the Top bar')
def click_on_solution_item(context):
    context.top_menu.click_on_item('Solutions')


@then('Sub menu occurs')
def is_sub_menu_visible(context):
    context.top_menu.is_element_visible(*TopMenuLocators.SUB_MENU)


@then('sub menu has green background')
def check_color_of_sub_menu(context):
    assert '#93DA45' in context.top_menu.get_color_of_sub_menu()


@then("Our Solutions and Our Platforms are present in Green submenu")
def check_text_of_sub_menu_items(context):
    sub_menu_text = context.top_menu.get_sub_menu_items_text()
    assert all([word in sub_menu_text for word in ['Our Solutions', 'Our Platforms']])


@when('user clicks on {green_sub_menu_item}')
def click_on_sub_menu_item(context, green_sub_menu_item):
    context.top_menu.click_on_sub_menu_item(green_sub_menu_item)


@then('{sub_heading} is visible')
def is_sub_heading_visible(context,sub_heading)->bool:
    assert context.top_menu.is_sub_heading_visible(sub_heading)

@when('click on Industries in the top bar')
def click_on_industries_in_top_bar(context):
    context.top_menu.click_on_item("Industries")
    context.top_menu.is_dropdown_visible(*TopMenuLocators.DROP_DOWN)

@then("appropriate values in dropdown are visible")
def dropdown_items_text(context)->List['str']:
    text = context.top_menu.get_text_of_drop_down_items()
    list_to_verify = ['OTT','Online Retail', 'Entertainment', 'Online Media', 'Influencers']
    assert  all ([item in text for item in list_to_verify ])




