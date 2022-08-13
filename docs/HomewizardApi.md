# hwe.HomewizardApi

All URIs are relative to *http://192.168.44.75*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_get**](HomewizardApi.md#api_get) | **GET** /api | Basic information
[**api_v1_data_get**](HomewizardApi.md#api_v1_data_get) | **GET** /api/v1/data | Recent measurement
[**api_v1_state_get**](HomewizardApi.md#api_v1_state_get) | **GET** /api/v1/state | Actual State
[**api_v1_telegram_get**](HomewizardApi.md#api_v1_telegram_get) | **GET** /api/v1/telegram | Recent telegram
[**control_state**](HomewizardApi.md#control_state) | **PUT** /api/v1/state | Control State


# **api_get**
> Basic api_get()

Basic information

This endpoint allows you to get basic information from the device.

### Example


```python
import time
import hwe
from hwe.api import homewizard_api
from hwe.model.basic import Basic
from hwe.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://192.168.44.75
# See configuration.py for a list of all supported configuration parameters.
configuration = hwe.Configuration(
    host = "http://192.168.44.75"
)


# Enter a context with an instance of the API client
with hwe.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = homewizard_api.HomewizardApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Basic information
        api_response = api_instance.api_get()
        pprint(api_response)
    except hwe.ApiException as e:
        print("Exception when calling HomewizardApi->api_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Basic**](Basic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_data_get**
> ApiV1DataGet200Response api_v1_data_get()

Recent measurement

This endpoint allows you to get the most recent measurement from the device.

### Example


```python
import time
import hwe
from hwe.api import homewizard_api
from hwe.model.error import Error
from hwe.model.api_v1_data_get200_response import ApiV1DataGet200Response
from pprint import pprint
# Defining the host is optional and defaults to http://192.168.44.75
# See configuration.py for a list of all supported configuration parameters.
configuration = hwe.Configuration(
    host = "http://192.168.44.75"
)


# Enter a context with an instance of the API client
with hwe.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = homewizard_api.HomewizardApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Recent measurement
        api_response = api_instance.api_v1_data_get()
        pprint(api_response)
    except hwe.ApiException as e:
        print("Exception when calling HomewizardApi->api_v1_data_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiV1DataGet200Response**](ApiV1DataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_state_get**
> SocketState api_v1_state_get()

Actual State

This endpoint returns the actual state of the Energy Socket. This endpoint is only available for the HWE-SKT.

### Example


```python
import time
import hwe
from hwe.api import homewizard_api
from hwe.model.error import Error
from hwe.model.socket_state import SocketState
from pprint import pprint
# Defining the host is optional and defaults to http://192.168.44.75
# See configuration.py for a list of all supported configuration parameters.
configuration = hwe.Configuration(
    host = "http://192.168.44.75"
)


# Enter a context with an instance of the API client
with hwe.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = homewizard_api.HomewizardApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Actual State
        api_response = api_instance.api_v1_state_get()
        pprint(api_response)
    except hwe.ApiException as e:
        print("Exception when calling HomewizardApi->api_v1_state_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SocketState**](SocketState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_telegram_get**
> str api_v1_telegram_get()

Recent telegram

This endpoint returns the most recent, valid telegram that was given by the P1 meter, therefore this endpoint is only available for the HWE-P1.

### Example


```python
import time
import hwe
from hwe.api import homewizard_api
from hwe.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://192.168.44.75
# See configuration.py for a list of all supported configuration parameters.
configuration = hwe.Configuration(
    host = "http://192.168.44.75"
)


# Enter a context with an instance of the API client
with hwe.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = homewizard_api.HomewizardApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Recent telegram
        api_response = api_instance.api_v1_telegram_get()
        pprint(api_response)
    except hwe.ApiException as e:
        print("Exception when calling HomewizardApi->api_v1_telegram_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_state**
> SocketState control_state(socket_state)

Control State

This endpoint controls the state of the Energy Socket. This endpoint is only available for the HWE-SKT.

### Example


```python
import time
import hwe
from hwe.api import homewizard_api
from hwe.model.socket_state import SocketState
from pprint import pprint
# Defining the host is optional and defaults to http://192.168.44.75
# See configuration.py for a list of all supported configuration parameters.
configuration = hwe.Configuration(
    host = "http://192.168.44.75"
)


# Enter a context with an instance of the API client
with hwe.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = homewizard_api.HomewizardApi(api_client)
    socket_state = SocketState(
        power_on=True,
        switch_lock=True,
        brightness=3.14,
    ) # SocketState | 

    # example passing only required values which don't have defaults set
    try:
        # Control State
        api_response = api_instance.control_state(socket_state)
        pprint(api_response)
    except hwe.ApiException as e:
        print("Exception when calling HomewizardApi->control_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **socket_state** | [**SocketState**](SocketState.md)|  |

### Return type

[**SocketState**](SocketState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

