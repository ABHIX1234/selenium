#1.HOW TO NEVIGATE WEB BROWSER
 #A.OPENING A BROWSER
 #B.NAGIVATE

 #import web driver module from selenium package
from selenium import webdriver
#time package
import time
#open chrome browser
driver = webdriver.Chrome()
#nevigate to google
driver.get("https://www.google.com")
time.sleep(5)
#negivate to yt
driver.get("https://www.youtube.com")
time.sleep(5)
#go back to google
driver.back()
#go forward to youtube
time.sleep(5)

driver.forward()
#refresh current page
time.sleep(5)
driver.refresh()
time.sleep(5)
#driver quit
driver.quit()



