# The Complete Journey — User Guide

**© 2023 dunnhumby / All rights reserved**

## 1. The Complete Journey

This dataset contains a representation of household level transactions over two years from a group of 2,500 households who are frequent shoppers at a retailer. It contains all of each household’s purchases, not just those from a limited number of categories. For certain households, demographic information as well as direct marketing contact history are included.

Due to the number of tables and the overall complexity of The Complete Journey, it is suggested that this database be used in more advanced classroom settings. Further, The Complete Journey would be ideal for academic research as it should enable one to study the effects of direct marketing to customers.

### Examples of questions for students or academic research

- How many customers are spending more over time? Less over time? Describe these customers.
- Of those customers who are spending more over time, which categories are growing at a faster rate?
- Of those customers who are spending less over time, with which categories are they becoming less engaged?
- Which demographic factors appear to affect customer spend? Engagement with certain categories?
- Is there evidence to suggest that direct marketing improves overall engagement?

---

## 2. Dataset Details

### 2.1 Data tables

## `transaction_data`

**Description:** This table contains all products purchased by households within the dataset. Each line found in this table is essentially the same line that would be found on a store receipt.

| Variable | Description |
|---|---|
| `household_key` | Uniquely identifies each household |
| `basket_id` | Uniquely identifies a purchase occasion |
| `day` | Day when transaction occurred |
| `product_id` | Uniquely identifies each product |
| `quantity` | Number of the products purchased during the trip |
| `sales_value` | Amount of dollars retailer receives from the sale |
| `store_id` | Identifies unique stores |
| `coupon_match_disc` | Discount applied due to retailer’s match of manufacturer coupon |
| `coupon_disc` | Discount applied due to manufacturer coupon |
| `retail_disc` | Discount applied due to retailer’s loyalty card programme |
| `trans_time` | Time of day when transaction occurred |
| `week_no` | Week of the transaction. Ranges 1–102 |

### `sales_value` and actual product prices

The variable `sales_value` in this table is the amount of dollars received by the retailer on the sale of the specific product, taking the coupon match and loyalty card discount into account. It is **not the actual price paid by the customer**.

If a customer uses a coupon, the actual price paid will be less than the `sales_value` because the manufacturer issuing the coupon will reimburse the retailer for the amount of the coupon.

To calculate the actual product prices, use the formulas below:

**Loyalty card price:**

```text
(sales_value - (retail_disc + coupon_match_disc)) / quantity
```

**Non-loyalty card price:**

```text
(sales_value - coupon_match_disc) / quantity
```

### Examples from the guide

- **Line 1:** When this product was purchased the `retail_disc` and `coupon_disc` were both zero, meaning the price of the product is the same as the amount received by the retailer.
- **Line 2:** Two items of this product were purchased, and there was a retail discount applied due to a loyalty card. To determine the regular shelf price of the product (exclusive of loyalty card discount), take the sum of the amount paid and the discount, then divide by the quantity: `($2 + $1.34) / 2 = $1.67`. The shelf price of the product including loyalty card discount is `$2 / 2 = $1`. The customer paid `$2` for both products, which is the same amount the retailer received.
- **Line 3:** The actual shelf price of each product here is `($2.89 + $0.45) / 2 = $1.67`. The customer paid `$2.34` (`$2.89 - $0.55`) for these products, but the retailer will receive `$2.89` due to the manufacturer discount.

---

## `hh_demographic`

**Description:** This table provides a representation of demographic information for a portion of households. The fields have been given generic names (`classification_1`, `classification_2`, etc.) and values (for example, `classification_1` has values Group1 through Group6). The values, however, have been chosen such that they provide meaningful information: **ordinality is important**. In other words, values are ordered in a logical fashion such that trends can be investigated.

