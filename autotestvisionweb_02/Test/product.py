import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException

class Product:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_product(self, auto_generate=True):
        try:
            logging.info("Clicking the product button")
            product_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "e0_15o"))
            )
            product_button.click()

            logging.info("Clicking the new button")
            new_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "e0_16o"))
            )
            new_button.click()

            logging.info("Entering product name")
            name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_name_"))
            )
            name_field.send_keys(self.config['product']['product_name'])

            if not auto_generate:
                logging.info("Turning off auto-generate code")
                auto_gen_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "record_auto_generate_code"))
                )
                auto_gen_button.click()

                logging.info("Entering manual product code")
                code_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "record_code"))
                    )
                code_field.send_keys(self.config['product']['product_code'])
                generated_code = self.config['product']['product_code']

            logging.info("Entering SAP Code")
            SAP_code_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "record_sap_code_"))
            )
            SAP_code_field.send_keys(self.config['product']['SAP_code'])

            logging.info("Clicking the Type dropdown")
            type_dropdown = Select(self.driver.find_element(By.ID, "record_type_id"))
            type_dropdown.select_by_visible_text(self.config['product']['option'])

            logging.info("Marked Exclusive")
            exclusive_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_exclusive_flag_"))
            )
            exclusive_button.click()

            logging.info("Marked: Price Listed")
            price_listed_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_price_listed_"))
            )
            price_listed_button.click()

            logging.info("Marked: NPI completed")
            npi_completed_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_npi_completed_"))
            )
            npi_completed_button.click()

            logging.info("Entering Tariff/HSN Classification")
            tariff_HSN_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_hsn_classification"))
            )
            tariff_HSN_field.send_keys(self.config['product']['tariff_HSN'])

            logging.info("Clicking the Identification dropdown")
            identification_dropdown = Select(self.driver.find_element(By.ID, "record_identification_"))
            identification_dropdown.select_by_visible_text(self.config['product']['identification'])

            logging.info("Entering Comments")
            comments_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_description"))
            )
            comments_field.send_keys(self.config['product']['comments'])

            logging.info("Entering MDG Change Request")
            MDG_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_mdg_change_request"))
            )
            MDG_field.send_keys(self.config['product']['MDG_change_request'])

            logging.info("Clicking the create button")
            create_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/p/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button)
            self.driver.execute_script("arguments[0].click();", create_button)

            generated_code_element = self.driver.find_element(By.XPATH,'//*[@id="product_code"]/dd/label')  # Adjust the ID as needed
            generated_code = generated_code_element.text
            logging.info(f"Auto-generated product code: {generated_code}")

            return generated_code

        except TimeoutException as e:
            logging.error(f"Timeout while creating product: {e}")

        except Exception as e:
            logging.error(f"Could not create the product: {e}")
            
        return None

        time.sleep(5)

    def delete_product(self):
        try:
            logging.info("Waiting to click the delete button")
            delete_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[15]/table/tbody/tr/td[8]/a"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", delete_button)
            logging.info("Clicking the delete button")
            self.driver.execute_script("arguments[0].click();", delete_button)

            logging.info("Waiting to click the YES button")
            yes_confirm_delete = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//form/p[2]/input[@type='submit' and @value='Yes']"))
            )
            logging.info("Clicking the YES button")
            self.driver.execute_script("arguments[0].click();", yes_confirm_delete)

            logging.info("Product deleted successfully")

        except Exception as e:
            logging.error(f"Could not delete the product: {e}")
        
            time.sleep(10)

    def cancel_product_creation(self, product_name, auto_generate=True):
        try:
            logging.info("Clicking the product button")
            product_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "e0_15o"))
            )
            product_button.click()

            logging.info("Clicking the new button")
            new_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "e0_16o"))
            )
            new_button.click()

            logging.info("Entering product name")
            name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_name_"))
            )
            name_field.send_keys(self.config['product']['product_name'])

            if not auto_generate:
                auto_gen_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "record_auto_generate_code"))
                )
                auto_gen_button.click()
                logging.info("Auto-generate code turned off")

                logging.info("Entering the Code")
                code_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "record_code"))
                )
                code_field.send_keys(self.config['product']['product_code'])

                logging.info("Entering the Version")
                version_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "record_version"))
                )
                version_field.send_keys(self.config['product']['version'])

            logging.info("Entering SAP Code")
            SAP_code_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_sap_code_"))
            )
            SAP_code_field.send_keys(self.config['product']['SAP_code'])

            logging.info("Clicking the Type dropdown")
            type_dropdown = Select(self.driver.find_element(By.ID, "record_type_id"))  
            type_dropdown.select_by_visible_text(self.config['product']['option'])

            exclusive_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_exclusive_flag_"))
            )
            exclusive_button.click()
            logging.info("Marked Exclusive")

            exclusive_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_price_listed_"))
            )
            exclusive_button.click()
            logging.info("Marked: Price Listed") 

            exclusive_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "record_npi_completed_"))
            )
            exclusive_button.click()
            logging.info("Marked: NPI completed") 

            logging.info("Entering Tariff/HSN Classification")
            tariff_HSN_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_hsn_classification"))
            )
            tariff_HSN_field.send_keys(self.config['product']['tariff_HSN'])
            
            logging.info("Entering Comments")
            comments_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_description"))
            )
            comments_field.send_keys(self.config['product']['comments'])

            logging.info("Entering MDG Change Request")
            MDG_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_mdg_change_request"))
            )
            MDG_field.send_keys(self.config['product']['MDG_change_request'])

            logging.info("Clicking the cancel button")
            cancel_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/p/a"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", cancel_button)
            self.driver.execute_script("arguments[0].click();", cancel_button)
            logging.info("Product creation canceled")

            time.sleep(5)

        except Exception as e:
            logging.error(f"An error occurred: {e}")
        logging.info("Function cancel_product_creation() ended")

    def search_product(self, generated_code):
        try:
            logging.info("Redirecting to the main page")
            self.driver.get(self.config['urls']['home_url'])

            logging.info("Entering the product to be searched")
            search_terms_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "main_search_terms"))
            ) 
            search_terms_field.send_keys(generated_code)

            logging.info("Clicking the search button")
            search_term_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/table/tbody/tr/td/div/form/table/tbody/tr[13]/td/input[1]"))
            )
            self.driver.execute_script("arguments[0].click();", search_term_button)
            
            logging.info("Search query entered successfully")

            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, "listDiv"))  # Assuming this ID represents the search results table
            )

            logging.info("Search results loaded successfully")
            
        except Exception as e:
            logging.error(f"An error occurred while searching for the product: {e}")
        time.sleep(10)
    
    def customer_codes(self, search_code_num):
        try:
            logging.info("Clicking the product button")
            product_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "e0_15o"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", product_button)
            product_button.click()

            logging.info("Clicking the customer code button")
            customer_codes_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, "e0_18o"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", customer_codes_button)
            customer_codes_button.click()

            logging.info("Entering the code to be searched")
            search_codes_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "linked-to-new-search-input"))
            )
            search_codes_field.send_keys(self.config['customer']['search_code_num'])

            logging.info("Clicking the search button")
            search_codes_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/form/table/tbody/tr[7]/td/input[1]"))
            )
            self.driver.execute_script("arguments[0].click();", search_codes_button)
            
            logging.info("Search code entered successfully")
        
        except UnexpectedAlertPresentException:
            try:
                # Wait for the alert to be present
                alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

                # Switch to the alert and get the alert text
                alert_text = alert.text
                logging.error(f"An unexpected alert was present: {alert_text}")

                # Dismiss the alert
                alert.accept()
            except Exception as e:
                logging.error(f"Error while handling alert: {e}")
        except Exception as e:
            logging.error(f"An error occurred while searching for the customer code: {e}")
        time.sleep(5)

    def synonyms(self, search_synonym):
        try:
            logging.info("Clicking the product button")
            product_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "e0_15o"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", product_button)
            product_button.click()

            logging.info("Clicking the synonym option")
            synonym_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, "e0_19o"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", synonym_button)
            synonym_button.click()

            logging.info("Entering the synonym  to be searched")
            search_synonym_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "as_search_synonym-search-input"))
            )
            search_synonym_field.send_keys(self.config['synonym']['search_synonym'])

            logging.info("Clicking the search button")
            search_synonym_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr/td/div/form/input[3]"))
            )
            self.driver.execute_script("arguments[0].click();", search_synonym_button)
            
            logging.info("synonym searched successfully")

        except Exception as e:
            logging.error(f"An error occurred while searching for the synonym: {e}")
        
        time.sleep(5)

    def new_development(self, dev_name):
        try:
            logging.info("Clicking the product button")
            product_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "e0_15o"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", product_button)
            product_button.click()

            logging.info("Choosing new development option")
            development_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, "e0_20o"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", development_button)
            development_button.click()

            logging.info("Entering the dev name to be created")
            dev_name_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "record_development_name_"))
            )
            dev_name_field.send_keys(self.config['development']['dev_name'])

            logging.info("Clicking the create button")
            create_dev_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/p/input"))
            )
            self.driver.execute_script("arguments[0].click();", create_dev_button)
            
            logging.info("developement created successfully")

        except UnexpectedAlertPresentException as e:
            logging.error(f"An unexpected alert is present: {e}")
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            logging.info(f"Alert text: {alert_text}")
            alert.accept()  # or alert.dismiss()

        except Exception as e:
            logging.error(f"An error occurred while creating the development: {e}")
        
        time.sleep(5)

    def customer_codes_create(self):
        try:
            logging.info("Opening the products page")
            self.driver.get("https://128.199.177.68:30443/linked_to/new")

            logging.info("Selecting product/rawmaterial search label") 
            product_rm_search_e = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/form/ol/div/li/dl/dd/input[1]"))
            )
            product_rm_search_e.send_keys(self.config['customer_details']['product_rm_search'])

            logging.info("Auto-Generate the product/raw material search")
            auto_generate_search_e = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "record_product_or_rm_search_auto_complete"))
            )
            auto_generate_search_e.click()

            logging.info("Selecting Customer")
            customer_search_e = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/form/ol/li[12]/ol/li[1]/div[1]/dl[1]/dd/input[1]"))
            )
            customer_search_e.send_keys(self.config['customer_details']['customer_search'])

            logging.info("Auto-Generate the product/raw material search")
            auto_generate_customer_search_e = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/ol/li[12]/ol/li[1]/div[1]/dl[1]/dd/div"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", auto_generate_customer_search_e)
            logging.info("Clicking the search costs button")
            self.driver.execute_script("arguments[0].click();", auto_generate_customer_search_e)

            logging.info("Auto-Generate the product/raw material search")
            auto_generate_customer_search_e = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/ol/li[12]/ol/li[1]/div[1]/dl[1]/dd/div"))
            )
            auto_generate_customer_search_e.click()

            logging.info("Enter Contact")
            enter_contact_e = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "record_contact"))
            )
            enter_contact_e.click()

            logging.info("Selecting Contact")
            select_contact_e = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/ol/li[12]/ol/li[1]/div[1]/dl[2]/dd/label/select/option[2]"))
            )
            select_contact_e.click()

            logging.info("Creating the customer code")
            create_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/p/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button)
            self.driver.execute_script("arguments[0].click();", create_button)


        except Exception as e:
            logging.error(f"An error occurred: could not create new customer code: {e}")

        time.sleep(10)
            