from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
import time

class RawMaterialPage:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_raw_material(self, rawmaterial_name, auto_generate=True):
        try:
            logging.info("Redirecting to the main page")
            self.driver.get("https://128.199.177.68:30443/product/list")
            
            logging.info("Waiting for the rm button to be clickable")
            rm_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            logging.info("Clicking the rm button")
            rm_button.click()

            logging.info("Waiting for the new rm button to be clickable")
            new_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_35o"))
            )
            logging.info("Clicking the new rm button")
            new_button.click()

            logging.info("Waiting for the rm name field to be present")
            name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_name_"))
            )
            logging.info("Entering rm name")
            name_field.send_keys(self.config['rawmaterial_name'])
            logging.info("Name of the rm is entered in name field")
        

            if not auto_generate:
                logging.info("Turning off auto-generate code")
                auto_gen_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "record_auto_generate_code"))
                )
                auto_gen_button.click()
                logging.info("Auto-generate code turned off")

                code_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "record_code"))
                )
                logging.info("Entering code manually")
                code_field.send_keys(self.config['code_create_rm'])
                logging.info("Code of the rm is entered in name field")
            
            logging.info("Waiting for the type label to be clickable")
            type_label = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/ol/li[3]/dl/dd/label/select"))
            )
            logging.info("Clicking type label")
            type_label.click()
            logging.info("Selected the type field")

            logging.info("Selecting Type")
            type_select_label = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/ol/li[3]/dl/dd/label/select/option[3]"))
            )
            logging.info("Entering the selected type")
            type_select_label.click()
            
            logging.info("Waiting for SAP code to be present")
            SAP_code_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_sap_code_"))
            )
            logging.info("Entering SAP code")
            SAP_code_field.send_keys(self.config['SAP_code'])
            logging.info("SAP code of the rm is entered in the field")

            logging.info("Waiting for the IUPAC name field to be present")
            chemicaliupac_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_chemical_name_"))
            )
            logging.info("Entering chemical IUPAC name")
            chemicaliupac_field.send_keys(self.config['chemical_name'])
            logging.info("Chemical IUPAC name of the rm is entered in the field")

            logging.info("Waiting for the printed name field to be present")
            printedname_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_printed_name_"))
            )
            logging.info("Entering printed name")
            printedname_field.send_keys(self.config["printed_name"])
            logging.info("Printed name of the rm is entered in the field")

            logging.info("Waiting for Ingridient description code to be present")
            Ingridient_description_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_ingredient_declaration"))
            )
            logging.info("Entering Ingridient Description ")
            Ingridient_description_field.send_keys(self.config['Ingredient_description'])
            logging.info("Ingredient description of the rm is entered in the field")

            logging.info("Waiting for the EC number field to be present")
            ECno_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_einecs_"))
            )
            logging.info("Entering EC number")
            ECno_field.send_keys(self.config["EC_no"])
            logging.info("EC number of the rm is entered in the field")

            logging.info("Waiting for the CAS number field to be present")
            CAS_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_cas_no_"))
            )
            logging.info("Entering CAS number")
            CAS_field.send_keys(self.config['cas_number'])
            logging.info("CAS number of the rm is entered in the field")

            logging.info("Waiting for the CAS2 number field to be present")
            CAS2_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_cas2_no_"))
            )
            logging.info("Entering CAS2 number")
            CAS2_field.send_keys(self.config['cas_number2'])
            logging.info("CAS2 number of the rm is entered in the field")

            logging.info("Clicking the legal status dropdown")
            legal_status_dropdown = Select(self.driver.find_element(By.ID, "record_legal_status_"))
            legal_status_dropdown.select_by_visible_text(self.config['legal_status'])

            logging.info("Clicking the FDA status dropdown")
            FDA_status_dropdown = Select(self.driver.find_element(By.ID, "record_fda_legal_status_"))
            FDA_status_dropdown.select_by_visible_text(self.config['FDA_status'])

            logging.info("Clicking the EU legal status dropdown")
            EU_status_dropdown = Select(self.driver.find_element(By.ID, "record_eu_legal_status_"))
            EU_status_dropdown.select_by_visible_text(self.config['EU_status'])

            logging.info("Waiting for the create button to be clickable")
            create_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "commit"))
            )
            logging.info("Scrolling to create button")
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button)
            logging.info("Clicking the create button")
            self.driver.execute_script("arguments[0].click();", create_button)
            logging.info("Raw material is successfully created")

            time.sleep(15)
            
            if auto_generate:
                raw_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "e0_34o"))
                )
                raw_button.click()
                search_raw = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "e0_36o"))
                )
                search_raw.click()
                search_button_rm = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/form/table/tbody/tr[8]/td/input[3]"))
                )
                self.driver.execute_script("arguments[0].scrollIntoView();", search_button_rm)
                logging.info("Clicking the search button")
                self.driver.execute_script("arguments[0].click();", search_button_rm)
                logging.info("Waiting for the auto-generated product code to be visible")
                generated_code_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[1]/a'))
                )
                generated_code = generated_code_element.text
                logging.info(f"Auto-generated product code: {generated_code}")
                return generated_code
        
            

        except Exception as e:
            logging.error(f"Raw Material not created: {e}")

    def search_raw_material(self, generated_code):
        try:
            logging.info("Waiting for the rm button to be clickable")
            rm1_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            logging.info("Clicking the rm button")
            rm1_button.click()

            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_36o"))
            )
            logging.info("Clicking the search rm button")
            search_button.click()
            logging.info("Clicked the search rm button successfully")

            logging.info("Waiting for the search rm button to be clickable")
            search_rm_element_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "rm-new-search-input"))
            )
            logging.info("Entering element to be searched")
            search_rm_element_field.send_keys(generated_code)
            logging.info("Raw Material to be searched is enetered in the field")

            logging.info("Waiting for the search button to be clickable")
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/form/table/tbody/tr[8]/td/input[3]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", search_button)
            logging.info("Clicking the search button")
            self.driver.execute_script("arguments[0].click();", search_button)
            logging.info("Raw Material searched successfully")

            time.sleep(15)

        except Exception as e:
            logging.error(f"Could not Search the Raw Material: {e}")
        
    def delete_raw_material(self):
        try:
            
            logging.info("Waiting to click the delete button")
            delete_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[15]/table/tbody/tr/td[8]/a"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", delete_button)
            logging.info("Clicking the delete button")
            self.driver.execute_script("arguments[0].click();", delete_button)
            
            logging.info("Waiting to click the delete button")
            Yes_confirm_delete = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/div/table/tbody/tr[3]/td/div/div/div/ol/div/form/p[2]/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", Yes_confirm_delete)
            logging.info("Clicking the delete button")
            self.driver.execute_script("arguments[0].click();", Yes_confirm_delete)

            time.sleep(15)

        except Exception as e:
            logging.error(f"Could not Delete the Raw Material: {e}")
    

    def costs(self):
        try:
            logging.info("Waiting for the rm button to be clickable")
            rm2_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            logging.info("Clicking the rm button")
            rm2_button.click()

            logging.info("Waiting for the costs button to be clickable")
            costs_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_37o"))
            )
            logging.info("Clicking the costs button")
            costs_button.click()
            logging.info("Clicked the costs button successfully")
            logging.info("0 elements found in costs")

            logging.info("Creating new Costs")
            create_new_costs = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/a[2]"))
            )
            logging.info("Clicking the create new costs button")
            create_new_costs.click()
            logging.info("Created new cost successfully")

            logging.info("Waiting for the RM search costs button to be clickable")
            RM_search_costs = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_product_or_rm_search"))
            )
            RM_search_costs.send_keys(self.config['search_costs'])
            logging.info("Searching for the RM in costs")

            logging.info("Clicking auto completer")
            auto_complete_costs = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/ol/li[1]/dl/dd/div"))
            )
            auto_complete_costs.click()
            logging.info("Clicked auto generate successfully")

            logging.info("Waiting for the Custom Cost per unit (USD) lable")
            Custom_Cost_per_unit_USD = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_custom_cost_"))
            )
            Custom_Cost_per_unit_USD.send_keys(self.config['enter_custom_costs'])
            logging.info("Entered the Cost for Custom Cost per unit (USD) for the RM")


            logging.info("Waiting for the create button to be clickable")
            create_button_costs = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/p/input"))
            )
            logging.info("Scrolling to create button")
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button_costs)
            logging.info("Clicking the create button")
            self.driver.execute_script("arguments[0].click();", create_button_costs)

            time.sleep(15)

        except Exception as e:
            logging.error(f"An error occurred: could not click raw material costs  : {e}")

    def search_costs(self):
        try:
            logging.info("Waiting for the search costs field to be clickable")
            search_costs = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "as_cost_rm-search-input"))
            )
            search_costs.send_keys(self.config['cost_to_be_searched'])

            logging.info("Waiting for the search costs button to be clickable")
            search_costs_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr/td/div/form/input[3]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", search_costs_button)
            logging.info("Clicking the search costs button")
            self.driver.execute_script("arguments[0].click();", search_costs_button)
            logging.info("Cost searched successfully")

            time.sleep(15)

        except Exception as e:
            logging.error(f"An error occurred: could not search the given cost : {e}")    
    
    def delete_costs(self):
        try:
            logging.info("Waiting to click the delete button")
            delete_costs_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "as_cost_rm-destroy-1648-link"))
            )
            logging.info("Clicking the delete button")
            delete_costs_button.click()
            
            logging.info("Waiting to click the YES button")
            Yes_confirm_delete_cost = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, ""))
            )
            logging.info("Clicking the YES button")
            Yes_confirm_delete_cost.click()

            time.sleep(15)

        except Exception as e:
            logging.error(f"An error occurred: could not delete the required cost  : {e}")


    def organoleptics(self):
        try:
            logging.info("Waiting for the rm button to be clickable")
            rm3_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            logging.info("Clicking the rm button")
            rm3_button.click()

            logging.info("Waiting for the organoleptics button to be clickable")
            organoleptics_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_38o"))
            )
            logging.info("Clicking the organoleptics button")
            organoleptics_button.click()
            logging.info("Clicked the organoleptics button successfully")
            logging.info("46 elements found in organoleptics")

            logging.info("Waiting for the RM code field to be present")
            RM_code_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "search_rm_code"))
            )
            logging.info("Entering RM code name")
            RM_code_field.send_keys(self.config["RM_code_organoleptics"])
            logging.info("RM code of the rm is entered in the field")

            logging.info("Waiting for the RM name field to be present")
            RM_name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "search_rm_name"))
            )
            logging.info("Entering RM name")
            RM_name_field.send_keys(self.config["RM_name_organoleptics"])
            logging.info("RM name of the rm is entered in the field")

            logging.info("Waiting for the organoleptics search button to be clickable")
            search_organoleptics_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr/td/div/form/p/input"))
            )
            logging.info("Clicking the search button")
            self.driver.execute_script("arguments[0].click();", search_organoleptics_button)
            logging.info("RM organoleptics element searched successfully")

            time.sleep(15)

        except Exception as e:
            logging.error(f"An error occurred: could not click raw material organoleptics : {e}")

    def flavour_development(self):
        try:
            logging.info("Waiting for the rm button to be clickable")
            rm4_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            logging.info("Clicking the rm button")
            rm4_button.click()

            logging.info("Waiting for the flavour development button to be clickable")
            flavour_development_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_39o"))
            )
            logging.info("Clicking the flavour development button")
            flavour_development_button.click()
            logging.info("Clicked the flavour development button successfully")

            create_new_flavour = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/a"))
            )
            logging.info("Clicking the create new flavour button")
            create_new_flavour.click()
            logging.info("Created new flavour successfully")

            fema_no_flavour = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_fema_no_"))
            )
            fema_no_flavour.send_keys(self.config['fema_no_flavour'])
            logging.info("Entering fema number of flavour")

            flavour_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_flavour_search"))
            )
            logging.info("Entering flavour")
            flavour_field.send_keys(self.config["enter_flavour"])
            logging.info("Flavour of the rm is entered in the field")

            time.sleep(10)

            logging.info("Clicking auto completer")
            auto_complete_flavour = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/ol/li[2]/dl/dd/div"))
            )
            auto_complete_flavour.click()
            logging.info("Clicked auto generate flavour successfully")

            time.sleep(10)

            logging.info("Waiting for the create button to be clickable")
            create_button_flavour = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/p/input"))
            )
            logging.info("Scrolling to create button")
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button_flavour)
            logging.info("Clicking the create button")
            self.driver.execute_script("arguments[0].click();", create_button_flavour)

            time.sleep(35)

        except Exception as e:
            logging.error(f"An error occurred: could not create flavour developement : {e}")