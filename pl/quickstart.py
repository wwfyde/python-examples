import polars as pl

# 创建一个 DataFrame
df = pl.DataFrame({
    "column1": [1, 2, 3, 4, 5],
    "column2": [10, 20, 30, 40, 50]
})

# 打印 DataFrame
print(df)

# 计算新列：column3 是 column1 和 column2 之和
df = df.with_columns((pl.col("column1") + pl.col("column2")).alias("column3"))

# 筛选出 column1 大于 2 的行
filtered_df = df.filter(pl.col("column1") % 2 != 0)

# 显示筛选后的 DataFrame
print(filtered_df)
