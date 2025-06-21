import logging  # Import the logging module
import time 
import pdb
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException

# Load configuration from YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('Login.log'),  # Log into a file named 'Login.log'
        logging.StreamHandler()
    ]
)

# Set Chrome options to ignore certificate errors
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")

# Start the WebDriver
driver = webdriver.Chrome(options=chrome_options)

def login():
    login_successful = False  # Initialize a variable to track login success
    try:
        logging.info("Opening the login page")
        driver.get(config['login_url'])

        logging.info("Waiting for the username field to be present")
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login"))
        )
        logging.info("Entering username")
        username_field.send_keys(config['username'])

        logging.info("Finding the password field")
        password_field = driver.find_element(By.ID, "password")
        logging.info("Entering password")
        password_field.send_keys(config['password'])

        logging.info("Waiting for the login button to be clickable")
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[3]/a[1]'))
        )
        logging.info("Scrolling to the login button")
        driver.execute_script("arguments[0].scrollIntoView();", login_button)
        logging.info("Clicking the login button")
        driver.execute_script("arguments[0].click();", login_button)

        # Wait for the page content to update (you can adjust the timeout as needed)
        WebDriverWait(driver, 10).until(
            EC.url_changes(config['new_url'])  # Wait for URL change to indicate successful login
        )

        login_successful = True  # Update login status

    except TimeoutException:
        logging.error("An error occurred: Unsuccessful login")

    finally:
        if login_successful:
            logging.info("Login successful and navigated to products page")
        else:
            logging.error("An error occurred: Unsuccessful login")

        return login_successful

def synonyms(search_synonym):
    try:
        logging.info("Clicking the product button")
        product_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "e0_15o"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", product_button)
        product_button.click()

        logging.info("Clicking the synonym option")
        synonym_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "e0_19o"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", synonym_button)
        synonym_button.click()

        logging.info("Entering the synonym  to be searched")
        search_synonym_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "as_search_synonym-search-input"))
        )
        search_synonym_field.send_keys(config['search_synonym'])

        logging.info("Clicking the search button")
        search_synonym_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr/td/div/form/input[3]"))
        )
        driver.execute_script("arguments[0].click();", search_synonym_button)
        
        logging.info("synonym searched successfully")

    except Exception as e:
        logging.error(f"An error occurred while searching for the synonym: {e}")
    
    time.sleep(10)

if __name__ == "__main__":
    login_successful = login()
    if login_successful:
        logging.info("Proceeding to additional actions")

        synonyms(config['search_synonym'])
        
    # Always make sure to close the driver
    input("Press Enter to close the browser...")
    driver.quit()
    logging.info("Closed the WebDriver")