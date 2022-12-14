"""
    HomeWizard Energy API

    With the HomeWizard Energy platform, you can get insights in your energy usage. Use the HomeWizard Wi-Fi P1 meter to access real-time data directly from your smart meter, the HomeWizard Wi-Fi Energy Socket to get energy insights from all your devices, the HomeWizard Wi-Fi kWh meter to measure devices such as solar panels and the HomeWizard Wi-Fi Watermeter to get insight in your water usage. With the open API you can integrate the data directly into your system of choice.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import hwe
from hwe.model.data_hwe_p1 import DataHweP1
from hwe.model.data_hwe_skt import DataHweSkt
from hwe.model.data_hwe_wtr import DataHweWtr
from hwe.model.data_sdm230_wifi import DataSDM230Wifi
from hwe.model.data_sdm630_wifi import DataSDM630Wifi
globals()['DataHweP1'] = DataHweP1
globals()['DataHweSkt'] = DataHweSkt
globals()['DataHweWtr'] = DataHweWtr
globals()['DataSDM230Wifi'] = DataSDM230Wifi
globals()['DataSDM630Wifi'] = DataSDM630Wifi
from hwe.model.api_v1_data_get200_response import ApiV1DataGet200Response


class TestApiV1DataGet200Response(unittest.TestCase):
    """ApiV1DataGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApiV1DataGet200Response(self):
        """Test ApiV1DataGet200Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApiV1DataGet200Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
