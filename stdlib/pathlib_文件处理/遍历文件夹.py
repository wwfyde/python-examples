from pathlib import Path


def get_all_files() -> list[str]:
    """
    递归获取目录中的所有文件
    :return: 
    """
    base_dir = Path.home() / 'Projects' / 'TechNotes'
    print(base_dir)
    checkpoints = []
    for root, dirs, files in base_dir.walk():
        # print(root, files)
        checkpoints.extend(
            [str(root.joinpath(file).relative_to(base_dir)) for file in files if file.endswith('.md')])
    return checkpoints


if __name__ == '__main__':
    print(get_all_files())
