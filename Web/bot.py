from selenium import webdriver

usernameStr = "bg@gmail.com"
passwordStr = "tt"

browser = webdriver.Chrome()
browser.get('http://localhost/index.php')

# fill in username and hit the next button
username = browser.find_element_by_id('email')
username.send_keys(usernameStr)

password = browser.find_element_by_id('Pwd')
password.send_keys(passwordStr)

nextButton = browser.find_element_by_id('submit')
nextButton.click()

