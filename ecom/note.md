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

3. có lẽ không cần `causal_data` table (**Description:** This table signifies whether a given product was featured in the weekly mailer or was part of an in-store display (other than regular product placement).)