import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# creating driver
driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2) # 2 sec time is given to load the page totally


try:
 # logging in process:-

  # step 1: sign-in bar -> username
 sign_in_username=driver.find_element(By.NAME, "username")
 sign_in_username.send_keys("Admin") # username : Admin
  # sign - in bar -> password
 sign_in_password=driver.find_element(By.NAME,"password")
 sign_in_password.send_keys("admin123") # password : admin123

 sign_in_username.send_keys(Keys.ENTER)  # clicking enter to log in
 print("Logged in successfully!")

 time.sleep(3)

 # log out process:-

  # step 1. click the profile option and click ..
 profile = driver.find_element(By.CLASS_NAME, 'oxd-userdropdown-tab') # choosing the profile option
 profile.click() # clicking on the top-down button to get the logout option
 time.sleep(3)
  # step 2. click the logout option and sign out ..
 sign_out=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a') # choosing the logout option
 sign_out.send_keys(Keys.ENTER) # clicking and signing out ......
 time.sleep(4)

 driver.quit()
 print("Logged out successfully!")
except Exception as e:
    print("Authentication error occurred!")

