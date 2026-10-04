# Outlier
1.detect discount > 0
```
############ WARNINGGGG ###############
count_retail_disc_gt0 = (tx["retail_disc"] > 0).sum()
share_retail_disc_gt0 = (tx["retail_disc"] > 0).mean() * 100

print("Số record có retail_disc > 0:", count_retail_disc_gt0)
print("Tỷ lệ:", share_retail_disc_gt0, "%")
```
2. detect sale_value=0, quantity=0
