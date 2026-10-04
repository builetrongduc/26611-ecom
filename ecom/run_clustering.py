import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import warnings
import os
warnings.filterwarnings('ignore')

print("Đọc dữ liệu...")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
trans_df = pd.read_csv(os.path.join(BASE_DIR, "data", "transaction_data.csv"))
demo_df = pd.read_csv(os.path.join(BASE_DIR, "data", "hh_demographic.csv"))
camp_df = pd.read_csv(os.path.join(BASE_DIR, "data", "campaign_desc.csv"))

# 1. Xác định T_start (Xét toàn bộ Type A, B, C)
t_start = camp_df['START_DAY'].min()
print(f"Ngày bắt đầu chiến dịch đầu tiên (toàn bộ Type A, B, C) (T_start) = {t_start}")

# 2. Lọc dữ liệu giao dịch TRƯỚC chiến dịch
pre_trans = trans_df[trans_df['DAY'] < t_start].copy()
print(f"Số lượng giao dịch trước chiến dịch: {len(pre_trans)}")

# 3. Tính toán các đặc trưng (RFM & Coupon Usage)
rfm = pre_trans.groupby('household_key').agg(
    Recency=('DAY', lambda x: t_start - x.max()),
    Frequency=('BASKET_ID', 'nunique'),
    Monetary=('SALES_VALUE', 'sum'),
    Coupon_Usage=('COUPON_DISC', lambda x: (x < 0).sum())
).reset_index()

# 4. Gộp Demographic
demo_df.columns = ['Age_Desc', 'Marital_Status', 'Income_Desc', 'Homeowner_Desc', 'HH_Comp_Desc', 'Household_Size_Desc', 'Kid_Category_Desc', 'household_key']
merged_df = pd.merge(rfm, demo_df, on='household_key', how='inner')

# Mã hóa trực tiếp từ dữ liệu ẩn danh (vd: 'Level4' -> 4, 'Age Group6' -> 6)
merged_df['Income_Level'] = merged_df['Income_Desc'].str.extract(r'(\d+)').astype(float)
merged_df['Household_Size'] = merged_df['Household_Size_Desc'].astype(str).str.extract(r'(\d+)').astype(float).fillna(1)
merged_df['Age_Level'] = merged_df['Age_Desc'].str.extract(r'(\d+)').astype(float)

features_cols = ['Recency', 'Frequency', 'Monetary', 'Coupon_Usage', 'Income_Level', 'Age_Level', 'Household_Size']
features = merged_df[features_cols].dropna()
final_df = merged_df.loc[features.index].copy()

print(f"Số lượng khách hàng đủ dữ kiện phân tích (trước chiến dịch): {len(features)}")

# 5. K-Means
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

silhouette_scores = []
K_range = range(2, 11)

print("Tính toán Silhouette...")
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X_scaled)
    silhouette_scores.append(silhouette_score(X_scaled, cluster_labels))

best_k = K_range[np.argmax(silhouette_scores)]
print(f"Số cụm tối ưu được chọn: k = {best_k}")

kmeans_opt = KMeans(n_clusters=best_k, random_state=42, n_init=10)
final_df['Cluster'] = kmeans_opt.fit_predict(X_scaled)

print("\n--- Kích thước mỗi cụm ---")
cluster_sizes = final_df['Cluster'].value_counts().sort_index()
cluster_props = final_df['Cluster'].value_counts(normalize=True).sort_index() * 100
size_df = pd.DataFrame({'Số lượng': cluster_sizes, 'Tỷ lệ (%)': cluster_props})
print(size_df)

print("\n--- Đặc điểm trung bình của mỗi cụm ---")
profile = final_df.groupby('Cluster')[features_cols].mean().round(2)
print(profile)

# Naming (3 cases logic)
cluster_names = {}
overall_monetary_mean = final_df['Monetary'].mean()
overall_recency_mean = final_df['Recency'].mean()

for cluster_id, row in profile.iterrows():
    if row['Monetary'] > overall_monetary_mean * 1.5:
        name = "High-Value Loyal"
    elif row['Recency'] > overall_recency_mean * 1.5:
        name = "Churned/At-Risk"
    else:
        name = "Standard Customers"
    
    if row['Income_Level'] > final_df['Income_Level'].mean():
        name += " (High Income)"
    
    cluster_names[cluster_id] = f"Cluster {cluster_id}: {name}"

final_df['Cluster_Name'] = final_df['Cluster'].map(lambda x: cluster_names[x].split(': ')[1])
print("\nTên các cụm đã gán:")
for k, v in cluster_names.items():
    print(v)

# LƯU FILE DATA CUỐI
causal_df = pd.get_dummies(final_df, columns=['Cluster_Name'], drop_first=False)
output_file = os.path.join(BASE_DIR, "data", "causal_ml_ready_data.csv")
causal_df.to_csv(output_file, index=False)
print(f"\nĐã lưu dataset cuối cùng vào '{output_file}', sẵn sàng cho mô hình Causal ML.")
