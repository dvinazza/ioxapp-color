#!/usr/bin/python 

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://game.ioxapp.com/color/")
driver.find_element_by_class_name('play-btn').click()

while True:
    try: print driver.find_element_by_class_name('time').text
    except: break 

    for s in driver.find_element_by_id('box').find_elements_by_tag_name('span'):
    	try: s.click()
    	except: break

raw_input()
