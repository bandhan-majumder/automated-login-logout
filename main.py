import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# creating driver
driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2) # 2 sec time is given to load the page totally

if not os.path.exists('autoSS'): # creating folder to store images
 os.mkdir('autoSS')

try:
 # logging in process:-

  # step 1: sign-in bar -> username
 log_in_username=driver.find_element(By.NAME, "username")
 log_in_username.send_keys("Admin") # username : Admin
  # sign - in bar -> password
 log_in_password=driver.find_element(By.NAME,"password")
 log_in_password.send_keys("admin123") # password : admin123

 driver.get_screenshot_as_file('autoSS/loginpage.png')  # screenshot 1 : login page

 log_in_username.send_keys(Keys.ENTER)  # clicking enter to log in
 print("Logged in successfully!")

 time.sleep(4)

 driver.get_screenshot_as_file('autoSS/loginSucc.png') # screenshot 2 : dashboard

 # log out process:-

  # step 1. click the profile option and click ..
 profile = driver.find_element(By.CLASS_NAME, 'oxd-userdropdown-tab') # choosing the profile option
 profile.click() # clicking on the top-down button to get the logout option
 time.sleep(2)
  # step 2. click the logout option and sign out ..
 log_out=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a') # choosing the logout option
 log_out.send_keys(Keys.ENTER) # clicking and signing out ......
 time.sleep(2)

 driver.get_screenshot_as_file('autoSS/loggedout.png') # screenshot 3 : logged out and back again to log in page
 driver.quit()
 print("Logged out successfully!")

except Exception as e: # if we get an error in the process, an error image will be saved
 response = requests.get(
  'https://developers.google.com/static/maps/documentation/maps-static/images/error-image-generic.png')
 if response.status_code==200: # if the http request was successful
  file_name = os.path.join('autoSS/', 'error.png')
  with open(file_name, 'wb') as file:
   file.write(response.content)
 print("Authentication error occurred!")

