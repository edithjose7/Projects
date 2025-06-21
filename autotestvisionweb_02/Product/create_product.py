import logging
import time 
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

# Load configuration from YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('Product.log'),
        logging.StreamHandler()
    ]
)

# Set Chrome options to ignore certificate errors
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")

# Start the WebDriver
driver = webdriver.Chrome(options=chrome_options)

def zoom_out():
    logging.info("Zooming out the screen")
    driver.execute_script("document.body.style.zoom='67%'")  # Adjust the zoom level as needed

def login():
    login_successful = False
    try:
        logging.info("Opening the login page")
        driver.get(config['login_url'])
        zoom_out()

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

        WebDriverWait(driver, 10).until(
            EC.url_changes(config['new_url'])
        )

        login_successful = True

    except TimeoutException:
        logging.error("An error occurred: Unsuccessful login")

    finally:
        if login_successful:
            logging.info("Login successful and navigated to products page")
        else:
            logging.error("An error occurred: Unsuccessful login")

        return login_successful

def create_product(product_name, auto_generate=True):
    try:
        logging.info("Clicking the product button")
        product_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "e0_15o"))
        )
        product_button.click()

        logging.info("Clicking the new button")
        new_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "e0_16o"))
        )
        new_button.click()

        logging.info("Entering product name")
        name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_name_"))
        )
        name_field.send_keys(product_name)

        if not auto_generate:
            logging.info("Turning off auto-generate code")
            auto_gen_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_auto_generate_code"))
            )
            auto_gen_button.click()
            logging.info("Auto-generate code turned off")

            logging.info("Entering the Code")
            code_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_code"))
            )
            code_field.send_keys(config['code'])

            logging.info("Entering the Version")
            version_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_version"))
            )
            version_field.send_keys(config['version'])

        logging.info("Entering SAP Code")
        SAP_code_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_sap_code_"))
        )
        SAP_code_field.send_keys(config['SAP_code'])

        logging.info("Clicking the Type dropdown")
        type_dropdown = Select(driver.find_element(By.ID, "record_type_id"))  # Replace "type_dropdown_id" with the actual ID of your dropdown
        type_dropdown.select_by_visible_text(config['option'])  # Replace ' ' with the desired option text
        
        '''
        logging.info("Clicking the Sub Type dropdown")
        sub_type_dropdown = Select(driver.find_element(By.ID, "record_sub_type_id"))  # Replace "type_dropdown_id" with the actual ID of your dropdown
        sub_type_dropdown.select_by_visible_text(config['sub_type'])  # Replace ' ' with the desired option text

        logging.info("Clicking the Schedule tag dropdown")
        Schedule_tag_dropdown = Select(driver.find_element(By.ID, "record_sub_type_id"))  # Replace "type_dropdown_id" with the actual ID of your dropdown
        Schedule_tag_dropdown.select_by_visible_text(config['schedule_tag'])  # Replace ' ' with the desired option text

        logging.info("Clicking the brand dropdown")
        brand_dropdown = Select(driver.find_element(By.ID, "record_sub_type_id"))  # Replace "type_dropdown_id" with the actual ID of your dropdown
        brand_dropdown.select_by_visible_text(config['brand'])  # Replace ' ' with the desired option text
        '''
        logging.info("clicked exclusive")
        exclusive_button = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.ID, "record_exclusive_flag_"))
        )
        exclusive_button.click()
        logging.info("Marked Exclusive")

        logging.info("clicked price listed")
        exclusive_button = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.ID, "record_price_listed_"))
        )
        exclusive_button.click()
        logging.info("Marked: Price Listed") 

        logging.info("clicked NPI Completed")
        exclusive_button = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.ID, "record_npi_completed_"))
        )
        exclusive_button.click()
        logging.info("Marked: NPI completed") 

        logging.info("Entering Tariff/HSN Classification")
        tariff_HSN_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_hsn_classification"))
        )
        tariff_HSN_field.send_keys(config['tariff_HSN'])
        
        logging.info("Clicking the Identification dropdown")
        identification_dropdown = Select(driver.find_element(By.ID, "record_identification_"))  # Replace "type_dropdown_id" with the actual ID of your dropdown
        identification_dropdown.select_by_visible_text(config['Identification'])  # Replace ' ' with the desired option text
        
        '''
        logging.info("clicked Taxable")
        taxable_button = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.ID, "record_taxable_"))
        )
        taxable_button.click()
        logging.info("Marked: Taxable")
        '''
        
        logging.info("Entering Comments")
        comments_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_description"))
        )
        comments_field.send_keys(config['comments'])

        logging.info("Entering MDG Change Request")
        MDG_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_mdg_change_request"))
        )
        MDG_field.send_keys(config['MDG_change_request'])

        logging.info("Clicking the create button")
        create_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/p/input"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", create_button)
        driver.execute_script("arguments[0].click();", create_button)

        WebDriverWait(driver, 10).until(
            EC.url_changes(driver.current_url)
        )
    
        if auto_generate:
            logging.info("Product created successfully with auto-generated code")
        else:
            logging.info("Product created successfully with manual code")

    except Exception as e:
        logging.error(f"An error occurred while creating the product: {e}")

