ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH
TRƯỜNG ĐẠI HỌC KINH TẾ - LUẬT

ĐỀ CƯƠNG NGHIÊN CỨU

PHÂN TÍCH MỨC ĐỘ PHỤ THUỘC KHUYẾN MÃI THEO KHÁCH HÀNG VÀ NGÀNH HÀNG BẰNG MACHINE LEARNING NHẰM CÁ NHÂN HÓA CHIẾN LƯỢC PHÂN BỔ MÃ GIẢM GIÁ TRONG BÁN LẺ HÀNG TIÊU DÙNG
GVHD: PGS.TS. Lê Hoành Sử
Thành viên nghiên cứu:

| STT | Họ và tên | Mã học viên |
| --- | --- | --- |
| 1 | Lê Bảo Minh | C26611093 |
| 2 | Đặng Tịnh Kim Nguyên | C26611373 |
| 3 | Bùi Lê Trọng Đức | C26611274 |

Thành phố Hồ Chí Minh, tháng 9 năm 2026
# 1. Tổng quan đề tài nghiên cứu
## 1.1. Bối cảnh nghiên cứu
Trong bán lẻ hàng tiêu dùng, phiếu giảm giá (coupon) từ lâu đã là công cụ quen thuộc để kích cầu và giữ chân khách hàng. Tuy nhiên, trên thực tế, coupon thường được phát đại trà hoặc chỉ dựa trên khả năng mua hàng dự đoán của khách hàng. Cách làm này có một hạn chế lớn: doanh nghiệp dễ tốn ngân sách cho những khách hàng vốn đã định mua, trong khi lại bỏ sót những khách hàng thực sự cần một "cú hích" từ khuyến mãi mới quyết định mua (Miller & Hosanagar, 2020; Langen & Huber, 2023).
Vì vậy, bài toán cá nhân hóa khuyến mãi không chỉ dừng ở câu hỏi "Khách hàng nào nên nhận coupon?" mà còn là "Nhóm khách hàng đó nên nhận coupon cho ngành hàng nào và nên ưu tiên ra sao khi ngân sách marketing có hạn?". Các nghiên cứu trước cho thấy mức phản ứng với coupon khác nhau giữa các nhóm khách hàng (Langen & Huber, 2023; Miller & Hosanagar, 2020), nên cần xem xét tác động theo từng nhóm khách hàng thay vì chỉ xét mức trung bình chung. Một số nghiên cứu đã tiếp cận bài toán nhiều ngành hàng bằng mô hình kinh tế lượng (Pan và cộng sự, 2026) hoặc mô hình học sâu (Gabel & Timoshenko, 2022). Các cách tiếp cận này giúp hiểu và dự đoán hành vi mua ở nhiều ngành hàng, nhưng không nhằm trả lời trực tiếp câu hỏi: một coupon thực sự mang lại thêm bao nhiêu doanh thu cho từng nhóm khách hàng tại từng ngành hàng.
Xuất phát từ bối cảnh đó, đề tài hướng tới việc ứng dụng học máy nhân quả (Causal Machine Learning), tức là nhóm phương pháp đo lường phần kết quả tăng thêm do một tác động gây ra, để xây dựng Ma trận Phụ thuộc Khuyến mãi Khách hàng - Ngành hàng. Ma trận này là cơ sở định lượng giúp nhà bán lẻ phân bổ ngân sách coupon hiệu quả hơn và cá nhân hóa chiến lược marketing.
## 1.2. Mục tiêu nghiên cứu
Mục tiêu tổng quát:
Xây dựng mô hình học máy nhân quả (Causal Machine Learning) nhằm định lượng mức độ tác động của coupon đến hành vi mua hàng ở cấp độ từng cặp khách hàng - ngành hàng, từ đó đề xuất chiến lược phân bổ coupon cá nhân hóa cho lĩnh vực bán lẻ.
Mục tiêu cụ thể:
Phân nhóm khách hàng dựa trên thói quen mua sắm, sở thích ngành hàng và lịch sử sử dụng khuyến mãi, nhằm làm cơ sở xem xét mức phản ứng với coupon khác nhau giữa các nhóm.
Ứng dụng kỹ thuật học máy nhân quả (Uplift Modeling, …) để đo lường một coupon khi được phát ra sẽ thực sự mang lại thêm bao nhiêu doanh thu đối với từng nhóm khách hàng, tại từng ngành hàng cụ thể.
Xây dựng "Ma trận Phụ thuộc Khuyến mãi Khách hàng - Ngành hàng" để trực quan hóa kết quả. Cuối cùng, đánh giá độ tin cậy của ma trận này bằng các thước đo chuyên dụng (Qini, AUUC) nhằm đánh giá xem việc phân bổ coupon theo ma trận có tốt hơn các phương pháp phát coupon đại trà hay không.
Đề xuất khung chiến lược coupon cá nhân hóa dựa trên sự kết hợp giữa phân khúc khách hàng và mức độ phụ thuộc vào khuyến mãi theo ngành hàng, trong điều kiện ngân sách marketing có hạn, nhằm hỗ trợ doanh nghiệp xác định khách hàng nào nên được tiếp cận, nên ưu tiên ngành hàng nào và mức độ ưu tiên coupon như thế nào.
## 1.3. Câu hỏi nghiên cứu
RQ1: Đặc điểm hành vi mua sắm, sở thích ngành hàng và lịch sử sử dụng khuyến mãi phân hóa như thế nào giữa các nhóm khách hàng?
RQ2: Phiếu giảm giá làm doanh thu tăng thêm bao nhiêu đối với từng nhóm khách hàng tại từng ngành hàng, và mức tăng này khác biệt như thế nào giữa các nhóm khách hàng và giữa các ngành hàng?
RQ3: Dựa trên kết quả ước lượng từ mô hình học máy nhân quả, nên phân bổ coupon cho nhóm khách hàng nào, ở ngành hàng nào khi ngân sách có hạn; và cách phân bổ này tạo ra giá trị tăng thêm sau chi phí giảm giá chênh lệch như thế nào so với phát đại trà hoặc nhắm theo xác suất mua, ở cùng mức ngân sách?
## 1.4. Giả thuyết nghiên cứu
Dựa trên khung lý thuyết ở mục 2.1 và kết quả của các nghiên cứu trước ở các mục 2.2 đến 2.4, nhóm đề xuất bốn giả thuyết sau. Trong đề cương này, “uplift” được hiểu là phần doanh thu tăng thêm nhờ nhận coupon, so với trường hợp không nhận coupon.
H1: Uplift của coupon khác nhau có ý nghĩa thống kê giữa các nhóm khách hàng.
Cơ sở: Langen và Huber (2023) ghi nhận tác động của coupon khác biệt rõ rệt giữa các nhóm khách hàng, đặc biệt theo mức chi tiêu trước chiến dịch. Miller và Hosanagar (2020) cũng cho thấy mức phản ứng với giảm giá khác nhau giữa các khách hàng. Luick và cộng sự (2024) ghi nhận doanh số tăng mạnh hơn ở các cửa hàng có nhiều khách hàng thu nhập thấp.
H2: Uplift của coupon khác nhau có ý nghĩa thống kê giữa các ngành hàng.
Cơ sở: Guan, Atlas và Vadiveloo (2018), sử dụng cùng nguồn dữ liệu Dunnhumby, cho thấy mức tăng lượng mua nhờ coupon chênh lệch lớn giữa các ngành hàng (thực phẩm tiện lợi tăng khoảng 1,17 đơn vị/tuần, trong khi các loại hạt chỉ tăng khoảng 0,03 đơn vị/tuần). Langen và Huber (2023) cũng ghi nhận chỉ hai trong năm nhóm coupon theo ngành hàng làm tăng chi tiêu có ý nghĩa thống kê.
H3: Tác động của coupon phụ thuộc đồng thời vào nhóm khách hàng và ngành hàng; do đó, xem xét cả hai chiều cùng lúc giúp chọn đúng khách hàng và đúng ngành hàng tốt hơn so với chỉ xét một chiều.
Cơ sở: Langen và Huber (2023) cho thấy coupon dược mỹ phẩm hiệu quả hơn với khách hàng chi tiêu nhiều trước chiến dịch, còn coupon nhóm thực phẩm khác lại hiệu quả hơn với khách hàng chi tiêu ít. Đây là giả thuyết trung tâm, gắn trực tiếp với khoảng trống nghiên cứu ở mục 3.1.
H4: Với cùng một mức ngân sách, chính sách phân bổ coupon dựa trên Ma trận Phụ thuộc Khuyến mãi mang lại giá trị tăng thêm sau khi trừ chi phí coupon cao hơn so với phát coupon đại trà hoặc chỉ nhắm theo xác suất mua.
Cơ sở: Miller và Hosanagar (2020) cho thấy khi nhắm mục tiêu có tính đến cả mức mua thông thường lẫn mức phản ứng với giảm giá của từng khách hàng, kết quả tốt hơn so với cách nhắm không tính đến chiết khấu. Zhou và cộng sự (2023) và Yan và cộng sự (2026) cũng ủng hộ việc đưa chi phí và ngân sách vào quyết định phân bổ.
Liên hệ giữa câu hỏi và giả thuyết: RQ1 là câu hỏi mô tả, được trả lời bằng kết quả phân cụm và thống kê mô tả, nên không đặt giả thuyết. H1, H2 và H3 trả lời RQ2, trong đó H3 là đóng góp phương pháp trọng tâm của đề tài. H4 trả lời RQ3. Cách kiểm định các giả thuyết được trình bày ở mục 4.2.5.
## 1.5. Đối tượng và phạm vi nghiên cứu
Đối tượng nghiên cứu: Tác động của coupon đến chi tiêu của khách hàng ở cấp độ từng cặp nhóm khách hàng - ngành hàng.
Về dữ liệu và thời gian: Nghiên cứu sử dụng bộ dữ liệu The Complete Journey của Dunnhumby (Dunnhumby, n.d.), ghi nhận giao dịch thực tế đã được ẩn danh của 2.500 hộ gia đình mua sắm thường xuyên tại một chuỗi bán lẻ trong khoảng hai năm. Đây là dữ liệu giao dịch thật, không phải dữ liệu mô phỏng. Nghiên cứu dự kiến được thực hiện từ 12/09/2026 đến 16/10/2026.
Về không gian: Do dữ liệu đã được ẩn danh, nghiên cứu không xác định cụ thể thị trường địa lý của chuỗi bán lẻ.
Phạm vi dữ liệu: Nghiên cứu sử dụng dữ liệu giao dịch ở cấp hộ gia đình, kết hợp thông tin sản phẩm, nhóm sản phẩm, chiến dịch khuyến mãi, việc nhận và sử dụng coupon, cùng thông tin nhân khẩu học (chỉ có cho một phần hộ gia đình). Mối quan hệ giữa khách hàng và nhóm sản phẩm là đơn vị phân tích chính.
Lưu ý về dữ liệu: Thứ nhất, coupon trong bộ dữ liệu không được phát ngẫu nhiên mà dựa trên lịch sử mua của khách hàng (Guan và cộng sự, 2018); vì vậy, khi ước lượng tác động, nghiên cứu cần kiểm soát hành vi mua trước chiến dịch (mục 4.2.3). Thứ hai, do đơn vị phân tích là cặp nhóm khách hàng × ngành hàng, một số ô trong ma trận có thể có ít quan sát; rủi ro này được xử lý ở bước tiền xử lý (mục 4.2.1).
## 1.6. Cấu trúc nghiên cứu
Chương 1 - Giới thiệu chung về đề tài nghiên cứu: Lý do chọn đề tài, mục tiêu, phạm vi và phương pháp nghiên cứu.
Chương 2 - Khái niệm và cơ sở lý thuyết của đề tài.
Chương 3 - Phương pháp thực hiện.
Chương 4 - Kết quả nghiên cứu.
Chương 5 - Đề xuất các chiến dịch kinh doanh phù hợp dựa trên dữ liệu.

