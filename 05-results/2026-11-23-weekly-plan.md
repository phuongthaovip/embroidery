---
updated: 2026-11-21
owner: CEO
status: DRAFT, chờ anh Nam duyệt. Chưa giao việc cho bot nào.
sources:
  - "brain/store-state.md"
  - "brain/team.md"
  - "brain/decisions.md"
  - "01-research/2026-11-12-holiday-calendar.md"
---

# Kế hoạch tuần 23–29/11/2026 — EmbroThread

**Mục tiêu tuần:** store nhận được tiền trước Black Friday (27/11), có đợt sale BF→CM chạy được, và catalog Christmas sạch, đủ để bán tới 10–15/12 (sau đó khách không còn kịp thêu).

Bot đang có: CEO, Product, QA, Shopify, Email. Chưa có Ads, SEO, Social, CS. Tuần này **không chạy quảng cáo trả tiền** (chưa có bot Ads, chưa có số liệu, chưa nhận tiền). Việc SEO/Social tuần này giao Shopify và Email làm phần tối thiểu. CS: CEO giữ (đơn đầu tiên gửi file thủ công).

## 1. Cần anh Nam quyết / làm (xếp theo mức chặn)

| # | Việc | Vì sao chặn | Hạn | Đề xuất của CEO |
|---|---|---|---|---|
| 1 | **Bật thanh toán**: hoàn tất Shopify Payments (Settings → Payments) hoặc bật **PayPal** trước | Không có nó thì 0 đơn, mọi việc khác vô nghĩa | **T3 24/11** | Bật PayPal ngay (vài phút, chỉ cần tài khoản PayPal), làm Shopify Payments song song |
| 2 | **Có chạy sale BF→CM không**, và mức giảm | Shopify + Email cần 2 ngày để dựng | T3 24/11 | Có, nếu #1 xong: giảm 30% toàn store 27–30/11, code tự áp dụng |
| 3 | **Chốt giá lẻ**: $3.99 (đang live) hay $3.23 (chuẩn) | Phải sửa trước khi chạy giảm giá, tránh giá gạch sai | T3 24/11 | Giữ $3.99 (Shopify không mất phí Etsy; sale 30% còn ~$2.79) |
| 4 | **Publish logo + favicon** trên Dawn | Store live đang không có logo, giảm niềm tin lúc có khách | T3 24/11 | Duyệt publish |
| 5 | **Ai gửi file cho khách, từ hộp mail nào** | Đơn đầu tiên cần giao trong 1–3 ngày làm việc | T4 25/11 | business@embrothread.com, anh hoặc 1 người team gửi; designer digitize trong 24h |
| 6 | **Duyệt lô Valentine V1–V14** | Phải list trước ~15/12 | T6 27/11 | Duyệt trong tuần để Product làm ảnh tuần sau |
| 7 | Hướng giao diện (Catalog / Theo mùa / Boutique) | Không chặn tuần này | Sau CM | Để sau 30/11, tuần này chỉ sửa nhỏ |
| 8 | Ngoại lệ font 26 chữ (vượt luật bundle 20); địa chỉ Contact; luật áp dụng Terms §13 | Không chặn | Khi tiện | Cho phép ngoại lệ font |

## 2. Kế hoạch theo ngày

