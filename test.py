# 导入所需的库
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.covariance import MinCovDet

# 1. 加载数据
data = pd.read_csv("old_faithful.csv")  # 替换为你的数据文件名

# 2. 数据可视化
# 使用Matplotlib绘制折线图
plt.figure(figsize=(10, 5))
plt.plot(data[data['Class'] == 0]['F1'], label='Class 0', marker='o', linestyle='-', color='blue')
plt.plot(data[data['Class'] == 1]['F1'], label='Class 1', marker='o', linestyle='-', color='red')
plt.xlabel('Sample')
plt.ylabel('F1')
plt.legend()
plt.title('F1 by Class')
plt.show()

# 3. 统计摘要
max_f1 = data['F1'].max()
min_f1 = data['F1'].min()
mean_f1 = data['F1'].mean()
std_f1 = data['F1'].std()

print(f"Maximum F1: {max_f1}")
print(f"Minimum F1: {min_f1}")
print(f"Mean F1: {mean_f1}")
print(f"Standard Deviation of F1: {std_f1}")

# 4. 散点图
plt.figure(figsize=(8, 8))
plt.scatter(data['F1'], data['F2'], c=data['Class'], cmap='viridis')
plt.xlabel('F1')
plt.ylabel('F2')
plt.title('Scatter Plot of F1 and F2')
plt.show()

# 5. 离群点检测
outlier_detector = MinCovDet()
outliers = outlier_detector.fit_predict(data[['F1', 'F2']])
data['Outliers'] = outliers
outlier_points = data[data['Outliers'] == -1]

plt.figure(figsize=(8, 8))
plt.scatter(data['F1'], data['F2'], c=data['Class'], cmap='viridis')
plt.scatter(outlier_points['F1'], outlier_points['F2'], color='red', marker='o', s=100, label='Outliers')
plt.xlabel('F1')
plt.ylabel('F2')
plt.legend()
plt.title('Scatter Plot with Outliers')
plt.show()

# 6. 相关矩阵
correlation_matrix_class_0 = data[data['Class'] == 0][['F1', 'F2']].corr()
correlation_matrix_class_1 = data[data['Class'] == 1][['F1', 'F2']].corr()

print("Correlation Matrix for Class 0:")
print(correlation_matrix_class_0)

print("Correlation Matrix for Class 1:")
print(correlation_matrix_class_1)

# 7. 属性规范化
scaler = MinMaxScaler()
data[['F1', 'F2']] = scaler.fit_transform(data[['F1', 'F2']])

# 8. 重新生成相关矩阵
correlation_matrix_normalized = data[['F1', 'F2']].corr()
print("Correlation Matrix for Normalized Data:")
print(correlation_matrix_normalized)
