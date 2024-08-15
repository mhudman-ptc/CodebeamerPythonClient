import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

ITEM_ID=4239

# Defining the host is optional and defaults to https://nvidiatrial.codebeamer.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = swagger_client.Configuration()
configuration.host = "http://localhost:8888/api"
configuration.username = "mhudman"
configuration.password = "password"

api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))

# Create an instance of the API class
try:
    # Get basic tracker item
    api_response = api_instance.get_tracker_item(ITEM_ID)
    print("The response of TrackerItemApi->get_tracker_item:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->get_tracker_item: %s\n" % e)
