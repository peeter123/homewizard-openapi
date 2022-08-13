# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from hwe.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from hwe.model.api_v1_data_get200_response import ApiV1DataGet200Response
from hwe.model.basic import Basic
from hwe.model.data_hwe_p1 import DataHweP1
from hwe.model.data_hwe_skt import DataHweSkt
from hwe.model.data_hwe_wtr import DataHweWtr
from hwe.model.data_sdm230_wifi import DataSDM230Wifi
from hwe.model.data_sdm630_wifi import DataSDM630Wifi
from hwe.model.error import Error
from hwe.model.socket_state import SocketState
