from selenium import webdriver
import unittest
from test_scripts import testScripts

class Test_1_DubaiMarina(unittest.TestCase):
    
    def test_step1_openChrome(self):
        self.assertEqual(testScripts.openWeb(driver, website), "Bayut: UAE's Largest Real Estate Portal")
    
    def test_step2_select_and_input(self):
        self.assertEqual(testScripts.select_and_input(driver, area_of_interest), True)
            
    def test_step3_search_properties(self):
     	self.assertEqual(testScripts.search_properties(driver), True)
     	
    def test_step4_check_results(self):
    	self.assertEqual(testScripts.check_results(driver, area_of_interest), True)
    
    

class Test_2_ValidateLinks(unittest.TestCase):
    
        # return to home page, as prerequisite to the second test. Verify browser is back on home page. 
        def test_step1_returnHome(self): 
            self.assertEqual(testScripts.back_to_HomePage(driver, website), "Bayut: UAE's Largest Real Estate Portal")
        
        def test_step2_popularRent(self):
            self.assertEqual(testScripts.select_popular_rent(driver), 1)
        
        def test_step3_popularRent_verifyLinks(self):
            self.assertEqual(testScripts.locate_validateDubaiApartments_links(driver, timeout_wait), 1)
    

        
#script starts here		
#init global objects

driver = webdriver.Chrome("/usr/bin/chromedriver") 
website = 'https://bayut.com'
area_of_interest = 'Dubai Marina'  
timeout_wait = 5 #global timeout wait time

if __name__ == '__main__':
    
    #tests start here
    unittest.main(verbosity = 2)
    
    