## 1.7. Quy trình nghiên cứu

| Giai đoạn | Thực hiện |
| --- | --- |
| 1. Xác định vấn đề | Xác định vấn đề, câu hỏi, giả thuyết, mục tiêu và phạm vi nghiên cứu về tác động của khuyến mãi đối với hành vi mua hàng. |
| 2. Tổng quan tài liệu | Tổng hợp các nghiên cứu liên quan, xác định khoảng trống và xây dựng khung nghiên cứu. |
| 3. Thu thập và lựa chọn dữ liệu | Lựa chọn bộ dữ liệu giao dịch phù hợp; xác định các biến về khách hàng, ngành hàng, khuyến mãi và phản ứng mua hàng. |
| 4. Khám phá và tiền xử lý dữ liệu | Phân tích khám phá (EDA), làm sạch dữ liệu, xử lý các ô ít quan sát, chọn biến cho mô hình. |
| 5. Xây dựng và đánh giá mô hình | Xây dựng mô hình học máy nhân quả để ước lượng tác động của coupon và đánh giá kết quả mô hình. |
| 6. Kiểm định H1, H2, H3 và xây dựng ma trận | Phân tích tác động theo nhóm khách hàng và ngành hàng, kiểm định H1, H2, H3, xây dựng ma trận phụ thuộc khuyến mãi. |
| 7. Phân bổ coupon và kiểm định H4 | Xây dựng chính sách phân bổ có ràng buộc ngân sách, so sánh với cách phát đại trà để kiểm định H4. |
| 8. Thảo luận và đề xuất | Thảo luận kết quả, đề xuất ứng dụng cá nhân hóa coupon, nêu hạn chế và hướng nghiên cứu tiếp theo. |

