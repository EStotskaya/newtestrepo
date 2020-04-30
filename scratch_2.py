from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver: WebDriver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://dev.app.wizer-training.com")
driver.find_element_by_name("email").click()
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("qastotskaya@gmail.com")
driver.find_element_by_name("password").click()
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("111222")
driver.find_element_by_css_selector("#root > div > div > div.Signin_formWrapper__MqlPj > div.SignFormWrapper_formContainer__3WuUw > form > div.SigninForm_btnWrapper__3SLEG > button").click()
driver.find_element_by_link_text("User Agreement").click()
driver.navigate().to("https://dev.app.wizer-training.com");
driver.find_element_by_link_text("Privacy Policy").click()

# Commented code, will use this function for the future!
"""
def check_exists_by_class_name():
    try:
        driver.find_elements_by_class_name("Navbar_headerLogo__2j7Ax")
    except NoSuchElementException:
        return False
    return True
    
    New test line of code -Useless!!!
    """


