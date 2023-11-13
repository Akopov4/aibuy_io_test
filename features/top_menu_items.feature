
Feature: verification of items of Top menu
  As a user i would like to see list of next items in the top menu: Home, Solutions, Industries, Patents,News

  Scenario: check presence of required menu items in the top menu
    Given  Home page is loaded
    Then   Home, Solutions, Industries, Patents,News are present in the TOP Menu


  Scenario:  Click on item Solutions of top Menu
    Given Home page is loaded
    When Click on item Solution in the Top bar
    Then Sub menu occurs
    Then sub menu has green background
    Then Our Solutions and Our Platforms are present in Green submenu


  Scenario Outline: Click on Submenu items
    Given Home page is loaded
    When Click on item Solution in the Top bar
    When user clicks on <green_sub_menu_item>
    Then <sub_heading> is visible
    Examples: Sub menu items and Headings
    |green_sub_menu_item| sub_heading|
    |Our Solutions|Our Solutions|
    |Our Platforms|Platforms|

Scenario: Get list of items in Industries dropdown
  Given Home page is loaded
  When click on Industries in the top bar
  Then appropriate values in dropdown are visible