| Variable | Description |
|---|---|
| `HOUSEHOLD_KEY` | Uniquely identifies each household |
| `BASKET_ID` | Household level demographic segmentation. Values have meaningful order. Possible values: Group1 through Group6. |
| `DAY` | Household level demographic segmentation. Possible values: X, Y and Z. |
| `PRODUCT_ID` | Household level demographic segmentation. Values have meaningful order. Possible values: Level1 through Level12. |
| `QUANTITY` | Household level demographic segmentation. Values have meaningful order. Possible values: 1 through 5+. |
| `SALES_VALUE` | Household level demographic segmentation. Values have meaningful order. Possible values: Group1 through Group6. |
| `STORE_ID` | Household level demographic segmentation. Values have meaningful order. Possible values: Group1 through Group5. |
| `COUPON_MATCH_DISC` | Household level demographic segmentation. Values have meaningful order. Possible values: 1, 2, 3, None/Unknown. |
| `COUPON_DISC` | Discount applied due to manufacturer coupon |
| `RETAIL_DISC` | Discount applied due to retailer’s loyalty card programme |
| `TRANS_TIME` | Time of day when transaction occurred |
| `WEEK_NO` | Week of the transaction. Ranges 1–102 |

> **Note:** The guide presents the `hh_demographic` variable descriptions as shown above.

---

## `campaign_table`

**Description:** This table lists the campaigns received by customers in the dataset. Each household may have received a different set of campaigns.

| Variable | Description |
|---|---|
| `HOUSEHOLD_KEY` | Uniquely identifies each household |
| `CAMPAIGN` | Uniquely identifies each campaign. Ranges 1–30 |
| `DESCRIPTION` | Type of campaign (TypeA, TypeB or TypeC) |

---

## `campaign_desc`

**Description:** This table gives the length of time for which a campaign runs. So, any coupons received as part of a campaign are valid within the dates contained in this table.

| Variable | Description |
|---|---|
| `CAMPAIGN` | Uniquely identifies each campaign. Ranges 1–30 |
| `DESCRIPTION` | Type of campaign (TypeA, TypeB or TypeC) |
| `START_DAY` | Start date of campaign |
| `END_DAY` | End date of campaign |

---

## `product`

**Description:** This table contains information on each product sold such as type of product, national or private label and a brand identifier.

| Variable | Description |
|---|---|
| `PRODUCT_ID` | Number that uniquely identifies each product |
| `DEPARTMENT` | Groups similar products together |
| `COMMODITY_DESC` | Groups similar products together at a lower level |
| `SUB_COMMODITY_DESC` | Groups similar products together at the lowest level |
| `MANUFACTURER` | Code that links products with same manufacturer together |
| `BRAND` | Indicates Private or National label brand |
| `CURR_SIZE_OF_PRODUCT` | Indicates package size (not available for all products) |

---

## `coupon`

**Description:** This table lists all the coupons sent to customers as part of a campaign, as well as the products for which each coupon is redeemable. Some coupons are redeemable for multiple products. One example is a coupon for any private label frozen vegetable. There are a large number of products where this coupon could be redeemed.

For campaign TypeA, this table provides the pool of possible coupons.

| Variable | Description |
|---|---|
| `CAMPAIGN` | Uniquely identifies each campaign. Ranges 1–30 |
| `COUPON_UPC` | Uniquely identifies each coupon (unique to household and campaign) |
| `PRODUCT_ID` | Uniquely identifies the product for which the coupon is redeemable |

---

## `coupon_redempt`

**Description:** This table identifies the coupons that each household redeemed.

| Variable | Description |
|---|---|
| `HOUSEHOLD_KEY` | Uniquely identifies each household |
| `DAY` | Day when the transaction occurred |
| `COUPON_UPC` | Uniquely identifies each coupon (unique to household and campaign) |
| `CAMPAIGN` | Uniquely identifies each campaign |

### Coupon distribution rules

- A customer participating in a TypeA campaign received 16 coupons out of the pool. The 16 coupons were selected based on the customer’s prior purchase behaviour.
- Identifying the specific 16 coupons that each customer received is outside the scope of this database.
- For campaign TypeB and TypeC, all customers participating in a campaign receive all coupons pertaining to that campaign.

---

## `causal_data`

