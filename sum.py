import urllib.request
import urllib.parse
import json

# Base URL for the API endpoint
base_url = "http://py4e-data.dr-chuck.net/json?"

# Prompt for a location
location = "Kokshetau Institute of Economics and Management"

# Encode the location parameter
parameters = {"address": location}
encoded_params = urllib.parse.urlencode(parameters)

# Construct the full URL
url = base_url + encoded_params

try:
    # Call the API and retrieve the JSON data
    response = urllib.request.urlopen(url)
    json_data = response.read().decode()

    # Parse the JSON data
    data = json.loads(json_data)

    # Retrieve the first place_id from the JSON
    place_id = data["results"][0]["place_id"]

    # Print the place_id
    print("Place id:", place_id)

except Exception as e:
    print("An error occurred:", str(e))
