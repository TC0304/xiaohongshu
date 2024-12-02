import pandas as pd

# 读取 CSV 文件
links_df = pd.read_csv('新加坡免签_links.csv')

# 去除重复的链接，保留唯一的链接
unique_links_df = links_df.drop_duplicates(subset=['Link'])

# 保存为新的 CSV 文件
unique_links_df.to_csv('unique_新加坡免签_links.csv', index=False, encoding='utf-8-sig')
print("已去除重复链接并保存到 unique_嵩溪村_links.csv 文件中。")
