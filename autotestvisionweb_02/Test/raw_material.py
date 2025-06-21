from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
import time

class RawMaterial:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_raw_material(self, auto_generate=True):
        raw_material_creation_successful = False
        generated_code = None

        try:
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
            logging.info("Clicking the new RM button")
            new_button.click()
            
            logging.info("Waiting for the rm name field to be present")
            name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_name_"))
            )
            logging.info("Entering the RM name")
            name_field.send_keys(self.config['raw_material']['rawmaterial_name'])
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
                code_field.send_keys(self.config['raw_material']['code_create_rm'])
            
            
            logging.info("Waiting for the type label to be clickable")
            type_label = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/ol/li[3]/dl/dd/label/select"))
            )
            logging.info("Selecting the type label")
            type_label.click()

            type_select_label = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/ol/li[3]/dl/dd/label/select/option[3]"))
            )
            logging.info("Entering the selected type")
            type_select_label.click()
        
            SAP_code_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_sap_code_"))
            )
            logging.info("Entering the SAP code")
            SAP_code_field.send_keys(self.config['raw_material']['SAP_code'])
            logging.info("SAP code of the rm is entered in the field")

            chemicaliupac_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_chemical_name_"))
            )
            logging.info("Entering the chemical IUPAC name")
            chemicaliupac_field.send_keys(self.config['raw_material']['chemical_name'])
            logging.info("Chemical IUPAC name of the rm is entered in the field")

            printedname_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_printed_name_"))
            )
            logging.info("Entering the printed name")
            printedname_field.send_keys(self.config['raw_material']["printed_name"])
            logging.info("Printed name of the rm is entered in the field")

            Ingridient_description_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_ingredient_declaration"))
            )
            logging.info("Entering Ingridient description")
            Ingridient_description_field.send_keys(self.config['raw_material']['Ingredient_description'])
            logging.info("Ingredient description of the rm is entered in the field")



            ECno_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_einecs_"))
            )
            logging.info("Entering EC number")
            ECno_field.send_keys(self.config['raw_material']["EC_no"])
            logging.info("EC number of the rm is entered in the field")

            CAS_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_cas_no_"))
            )
            logging.info("Entering CAS number")
            CAS_field.send_keys(self.config['raw_material']['cas_number'])
            logging.info("CAS number of the rm is entered in the field")

            CAS2_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_cas2_no_"))
            )
            logging.info("Entering CAS2 number")
            CAS2_field.send_keys(self.config['raw_material']['cas_number2'])
            logging.info("CAS2 number of the rm is entered in the field")
            
            logging.info("Clicking the legal status dropdown")
            legal_status_dropdown = Select(self.driver.find_element(By.ID, "record_legal_status_"))
            legal_status_dropdown.select_by_visible_text(self.config['raw_material']['legal_status'])

            logging.info("Clicking the FDA status dropdown")
            FDA_status_dropdown = Select(self.driver.find_element(By.ID, "record_fda_legal_status_"))
            FDA_status_dropdown.select_by_visible_text(self.config['raw_material']['FDA_status'])

            logging.info("Clicking the EU legal status dropdown")
            EU_status_dropdown = Select(self.driver.find_element(By.ID, "record_eu_legal_status_"))
            EU_status_dropdown.select_by_visible_text(self.config['raw_material']['EU_status'])
            
            logging.info("Waiting for the create button to be clickable")
            create_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/p/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button)
            logging.info("Clicking the create button")
            self.driver.execute_script("arguments[0].click();", create_button)
        
             
            # Check for the presence of a success message or specific element indicating successful creation
            success_message_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[1]/form/div/div'))  # Adjust the XPATH as needed
            )

            if success_message_element:
                logging.info("Raw Material creation was successful")
                raw_material_creation_successful = True
                       

                # Retrieve the generated code
                logging.info("Waiting for the rm button to be clickable")
                RM_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "e0_34o"))
                )
                logging.info("Clicking the rm button")
                RM_button.click()

                Search_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "e0_36o"))
                )
                logging.info("Clicking the search rm button")
                Search_button.click()
                logging.info("Clicked the search rm button successfully")

                search_rm_element_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "rm-new-search-input"))
                )
                logging.info("Click field")
                search_rm_element_field.click()

                Search_button_rm = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/form/table/tbody/tr[8]/td/input[3]"))
                )
                self.driver.execute_script("arguments[0].scrollIntoView();", Search_button_rm)
                logging.info("Clicking the search button")
                self.driver.execute_script("arguments[0].click();", Search_button_rm)
                logging.info("Waiting for the auto-generated raw material code to be visible")
                
                generated_code_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[1]/a'))  # Adjust the XPATH as needed
                )
                generated_code = generated_code_element.text
                logging.info(f"Raw Material code: {generated_code}")

        except Exception as e:
            logging.error("An error occurred while creating raw material: %s", e)

        if raw_material_creation_successful:
            logging.info("Raw Material creation successful")
            return generated_code
        else:
            logging.error("Raw Material creation unsuccessful")

            time.sleep(5)
            return None
        
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
            logging.info("Search Raw material - Passed")

            time.sleep(15)

        except Exception as e:
            logging.error("Search Raw material - Passed")
        
    def delete_raw_material(self):
        try:
            logging.info("Waiting for the delete button to be clickable")
            delete_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[15]/table/tbody/tr/td[3]/a"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", delete_button)
            logging.info("Clicking the delete button")
            self.driver.execute_script("arguments[0].click();", delete_button)
            
            logging.info("Waiting to click the YES confirm delete button")
            Yes_confirm_delete = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/div/table/tbody/tr[1]/td/div/div/div/ol/div/form/p[2]/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", Yes_confirm_delete)
            self.driver.execute_script("arguments[0].click();", Yes_confirm_delete)
            logging.info("Clicked the yes button")
            logging.info("Delete Raw material - Passed")
            time.sleep(15)

        except Exception as e:
            logging.error("Delete Raw material - Failed")
    

    def costs(self, generated_code_cost):
        try:
            rm2_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            logging.info("Clicking the RM label")
            rm2_button.click()

            costs_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_37o"))
            )
            logging.info("Clicking the costs label")
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

            RM_search_costs = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_product_or_rm_search"))
            )
            RM_search_costs.send_keys(generated_code_cost)
            logging.info("Searching for the RM in costs")

            auto_complete_costs = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/ol/li[1]/dl/dd/div"))
            )
            auto_complete_costs.click()
            logging.info("Auto-completed the required element successfully")

            Custom_Cost_per_unit_USD = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_custom_cost_"))
            )
            Custom_Cost_per_unit_USD.send_keys(self.config['raw_material']['enter_custom_costs'])
            logging.info("Custon code entered successfully")
            
            logging.info("Waiting for the create costs button to be clickable ")
            create_button_costs = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/p/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button_costs)
            logging.info("Clicking the create button")
            self.driver.execute_script("arguments[0].click();", create_button_costs)
            logging.info("Successfully created costs")
            logging.info("Create costs - Passed")
            time.sleep(15)

        except Exception as e:
            logging.error("Create costs - Failed")

    def search_costs(self, generated_code_cost):
        try:
            search_costs = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "as_cost_rm-search-input"))
            )
            logging.info("Enter cost to be searched")
            search_costs.send_keys(generated_code_cost)

            search_costs_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr/td/div/form/input[3]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", search_costs_button)
            logging.info("Clicking the search costs button")
            self.driver.execute_script("arguments[0].click();", search_costs_button)
            logging.info("Searched cost successfully")
            logging.info("Search cost - Passed")
            time.sleep(15)

        except Exception as e:
            logging.error("Search cost - Failed") 
    
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
            logging.info("Clicking the YES confirm delete button")
            Yes_confirm_delete_cost.click()
            logging.info("Delete cost - Passed")
            time.sleep(15)

        except Exception as e:
            logging.error("Delete cost - Failed")


    def search_organoleptics(self):
        try:
            rm3_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            logging.info("Clicking the RM label")
            rm3_button.click()

            organoleptics_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_38o"))
            )
            logging.info("Clicking the organoleptics element")
            organoleptics_button.click()
            logging.info("48 elements found in organoleptics")

            RM_code_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "search_rm_code"))
            )
            logging.info("Entering the RM code")
            RM_code_field.send_keys(self.config['raw_material']["RM_code_organoleptics"])
            logging.info("RM code of the rm is entered in the field")


            RM_name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "search_rm_name"))
            )
            logging.info("Entering the RM name")
            RM_name_field.send_keys(self.config['raw_material']["RM_name_organoleptics"])
            logging.info("RM name of the rm is entered in the field")


            search_organoleptics_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr/td/div/form/p/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", search_organoleptics_button)
            logging.info("Clicking the search button")
            self.driver.execute_script("arguments[0].click();", search_organoleptics_button)
            logging.info("Searched the organoleptics element successfully")
            logging.info("Search organoleptics - Passed")

            time.sleep(15)

        except Exception as e:
            logging.error("Search organoleptics - Failed")

    def flavour_development(self):
        try:
            rm4_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            logging.info("Clicking the rm button")
            rm4_button.click()

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
            fema_no_flavour.send_keys(self.config['raw_material']['fema_no_flavour'])
            logging.info("Entering fema number of flavour")

            flavour_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_flavour_search"))
            )
            logging.info("Entering flavour")
            flavour_field.send_keys(self.config['raw_material']["enter_flavour"])
            logging.info("Flavour of the rm is entered in the field")

            time.sleep(10)

            auto_complete_flavour = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/ol/li[2]/dl/dd/div"))
            )
            auto_complete_flavour.click()
            logging.info("Clicked auto generate flavour successfully")

            time.sleep(10)

            create_button_flavour = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/p/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button_flavour)
            self.driver.execute_script("arguments[0].click();", create_button_flavour)
            logging.info("Clicking the create button")
            logging.info("Create Flavour development - Passed" )
            time.sleep(35)

        except Exception as e:
            logging.error("Create Flavour development - Failed" )

    def empty_search(self):
        try:
            logging.info("Waiting for the rm button to be clickable")
            RM_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            logging.info("Clicking the rm button")
            RM_button.click()

            Search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_36o"))
            )
            logging.info("Clicking the search rm button")
            Search_button.click()
            logging.info("Clicked the search rm button successfully")

            search_rm_element_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "rm-new-search-input"))
            )
            logging.info("Click field")
            search_rm_element_field.click()

            Search_button_rm = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/form/table/tbody/tr[8]/td/input[3]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", Search_button_rm)
            logging.info("Clicking the search button")
            self.driver.execute_script("arguments[0].click();", Search_button_rm)
            logging.info("Waiting for the auto-generated raw material code to be visible")

            generated_code_costs = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[1]/a'))
            )
            generated_code_cost = generated_code_costs.text
            logging.info(f"Auto-generated product code: {generated_code_cost}")
            logging.info("Empty search- Passed ")
            return generated_code_cost
        
        except Exception as e:
            logging.error("Empty search - Failed" )

