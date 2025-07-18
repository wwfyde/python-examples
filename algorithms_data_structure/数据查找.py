
def check_samples(samples: list[str], resources: list[str]) -> bool:
    # dedup_samples = set(samples)
    for sample in samples:
        if sample in resources:
            # 就地删除遍历的样本一个
            resources.remove(sample)
            continue
        else:
            print(f'样本{sample}未找到, 或数量不足')
            return False
    return True

def main():
    samples = ['a', 'b', 'c', 'd', 'e','f', 'f']
    resources = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
    is_matched = check_samples(samples, resources)
    print(is_matched)



if __name__ == '__main__':
    main()