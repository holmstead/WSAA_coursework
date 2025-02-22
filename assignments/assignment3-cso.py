import requests
import json

# Define the API endpoint
url = "https://www.cso.ie/en/methods/nationalaccounts/nationalaccountshistoricalseries1970to1995/"  # Replace with the actual URL

# Fetch data from the CSO API
response = requests.get(url)

# Print the status code returned
print(response.status_code)

# Check if the request was successful
if response.status_code == 200:

    # Print the text response
    print(response.text)
    
    # Parse the JSON data from the response
    #data = response.json()
    
    # Store the JSON data in a file
    with open("cso.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print("Data has been successfully written to cso.json")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
