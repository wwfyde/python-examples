# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys
import json

from typing import List

from alibabacloud_imageenhan20190930.client import Client as imageenhan20190930Client
from alibabacloud_credentials.client import Client as CredentialClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_imageenhan20190930 import models as imageenhan_20190930_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> imageenhan20190930Client:
        """
        使用凭据初始化账号Client
        @return: Client
        @throws Exception
        """
        # 工程代码建议使用更安全的无AK方式，凭据配置方式请参见：https://help.aliyun.com/document_detail/378659.html。
        credential = CredentialClient(

        )
        config = open_api_models.Config(
            access_key_id=os.getenv('ALIYUN_ACCESS_KEY_ID'),
            access_key_secret=os.getenv('ALIYUN_ACCESS_KEY_SECRET'),
            # credential=credential
        )
        # Endpoint 请参考 https://api.aliyun.com/product/imageenhan
        config.endpoint = f'imageenhan.cn-shanghai.aliyuncs.com'
        return imageenhan20190930Client(config)

    @staticmethod
    def main(
            args: List[str],
    ) -> None:
        client = Sample.create_client()
        make_super_resolution_image_request = imageenhan_20190930_models.MakeSuperResolutionImageRequest(
            upscale_factor=4,
            url='http://workbench-file-transfer.oss-cn-shanghai.aliyuncs.com/user-files/cf767831-27c6-4ac8-a443-d9fa259f2127-erin-lindford.90b9d461.jpg?OSSAccessKeyId=LTAI5tRvL6vYdjKSfTFZ156m&Expires=1769483096&Signature=hWWmgfJKyhYJUrfmcgMrR2%2By%2Bpw%3D&response-content-disposition=attachment',
            mode='enhancement',
            output_format='png',
            output_quality=95
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = client.make_super_resolution_image_with_options(make_super_resolution_image_request, runtime)
            print(json.dumps(resp, default=str, indent=2))
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend") if error.data else '没有')

    @staticmethod
    async def main_async(
            args: List[str],
    ) -> None:
        client = Sample.create_client()
        make_super_resolution_image_request = imageenhan_20190930_models.MakeSuperResolutionImageRequest(
            upscale_factor=4,
            url='http://workbench-file-transfer.oss-cn-shanghai.aliyuncs.com/user-files/cf767831-27c6-4ac8-a443-d9fa259f2127-erin-lindford.90b9d461.jpg?OSSAccessKeyId=LTAI5tRvL6vYdjKSfTFZ156m&Expires=1769483096&Signature=hWWmgfJKyhYJUrfmcgMrR2%2By%2Bpw%3D&response-content-disposition=attachment',
            mode='enhancement',
            output_format='png',
            output_quality=95
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = await client.make_super_resolution_image_with_options_async(make_super_resolution_image_request,
                                                                               runtime)
            print(json.dumps(resp, default=str, indent=2))
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
