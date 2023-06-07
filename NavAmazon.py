from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By as by
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")

#Location button
driver.find_element(by.ID,"glow-ingress-block").click()
CYL = driver.find_element(by.ID,"a-popover-header-1").text
assert CYL == "Choose your location"
driver.refresh()

#navsearch
assert driver.find_element(by.ID,"nav-search").is_displayed()

#language
assert driver.find_element(by.ID,"icp-nav-flyout").is_displayed()

#account
driver.find_element(by.ID,"nav-link-accountList-nav-line-1").click()
TagName = driver.find_element(by.TAG_NAME,"h1").text
assert TagName == "Sign in"
driver.back()

#return&order
driver.find_element(by.XPATH,"//span[normalize-space()='& Orders']").click()
TagName = driver.find_element(by.TAG_NAME,"h1").text
assert TagName == "Sign in"
driver.back()

#cart
driver.find_element(by.XPATH,"//a[@id='nav-cart']").click()
TagName = driver.find_element(by.TAG_NAME,"h2").text
assert TagName == "Your Amazon Cart is empty"
driver.back()

#searchbar functionality
driver.find_element(by.ID,"twotabsearchtextbox").send_keys("razor mouse")
driver.find_element(by.ID,"nav-search-submit-button").click()

#transferrign to next page
Text = "Razer Basilisk V3 Pro Customizable Wireless Gaming"
driver.find_element(by.XPATH,"//div[@class='rush-component s-featured-result-item ']//span[@class='a-size-medium a-color-base a-text-normal'][contains(text(),Text)]").click()
Name = driver.window_handles
driver.switch_to.window(Name[1])
Title = driver.find_element(by.XPATH,"//span[@id='productTitle']").text
print(Title)

#buying item if matches the requirement
if Text in Title:
    driver.find_element(by.ID,"buy-now-button").click()

#switching back to previous window and navigate to Home page
driver.close()
Name = driver.window_handles
driver.switch_to.window(Name[0])
driver.back()
time.sleep(3)
driver.close()

