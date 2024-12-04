import pandas as pd

# 读取file2和file3
file2_path = r"C:\Users\ASUS\Desktop\地表水质\合并数据集12.csv"
file3_path = r"C:\Users\ASUS\Desktop\地表水质\月均CSV数据\“十四五”融合地表水国控断面水质月均数据_202310.csv"

df2 = pd.read_csv(file2_path)
df3 = pd.read_csv(file3_path)

# 将“月份”列转换为日期时间对象
df3['月份'] = pd.to_datetime(df3['月份'], format='%Y%m')

# 提取file2中的站点代码
stations = df2['站点代码'].unique()

# 遍历每个站点，检索file3中的数据
for station in stations:
    station_data = df3[df3['站点代码'] == station]
    if not station_data.empty:
        dissolved_oxygen_data_count = station_data['溶解氧'].count()

        # 直接从Timestamp对象中提取年份
        start_year = station_data['月份'].min().year
        end_year = station_data['月份'].max().year

        df2.loc[df2['站点代码'] == station, '月尺度数据开始年份'] = start_year
        df2.loc[df2['站点代码'] == station, '月尺度数据截止年份'] = end_year
        df2.loc[df2['站点代码'] == station, '所包含的月尺度数据量'] = dissolved_oxygen_data_count

# 将更新后的df2写回到file2文件
df2.to_csv(file2_path, index=False, encoding='utf-8')