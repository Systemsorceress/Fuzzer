from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Path to your Chrome profiles directory (update this as needed)
profile_directory = 'C:\Users\Malaika\AppData\Local\Google\Chrome\User Data\Profile 1'

# Profile to use
profile_name = 'Profile 1'

# Set up Chrome options
options = Options()
options.add_argument(f"user-data-dir={profile_directory}")
options.add_argument(f"profile-directory={profile_name}")

# Set up WebDriver with webdriver_manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open a page
driver.get("https://www.google.com")

# Wait for user input to close
input("Press Enter to close the browser...")
driver.quit()
