# -*- coding: utf-8 -*-

import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Internet Explorer session
driver = webdriver.Ie(os.path.join(os.path.dirname(__file__), 'IEDriverServer.exe'))
driver.implicitly_wait(30)
driver.maximize_window()
 
# navigate to the application home page
driver.get('http://www.google.com')
 
# get the search textbox
search_field = driver.find_element_by_name('q')
 
# enter search keyword and submit
search_field.send_keys(u'健保署')
search_field.submit()
 
# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name  method
lists= driver.find_elements_by_class_name('r')
 
# get the number of elements found
print ('Found ' + str(len(lists)) + ' searches:')
 
# iterate through each element and print the text that is
# name of the search
 
i = 0
for listitem in lists:
   print(listitem)
   i +=1
   if i > 10:
      break
 
# close the browser window
driver.quit()
