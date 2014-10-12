#!/usr/bin/python 

from selenium import webdriver
from time import sleep
from collections import Counter
from operator import itemgetter

driver = webdriver.Firefox()
driver.get("http://game.ioxapp.com/color/")
driver.find_element_by_class_name('play-btn').click()

while True:
    try:
	driver.find_element_by_class_name('time')

    	spans = driver.find_element_by_id('box').find_elements_by_tag_name('span')
	colores = [s.get_attribute('style') for s in spans[:3]]
	counter = Counter(colores)

    	if len(counter) > 1: # el distinto esta aca
    	    distinto = sorted(counter.items(), key=itemgetter(1))[0][0]

	    for s in spans[:3]:
		if s.get_attribute('style') == distinto:
		    break

	else: # ya se cual es el color normal 
	    for s in spans[3:]:
	        if s.get_attribute('style') != colores[0]:
		    break

	s.click()
    except: # Oops
	break

print driver.find_element_by_class_name('gameover').find_element_by_tag_name('h3').text
print "Presione una tecla para terminar..."
raw_input()
driver.close()
