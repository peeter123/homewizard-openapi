import time
import hwe
from pprint import pprint
from hwe.api import homewizard_api
from hwe.model.api_v1_data_get200_response import ApiV1DataGet200Response
from hwe.model.basic import Basic
from hwe.model.error import Error
from hwe.model.socketstate import SOCKETSTATE
# Defining the host is optional and defaults to http://192.168.44.75
# See configuration.py for a list of all supported configuration parameters.
configuration = hwe.Configuration(
    host="http://192.168.44.75"
)

# Enter a context with an instance of the API client
with hwe.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = homewizard_api.HomewizardApi(api_client)

    try:
        # Basic information
        api_response = api_instance.api_get()
        pprint(api_response)
    except hwe.ApiException as e:
        print("Exception when calling HomewizardApi->api_get: %s\n" % e)

    try:
        # Data
        api_response = api_instance.api_v1_data_get()
        pprint(api_response)
    except hwe.ApiException as e:
        print("Exception when calling HomewizardApi->api_v1_data_get: %s\n" % e)