import httpx
from tqdm import tqdm


def download_file(url, output_path):
    with httpx.stream("GET", url) as response:
        # 获取文件总大小（如果服务器提供了 Content-Length 头）
        total_size = int(response.headers.get('Content-Length', 0))

        # 打开文件进行写入
        with open(output_path, "wb") as file:
            # 使用 tqdm 创建进度条
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=output_path)

            # 按块读取响应内容，并更新进度条
            for chunk in response.iter_bytes(chunk_size=1024):
                file.write(chunk)
                progress_bar.update(len(chunk))

            # 关闭进度条
            progress_bar.close()


if __name__ == "__main__":
    # 示例：下载文件并显示进度
    file_url = "https://static.molook.cn/temp/a59d1929-64f7-49ab-9c9f-dbb0fdabfe32.zip"
    output_file = "largefile.zip"

    download_file(file_url, output_file)
