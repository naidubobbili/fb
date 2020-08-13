from selenium import webdriver

driver=webdriver.Chrome('chromedriver.exe')

driver.get('https://www.facebook.com/login.php')

driver.find_element_by_name('email').send_keys('eeeeeeeeeeeeeeeeeeee')
driver.find_element_by_name('pass').send_keys('eeeeeeeeeeeeeeeeeeeee')
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
