#!/usr/bin/env python3
# -*- coding: utf-8 -*-

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_login_link(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn-add-to-basket")
    
