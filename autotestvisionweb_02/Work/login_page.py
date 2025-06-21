from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging, time

class LoginPage:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def login(self):
        login_successful = False
        try:
            logging.info("Opening the login page")
            self.driver.get(self.config['login_url'])
            logging.info("Waiting for the username field to be present")
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "login"))
            )
            logging.info("Entering username")
            username_field.send_keys(self.config['username'])

            logging.info("Finding the password field")
            password_field = self.driver.find_element(By.ID, "password")
            logging.info("Entering password")
            password_field.send_keys(self.config['password'])


            logging.info("Waiting for the login button to be clickable")
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[3]/a[1]'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", login_button)
            logging.info("Clicking the login button")
            self.driver.execute_script("arguments[0].click();", login_button)

            WebDriverWait(self.driver, 10).until(
                EC.url_changes(self.config['new_url'])
            )

            login_successful = True

            time.sleep(5)

        except TimeoutException:
            logging.error("Unsuccessful login")
        finally:
            return login_successful