def cancel_product_creation(product_name, auto_generate=True):
    try:
        logging.info("Clicking the product button")
        product_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "e0_15o"))
        )
        product_button.click()

        logging.info("Clicking the new button")
        new_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "e0_16o"))
        )
        new_button.click()

        logging.info("Entering product name")
        name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_name_"))
        )
        name_field.send_keys(product_name)

        if not auto_generate:
            logging.info("Turning off auto-generate code")
            auto_gen_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_auto_generate_code"))
            )
            auto_gen_button.click()
            logging.info("Auto-generate code turned off")

            logging.info("Entering the Code")
            code_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_code"))
            )
            code_field.send_keys(config['code'])

            logging.info("Entering the Version")
            version_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_version"))
            )
            version_field.send_keys(config['version'])

        logging.info("Entering SAP Code")
        SAP_code_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_sap_code_"))
        )
        SAP_code_field.send_keys(config['SAP_code'])

        logging.info("Clicking the Type dropdown")
        type_dropdown = Select(driver.find_element(By.ID, "record_type_id"))  # Replace "type_dropdown_id" with the actual ID of your dropdown
        type_dropdown.select_by_visible_text(config['option'])  # Replace ' ' with the desired option text

        logging.info("clicked exclusive")
        exclusive_button = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.ID, "record_exclusive_flag_"))
        )
        exclusive_button.click()
        logging.info("Marked Exclusive")

        logging.info("clicked price listed")
        exclusive_button = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.ID, "record_price_listed_"))
        )
        exclusive_button.click()
        logging.info("Marked: Price Listed") 

        logging.info("clicked NPI Completed")
        exclusive_button = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.ID, "record_npi_completed_"))
        )
        exclusive_button.click()
        logging.info("Marked: NPI completed") 

        logging.info("Entering Tariff/HSN Classification")
        tariff_HSN_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_hsn_classification"))
        )
        tariff_HSN_field.send_keys(config['tariff_HSN'])
        
        logging.info("Clicking the Identification dropdown")
        identification_dropdown = Select(driver.find_element(By.ID, "record_identification_"))  # Replace "type_dropdown_id" with the actual ID of your dropdown
        identification_dropdown.select_by_visible_text(config['Identification'])  # Replace ' ' with the desired option text
        
        logging.info("Entering Comments")
        comments_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_description"))
        )
        comments_field.send_keys(config['comments'])

        logging.info("Entering MDG Change Request")
        MDG_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_mdg_change_request"))
        )
        MDG_field.send_keys(config['MDG_change_request'])

        logging.info("Clicking the cancel button")
        cancel_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/p/a"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", cancel_button)
        driver.execute_script("arguments[0].click();", cancel_button)
        logging.info("Product creation canceled")

        time.sleep(5)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    logging.info("Function cancel_product_creation() ended")

def logout():
    try:
        login_successful = False
        Configure_label = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "e0_134o"))
        )
        logging.info("Clicking Configure label")
        Configure_label.click()

        select_logout = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "e0_138o"))
        )
        logging.info("Selection logout from the drop_down menu")
        select_logout.click()
        logging.info("Logging out....")

        login_successful = True  # Update login status

        time.sleep(10)

    except TimeoutException:
        logging.error("An error occurred: Unsuccessful logout")

if __name__ == "__main__":
    login_successful = login()
    if login_successful:
        logging.info("Proceeding to additional actions")
        
        '''
        # Test Case 1: Auto-generate code
        logging.info("Test Case 1: Creating product with auto-generated code")
        create_product(config['product_name'], auto_generate=True)

        # Navigate back to home
        logging.info("Navigating back to home")
        driver.get(config['home_url'])

        # Test Case 2: Manual code entry
        logging.info("Test Case 2: Creating product with manual code entry")
        create_product(config['product_name'], auto_generate=False)
        '''

        #Test Case 3: Cancelling Product creation
        logging.info("Test Case 3: Cancelling product creation with Auto generate on")
        cancel_product_creation(config['product_name'], auto_generate=True)
         
        #Test Case 4: Cancelling Product creation
        logging.info("Test Case 3: Cancelling product creation with Auto generate off")
        cancel_product_creation(config['product_name'], auto_generate=False)

        logout()

    input("Press Enter to close the browser...")
    driver.quit()
    logging.info("Closed the WebDriver")