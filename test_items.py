import pytest
import time
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_could_add_item_to_the_basket(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_class_name("btn-add-to-basket")