# Báo cáo Phân tích Khám phá Dữ liệu (EDA) - Bộ dữ liệu Dunnhumby The Complete Journey

*(Lưu ý: Báo cáo này được thiết kế để đưa trực tiếp vào phần "Khám phá và Tiền xử lý dữ liệu" trong Research Proposal)*

Bộ dữ liệu The Complete Journey phản ánh hành vi mua sắm thực tế của các hộ gia đình thường xuyên mua sắm tại một chuỗi bán lẻ. Qua quá trình phân tích khám phá (EDA), nhóm nghiên cứu đã rút ra được các đặc trưng quan trọng làm cơ sở cho mô hình Causal Machine Learning như sau:

## 1. Tổng quan về Giao dịch (Transactions)
*   **Quy mô dữ liệu:** Bộ dữ liệu bao gồm **2,595,732** bản ghi giao dịch (transactions), trải dài qua **102 tuần** (khoảng 2 năm).
*   **Doanh thu tổng:** Tổng giá trị doanh thu thuần (sales_value - số tiền siêu thị thực nhận) đạt mức **$8,057,463.08**, tương ứng với hơn **276,484 giỏ hàng (baskets)**.
*   **Chất lượng dữ liệu:** Việc phân tích sâu phát hiện một số giao dịch có doanh thu/số lượng bằng 0 hoặc chiết khấu (discount) mang giá trị dương (trái với quy ước hệ thống ghi nhận số âm cho giảm giá). Đây là những giao dịch lỗi hoặc trả hàng (returns), đòi hỏi phải được loại bỏ ở bước tiền xử lý để không làm nhiễu mô hình.

## 2. Đặc điểm Khách hàng (Customers)
*   Dữ liệu ghi nhận hành vi mua sắm của **2,500 hộ gia đình** (household). 
*   **Mức chi tiêu:** Trung bình, mỗi hộ gia đình chi tiêu khoảng **$3,222.99** trong suốt vòng đời của bộ dữ liệu. Tần suất và giá trị đơn hàng biến động rất lớn giữa các nhóm, phản ánh tiềm năng ứng dụng phân cụm (Clustering) để tìm ra nhóm khách hàng nhạy cảm với khuyến mãi.

## 3. Phân bổ Ngành hàng (Category - COMMODITY_DESC)
Để phù hợp với bài toán phân bổ coupon cá nhân hóa theo ngành hàng, nhóm nghiên cứu chọn cấp độ `COMMODITY_DESC` làm đơn vị phân tích (category).
*   **Đa dạng sản phẩm:** Có tổng cộng **308 ngành hàng** khác nhau.
*   **Độ tập trung doanh thu:** Doanh thu có sự phân hóa cao, dẫn đầu bởi các ngành hàng thiết yếu và đồ uống. Top 5 ngành hàng có doanh số lớn nhất gồm: *COUPON/MISC ITEMS ($639,878), SOFT DRINKS ($327,647), BEEF ($312,103), FLUID MILK PRODUCTS ($205,356), và CHEESE ($189,528)*.

## 4. Hành vi sử dụng Khuyến mãi (Promotions & Coupons)
*   Trong suốt 2 năm, chuỗi bán lẻ đã thực hiện **30 chiến dịch (Campaigns)** đa dạng.
*   Tuy nhiên, tỷ lệ thâm nhập của coupon vào từng giao dịch cá nhân là khá thấp. Chỉ có khoảng **36,422 giao dịch** (chiếm **1.40%** tổng số giao dịch) là có áp dụng chiết khấu coupon của nhà sản xuất (`COUPON_DISC < 0`).
*   Bảng ghi nhận đổi mã (`coupon_redempt`) cho thấy có **2,318 lượt redeem** coupon trực tiếp. Số liệu này chứng minh việc phát coupon đại trà đang có tỷ lệ chuyển đổi rất thấp, củng cố tính cấp thiết của bài toán Tối ưu hóa phân bổ (Optimization) bằng Causal ML.

## 5. Đánh giá Mức độ Thưa thớt (Sparsity Check)
Đây là bước đánh giá để xác định tính khả thi của mô hình Uplift ở cấp độ Khách hàng × Ngành hàng:
*   **Tổng số tổ hợp lý thuyết:** Với 2,500 khách hàng và 308 ngành hàng, về mặt lý thuyết sẽ có **770,000 cặp** tương tác.
*   **Thực tế giao dịch:** Chỉ có **288,690 cặp** Khách hàng - Ngành hàng có thực sự phát sinh ít nhất 1 giao dịch trong toàn bộ dữ liệu.
*   **Tỷ lệ thưa thớt (Sparsity):** Lên đến **62.51%**.
*   **Hệ quả cho Mô hình:** Tỷ lệ thưa thớt cao đồng nghĩa với việc phần lớn khách hàng không bao giờ mua phần lớn các ngành hàng. Khi xây dựng mô hình nhân quả, nhóm nghiên cứu sẽ cần cross-join để làm đầy dữ liệu (zero-filling) cho các khoảng thời gian trống, đồng thời áp dụng các bộ lọc để loại bỏ bớt các ngành hàng quá nhỏ lẻ hoặc các khách hàng hoàn toàn ngưng hoạt động (inactive) nhằm đảm bảo thuật toán học tập hiệu quả.
