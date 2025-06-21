from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging, time

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        logout_successful = False
        try:
            Configure_label = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_134o"))
            )
            Configure_label.click()

            select_logout = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_138o"))
            )
            select_logout.click()

            logout_successful = True

            time.sleep(5)
            
        except TimeoutException:
            logging.error("Unsuccessful logout")
        finally:
            return logout_successful
