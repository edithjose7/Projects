import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class Login:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def login(self):
        login_successful = False
        try:
            self.driver.get(self.config['login']['login_url'])

            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "login"))
            )
            username_field.send_keys(self.config['login']['username'])

            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(self.config['login']['password'])

            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[3]/a[1]'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", login_button)
            self.driver.execute_script("arguments[0].click();", login_button)

            WebDriverWait(self.driver, 10).until(
                EC.url_changes(self.config['login']['new_url'])
            )

            login_successful = True

            time.sleep(5)

        except TimeoutException:
            logging.error("Login - Failed")

        finally:
            if login_successful:
                logging.info("Login - Passed")
            else:
                logging.error("Login - Failed")

            return login_successful

    def logout(self):
        try:
            configure_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_134o"))
            )

            # Retry mechanism for clicking the configure button
            for attempt in range(3):
                try:
                    configure_button.click()
                    break
                except ElementClickInterceptedException as e:
                    WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.ID, "e0_134o"))
                    )
            else:
                logging.error("Logout - Failed")
                return
            
            logout_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, "e0_138i"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", logout_button)

            # Retry mechanism for clicking the logout button
            for attempt in range(3):
                try:
                    logout_button.click()
                    break
                except ElementClickInterceptedException as e:
                    WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.ID, "e0_138o"))
                    )
            else:
                return

            WebDriverWait(self.driver, 10).until(
                EC.url_changes(self.config['login']['login_url'])
            )

        except TimeoutException:
            pass  # logging.error("An error occurred: Unsuccessful logout")
        except Exception as e:
            pass  # logging.error(f"An unexpected error occurred: {e}")
        finally:
                logging.info("Logout - Passed")
            