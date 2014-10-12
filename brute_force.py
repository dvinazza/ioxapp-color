#!/usr/bin/python 

from selenium import webdriver
from time import sleep
from collections import Counter
from operator import itemgetter

from IPython import embed

game_url = "http://game.ioxapp.com/color/"

driver = webdriver.Firefox()
driver.get(game_url)

driver.find_element_by_class_name('play-btn').click()

while True:
    try: print driver.find_element_by_class_name('time').text
    except: break 

    spans = driver.find_element_by_id('box').find_elements_by_tag_name('span')
    colores = Counter([s.get_attribute('style') for s in spans])
    distinto = sorted(colores.items(), key=itemgetter(1))[0][0]

    for s in spans:
	if s.get_attribute('style') == distinto:
	    s.click()
	    break
    
    #le doy un respiro
    #sleep(0.05)

raw_input()
