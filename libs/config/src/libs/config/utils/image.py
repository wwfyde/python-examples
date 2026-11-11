import uuid

import oss2

from lib import settings


def upload_image(
    filename: str,
    data: str | bytes,
    prefix: str = "tmp",
    rename: bool = True,
    domain: str = None,
) -> str | None:
    """
    上传图片到OSS
    :param filename: 文件名
    :param data: 文件内容, 二进制数据或字符串
    :param prefix: OSS路径前缀 上传到OSS的路径
    :param rename: 是否重命名, 默认为True
    :param domain: OSS域名, 默认为None时使用bucket_name+endpoint
    """
    endpoint = settings.oss.endpoint

    auth = oss2.Auth(settings.oss.access_key_id, settings.oss.access_key_secret)
    bucket_name = settings.oss.bucket_name
    bucket = oss2.Bucket(auth, endpoint, bucket_name)

    if rename:
        uid = uuid.uuid4()
        upload_file_name = f"{prefix}/{uid}.{filename.split('.')[-1]}"
    else:
        upload_file_name = f"{prefix}/{filename}"
    if prefix is None:
        # 临时文件, 使用OSS生命周期自动删除
        upload_file_name = f"tmp/{upload_file_name}"

    result = bucket.put_object(upload_file_name, data)
    domain = domain or settings.oss.domain
    if domain:
        image_link = f"https://{domain}/{upload_file_name}"
    else:
        image_link = f"https://{bucket_name}.{endpoint}/{upload_file_name}"
    if result.status == 200:
        return image_link
    else:
        return None


if __name__ == "__main__":
    file = settings.temp_dir.joinpath("img.png")
    id = f"{str(uuid.uuid4())}{file.suffix}"
    image_bytes = file.read_bytes()
    url = upload_image(id, image_bytes, prefix="test", rename=False, domain=None)
    print(url)
