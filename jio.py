from selenium import webdriver


#Open Browser and specified webpage
chromedriver = 'C:\chromedriver\chromedriver.exe' #chromedriver location required to open google chrome browser
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.jio.com/Jio/portal/jioLogin?_afrLoop=13813813668244865&_afrWindowMode=0&_afrWindowId=nek3frvnu_1#!%40%40%3F_afrWindowId%3Dnek3frvnu_1%26_afrLoop%3D13813813668244865%26_afrWindowMode%3D0%26_adf.ctrl-state%3Dun6c2wuto_4')

browser.implicitly_wait(150)
#Click on the link
link = browser.find_element_by_link_text('Sign In using Email ID')
link.click()

#wait for 150 seconds
browser.implicitly_wait(150)

username = browser.find_element_by_id("pt1:r1:1:sb11:it1::content")
password = browser.find_element_by_id("pt1:r1:1:sb11:it2::content")

username.send_keys("username")
password.send_keys("password")


browser.find_element_by_id("pt1:r1:1:sb11:cb1").click()

browser.implicitly_wait(150)
browser.find_element_by_id("pt1:r1:0:cl10").click()

#if you want to check remaning internet in one of your linked account
#browser.implicitly_wait(150)
#browser.find_element_by_link_text('Prepaid VoLTE - xxxxxxxxxx').click()  #here xxxxxxxxxx is your jio number
