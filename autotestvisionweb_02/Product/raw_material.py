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
        try:
            self.driver.get("https://128.199.177.68:30443/product/list")
    
            rm_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            rm_button.click()

            new_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_35o"))
            )
            new_button.click()

            name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_name_"))
            )
            name_field.send_keys(self.config['raw_material']['rawmaterial_name'])
        

            if not auto_generate:
                auto_gen_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "record_auto_generate_code"))
                )
                auto_gen_button.click()

                code_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "record_code"))
                )
                code_field.send_keys(self.config['raw_material']['code_create_rm'])
            
            type_label = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/ol/li[3]/dl/dd/label/select"))
            )
            type_label.click()

            type_select_label = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/ol/li[3]/dl/dd/label/select/option[3]"))
            )
            type_select_label.click()
        
            SAP_code_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_sap_code_"))
            )
            SAP_code_field.send_keys(self.config['raw_material']['SAP_code'])

            chemicaliupac_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_chemical_name_"))
            )
            chemicaliupac_field.send_keys(self.config['raw_material']['chemical_name'])

            printedname_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_printed_name_"))
            )
            printedname_field.send_keys(self.config['raw_material']["printed_name"])

            Ingridient_description_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_ingredient_declaration"))
            )
            Ingridient_description_field.send_keys(self.config['raw_material']['Ingredient_description'])

            ECno_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_einecs_"))
            )
            ECno_field.send_keys(self.config['raw_material']["EC_no"])

            CAS_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_cas_no_"))
            )
            CAS_field.send_keys(self.config['raw_material']['cas_number'])

            CAS2_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_cas2_no_"))
            )
            CAS2_field.send_keys(self.config['raw_material']['cas_number2'])

            legal_status_dropdown = Select(self.driver.find_element(By.ID, "record_legal_status_"))
            legal_status_dropdown.select_by_visible_text(self.config['raw_material']['legal_status'])

            FDA_status_dropdown = Select(self.driver.find_element(By.ID, "record_fda_legal_status_"))
            FDA_status_dropdown.select_by_visible_text(self.config['raw_material']['FDA_status'])

            EU_status_dropdown = Select(self.driver.find_element(By.ID, "record_eu_legal_status_"))
            EU_status_dropdown.select_by_visible_text(self.config['raw_material']['EU_status'])

            create_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "commit"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button)
            self.driver.execute_script("arguments[0].click();", create_button)
            logging.info("Create Raw material without autogenerate- Passed ")

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
                self.driver.execute_script("arguments[0].click();", search_button_rm)

                generated_code_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[1]/a'))
                )
                generated_code = generated_code_element.text
                logging.info("Create Raw material with autogenerate- Passed ")
                return generated_code

        except:
            logging.error("Create Raw material - Failed")

    def search_raw_material(self, generated_code):
        try:
            rm1_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            rm1_button.click()

            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_36o"))
            )
            search_button.click()

            search_rm_element_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "rm-new-search-input"))
            )
            search_rm_element_field.send_keys(generated_code)
            
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/form/table/tbody/tr[8]/td/input[3]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", search_button)
            self.driver.execute_script("arguments[0].click();", search_button)
            logging.info("Search Raw material - Passed")

            time.sleep(15)

        except:
            logging.error("Search Raw material - Failed")
        
    def delete_raw_material(self):
        try:
            delete_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[15]/table/tbody/tr/td[3]/a"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", delete_button)
            self.driver.execute_script("arguments[0].click();", delete_button)

            Yes_confirm_delete = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr/td/div/div/table/tbody/tr[1]/td/div/div/div/ol/div/form/p[2]/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", Yes_confirm_delete)
            self.driver.execute_script("arguments[0].click();", Yes_confirm_delete)
            logging.info("Delete Raw material - Passed")
            time.sleep(15)

        except:
            logging.error("Delete Raw material - Failed")
    

    def costs(self):
        try:
            rm2_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            rm2_button.click()

            costs_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_37o"))
            )
            costs_button.click()

            create_new_costs = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/a[2]"))
            )
            create_new_costs.click()

            RM_search_costs = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_product_or_rm_search"))
            )
            RM_search_costs.send_keys(self.config['raw_material']['search_costs'])

            auto_complete_costs = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/ol/li[1]/dl/dd/div"))
            )
            auto_complete_costs.click()

            Custom_Cost_per_unit_USD = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_custom_cost_"))
            )
            Custom_Cost_per_unit_USD.send_keys(self.config['raw_material']['enter_custom_costs'])
       
            create_button_costs = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/p/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button_costs)
            self.driver.execute_script("arguments[0].click();", create_button_costs)
            logging.info("Create cost - Passed")
            time.sleep(15)

        except:
            logging.error("Create cost - Failed")

    def search_costs(self):
        try:
            search_costs = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "as_cost_rm-search-input"))
            )
            search_costs.send_keys(self.config['raw_material']['cost_to_be_searched'])

            search_costs_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr/td/div/form/input[3]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", search_costs_button)
            self.driver.execute_script("arguments[0].click();", search_costs_button)
            logging.info("Search cost - Passed")
            time.sleep(15)

        except Exception as e:
            logging.error("Search cost - Failed")    
    
    def delete_costs(self):
        try:
            delete_costs_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "as_cost_rm-destroy-1648-link"))
            )
            delete_costs_button.click()
            
            Yes_confirm_delete_cost = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, ""))
            )
            Yes_confirm_delete_cost.click()
            logging.info("Delete cost - Passed")
            time.sleep(15)

        except Exception as e:
            logging.error("Delete cost - Failed")

    def create_organoleptics(self):
        try:
            organoleptics = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/ul/li[3]/a"))
            )
            organoleptics.click()

            create_new_organoleptics = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div/div[1]/div/a[1]"))
            )
            create_new_organoleptics.click()

            family_label = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "record_family_1cc476b0518ca84e98a03f68a6f0c1ae"))
            )
            family_label.click()

            select_family_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div/table/tbody/tr[1]/td/div/form/ol/li[1]/dl/dd/select/option[9]"))
            )
            select_family_dropdown.click()

            strength_label = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "record_strength_1cc476b0518ca84e98a03f68a6f0c1ae"))
            )
            strength_label.click()

            select_strength_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div/table/tbody/tr[1]/td/div/form/ol/li[2]/dl/dd/select/option[3]"))
            )
            select_strength_dropdown.click()

            taste_label = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "record_profile_descriptor_1cc476b0518ca84e98a03f68a6f0c1ae_organoleptic_taste_descriptor_1719466772499"))
            )
            taste_label.click()

            select_taste_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div/table/tbody/tr[1]/td/div/form/ol/li[4]/div/table/tbody/tr/td[2]/dl/dd/select/option[28]"))
            )
            select_taste_dropdown.click()

            create_button_o = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div/table/tbody/tr[1]/td/div/form/p/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button_o)
            self.driver.execute_script("arguments[0].click();", create_button_o)
            logging.info("Create organoleptics- Passed ")
        
        except Exception as e:
            logging.error("Create organoleptics - Failed")

    def search_organoleptics(self):
        try:
            rm3_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            rm3_button.click()

            organoleptics_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_38o"))
            )
            organoleptics_button.click()

            RM_code_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "search_rm_code"))
            )
            RM_code_field.send_keys(self.config['raw_material']["RM_code_organoleptics"])

            RM_name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "search_rm_name"))
            )
            RM_name_field.send_keys(self.config['raw_material']["RM_name_organoleptics"])

            search_organoleptics_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr/td/div/form/p/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", search_organoleptics_button)
            self.driver.execute_script("arguments[0].click();", search_organoleptics_button)
            logging.info("Search organoleptics - Passed")

            time.sleep(15)

        except Exception as e:
            logging.error("Search organoleptics - Failed")

    def flavour_development(self):
        try:
            rm4_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_34o"))
            )
            rm4_button.click()

            flavour_development_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "e0_39o"))
            )
            flavour_development_button.click()

            create_new_flavour = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/a"))
            )
            create_new_flavour.click()

            fema_no_flavour = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_fema_no_"))
            )
            fema_no_flavour.send_keys(self.config['raw_material']['fema_no_flavour'])

            flavour_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "record_flavour_search"))
            )
            flavour_field.send_keys(self.config['raw_material']["enter_flavour"])

            time.sleep(10)

            auto_complete_flavour = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/ol/li[2]/dl/dd/div"))
            )
            auto_complete_flavour.click()

            time.sleep(10)

            create_button_flavour = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/table/tbody/tr[1]/td/div/form/p/input"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", create_button_flavour)
            self.driver.execute_script("arguments[0].click();", create_button_flavour)
            logging.info("Create Flavour development - Passed" )
            time.sleep(35)

        except Exception as e:
            logging.error("Create flavour developement - Failed")