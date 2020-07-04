from selenium import webdriver

browser = webdriver.Chrome(executable_path="C:/Users/revalGovender/Downloads/chromedriver.exe")
browser.get("https://www.asda.com/login?redirect_uri=https://groceries.asda.com")

email = browser.find_element_by_css_selector("#app > main > div > div > div > div > form > div.input-box > input")
email.send_keys('lashanthapillay@gmail.com')
password = browser.find_element_by_css_selector("#password")
password.send_keys('Survive1')

sign_in_button = browser.find_element_by_css_selector("#app > main > div > div > div > div > form > button")
sign_in_button.click()
