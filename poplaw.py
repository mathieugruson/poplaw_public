from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
import time
import requests
import logging

PARIS1_LOGIN_PAGE = "https://cas.univ-paris1.fr/cas/login?service=https://ent.univ-paris1.fr/EsupUserApps/login?target=https%3A%2F%2Fent.univ-paris1.fr%2Faccueil%2F"
LOGIN_USER_NAME = "example"
LOGIN_USER_PASSWORD = "example"

def init_webdriver():
    try: 
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument('--no-sandbox')  # # Bypass OS security model, WARNING: NOT RECOMMENDED IF YOU'RE NOT AWARE OF THE IMPLICATIONS
        chrome_options.add_argument('--disable-gpu')  # Applicable to windows os only
        chrome_options.add_argument('start-maximized')  # Start with maximized window
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('window-size=1920x1080')  # Set window size
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36')  # Set user agent
        chrome_options.add_argument("--enable-logging")
        chrome_options.add_argument("--v=1")  # Verbose logging
        chrome_options.add_argument('--disable-dev-shm-usage')        

        service = Service(executable_path="/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)

        return driver
    except Exception as e:
        print(f"init_webdriver failed: {str(e)}")
    

# Perform login
def login(driver):

    try:
        driver.get(PARIS1_LOGIN_PAGE)
        print("Navigated to LOGIN_URL")
        title = driver.title
        print('title')
        print(title)
        # Set an explicit wait to ensure that elements are loaded.
        wait = WebDriverWait(driver, 10)
        print('c1')

        # Explicitly wait for the email field to be present
        email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        print('email_field')
        print(email_field)
        # Explicitly wait for the password field to be present
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        # Wait for the login button to be clickable

        email_field.send_keys(LOGIN_USER_NAME)
        password_field.send_keys(LOGIN_USER_PASSWORD)

        login_button = wait.until(EC.element_to_be_clickable((By.NAME, "submitBtn")))
        login_button.click()
        # Wait a moment for the login process to complete
        time.sleep(5)  # Consider using an explicit wait here as well
        print("Login successful.")
        
    except Exception as e:
        print(f"Login failed: {str(e)}")


# Main process
def main():
    
    try:
        print("Start")
        driver = init_webdriver()
        login(driver)
        wait = WebDriverWait(driver, 20)
        print(driver.title)
        mikado_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Mikado")))
        mikado_link.click()
        print('mikado')
        print(driver.title)
        try:
            domino_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.logo.comptelecteur")))
            domino_link.click()
            print('domino')
            print(driver.title)
        except TimeoutException:
            print("domino_link Element not found within the timeout period.")
            return
        try:
            original_window = driver.current_window_handle
            new_window = [window for window in driver.window_handles if window != original_window][0]
            driver.switch_to.window(new_window)
            wait = WebDriverWait(driver, 20)
            juris_library = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@src='https://domino-scd.univ-paris1.fr/INS01/icon_fre/droit.png']/parent::a")))
            print("juris_library Element found.")
            juris_library.click()
        except TimeoutException:
            print("juris_library Element not found within the timeout period.")
            return
        print('library')
        print(driver.title)
        try:
            next_page_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Suivant>")))
            next_page_link.click()
            print('next_page_link')
            print(driver.title)
        except TimeoutException:
            print("next_page_link Element not found within the timeout period.")
            return
        try:
            dalloz_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Dalloz gÃ©nÃ©ral - AccÃ¨s Ã©tudiants + enseignants")))
            print("Dalloz element found.")
            dalloz_link.click()
        except TimeoutException:
            print("Dalloz element not found within the timeout period.")
            return
        third_tab = driver.window_handles[2]  # This is because lists are zero-indexed
        driver.switch_to.window(third_tab)
        wait = WebDriverWait(driver, 20)
        try:
            dalloz_research = wait.until(EC.presence_of_element_located((By.NAME, "a$word0")))
            print("dalloz_research element found.")
            dalloz_research.send_keys("Droit pénal")
            dalloz_research.send_keys(Keys.RETURN)
            # button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Étudiants')]")))
            # button.click()
        except TimeoutException:
            print("dalloz_research element not found within the timeout period.")
            return

        print(driver.title)
        result_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "result-item")))
        print(result_items)
        for item in result_items:
            print(item.get_attribute('innerHTML'))

    except Exception as e:
        print(f"Logic error: {str(e)}")
    driver.quit()

if __name__ == "__main__":
    main()