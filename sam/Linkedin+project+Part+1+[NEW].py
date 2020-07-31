from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/home/samay/chromedriver')
driver.maximize_window()
sleep(0.5)

driver.get('https://www.linkedin.com/')
sleep(5)

driver.find_element_by_xpath('//a[text()="Sign in"]').click()
sleep(3)

username_input = driver.find_element_by_name('session_key')
username_input.send_keys('varshneysamay14@gmail.com')
sleep(0.5)

password_input = driver.find_element_by_name('session_password')
password_input.send_keys('mud31347')
sleep(0.5)

# click on the sign in button
driver.find_element_by_xpath('//button[text()="Sign in"]').click()
sleep(5)
