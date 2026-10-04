# Yêu cầu Preprocessing Dataset cho Mô hình Causal ML

Tài liệu này tổng hợp các bước tiền xử lý dữ liệu (preprocessing) cần thiết để chuẩn bị dữ liệu đầu vào cho mô hình Uplift Modeling (Causal ML), dựa trên đề cương nghiên cứu và quá trình EDA. Tạm thời, quy trình sẽ bỏ qua xử lý ngoại lệ cho chiến dịch TypeA để tập trung hoàn thiện full flow trước.

## 1. Xử lý Dữ liệu Ngoại lệ (Outliers & Anomalies)

Dựa trên phát hiện trong quá trình phân tích:

*   **Lọc Discount > 0:** 
    Trong bộ dữ liệu The Complete Journey, các khoản giảm giá (`retail_disc`, `coupon_disc`, `coupon_match_disc`) được ghi nhận là số âm (ví dụ: `-1.34`). Những giao dịch có discount lớn hơn `0` là bất thường (có thể là hoàn tiền hoặc lỗi hệ thống).
    *   **Hành động:** Xóa bỏ (drop) các bản ghi có `retail_disc > 0`, `coupon_disc > 0` hoặc `coupon_match_disc > 0`.
*   **Lọc giao dịch rỗng (`sales_value = 0` VÀ `quantity = 0`):** 
    Những giao dịch này không mang lại doanh thu hay số lượng sản phẩm (thường do quét mã lỗi hoặc trả hàng).
    *   **Hành động:** Xóa bỏ (drop) các bản ghi có `sales_value == 0` VÀ `quantity == 0`.

## 2. Định nghĩa Target / Biến Kết quả (Outcome Variable)

Mục tiêu là tính toán doanh thu thuần mà nhà bán lẻ thực tế thu được (để tính ROI cho ngân sách khuyến mãi).

*   Theo User Guide, cột `sales_value` là số tiền mà siêu thị thực nhận (đã được nhà sản xuất hoàn trả phần tiền từ `coupon_disc`).
*   **Hành động:** 
    *   Sử dụng trực tiếp `sales_value` làm biến Outcome (Doanh thu). 
    *   Không cộng/trừ thêm `coupon_disc` vì nó không ảnh hưởng đến doanh thu thực nhận của siêu thị. Nếu cần ước tính *Giá gốc niêm yết (Shelf price)*, công thức là: `(sales_value - retail_disc - coupon_match_disc) / quantity` (lưu ý disc là số âm nên trừ sẽ thành cộng).

## 3. Khắc phục vấn đề Thưa thớt dữ liệu (Sparsity & Zero-filling)

Mô hình Uplift đo lường tác động của coupon trên cặp "Khách hàng × Ngành hàng" (Sử dụng `COMMODITY_DESC` làm category).

*   **Vấn đề:** Bảng `transaction_data` chỉ lưu các giao dịch thực tế (khi có phát sinh mua). Nếu khách hàng không mua ngành hàng A trong tuần 10, dữ liệu sẽ không tồn tại.
*   **Hành động:** 
    *   Thực hiện phép Cross-Join (tích Đề-các) để tạo một panel đủ các tổ hợp: `household_key` × `COMMODITY_DESC` × `week_no`.
    *   Dùng hàm `fillna(0)` cho các cột `sales_value` và `quantity` với những dòng được sinh ra từ Cross-Join.
    *   *Lưu ý:* Việc này rất quan trọng để mô hình ML hiểu được mức baseline (không mua hàng) thay vì hiểu nhầm là thiếu dữ liệu. Nếu dung lượng dữ liệu quá lớn, có thể gộp các khách hàng không bao giờ mua một ngành hàng (inactive) vào một nhóm hoặc loại bỏ để giảm chiều dữ liệu.

## 4. Xử lý Biến Nhiễu (Confounders) với `causal_data`

Để thỏa mãn điều kiện Không bị nhiễu (Unconfoundedness) trong Causal ML, các yếu tố kích thích mua sắm cần được kiểm soát.

*   **Vấn đề:** Nếu một sản phẩm vừa chạy coupon vừa được đưa lên trang nhất tạp chí (mailer) hoặc trưng bày nổi bật (display), việc tăng doanh số có thể do trưng bày chứ không hẳn do coupon.
*   **Hành động:** 
    *   Bắt buộc phải join (kết nối) bảng `causal_data` vào dataset.
    *   Tạo các cờ (flag) hoặc biến đếm cho mỗi cặp Khách hàng × Ngành hàng × Tuần:
        *   `is_on_display`: Có sản phẩm nào trong ngành hàng được lên khu trưng bày đặc biệt không?
        *   `is_on_mailer`: Có sản phẩm nào trong ngành hàng lên mailer không?
    *   Đưa các cờ này vào làm Control Features trong mô hình.

## 5. Tránh Data Leakage (Chảy máu dữ liệu)

Khi xây dựng các Features mô tả "Thói quen mua sắm" hoặc "Lịch sử mua hàng" (RFM), cần kiểm soát nghiêm ngặt mốc thời gian.

*   **Hành động:** 
    *   Giả sử chiến dịch X bắt đầu vào ngày $T_{start}$ (lấy từ bảng `campaign_desc`).
    *   Tất cả các Features mô tả quá khứ của khách hàng (ví dụ: Tổng doanh thu, Số lần đến siêu thị, Lượng chi tiêu cho nhóm ngành hàng) **chỉ được phép tính toán trên tập dữ liệu có $day < T_{start}$**.
    *   Outcome (Sự phản ứng của khách) sẽ được đánh giá ở giai đoạn $T_{start} \leq day \leq T_{end}$.

## 6. Định nghĩa Biến Can thiệp (Treatment Variable)

Tạm thời bỏ qua vấn đề "ẩn thông tin phân bổ 16 coupon của TypeA", flow đầy đủ sẽ như sau:

*   **Hành động:**
    *   Treatment (T) = 1 nếu khách hàng có nhận được coupon cho ngành hàng đó trong khoảng thời gian diễn ra chiến dịch.
    *   Treatment (T) = 0 nếu khách hàng không nhận được coupon.
    *   (Tạm thời ở bước này, có thể giả định khách hàng tham gia TypeA được gán Treatment cho các coupon thực tế họ đã Redeem, HOẶC xem toàn bộ pool của TypeA như là một Treatment - tùy vào hướng tiếp cận của nhóm khi quay lại xử lý sau).
