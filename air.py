from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 
import requests # Optional, if you want to wait for a few seconds

def check_success(driver):
    # Define this function based on your requirements
    # For now, just returning a placeholder
    return "Check success criteria here"

def get_status_code(url):
    response = requests.get(url)
    return response.status_code

def main():
    # Setup WebDriver (Chrome in this case)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Navigate to the website
        driver.get("http://altoro.testfire.net/login.jsp")

        # Find the input field and enter "Hello"
        input1 = driver.find_element(By.ID, "uid")
        input1.send_keys("hello")

        input2 = driver.find_element(By.ID, "passw")
        input2.send_keys("hello")

        # Find the "Login" button and click it
        login_button = driver.find_element(By.NAME, "btnSubmit")
        login_button.click()

        # Optionally, you can wait for the page to load or perform additional actions
        # For example, wait for a few seconds to see the result
        time.sleep(5)  # Adjust the sleep duration as needed

        result = check_success(driver)
        print("Result:", result)
        current_url = driver.current_url
        status_code = get_status_code(current_url)
        print("Status Code:", status_code)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()