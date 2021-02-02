from time import sleep
from selenium import webdriver

#insert path to the chromedriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://www.facebook.com/")

login_button = driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]')
login_button.click()

#allow some time for the page to load before moving on
sleep(1)

username = driver.find_element_by_xpath('//*[@id="email"]')
#type in your email
username.send_keys("your email here")

password = driver.find_element_by_xpath('//*[@id="password"]')
#type in your email password
password.send_keys("your password here")

#submits
driver.find_element_by_xpath('//*[@id="submit-button"]').click()