# 2. Khung lý thuyết và tổng quan các nghiên cứu liên quan
Coupon là công cụ kích cầu phổ biến trong bán lẻ hàng tiêu dùng, nhưng câu hỏi quản trị xoay quanh công cụ này đã thay đổi đáng kể. Trước đây, câu hỏi thường là “Khách hàng nào có khả năng mua cao nhất?”. Hiện nay, câu hỏi là: “Khách hàng nào sẽ mua nhờ nhận được coupon, ở ngành hàng nào và với chi phí bao nhiêu?”. Phần này trình bày khung lý thuyết của đề tài và ba luồng nghiên cứu liên quan.
## 2.1. Khung lý thuyết: mô hình kết quả tiềm năng
Đề tài dựa trên khung “kết quả tiềm năng” (potential outcomes), là khung lý thuyết nền của học máy nhân quả, được Langen và Huber (2023) áp dụng để đánh giá chiến dịch coupon của một nhà bán lẻ. Theo khung này, mỗi hộ gia đình có hai kết quả có thể xảy ra: mức chi tiêu nếu nhận coupon và mức chi tiêu nếu không nhận coupon. Tác động của coupon chính là chênh lệch giữa hai mức này. Khó khăn là, trên thực tế, mỗi hộ chỉ quan sát được một trong hai kết quả, nên tác động không thể đo trực tiếp cho từng hộ mà phải ước lượng bằng cách so sánh các hộ có đặc điểm tương tự nhau.
Khi lấy trung bình chênh lệch này cho một nhóm đối tượng có chung đặc điểm, ta có tác động trung bình có điều kiện (CATE). Trong đề tài, nhóm đối tượng là từng cặp nhóm khách hàng - ngành hàng, và CATE của mỗi cặp chính là “mức độ phụ thuộc khuyến mãi” được thể hiện trong ma trận. Các giả thuyết H1, H2 và H3 thực chất là câu hỏi CATE có khác nhau giữa các nhóm khách hàng, giữa các ngành hàng và giữa các cặp kết hợp hay không.
Để ước lượng đáng tin cậy khi coupon không được phát ngẫu nhiên, Langen và Huber (2023) nêu ba điều kiện chính: (1) các yếu tố vừa ảnh hưởng đến việc nhận coupon, vừa ảnh hưởng đến chi tiêu phải có trong dữ liệu để kiểm soát; (2) ở mỗi nhóm đặc điểm phải có cả hộ nhận và hộ không nhận coupon để so sánh; (3) coupon của hộ này không làm thay đổi chi tiêu của hộ khác. Nghiên cứu áp dụng các điều kiện này ở mục 4.2.3 và nêu rủi ro khi chúng không được đáp ứng hoàn toàn ở mục 6.
Bên cạnh đó, Miller và Hosanagar (2020) đặt bài toán phát coupon vào một khung ra quyết định: có nên phát coupon cho một khách hàng hay không phụ thuộc vào cả mức mua thông thường của khách hàng đó (vì khách vốn đã định mua cũng được hưởng giảm giá, làm phát sinh chi phí) lẫn phần tăng thêm mà coupon tạo ra. Đây là cơ sở cho bước phân bổ coupon có giới hạn ngân sách ở mục 4.2.4 và cho giả thuyết H4.
## 2.2. Luồng 1: Sự lãng phí của khuyến mãi đại trà và giới hạn của cách tiếp cận dự đoán
Cách tiếp cận truyền thống thường ưu tiên phát coupon cho những khách hàng có xác suất mua hoặc giá trị giao dịch dự đoán cao nhất. Langen và Huber (2023) chỉ ra rằng cách làm này dễ nhầm lẫn giữa tương quan và nhân quả. Ví dụ, nếu coupon được phát tại cửa hàng thì khách hàng thường xuyên sẽ nhận được nhiều coupon hơn; khi đó, mô hình dự đoán sẽ thấy coupon “đi kèm” doanh số cao, ngay cả khi coupon thực ra không làm tăng doanh số. Khi dùng học máy nhân quả trên dữ liệu các chiến dịch coupon của một nhà bán lẻ, hai tác giả thấy chỉ hai trong năm nhóm coupon tạo ra tác động dương có ý nghĩa thống kê lên chi tiêu.
Miller và Hosanagar (2020) đưa lập luận này vào một khung ra quyết định, theo đó, quyết định phát coupon tối ưu cần cân nhắc đồng thời mức mua thông thường của khách hàng và mức phản ứng của họ với giảm giá. Nói cách khác, chỉ nhắm vào người có khả năng mua cao hoặc chỉ nhắm vào người có phản ứng dương đều chưa đủ. Tổng quan của De Biasio, Navarin và Jannach (2024) về các hệ thống gợi ý kinh tế cũng cho thấy các hệ thống này ngày càng quan tâm đến mục tiêu kinh tế của doanh nghiệp như doanh thu và lợi nhuận, chứ không chỉ độ chính xác dự đoán.
## 2.3. Luồng 2: Tác động khuyến mãi khác nhau giữa các ngành hàng
Nếu Luồng 1 trả lời câu hỏi “tặng coupon cho ai”, thì Luồng 2 cho thấy câu hỏi đó chưa đầy đủ khi chưa biết “coupon cho ngành hàng nào”. Ở cấp tổng thể, Leeflang và Parreño-Selva (2012) cho thấy khuyến mãi giá ở một ngành hàng có thể ảnh hưởng đến nhu cầu của các ngành hàng khác. Trong khi đó, Luick và cộng sự (2024), qua ba thử nghiệm tự nhiên tại siêu thị ở Anh, ghi nhận hiệu quả khuyến mãi không đồng đều giữa các nhóm sản phẩm và không thấy thay đổi kéo dài sau khi chương trình kết thúc.
Ở cấp hộ gia đình, Guan, Atlas và Vadiveloo (2018) phân tích dữ liệu của 2.500 hộ gia đình trong hai năm từ cùng nguồn Dunnhumby và thấy mức tăng lượng mua nhờ coupon chênh lệch lớn giữa các ngành hàng. Các tác giả cũng lưu ý rằng coupon được nhắm theo hành vi mua trước đó, nên kết quả có thể bị ảnh hưởng bởi cách chọn khách hàng. Langen và Huber (2023) bổ sung một góc nhìn quan trọng: coupon dược mỹ phẩm hiệu quả hơn với khách hàng chi tiêu nhiều trước chiến dịch, còn coupon nhóm thực phẩm khác lại hiệu quả hơn với khách hàng chi tiêu ít.
Về mặt mô hình hóa, các mô hình kinh tế lượng như của Pan và cộng sự (2026) giúp hiểu cách khách hàng mua nhiều ngành hàng cùng lúc và phản ứng với khuyến mãi; các mô hình học sâu như của Gabel và Timoshenko (2022) xử lý tốt số lượng sản phẩm rất lớn. Tuy nhiên, các hướng này tập trung vào mô tả và dự đoán hành vi lựa chọn, chưa đặt trọng tâm vào việc đo lường phần doanh thu tăng thêm mà coupon mang lại cho từng nhóm khách hàng ở từng ngành hàng.
## 2.4. Luồng 3: Học máy nhân quả và bài toán phân bổ có giới hạn ngân sách
Học máy nhân quả, với trọng tâm là mô hình uplift và ước lượng tác động theo từng nhóm đối tượng (CATE, tức tác động trung bình có điều kiện), cung cấp công cụ để vượt qua những hạn chế trên. Các nghiên cứu so sánh quy mô lớn của Olaya, Coussement và Verbeke (2020) và Gubela, Lessmann và Stöcker (2024) cho thấy nhóm phương pháp này đã được thử nghiệm rộng rãi trong marketing, kể cả khi có nhiều loại can thiệp khác nhau.
Một hướng phát triển quan trọng là đưa chi phí và ngân sách trực tiếp vào quá trình ra quyết định. Zhou và cộng sự (2023) đề xuất học trực tiếp một “chỉ số quyết định” thay cho cách làm hai bước tách rời (dự đoán trước rồi tối ưu sau) và ghi nhận cải thiện rõ rệt qua thử nghiệm thực tế. Zhang và cộng sự (2024) xây dựng một khung học liên tục để phân bổ giảm giá cá nhân hóa. Yan và cộng sự (2026) so sánh các chính sách phân bổ coupon trong thương mại điện tử dưới giới hạn về số người nhận và tổng ngân sách, đồng thời nhấn mạnh cần tách bạch chi phí coupon khi đánh giá hiệu quả thay vì chỉ nhìn vào doanh thu.
# 3. Khoảng trống nghiên cứu và điểm mới
## 3.1. Khoảng trống nghiên cứu
Khi đặt ba luồng nghiên cứu cạnh nhau, có thể thấy một sự lệch pha. Các nghiên cứu dùng học máy nhân quả thường đo tác động trên một chỉ số tổng hợp như xác suất mua (Miller & Hosanagar, 2020), chi tiêu bình quân ngày (Langen & Huber, 2023) hoặc tổng giá trị giao dịch (Zhou và cộng sự, 2023; Yan và cộng sự, 2026). Langen và Huber (2023) đã tách coupon thành năm nhóm theo ngành hàng và so sánh giữa các nhóm khách hàng, nhưng biến kết quả vẫn là tổng chi tiêu và số nhóm ngành hàng còn ít. Ngược lại, Guan và cộng sự (2018) so sánh tác động của coupon giữa nhiều ngành hàng trên cùng nguồn dữ liệu với đề tài này, nhưng chủ yếu ở mức toàn bộ hộ gia đình, chưa đi đến từng nhóm khách hàng và chưa gắn với bài toán phân bổ ngân sách.
Trong phạm vi tài liệu nhóm đã khảo sát, chưa thấy nghiên cứu nào dùng học máy nhân quả để đo tác động của coupon lên chi tiêu của từng ngành hàng, cho từng cặp nhóm khách hàng - ngành hàng, trên nhiều ngành hàng, đồng thời gắn kết quả với chi phí và ngân sách. Thiếu công cụ này, doanh nghiệp có thể gặp một kiểu lãng phí khó nhận ra nếu chỉ nhìn vào tổng doanh thu: gửi coupon đúng người nhưng sai ngành hàng.
## 3.2. Điểm mới của đề tài
Đề tài được thiết kế để lấp đầy khoảng trống trên bằng cách đưa năng lực của học máy nhân quả xuống cấp độ khách hàng × ngành hàng:
Chuyển biến kết quả từ tổng doanh thu sang doanh thu theo từng ngành hàng, cho phép ước lượng tác động riêng cho từng cặp nhóm khách hàng - ngành hàng (kiểm định H1, H2, H3; trả lời RQ2).
Xây dựng Ma trận Phụ thuộc Khuyến mãi Khách hàng - Ngành hàng để nhận diện trực quan những vùng phụ thuộc khuyến mãi cao nên đầu tư và những vùng khách hàng vẫn mua dù không có khuyến mãi nên cắt giảm.
Chuyển ma trận thành chính sách phân bổ coupon có giới hạn ngân sách, cung cấp cơ sở định lượng cho doanh nghiệp (kiểm định H4; trả lời RQ3).
Tóm tắt tính mới: Khác với các nghiên cứu trước chỉ đo tác động của coupon trên tổng chi tiêu (Langen & Huber, 2023) hoặc so sánh mức tăng mua theo ngành hàng ở mức toàn bộ hộ gia đình (Guan và cộng sự, 2018), nghiên cứu này đo tác động của coupon lên chi tiêu từng ngành hàng cho từng cặp nhóm khách hàng - ngành hàng, và chuyển kết quả thành chính sách phân bổ coupon có giới hạn ngân sách.
# 4. Cơ sở lý thuyết và phương pháp nghiên cứu
## 4.1. Cơ sở lý thuyết
### 4.1.1. Coupon/Promotion
Coupon và promotion là các công cụ marketing được sử dụng nhằm tạo động lực và ảnh hưởng đến hành vi mua của khách hàng. Trong bán lẻ, hiệu quả của promotion có thể khác nhau giữa các ngành hàng và không nhất thiết chỉ tác động đến sản phẩm được khuyến mãi. Guan et al. (2018) cho thấy coupon được nhắm mục tiêu có thể ảnh hưởng đến mức mua ở cấp ngành hàng, trong khi Leeflang và Parreño-Selva (2012) chỉ ra rằng promotion có thể tạo ra cả tác động trong ngành hàng và tác động giữa các ngành hàng. Vì vậy, coupon được xem là một dạng can thiệp marketing có khả năng tạo ra những thay đổi khác nhau trong hành vi mua.
### 4.1.2. Causal Machine Learning và Uplift Modeling
Causal Machine Learning là cách tiếp cận kết hợp suy luận nhân quả với học máy nhằm ước lượng tác động của một treatment lên outcome. Khác với mô hình dự đoán thông thường, phương pháp này tập trung vào việc xác định outcome thay đổi như thế nào khi một đối tượng nhận treatment so với khi không nhận treatment. Langen và Huber (2023) cho thấy Causal Machine Learning có thể được áp dụng để đánh giá tác động của coupon trong marketing. Trong khi đó, Olaya et al. (2020) định nghĩa Uplift Modeling là phương pháp ước lượng sự thay đổi của outcome do treatment gây ra ở cấp độ từng đối tượng.
### 4.1.3. Mục tiêu cá nhân hóa
Mục tiêu cá nhân hóa (Personalized Targeting) là cách tiếp cận trong marketing nhằm lựa chọn và cung cấp ưu đãi phù hợp với đặc điểm và phản ứng của từng khách hàng. Miller và Hosanagar (2020) cho thấy dữ liệu và phương pháp học máy nhân quả có thể được sử dụng để cá nhân hóa mức giảm giá dựa trên tác động của khuyến mãi đối với từng khách hàng. Gubela et al. (2024) cũng cho thấy trong các chiến dịch marketing có nhiều hình thức can thiệp, việc lựa chọn hình thức phù hợp cần xem xét sự khác biệt trong phản ứng của từng đối tượng. Do đó, nhắm mục tiêu cá nhân hóa hướng đến việc phân bổ các ưu đãi dựa trên mức độ phản ứng của từng khách hàng thay vì áp dụng một chính sách chung cho toàn bộ khách hàng.