| Ngày | Việc | Bot chủ | Đầu ra | Hạn |
|---|---|---|---|---|
| **T2 23/11** | Đếm lại sản phẩm thật trên Admin (ACTIVE/DRAFT/ảnh/giá), chốt 143 hay 153 | QA | Bảng đếm + danh sách lỗi listing, `05-results/2026-11-23-qa-count.md` | T2 |
| T2 23/11 | Kiểm Bundles / ITH / Faith đã có sản phẩm chưa → thêm lại vào menu; ảnh cho 6 collection | Shopify | Menu đủ, collection có ảnh | T3 |
| T2 23/11 | Bắt đầu làm lại ảnh 123 card bằng Canva, ưu tiên mẫu Christmas có nhiều ảnh lifestyle nhất | Product | 30 card/ngày, list sau khi QA đạt | T2–T6 |
| T2 23/11 | Bật form thu email (popup + footer) với lời mời "nhận ưu đãi Black Friday sớm" | Email | Form chạy, có thẻ khách `bf-2026` | T3 |
| **T3 24/11** | Sau khi anh chốt giá: sửa giá toàn bộ sản phẩm lẻ cho khớp | Product (Shopify CLI hàng loạt) | Mọi sản phẩm lẻ cùng 1 giá, ghi vào store-state | T3 |
| T3 24/11 | List 9 card EMBN Christmas (board Nguyen Hop) theo chuẩn | Product → QA | 9 sản phẩm ACTIVE | T4 |
| T3 24/11 | Publish logo + favicon (nếu anh duyệt) | Shopify | Dawn live có logo | T3 |
| **T4 25/11** | Dựng sale BF→CM (nếu anh duyệt): mã giảm tự động, thanh thông báo, banner trang chủ, collection "Black Friday Picks" (top 20 mẫu) | Shopify | Sale hẹn giờ 27/11 00:00 → 30/11 23:59 (giờ Mỹ ET) | T4 |
| T4 25/11 | Soạn 3 email: Early access (26/11), BF mở (27/11), Last chance CM (30/11); email giao file đơn hàng mẫu | Email | 3 email hẹn giờ + 1 mẫu email giao file | T4 |
| T4 25/11 | Viết SOP giao đơn: có đơn → báo designer → digitize → gửi mail → đánh dấu fulfilled | CEO | `brain/sops/order-digitize-delivery.md` cập nhật, có người + hộp mail | T4 |
| **T5 26/11** (Thanksgiving) | QA toàn store trước sale: test mua 1 đơn thật (nếu có thanh toán), kiểm giá giảm, link, mobile | QA | Báo cáo đạt/không đạt | T5 |
| T5 26/11 | Gửi email Early access | Email | Đã gửi | T5 |
| **T6 27/11** (Black Friday) | Sale bắt đầu. CEO xem số mỗi sáng tối: sessions, giỏ, đơn, doanh thu | CEO | Báo anh 2 lần/ngày tới 30/11 | T6–T2 |
| T6 27/11 | Giao file cho đơn đầu tiên trong 24h (nhanh hơn hứa 1–3 ngày) | CEO điều phối, người giao file | Đơn fulfilled | mỗi đơn |
| **T7 28/11 – CN 29/11** | Product tiếp tục ảnh + list; Shopify sửa nhanh chỗ khách rơi (trang thoát nhiều nhất) | Product, Shopify | Thêm 30 card/ngày | CN |
| CN 29/11 | Lint brain hằng tuần + snapshot metrics tuần | CEO | `brain/metrics/2026-11-29.md`, log | CN |
| **T2 30/11** (Cyber Monday) | Email Last chance; sale kết thúc 23:59 | Email, Shopify | Đóng sale, báo cáo BF→CM | T2 1/12 |

## 3. BF→CM: hai kịch bản

**A. Thanh toán xong trước T4 25/11 (nên làm):**
- Giảm 30% toàn store, tự áp dụng (không cần nhập code), 27–30/11.
- Collection "Black Friday Picks" 20 mẫu đẹp nhất + bundle nổi bật ở trang chủ.
- 3 email cho danh sách mới thu (sẽ ít, chủ yếu để có thói quen).
- Traffic: anh/ team chia sẻ thủ công lên Pinterest, nhóm Facebook thêu máy, Etsy shop bio của Paola/Kyra (link sang store). Không chạy ads.
- Kỳ vọng thực tế: vài đơn đầu tiên, quan trọng nhất là kiểm quy trình giao file chạy thật.

**B. Thanh toán chưa xong:**
- Không chạy sale (khách vào không mua được, mất uy tín).
- Dùng tuần để làm catalog: ảnh 123 card, 9 card EMBN, menu, logo, QA.
- Thu email với lời mời "Christmas sale sắp mở", chạy sale ngắn "Cyber Week kéo dài" 1–3/12 ngay khi thanh toán xong. File Christmas vẫn bán được tới ~10–15/12.

## 4. Sau khi anh duyệt
CEO giao từng dòng cho bot chủ, theo dõi trên Orca items, cập nhật `brain/store-state.md` (cột Chủ) và `brain/log.md` khi có thay đổi.
