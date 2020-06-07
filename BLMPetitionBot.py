#Drivers for Chrome Headless Browser
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)

#SETUP

# Headless
opts = webdriver.FirefoxOptions()
# opts.headless = True

# Set Driver
driver = webdriver.Firefox(executable_path="./geckodriver", options=opts)
set_viewport_size(driver, 800, 600)
driver.get('https://blacklivesmatters.carrd.co/#more')

# Get Change.org Petitions
search_text = "www.change.org"
links = driver.find_elements_by_xpath('//a[contains(@href, "%s")]' % search_text)
petition_list = []

# Set Count of Petitions
count = 0

#Function to emulate human input and avoid Captcha
def send_keys_delay_random(controller,keys,min_delay=0.05,max_delay=0.25):
    for key in keys:
        controller.send_keys(key)
        time.sleep(random.uniform(min_delay,max_delay))

def SignPetitions():
    # Append links into list
    for link in links:
        petition_list.append(link.get_attribute("href"))

    # Banner Displaying Petitions
    print("------- Below are the petitions that will be signed -------")
    print("")
    for petition in petition_list:
        print(petition)
    print("")

    # Set Sign In Fields
    first_name = input("Please enter your first name to sign petitions: ")
    last_name = input("Please provide your last name to sign petitions: ")
    email = input("Please provide your email to sign petitions: ")

    # Set Count
    success_count = 0
    total_count = 0

    # Iterate Through Petitions
    for petition in petition_list:

        # Open Petition Page and Avoid Session Timeout
        driver.delete_all_cookies()
        driver.get(petition)
        driver.refresh()

        # sleep avoid RC
        time.sleep(2.0)

        # Username Input
        try:
            First_Name = driver.find_element_by_id('firstName')
            send_keys_delay_random(First_Name, first_name, min_delay=0.05, max_delay=0.25)
        except:
            pass

        # Sleep to prevent race conditions
        time.sleep(1.0)
        # Password Input
        try:
            Last_Name = driver.find_element_by_id('lastName')
            send_keys_delay_random(Last_Name, last_name, min_delay=0.05, max_delay=0.25)
        except:
            pass

        # Sleep to prevent race conditions
        time.sleep(1.0)

        # Email Input
        try:
            Email_Field = driver.find_element_by_id('email')
            send_keys_delay_random(Email_Field, email, min_delay=0.05, max_delay=0.25)
        except:
            pass

        # Sleep to prevent race conditions
        time.sleep(2.0)

        # Submit Petition
        page = driver.find_element_by_xpath("//body")
        page.send_keys(Keys.RETURN)

        # Sleep to prevent race conditions
        time.sleep(5.0)

        #Check to see if confirmation happened

        try:
            confirmation = driver.find_element_by_xpath('//*[@data-testid="flash-message"]')
            confirmation = True
        except NoSuchElementException:
            print('You got stuck on a captcha')
            confirmation = False

        #Attempt to prevent captcha
        driver.delete_all_cookies()

        # Sleep to prevent race conditions
        time.sleep(5.0)

        # Sign_Button = driver.find_element_by_xpath('//*[@type="submit"]')
        # Sign_Button.click()

        total_count = total_count + 1

        # Summary Banner
        print("")
        print("**----------------Petition Summary----------------**")
        if confirmation == True:
            print("")
            print("The following petition has been signed: " + str(petition))
        print("")

        #Count if confirmation received
        if confirmation == True:
            success_count = success_count + 1
        elif confirmation == False:
            print("Oh No! You've been Captcha'ed! Skipping Petition and Moving to Next...")
            print("")

        print("Total Petitions Signed: " + str(success_count))
        print("Total Petitions Attempted: " + str(success_count))

        print("Signing Next Petition...")
        print("")

    # Completion Output
    print("successful signing")
    print("You have successfully signed " + str(success_count) + " petitions out of " + str(total_count) + " thank you.")

def main():
    SignPetitions()


main()






