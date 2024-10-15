import requests
from bs4 import BeautifulSoup

def print_input_elements_with_class_or_id(url, output_file):
    try:
        # Fetch the content of the website
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <input> elements with either a class or id attribute
        input_elements = soup.find_all(lambda tag: tag.name == 'input' and (tag.has_attr('class') or tag.has_attr('id')))

        # Open the file in write mode
        with open(output_file, 'w') as file:
            # Print and save each <input> element
            for input_element in input_elements:
                print(input_element)
                file.write(str(input_element) + "\n")  # Save to file
                
                if input_element.has_attr('id'):
                    element_id = input_element['id']
                    print(f"ID: {element_id}")
                    file.write(f"ID: {element_id}\n")  # Save ID to file

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        with open(output_file, 'w') as file:
            file.write(f"An error occurred: {e}\n")

# Input URL from the user
url = input("Enter the website URL: ")
output_file = "output.txt"  # Name of the output file
print_input_elements_with_class_or_id(url, output_file)
