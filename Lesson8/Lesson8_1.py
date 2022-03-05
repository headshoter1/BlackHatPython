from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://hackeru.com")
driver.maximize_window()

contact_us = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/nav/div/ul[1]/li/a")
contact_us.click()

full_name_input = driver.find_element(By.ID, "fullName")
full_name_input.send_keys("Alexey")
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("test@mail.com")
phone_input = driver.find_element(By.XPATH, "/html/body/div[1]/section[3]/div/div/div/form/div[2]/div[2]/input")