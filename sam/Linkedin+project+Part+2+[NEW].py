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
username_input.send_keys('foo@gmail.com')
sleep(0.5)

password_input = driver.find_element_by_name('session_password')
password_input.send_keys('pass123')
sleep(0.5)

# click on the sign in button
driver.find_element_by_xpath('//button[text()="Sign in"]').click()
sleep(5)


driver.get('https://www.google.com/')
sleep(5)

search_input = driver.find_element_by_name('q')
search_input.send_keys('site:linkedin.com/in/ AND "python developer" AND "New York"')
sleep(1)

search_input.send_keys(Keys.RETURN)
sleep(3)

profiles = driver.find_elements_by_xpath('//*[@class="r"]/a[1]')
profiles = [profile.get_attribute('href') for profile in profiles]