**Description:** This table signifies whether a given product was featured in the weekly mailer or was part of an in-store display (other than regular product placement).

| Variable | Description |
|---|---|
| `product_id` | Uniquely identifies each product |
| `store_id` | Identifies unique stores |
| `week_no` | Week of the transaction |
| `display` | Display location |
| `mailer` | Mailer location |

### `display` values

| Value | Meaning |
|---|---|
| `0` | Not on Display |
| `1` | Store Front |
| `2` | Store Rear |
| `3` | Front End Cap |
| `4` | Mid-Aisle End Cap |
| `5` | Rear End Cap |
| `6` | Side-Aisle End Cap |
| `7` | In-Aisle |
| `9` | Secondary Location Display |
| `A` | In-Shelf |

### `mailer` values

| Value | Meaning |
|---|---|
| `0` | Not on ad |
| `A` | Interior page feature |
| `C` | Interior page line item |
| `D` | Front page feature |
| `F` | Back page feature |
| `H` | Wrap front feature |
| `J` | Wrap interior coupon |
| `L` | Wrap back feature |
| `P` | Interior page coupon |
| `X` | Free on interior page |
| `Z` | Free on front page, back page or wrap |

---

# 3. Case Study

## John Smith

John Smith is a valued customer at a national grocery retailer for which detailed transaction data is available. Throughout all the tables in the database, he is identified with a `household_key` of `208`.

From `campaign_table`, John received 8 different campaigns. Five of the campaigns were TypeA, and three were TypeB. These campaigns were spread out over the two-year period represented by the data.

To understand the time periods of these campaigns, use the records in `campaign_desc` for the campaigns listed for John.

### Campaign 22

For campaign 22, the distinct `coupon_upc` values in the `coupon` table show that there were 21 distinct coupons sent out as part of the campaign.

One specific coupon, `51800000050`, could be redeemed for a number of products. Although all products are not displayed in the guide, the coupon was valid for 38 distinct products. Looking at the corresponding `product_id` values in the `product` table shows that this coupon was valid for refrigerated specialty rolls from a national brand.

### John's coupon redemptions

John did not necessarily redeem every coupon he received. Looking at all records in `coupon_redempt` where `household_key = 208` shows that he redeemed 7 coupons from 3 campaigns.

### John's purchasing behavior

Looking at records in `transaction_data` where `household_key = 208` shows everything John purchased.

---

## Coupon redemption and other store activity

The guide notes that it is not possible to know a customer's reason for purchasing an item. However, the data does show whether an item was featured during the time of purchase.

For product `72717`, records in `causal_data` show the weeks and stores where the product was featured in the weekly mailer and where it was featured as part of an in-store display.

For example, in store `421` and week `12`, the product was featured on a display in the rear of the store and was featured on an interior page of the mailer.

The transaction data can be combined with the other tables to understand John's behavior when he was redeeming a coupon and when he was not.

### Example chain

- John received offers as part of campaign `22`, which occurred between days `624` and `656`.
- John redeemed coupon `51800000050` on day `654`.
- Through the `coupon` table, the coupon is known to be valid for a number of products, including product `1017772`.
- The transaction data shows where John purchased this item and received a discount from using a coupon.

---

# 4. Research Questions Suggested by the Dataset

The guide highlights several possible research directions:

- Do campaigns cause customers to purchase more items than they did previously?
- Are customers more likely to redeem coupons for products they already purchase?
- Do coupons entice customers to try products they have never purchased before?
- Which customers increase or decrease spending over time?
- Which categories grow faster among customers whose spending increases?
- Which categories become less engaged among customers whose spending decreases?
- Which demographic factors appear to affect customer spend and engagement with certain categories?
- Is there evidence that direct marketing improves overall customer engagement?

---

# 5. Source

**The Complete Journey — User Guide**

© 2023 dunnhumby / All rights reserved.

For general questions about dunnhumby or the Source Files programme, or for technical questions regarding use of this dataset:

`sourcefiles@dunnhumby.com`

`dunnhumby.com`
