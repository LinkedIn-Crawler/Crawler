import csv
import sys
import fileinput
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import parameters
from parsel import Selector

driver = webdriver.Chrome('/home/samay/chromedriver')
driver.maximize_window()
sleep(0.5)

driver.get('https://www.linkedin.com/')
sleep(2)
driver.find_element_by_xpath('//a[text()="Sign in"]').click()
sleep(3)
username = driver.find_element_by_name('session_key')
username.send_keys(parameters.username)
sleep(0.5)
password = driver.find_element_by_name('session_password')
password.send_keys(parameters.password)
sleep(0.5)
driver.find_element_by_xpath('//button[text()="Sign in"]').click()
sleep(5)

driver.get('https://www.google.com/')
sleep(2)
search_input = driver.find_element_by_name('q')

beg = 'site:linkedin.com/school'
line = input('Enter the Institute Name\n')
r1 = line.rstrip()
beg = beg + ' AND '
beg = beg +  '"{}"'.format(r1)
search_input.send_keys(beg)
sleep(0.5)
search_input.send_keys(Keys.RETURN)
sleep(3)

schools = driver.find_elements_by_xpath('//*[@class="r"]/a[1]')
school = [school.get_attribute('href') for school in schools]
driver.get(school[0])
sleep(3);

url = driver.current_url + 'people/'
driver.get(url)
print(url)

