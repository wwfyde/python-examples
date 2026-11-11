from pathlib import Path


def find_missing_file(samples: list[str], target_path: Path | str):
    if isinstance(target_path, str):
        target_path = Path(target_path)
    target_files = set([item.stem for item in target_path.iterdir()])
    # print(target_files)
    missing_files = [file for file in samples if file.strip() not in target_files]
    print(missing_files)
    return missing_files

    pass


def find_out_file(samples: list[str], target_path: Path | str) -> list[Path]:
    if isinstance(target_path, str):
        target_path = Path(target_path)
    target_files = [item for item in target_path.iterdir()]
    # print(target_files)
    out_files = [file for file in target_files if file.stem not in samples]
    print(out_files)
    return out_files


def delete_files(files: list[Path]):
    for file in files:
        file.unlink(missing_ok=True)


if __name__ == "__main__":
    files = [
        "国风插画设计",  ##
        "二次元景物绘画",  ##
        "潮流人物IP",  ##
        "机器人IP",  ##
        "极智棱镜·电商数码 C4D渲染",  ##
        "银镜流光",  ##
        "冰晶",  # 1
        "商业办公外景",  ##
        "室内设计绘图",  ##
        "扁平设计",  ##
        "国潮绘艺",  ##
        "毛绒玩具IP设计",  ##
    ]
    target_path = "/data/models/Lora"
    find_missing_file(files, target_path=target_path)
    files_to_delete = find_out_file(files, target_path)
    delete_files(files_to_delete)