## 4.2. Phương pháp nghiên cứu
Nghiên cứu được thực hiện theo phương pháp định lượng dựa trên dữ liệu (data-driven quantitative research), kết hợp giữa khai phá dữ liệu, phân cụm khách hàng và Causal Machine Learning nhằm xác định mức độ tác động gia tăng của coupon đối với hành vi mua hàng tại từng nhóm khách hàng và từng ngành hàng. Phương pháp nghiên cứu gồm năm phần chính:
### 4.2.1. Xử lý và phân tích dữ liệu
Khai phá, làm sạch, chuẩn hóa dữ liệu và thực hiện phân tích thống kê để xây dựng các đặc trưng về hành vi mua sắm và sử dụng khuyến mãi của khách hàng. Các đặc trưng được lấy từ giai đoạn trước chiến dịch; ngành hàng có ít giao dịch sẽ được gộp lại để tránh thiếu dữ liệu.
### 4.2.2. Phân cụm khách hàng
Áp dụng các phương pháp phân cụm để xác định các nhóm khách hàng có đặc điểm hành vi tương đồng và xây dựng chân dung cho từng nhóm.
### 4.2.3. Xây dựng mô hình Causal Machine Learning
Áp dụng các phương pháp Causal ML/Uplift Modeling để ước lượng CATE, qua đó đo lường tác động gia tăng của coupon đối với từng nhóm khách hàng trong từng ngành hàng. Do coupon không được phát ngẫu nhiên, mô hình sẽ so sánh những hộ có hành vi mua trước chiến dịch tương tự nhau, chỉ khác ở việc có nhận coupon hay không.
### 4.2.4. Tối ưu hóa phân bổ coupon
Dựa trên giá trị CATE, xây dựng cơ chế phân bổ có giới hạn ngân sách và đề xuất mức khuyến mãi phù hợp (5%, 10%, 20%, …) cho từng nhóm khách hàng và ngành hàng.
### 4.2.5. Đánh giá mô hình và kiểm định giả thuyết
Đánh giá mô hình bằng Qini và AUUC trên tập dữ liệu giữ lại. H1 và H2 được kiểm định bằng cách so sánh mức uplift giữa các nhóm khách hàng và giữa các ngành hàng; H3 bằng cách so sánh hiệu quả khi nhắm theo hai chiều (khách hàng × ngành hàng) với khi chỉ nhắm theo một chiều; H4 bằng cách so sánh giá trị tăng thêm sau chi phí coupon giữa chính sách theo ma trận, phát đại trà và nhắm theo xác suất mua, ở cùng mức ngân sách.

