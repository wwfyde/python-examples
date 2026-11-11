import mimetypes
import uuid
import alibabacloud_oss_v2 as oss
from libs.config import settings, AliyunOssConfig

oss_config: AliyunOssConfig = settings.oss

# 1. 配置凭证提供者 (静态 AK/SK)
cred_provider = oss.credentials.StaticCredentialsProvider(
    access_key_id=oss_config.access_key_id,
    access_key_secret=oss_config.access_key_secret
)

# 2. 加载默认配置并覆盖 Endpoint/Region
# 如果 oss_config.endpoint 是完整的 URL (如 https://oss-cn-hangzhou.aliyuncs.com)
# v2 SDK 通常推荐使用 region，但也可以直接指定 endpoint
cfg = oss.config.load_default()
cfg.credentials_provider = cred_provider
cfg.endpoint = oss_config.endpoint
cfg.region = oss_config.region  # 如果你的配置里有 region 最好加上，没有则依赖 endpoint

client = oss.Client(cfg)


def upload_image(
        filename: str,
        data: str | bytes,
        prefix: str = "tmp",
        rename: bool = True,
        domain: str | None = None,
) -> str | None:
    """
    上传图片到OSS (使用 alibabacloud-oss-v2)
    """
    bucket_name = oss_config.bucket_name

    # --- 1. 处理文件名逻辑 (保持原有业务逻辑) ---
    if rename:
        uid = uuid.uuid4()
        # 优化：使用 split 安全获取后缀，防止文件名无后缀报错
        suffix = filename.split('.')[-1] if '.' in filename else ""
        file_key = f"{uid}.{suffix}" if suffix else str(uid)
        upload_key = f"{prefix}/{file_key}"
    else:
        upload_key = f"{prefix}/{filename}"

    # 处理 prefix 为 None 的特殊情况 (根据你原代码逻辑调整)
    # 原代码逻辑：如果 prefix 显式传 None，会在路径前再加 tmp/
    if prefix is None:
        upload_key = f"tmp/{upload_key}"

    # 统一将 data 转换为 bytes，v2 对类型检查更严格
    body_content = data.encode("utf-8") if isinstance(data, str) else data

    content_type, _ = mimetypes.guess_type(filename)
    if content_type is None:
        content_type = "application/octet-stream"

    print(content_type)

    # 构造强类型请求对象 (Rust 风格)
    request = oss.PutObjectRequest(
        bucket=bucket_name,
        key=upload_key,
        body=body_content,
        # 如果需要设置 Content-Type，可以在这里添加 headers
        headers={
            "Content-Type": content_type,
            "Content-Disposition": "inline",
        }
    )

    try:
        # 执行上传
        # v2 SDK 如果失败通常会抛出 oss.exceptions.OperationError
        result = client.put_object(request)

        # --- 3. 构造返回 URL ---
        # 只有上传成功才会执行到这里
        final_domain = domain or oss_config.domain

        if final_domain:
            # 这种拼接适用于公共读 Bucket 或绑定了 CDN 的情况
            return f"https://{final_domain}/{upload_key}"
        else:
            # 回退到默认域名
            # 注意：oss_config.endpoint 可能带 https:// 前缀，需要处理
            endpoint_host = oss_config.endpoint.replace("https://", "").replace("http://", "")
            return f"https://{bucket_name}.{endpoint_host}/{upload_key}"

    except oss.exceptions.OperationError as e:
        # 类似 Rust 的 Result::Err 处理
        print(f"OSS Upload Failed: {e.code}, {e.message}, RequestId: {e.request_id}")
        return None
    except Exception as e:
        print(f"Unexpected Error during upload: {e}")
        return None


if __name__ == "__main__":
    file = settings.temp_dir / "img.png"
    # 使用 pathlib 风格更现代
    if file.exists():
        # 模拟 ID 生成
        file_id = f"{uuid.uuid4()}{file.suffix}"
        image_bytes = file.read_bytes()

        url = upload_image(file_id, image_bytes, prefix="test", rename=False)
        print(f"Uploaded URL: {url}")
    else:
        print(f"File not found: {file}")
