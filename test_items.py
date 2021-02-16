#!/usr/bin/env python3
# -*- coding: utf-8 -*-

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_item_has_add_to_cart_button(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn-add-to-basket")
    
