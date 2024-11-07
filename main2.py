from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace with your LinkedIn credentials
username = 'lakshmanangokul2q@gmail.com'
password = 'gokulgokul1108@'

# Set up Chrome WebDriver with additional options
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome()

try:
    # Step 1: Open LinkedIn login page
    driver.get("https://www.linkedin.com/login")

    # Step 2: Log in to LinkedIn
    email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    email_element.send_keys(username)

    password_element = driver.find_element(By.ID, "password")
    password_element.send_keys(password)
    password_element.send_keys(Keys.RETURN)

    # Wait for login to complete
    time.sleep(5)

    # Step 3: Navigate to the LinkedIn profile contact info overlay
    profile_url = "https://www.linkedin.com/in/gokulr1108/overlay/contact-info/"
    driver.get(profile_url)

    # Allow time for the profile page to load
    time.sleep(5)

    # Step 4: Locate and print the profile name
    try:
        profile_name_element = driver.find_element(By.TAG_NAME, "h1")
        profile_name = profile_name_element.text
        print("Profile Name:", profile_name)
    except Exception as e:
        print("Failed to locate the profile name element.")

    # Step 5: Locate the email address in the contact information section
    try:
        # Locate the email element by its tag or CSS selector
        email_element = driver.find_element(By.CSS_SELECTOR, "a[href^='mailto:']")
        email = email_element.get_attribute("href").replace("mailto:", "")
        print("Email:", email)
    except Exception as e:
        print("Failed to locate the email address.")

except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()
