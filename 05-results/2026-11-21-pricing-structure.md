---
updated: 2026-11-21
owner: CEO
status: ĐỀ XUẤT, chờ anh Nam duyệt. Chưa đổi gì trên store.
sources:
  - "Shopify Admin API, 2026-11-21 (154 sản phẩm)"
  - "00-context/shopify-listing-standard.md §7"
  - "01-research/2026-10-17-shop-competitor-analysis.md"
  - "01-research/2026-11-20-store-design-benchmark.md"
---

# Cấu trúc giá EmbroThread — đề xuất

## Hiện trạng (Shopify, 2026-11-21)
137 ACTIVE / 17 DRAFT / 154 tổng.

| Loại (ACTIVE) | Số | Giá đang để |
|---|---|---|
| Lẻ | 100 | 90 cái $3.23, **10 cái $3.99** (đợt 1) — lẫn giá |
| Bundle 2–5 | 2 | $5.99 |
| Bundle 6–10 | 14 | $8.99 |
| Bundle 11–15 | 12 | $11.99 |
| Bundle 16–20 | 5 | $14.99 |
| Alphabet / font | 4 | $9.99 |

Vấn đề:
1. Giá lẻ lẫn $3.23 / $3.99. Số lẻ .23 là từ quy đổi VND trên Etsy, trên web riêng nhìn lạ.
2. Không có gì khuyến khích mua nhiều mẫu lẻ (giỏ trung bình sẽ ~1 file ≈ $3–4, phí thanh toán ~$0.40/đơn ăn ~10%).
3. Không có mẫu free đổi email (cả 4 store lớn đều có).
4. Ràng buộc: **chỉ digitize khi có đơn** → mỗi mẫu bán ra tốn công designer. Bundle càng lớn, đơn càng tốn công. Vì vậy giữ luật bundle ≤ 20, không làm mega bundle 100+ cho tới khi file có sẵn.

Tham chiếu: đối thủ Etsy bán lẻ $3.99–4.70; mega bundle 300–400 mẫu $13–17 (file có sẵn). Store lớn (Urban Threads) bán lẻ cao hơn, giá sale ≈ giá mình.

## Đề xuất: 4 tầng

### 1. Giá niêm yết (cố định, dễ nhớ, đuôi .99)
| Loại | Giá mới | Đổi |
|---|---|---|
| Lẻ (1 mẫu) | **$3.99** | 90 sản phẩm $3.23 → $3.99 |
| Bundle 2–5 | $5.99 | giữ |
| Bundle 6–10 | $8.99 | giữ |
| Bundle 11–15 | $11.99 | giữ |
| Bundle 16–20 | $14.99 | giữ |
| Alphabet / font | $9.99 | giữ |

Lý do giữ bundle: giá mỗi mẫu trong bundle đã rẻ ($0.75–1.20/mẫu), đúng vai trò "mua bundle lợi hơn", và đã cạnh tranh với đối thủ. Lẻ lên $3.99 vẫn ngang đối thủ thấp nhất, và làm bundle trông hời hơn.

### 2. Mua nhiều, giảm tự động (mix & match mẫu lẻ)
- 3 mẫu lẻ trở lên: **-20%**
- 5 mẫu lẻ trở lên: **-30%**
Dùng Automatic discount của Shopify (không cần mã). Mục tiêu: đẩy giỏ từ 1 file lên 3–5 file.

### 3. Free design đổi email
1 mẫu Christmas đơn giản, đã digitize sẵn, giao ngay qua app Digital Products khi khách đăng ký email. Đây là lý do để Email bot có danh sách.

### 4. Khuyến mãi theo mùa (chỉ dùng giảm giá THẬT)
- Black Friday → Cyber Monday 27–30/11: **-30% toàn store** (không cộng dồn với tầng 2; Shopify lấy mức có lợi nhất cho khách).
- Không dùng giá gạch (compare-at) giả kiểu "luôn sale 50%" như Etsy: trên web riêng dễ bị coi là giá ảo (luật FTC Mỹ). Chỉ gạch giá trong thời gian sale thật.

## Việc cần làm sau khi anh duyệt
| Việc | Bot |
|---|---|
| Đổi 90 sản phẩm lẻ $3.23 → $3.99 (Shopify CLI hàng loạt), sửa §7 trong `00-context/shopify-listing-standard.md` | Product |
| Tạo 2 automatic discount mix & match + discount BF→CM | Shopify |
| Chọn + chuẩn bị file free design, form email | Product + Email |
| QA giá sau khi đổi (đếm lại theo bảng trên) | QA |
| Ghi quyết định vào `brain/decisions.md`, cập nhật `brain/store-state.md` mục Giá | CEO |
