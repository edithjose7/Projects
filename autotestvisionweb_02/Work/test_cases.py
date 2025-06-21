from Test.base import BaseTest
from login_page import LoginPage
from raw_material_page import RawMaterialPage
from logout_page import LogoutPage
import yaml
import logging, time

# Load configuration from YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('Login.log'),  # Log into a file named 'Login.log'
        logging.StreamHandler()
    ]
)

class TestSuite(BaseTest):
    def RM_test_case_01(self):
        login_page = LoginPage(self.driver, self.config)
        raw_material_page = RawMaterialPage(self.driver, self.config)
        logout_page = LogoutPage(self.driver)
        
        if login_page.login():
            logging.info("Login successful for Raw Material Test 01")
            raw_material_page.create_raw_material(config['rawmaterial_name'], True)
            raw_material_page.create_raw_material(config['rawmaterial_name'], False)
            logout_page.logout()
            logging.info("Logout successful for Raw Material Test 01")

        else:
            logging.error("Login failed for Raw Material Test 01")


    def RM_test_case_02(self):
        login_page = LoginPage(self.driver, self.config)
        raw_material_page = RawMaterialPage(self.driver, self.config)
        logout_page = LogoutPage(self.driver)
        

        if login_page.login():
            logging.info("Login successful for Raw Material Test 02")
            generated_code = raw_material_page.create_raw_material(config['rawmaterial_name'], True)
            raw_material_page.search_raw_material(generated_code)
            raw_material_page.delete_raw_material()
            raw_material_page.search_raw_material(generated_code)
            logout_page.logout()
            logging.info("Logout successful for Raw Material Test 02")
        
        else:
            logging.error("Login failed for Raw Material Test 02")

    
    def RM_test_case_03(self):
        login_page = LoginPage(self.driver, self.config)
        raw_material_page = RawMaterialPage(self.driver, self.config)
        logout_page = LogoutPage(self.driver)

        if login_page.login():
            logging.info("Login successful for Raw Material Test 03")
            raw_material_page.costs()
            raw_material_page.search_costs()
            raw_material_page.organoleptics()
            logout_page.logout()
            logging.info("Logout successful for Raw Material Test 03")
        
        else:
            logging.error("Login failed for Raw Material Test 03")

    def RM_test_case_04(self):
        login_page = LoginPage(self.driver, self.config)
        raw_material_page = RawMaterialPage(self.driver, self.config)
        logout_page = LogoutPage(self.driver)

        if login_page.login():
            logging.info("Login successful for Raw Material Test 04")
            raw_material_page.customer_codes_edith()
            logout_page.logout()
            logging.info("Logout successful for Raw Material Test 04")
        else:
            logging.error("Login failed for Raw Material Test 04")

if __name__ == "__main__":
    logging.info("Starting test cases...")
    test_suite = TestSuite()
    
    # Uncomment the test cases you want to run
    #test_suite.RM_test_case_01()
    #test_suite.RM_test_case_02()
    #test_suite.RM_test_case_03()
    test_suite.RM_test_case_04()


    input("Press Enter to close the browser...")
    test_suite.quit()
    logging.info("Closed the WebDriver successfully")
