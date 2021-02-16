#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose user language of web-page: --language=lan. Default ru")

@pytest.fixture(scope='function')
def browser(request):
    print('\nstart test')
    user_language = request.config.getoption('language')
    options = Options() 
    options.add_argument("--headless")
    fp = webdriver.FirefoxProfile()
    fp.set_preference('intl.accept_languages', user_language)
    browser = webdriver.Firefox(options=options, firefox_profile=fp, executable_path="./geckodriver") 
    yield browser
    print('\ndone!')
    browser.quit()
    
'''
def browser(request):
    print('\nstart test')
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\ndone!')
    browser.quit() 
'''    
