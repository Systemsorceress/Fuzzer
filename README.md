# Fuzzer
# Selenium Login Script with Status Code and Header Check

## Overview

This Python script uses Selenium to automate login attempts on a website. It reads login credentials from a file, attempts to log in using the credentials, and checks if the login is successful by comparing URLs. Additionally, it fetches the HTTP status code and response headers of the current page after each login attempt.

## Prerequisites

- Install Python (>= 3.6)
- Install the required libraries by running:

   ```bash
   pip install selenium webdriver-manager requests
 ```
Ensure that Chrome browser is installed on your system.

 ```bash
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

def check_success(driver, initial_url):
    current_url = driver.current_url
    if current_url != initial_url:
        return True, current_url
    else:
        return False, current_url

def get_status_code_and_headers(url):
    response = requests.get(url)
    return response.status_code, response.headers

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        initial_url = "http://altoro.testfire.net/login.jsp"
        driver.get(initial_url)

        with open("login.txt", "r") as file:
            for line in file:
                # Strip any leading/trailing whitespace from the line
                payload = line.strip()

                # Find the input fields and insert the payload
                input1 = driver.find_element(By.ID, "uid")
                input1.clear()
                input1.send_keys(payload)

                input2 = driver.find_element(By.ID, "passw")
                input2.clear()
                input2.send_keys(payload)

                # Click the login button
                login_button = driver.find_element(By.NAME, "btnSubmit")
                login_button.click()

                # Wait for the page to load
                time.sleep(5)

                # Check if the login was successful
                success, current_url = check_success(driver, initial_url)
                status_code, headers = get_status_code_and_headers(current_url)

                if success:
                    print("Login successful")
                    print("Status Code:", status_code)
                    print("Response Headers:", headers)
                    break
                else:
                    print(f"Login unsuccessful with payload: {payload}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
 ```
Instructions
Login Attempts:

The script reads login credentials from a file named login.txt.
The login page fields are identified by their respective IDs (uid for username and passw for password).
It attempts a login by clicking the button with the name btnSubmit.
Checking Success:

After submitting the login form, the script waits for 5 seconds to allow the page to load.
It compares the current URL with the initial URL to determine if the login was successful.
Fetching Status Code and Headers:

If the login attempt is successful (i.e., the URL changes), the script prints the status code and the HTTP response headers of the current page.
Input File (login.txt):

Create a login.txt file where each line represents a new payload (combination of username and password) for login attempts.

Here is the md file for your Selenium script in markdown format:

md
Copy code
# Selenium Login Script with Status Code and Header Check

## Overview

This Python script uses Selenium to automate login attempts on a website. It reads login credentials from a file, attempts to log in using the credentials, and checks if the login is successful by comparing URLs. Additionally, it fetches the HTTP status code and response headers of the current page after each login attempt.

## Prerequisites

- Install Python (>= 3.6)
- Install the required libraries by running:

   ```bash
   pip install selenium webdriver-manager requests
Ensure that Chrome browser is installed on your system.
Code
python
Copy code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

def check_success(driver, initial_url):
    current_url = driver.current_url
    if current_url != initial_url:
        return True, current_url
    else:
        return False, current_url

def get_status_code_and_headers(url):
    response = requests.get(url)
    return response.status_code, response.headers

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        initial_url = "http://altoro.testfire.net/login.jsp"
        driver.get(initial_url)

        with open("login.txt", "r") as file:
            for line in file:
                # Strip any leading/trailing whitespace from the line
                payload = line.strip()

                # Find the input fields and insert the payload
                input1 = driver.find_element(By.ID, "uid")
                input1.clear()
                input1.send_keys(payload)

                input2 = driver.find_element(By.ID, "passw")
                input2.clear()
                input2.send_keys(payload)

                # Click the login button
                login_button = driver.find_element(By.NAME, "btnSubmit")
                login_button.click()

                # Wait for the page to load
                time.sleep(5)

                # Check if the login was successful
                success, current_url = check_success(driver, initial_url)
                status_code, headers = get_status_code_and_headers(current_url)

                if success:
                    print("Login successful")
                    print("Status Code:", status_code)
                    print("Response Headers:", headers)
                    break
                else:
                    print(f"Login unsuccessful with payload: {payload}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
Instructions
Login Attempts:

The script reads login credentials from a file named login.txt.
The login page fields are identified by their respective IDs (uid for username and passw for password).
It attempts a login by clicking the button with the name btnSubmit.
Checking Success:

After submitting the login form, the script waits for 5 seconds to allow the page to load.
It compares the current URL with the initial URL to determine if the login was successful.
Fetching Status Code and Headers:

If the login attempt is successful (i.e., the URL changes), the script prints the status code and the HTTP response headers of the current page.
Input File (login.txt):

Create a login.txt file where each line represents a new payload (combination of username and password) for login attempts.

## Example
Example content of the login.txt file:
  ```bash
admin
admin123
testuser
password
  ```
## Running the Script
To run the script, use the following command in your terminal:
  ```bash
python your_script_name.py
 ```
Ensure that you have the login.txt file in the same directory as your script.
