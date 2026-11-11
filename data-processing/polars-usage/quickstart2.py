import pandas as pd

# 创建 penguins 数据集
data = {
    'species': ['Adelie', 'Adelie', 'Adelie', 'Chinstrap', 'Chinstrap', 'Gentoo', 'Gentoo'],
    'island': ['Torgersen', 'Torgersen', 'Dream', 'Dream', 'Dream', 'Biscoe', 'Biscoe'],
    'bill_length_mm': [39.1, 39.5, 40.3, 50.4, 45.8, 48.7, 50.0],
    'bill_depth_mm': [18.7, 17.4, 18.0, 19.5, 18.0, 14.3, 15.2],
    'flipper_length_mm': [181, 186, 195, 193, 201, 210, 222],
    'body_mass_g': [3750, 3800, 3250, 3800, 3700, 5000, 5050],
    'sex': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female']
}

# 转换为 pandas DataFrame
penguins_df = pd.DataFrame(data)

# 保存为 CSV 文件
file_path = 'penguins.csv'
penguins_df.to_csv(file_path, index=False)