# 5. Kết quả dự kiến
Về lý thuyết: Mở rộng cách tiếp cận học máy nhân quả từ mức tổng thể xuống cấp độ nhóm khách hàng kết hợp ngành hàng, qua đó đo tác động tăng thêm của coupon lên doanh thu từng ngành hàng. Đề xuất Ma trận Phụ thuộc Khuyến mãi Khách hàng - Ngành hàng như một công cụ trực quan để phân tích mức độ phụ thuộc vào khuyến mãi, cùng với kết quả kiểm định các giả thuyết H1 đến H4.
Về thực tiễn: Xây dựng khung chiến lược cá nhân hóa coupon, giúp xác định khách hàng nào cần được tiếp cận, ngành hàng nào nên ưu tiên và mức độ ưu tiên coupon cho từng nhóm.
Về ứng dụng: Cung cấp cơ sở định lượng giúp doanh nghiệp sử dụng ngân sách khuyến mãi hiệu quả hơn, tập trung nguồn lực vào những nhóm khách hàng và ngành hàng có tác động tăng thêm cao.
# 6. Hạn chế dự kiến
Coupon không được phát ngẫu nhiên, nên dù đã kiểm soát hành vi mua trước chiến dịch, kết quả vẫn có thể bị ảnh hưởng bởi các yếu tố không có trong dữ liệu.
Thông tin nhân khẩu học chỉ có cho một phần hộ gia đình.
Dữ liệu đến từ một chuỗi bán lẻ và đã được ẩn danh theo thị trường, nên cần thận trọng khi áp dụng cho thị trường khác như Việt Nam.
Một số cặp nhóm khách hàng - ngành hàng có ít quan sát nên kết quả ở các ô này kém chắc chắn hơn.

