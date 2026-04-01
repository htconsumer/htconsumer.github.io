import pandas as pd
import json

# 读取Excel文件
excel_path = r'F:/华泰工作/项目/260401 AI-消费路演主题/财富研究大消费26年4月可选主题.xlsx'
df = pd.read_excel(excel_path)

# 转换为JSON格式
result = df.to_dict(orient='records')

# 打印列名
print("列名:", df.columns.tolist())
print("\n数据条数:", len(result))
print("\n前5条数据:")
for i, item in enumerate(result[:5]):
    print(f"\n第{i+1}条:")
    for key, value in item.items():
        print(f"  {key}: {value}")

# 保存为JSON文件
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("\n\n完整数据已保存到 data.json")
