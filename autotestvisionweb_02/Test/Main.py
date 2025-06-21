import logging
import yaml
from selenium import webdriver
from base import Base
from login import Login
from product import Product
from raw_material import RawMaterial

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
            
class TestProducts(Base):
    def login(self):
        login = Login(self.driver, config)
        login.login()

    def Products_test(self):
        login = Login(self.driver, config)
        if login.login():
            logging.info("Login successful")

            # Create Product
            product = Product(self.driver, config)
            product_name = config['product']['product_name']
            generated_code = product.create_product(auto_generate=True)
            self.driver.get(config['urls']['home_url'])
            product.create_product(auto_generate=False)
            logging.info(f"Product '{product_name}' created")

            # Cancelling Product Creation
            product.cancel_product_creation(product_name, auto_generate=True)
    
            # Search Product
            product.search_product(generated_code)
            logging.info(f"Product searched")
            
            # Customer Codes
            product.customer_codes(self)

            # Synonyms
            product.synonyms(self)
            
            # New Development
            product.new_development(self)

            self.driver.get(config['urls']['home_url'])
            
            # Logout
            login.logout()
            logging.info("Logout successful")
            
        else:
            logging.error("Login failed")

    def product_test_create(self):
        login = Login(self.driver, config)
        if login.login():
            logging.info("Login successful")
            
            # Create Product
            product = Product(self.driver, config)
            product_name = config['product']['product_name']
            product.create_product(auto_generate=True)
            '''
            self.driver.get(config['urls']['home_url'])
            product.create_product(auto_generate=False)
            logging.info(f"Product '{product_name}' created")
            '''
            # Logout
            login.logout()
            logging.info("Logout successful")
        else:
            logging.error("Login failed")

    def product_test_search(self): # Search for a product
        login = Login(self.driver, config)
        if login.login():
            logging.info("Login successful")
            
            # Create Product
            product = Product(self.driver, config)
            product_name = config['product']['product_name']
            generated_code = product.create_product(auto_generate=True)
            logging.info(f"Product '{product_name}' created with auto-generated code: {generated_code}")

            # Search Product
            product.search_product(generated_code)
            logging.info(f"Product with code '{generated_code}' searched")

            # Delete Product
            product.delete_product()
            logging.info("Product Deleted")

            product.search_product(generated_code)
            logging.info(f"Product with code '{generated_code}' searched again after deletion")
            
            # Logout
            login.logout()
            logging.info("Logout successful")
        else:
            logging.error("Logout failed")

    def customer_code(self):
        login = Login(self.driver, config)
        if login.login():
            product = Product(self.driver, config)
            logging.info("Login successful")
            product.customer_codes_create()
            logging.info("Customer code created succesfully")
            login.logout()
            logging.info("Logout successful")
        else:
            logging.error("Logout failed")

class TestSuite(Base):
    def RM_test_case_01(self):
        login = Login(self.driver, config)
        if login.login():
            raw_material = RawMaterial(self.driver, config)
            logging.info("Login successful for Raw Material Test 01")
            raw_material.create_raw_material(True)
            raw_material.create_raw_material(False)
            login.logout()
            logging.info("Logout successful for Raw Material Test 01")

        else:
            logging.error("Login failed for Raw Material Test 01")


    def RM_test_case_02(self):
        login = Login(self.driver, config)
        if login.login():
            raw_material = RawMaterial(self.driver, config)
            logging.info("Login successful for Raw Material Test 02")
            generated_code = raw_material.create_raw_material(True)
            raw_material.search_raw_material(generated_code)
            raw_material.delete_raw_material()
            raw_material.search_raw_material(generated_code)
            login.logout()
            logging.info("Logout successful for Raw Material Test 02")
        
        else:
            logging.error("Login failed for Raw Material Test 02")

    
    def RM_test_case_03(self):
        login = Login(self.driver, config)
        
        if login.login():
            raw_material = RawMaterial(self.driver, config)
            logging.info("Login successful for Raw Material Test 03")
            generated_code_cost = raw_material.empty_search()
            raw_material.costs(generated_code_cost)
            raw_material.search_costs(generated_code_cost)
            raw_material.search_organoleptics()
            login.logout()
            logging.info("Logout successful for Raw Material Test 03")
        
        else:
            logging.error("Login failed for Raw Material Test 03")

    def RM_test_case_04(self):
        login = Login(self.driver, config)
        
        if login.login():
            raw_material = RawMaterial(self.driver, config)
            logging.info("Login successful for Raw Material Test 04")
            raw_material.customer_codes_edith()
            login.logout()
            logging.info("Logout successful for Raw Material Test 04")
        
        else:
            logging.error("Login failed for Raw Material Test 04")


if __name__ == "__main__":
    '''
    test_products = TestProducts()
    
    test_products.login()
    test_products.product_test_create()
    test_products.Products_test()
    test_products.product_test_search()
    test_products.customer_code()
    '''
    test_suite = TestSuite()
    
    test_suite.RM_test_case_01()
    test_suite.RM_test_case_02()
    test_suite.RM_test_case_03()