# Tài liệu tham khảo

[1] De Biasio, A., Navarin, N., & Jannach, D. (2024). Economic recommender systems – A systematic review. Electronic Commerce Research and Applications, 63, 101352. https://doi.org/10.1016/j.elerap.2023.101352
[2] dunnhumby. (n.d.). The Complete Journey [Data set]. https://www.dunnhumby.com/source-files/
[3] Gabel, S., & Timoshenko, A. (2022). Product choice with large assortments: A scalable deep-learning model. Management Science, 68(3), 1808–1827. https://doi.org/10.1287/mnsc.2021.3969
[4] Guan, X., Atlas, S. A., & Vadiveloo, M. (2018). Targeted retail coupons influence category-level food purchases over 2-years. International Journal of Behavioral Nutrition and Physical Activity, 15, 111. https://doi.org/10.1186/s12966-018-0744-7
[5] Gubela, R. M., Lessmann, S., & Stöcker, B. (2024). Multiple treatment modeling for target marketing campaigns: A large-scale benchmark study. Information Systems Frontiers, 26, 875–898. https://doi.org/10.1007/s10796-022-10283-4
[6] Langen, H., & Huber, M. (2023). How causal machine learning can leverage marketing strategies: Assessing and improving the performance of a coupon campaign. PLOS ONE, 18(1), e0278937. https://doi.org/10.1371/journal.pone.0278937
[7] Leeflang, P. S. H., & Parreño-Selva, J. (2012). Cross-category demand effects of price promotions. Journal of the Academy of Marketing Science, 40(4), 572–586. https://doi.org/10.1007/s11747-010-0244-z
[8] Luick, M., Bandy, L., Piernas, C., Jebb, S. A., & Pechey, R. (2024). Do promotions of healthier or more sustainable foods increase sales? Findings from three natural experiments in UK supermarkets. BMC Public Health, 24, Article 1658. https://doi.org/10.1186/s12889-024-19080-x
[9] Miller, A. P., & Hosanagar, K. (2020). Personalized discount targeting with causal machine learning. In Proceedings of the 41st International Conference on Information Systems (ICIS 2020). https://aisel.aisnet.org/icis2020/digital_commerce/digital_commerce/7
[10] Olaya, D., Coussement, K., & Verbeke, W. (2020). A survey and benchmarking study of multitreatment uplift modeling. Data Mining and Knowledge Discovery, 34(1), 273–308. https://doi.org/10.1007/s10618-019-00670-y
[11] Pan, Y., Russell, G., Gruca, T. S., & Li, C. (2026). Multicategory purchase behavior: Basket choice, shopping frequency, and promotional analysis. Journal of Retailing, 102(1), 44–62. https://doi.org/10.1016/j.jretai.2025.08.002
[12] Yan, Y., Qiu, S., Son, S., Duan, X., & Li, J. (2026). Incremental net contribution from targeted coupons: A budget-constrained policy evaluation framework. Journal of Theoretical and Applied Electronic Commerce Research, 21(8), 240. https://doi.org/10.3390/jtaer21080240
[13] Zhang, J. S., Howson, B., Savva, P., & Loh, E. (2024). DISCO: An end-to-end bandit framework for personalised discount allocation [Preprint]. arXiv. https://arxiv.org/abs/2406.06433
[14] Zhou, H., Li, S., Jiang, G., Zheng, J., & Wang, D. (2023). Direct heterogeneous causal learning for resource allocation problems in marketing. Proceedings of the AAAI Conference on Artificial Intelligence, 37(4), 5446–5454. https://doi.org/10.1609/aaai.v37i4.25677
