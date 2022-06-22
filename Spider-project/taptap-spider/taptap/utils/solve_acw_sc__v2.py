#!pip install PyExecJS
# -*- coding: UTF-8 -*-
import execjs
import re
import requests


def get_acw_sc__v2(headers):
    url = 'https://www.taptap.com/webapiv2/gate/v3/rec1?&X-UA=V%3D1%26PN%3DWebApp%26LANG%3Dzh_CN%26VN_CODE%3D77%26VN' \
          '%3D0.1.0%26LOC%3DCN%26PLT%3DPC%26DS%3DAndroid%26UID%3D561fbe1d-d85f-4710-9de2-4a5efc00c1c7%26DT%3DPC%26OS' \
          '%3DWindows%26OSV%3D10.0.0%20'
    response = requests.get(url=url, headers=headers)
    arg1 = re.findall("arg1='(.*?)'", response.text)[0]
    # print(f'get arg1= {arg1}')
    with open('taptap/utils/get_acw_sc_v2.js', 'r', encoding='gbk') as f:
        acw_sc_v2_js = f.read()
    acw_sc__v2 = execjs.compile(acw_sc_v2_js).call('getAcwScV2', arg1)
    # print(f'acw_sc__v2={acw_sc__v2}')
    return acw_sc__v2
