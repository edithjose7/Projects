import logging
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        
        # Configure logging
        self.configure_logging()

    def configure_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('Login.log'),  # Log into a file named 'Login.log'
                logging.StreamHandler()
            ]
        )

    def quit(self):
        self.driver.quit()
