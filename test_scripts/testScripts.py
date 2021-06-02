from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


########################TEST 1####################

#initialize web driver and area of interest as global variables

#step 1 Open bayut.com

def openWeb(driver, website):
    driver.get(website)
    time.sleep(1)
    return driver.title


#step 2 - Select properties For Sale and input Dubai Marina

def select_and_input(driver, area):
    
    try:
    	for_sale_btn = driver.find_element_by_css_selector('.b7afbb84') #look for the "For Sale" button
    	for_sale_btn.click()
    	search_box = driver.find_element_by_css_selector('.a41c4dcc') #look for search bar
    	search_box.click()
    	search_box.send_keys(area) #type area of interest
    	search_box.send_keys(Keys.RETURN) #save location tag
    	return 1
    
    except:
    	return 0    #if the try block encounters an error, return 0, thus the test fails.
   

#step 3 - Search for properties

def search_properties(driver):
    
    try:
    	find_btn = driver.find_element_by_xpath('//*[@id="body-wrapper"]/header/div[4]/div/div[2]/div[1]/a')
    	find_btn.click() #click search button
    	return 1
    
    except:
    	return 0

#step 4 - Check results for area of interest

def check_results(driver, area):    
    
    number_of_properties_w_correct_address_per_page = 0
    time.sleep(2) # wait for page to load - not the most elegant way 
    
    try:
        area_tag = driver.find_elements_by_css_selector("[aria-label=Location]") #looks for the adress enclosed within the actual ads.
        number_of_properties_detected_per_page = driver.find_element_by_class_name('ca3976f7') # looks for the "1 to X of Y properties found" string, at the bottom of the page
        number_of_properties_detected_per_page = number_of_properties_detected_per_page.text.split(sep = " ", maxsplit= 5) # split the string above, determining how many properties per page are being displayed
        number_of_properties_per_page = int(number_of_properties_detected_per_page[2]) #element number 2 of the list is the actual number of properties displayed per page, converting it to an integer.
    
    except:
        print('Possible timeout error')
        return None   
    
    for areas in area_tag:        
        if area in (areas.text):
            number_of_properties_w_correct_address_per_page+=1 #increment by one, for each ad containing Dubai Marina.
            
    if(number_of_properties_w_correct_address_per_page == number_of_properties_per_page): # if each result contains Dubai Marina, test passes.
    	print("all displayed results contain desired location - OK")
    	return True
    	
    elif(number_of_properties_w_correct_address_per_page != number_of_properties_per_page): #test fails if number of found properties isn't equal to number of properties found within the correct location
    	print("Not all properties contain the desired search location.")
    	return False


########################TEST 2####################

#Validate Web links

#step 1 - Return to home page

def back_to_HomePage(driver, website):
    
    driver.get(website)
    time.sleep(1)
    return driver.title
    
#step 2 - click "to rent" popular searches button at the bottom of the page
def select_popular_rent(driver):
    
    try:
        toRent_btn = driver.find_element_by_css_selector('.d8530318')
        toRent_btn.click()
        return 1
    
    except:
        return 0


def locate_validateDubaiApartments_links(driver):
   
   list_of_links = []
   list_of_loaded_pages = []
   list_of_failed_pages = []
   timeout = 5 # 5 seconds - wait time for page to find _1e33cd36 
   
   elems = driver.find_elements_by_xpath("//a[contains(@href, '/to-rent/apartments/dubai/')]") #find all the href elements containing the substring
   
   for elem in elems:
       url = elem.get_attribute("href")
       list_of_links.append(url) #append found urls to list
       
   #print(list_of_links, "\n") #debug print - lists all links which contain the string '/to-rent/apartments/dubai/'
   
   for link in list_of_links:
       try:
           driver.get(link) #go to every link in the list
           element_present = EC.presence_of_element_located((By.CLASS_NAME, '_1e33cd36')) #_1e33cd36 is the selector which encloses the actual ads. (apartment, location, pictures, price etc.) 
           WebDriverWait(driver, timeout).until(element_present) #wait until found
           if(element_present): 
               list_of_loaded_pages.append(link)
               print("Succesfully loaded: ",link)
           
       except:
           list_of_failed_pages.append(link) #if page was not loaded, add it to @list_of_failed_links list.
           print("Failed loading: ", link)
        
   if not (list_of_failed_pages):  #if there are failed pages inside the list, test fails, else passes.
       return 1
   
   else:
       return 0           
           
    
       
       
       
       


    
