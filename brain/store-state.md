---
updated: 2026-11-21
owner: Shopify (tạm: Claude / CEO)
sources:
  - "00-context/shop-profile.md"
  - "04-listings/2026-11-20-shopify-christmas-batch1.md"
  - "04-listings/2026-11-21-shopify-christmas-batch2.md"
  - "00-context/shopify-listing-standard.md"
---

# EmbroThread.com — trạng thái hiện tại

> Một trang dashboard. Mỗi fact có ngày kiểm tra + cách kiểm. **Đổi store xong → sửa dòng ở đây + ghi log cuối file.**
> Lịch sử setup chi tiết (11-19 → 11-21): [`00-context/shop-profile.md`](../00-context/shop-profile.md) mục "Store Shopify". Từ 2026-11-21 phần đó **không ghi thêm**, ghi ở đây.

## Tổng quan
| Mục | Trạng thái | Kiểm tra |
|---|---|---|
| Store | embrothread.com · Shopify Basic · USD · múi giờ +07 · country US · tên Admin "EmbroThread" | 2026-11-19 MCP / 2026-11-20 |
| Mở công khai | Có (Private mode tắt) | 2026-11-20 Chrome |
| Mở bán từ | 2026-11-19 | metrics |
| **Thanh toán** | ❌ **Chưa nhận được tiền**: checkout báo "This store can't accept payments right now". Shopify Payments chưa hoàn tất (anh tự làm giấy tờ + ngân hàng ở Settings → Payments) | 2026-11-21 Chrome |
| Theme live | **"Dawn – EmbroThread"** (Dawn 16.2.0). Horizon (màu kem #FBF7EF / navy #14284B / coral #F4A9A0, font Fraunces + Nunito Sans, có hero coastal + logo) giờ UNPUBLISHED | 2026-11-21 Chrome |
| Logo / favicon | [`logo.png`](../logo.png), [`logo-inverse.png`](../logo-inverse.png), [`icon-embrothread.png`](../icon-embrothread.png). Đã lưu vào Dawn nhưng **chưa publish** (anh nói chưa). Dawn live đang không có logo ảnh + favicon | 2026-11-21 Chrome |
| Hero | Live trên Horizon: vòng thêu ếch + cua/cá/vỏ sò (Magnific, có bản mobile). Hero mới anh chọn "máy thêu thêu dở mẫu ếch" — đã gen thử, chưa gắn. Trên Dawn `[?]` | 2026-11-20 |
| SEO trang chủ | Title "EmbroThread \| Machine Embroidery Designs & Bundles" + meta description | 2026-11-20 |
| Trang | About (/pages/about), FAQ (/pages/faq), Contact | 2026-11-19 |
| Chính sách | Đủ 5 mục: Refund, Shipping, Terms 14 mục, Contact (tên + web + email, chưa địa chỉ/điện thoại), Privacy (Shopify tạo). Nội dung: [`00-context/2026-11-19-shopify-policies.md`](../00-context/2026-11-19-shopify-policies.md) | 2026-11-20 |
| Apps | Digital Products (đã cài, chưa dùng vì file chưa có sẵn) | 2026-11-20 |
| Tool | Shopify MCP (không có quyền sửa Policies, chặn bulk mutation) · Shopify CLI 5.0.2 `~/.local/bin/shopify` đã đăng nhập, dùng `shopify store execute` cho việc hàng loạt | 2026-11-21 |

## Sản phẩm
| Mục | Số | Kiểm tra |
|---|---|---|
| Tổng | **153** = 10 (đợt 1, 11-20) + 143 (đợt 2, 11-21) — toàn Christmas | 2026-11-21, [`shop-profile.md`](../00-context/shop-profile.md) + 2 file batch |
| ACTIVE (publish Online Store) | **137** (10 đợt 1 + 127 đợt 2) | như trên |
| DRAFT | **16** (lý do trong batch2: cá nhân hoá, lạc mùa, nghi IP, card tên file…) | [`04-listings/2026-11-21-shopify-christmas-batch2.md`](../04-listings/2026-11-21-shopify-christmas-batch2.md) |
| Chờ làm lại ảnh bằng Canva | 123 card cột Christmas VP-EMBROIDERY (badge Instant Download / logo shop khác / clip-art phẳng) | 2026-11-21 |
| Bỏ qua | 99 card (không mockup, IP, trùng, không ảnh) | 2026-11-21 |
| Ảnh | 159 ảnh WebP 1000px, đã đổi tên theo handle + alt theo vai trò (`fileUpdate`) | 2026-11-21 |
| Chuẩn | [`00-context/shopify-listing-standard.md`](../00-context/shopify-listing-standard.md) | 2026-11-21 |

⚠️ **Mâu thuẫn số lượng:** snapshot metrics ngày 2026-11-21 ghi 143 sản phẩm (127 ACTIVE / 16 DRAFT) — đó là riêng đợt 2. [`shop-profile.md`](../00-context/shop-profile.md) ghi tổng 153 (137 / 16). Cùng ngày, dòng "Kiểm tra 2026-11-21 (Chrome)" trong [`shop-profile.md`](../00-context/shop-profile.md) còn ghi "10 sản phẩm Christmas ACTIVE" (ghi trước khi đợt 2 lên). Cần 1 lần đếm lại trên Admin để chốt.

## Giá
| Loại | Chuẩn (anh chốt 2026-11-21) | Live |
|---|---|---|
| Lẻ | $3.23 | ⚠️ **$3.99** theo Chrome 2026-11-21; batch1/batch2 ghi $3.23 |
| Bundle 2–5 / 6–10 / 11–15 / 16–20 | $5.99 / $8.99 / $11.99 / $14.99 | theo batch2 (vd. bundle 20 = $14.99) |
| Alphabet / font | $9.99 | `[?]` |
Nguồn: [`shopify-listing-standard.md`](../00-context/shopify-listing-standard.md) §7. Etsy Paola để so: lẻ $3.23, bundle $4.85–6.06.

## Giao file
- Thủ công qua **email trong 1–3 ngày làm việc** (chỉ digitize khi có đơn). Checkout bắt khách nhập email. Sản phẩm `requiresShipping=false`.
- Ai gửi, gửi từ hộp nào (business@embrothread.com?) `[?]`. Quy trình: [[order-digitize-delivery]].

## Menu & collection
- Collection tự gom theo tag: Bundles `bundle` · Animals `animals` · Coastal & Preppy `coastal` · In the Hoop `ith` · Christian & Faith `faith` · Christmas `christmas` (+ tag `alphabet` theo chuẩn listing). Chưa có ảnh collection.
- Menu chính: 2026-11-21 đã **bỏ link tới collection trống** (Bundles, In the Hoop, Christian & Faith = 0 sản phẩm lúc kiểm). Thêm lại khi có sản phẩm. ⚠️ Đợt 2 đã có bundle + ITH + faith → cần kiểm lại và thêm lại vào menu.
- Footer: Search · FAQ · About Us · Contact · Your Privacy Choices.

## Việc đang mở
| Việc | Chủ | Trạng thái |
|---|---|---|
| Setup Shopify Payments (giấy tờ, ngân hàng) | **anh Nam** (bot không làm được) | Chặn mọi doanh thu. Anh hẹn "khi bắt đầu list" — đã tới |
| Chốt giá lẻ $3.23 vs $3.99 live, rồi sửa cho khớp | anh Nam → Shopify bot | mở |
| Publish logo + favicon trên Dawn | anh Nam duyệt → Shopify bot | chờ anh |
| Chọn hướng giao diện (Catalog / Theo mùa / Boutique) rồi làm lại theme | anh Nam → Shopify bot | "lưu lại tính sau" (2026-11-20) |
| Gắn hero "máy thêu thêu dở ếch" | Shopify bot | ảnh chưa đạt (bản mở rộng lỗi) |
| Thêm lại Bundles / ITH / Faith vào menu khi có sản phẩm | Shopify bot | cần kiểm |
| Ảnh cho từng collection | Shopify bot | mở |
| Làm lại ảnh 123 card bằng Canva rồi list | Product (+ QA kiểm) | mở |
| List 9 card Christmas board Designer Online - Nguyen Hop (EMBN) | Product | chưa list |
| Đếm lại số sản phẩm thật trên Admin | QA | mở (mâu thuẫn 143 vs 153) |
| Bán Black Friday → Cyber Monday (27–30/11) | CEO / Ads | `[?]` chưa có kế hoạch — và chưa nhận được tiền |
| Lô Valentine V1–V14 (list trước ~15/12) | Product | chờ anh duyệt ([`01-research/2026-11-21-valentine-competitor-scan.md`](../01-research/2026-11-21-valentine-competitor-scan.md)) |
| Contact: địa chỉ/điện thoại; Terms §13 governing law | anh Nam | `[?]` |

## Log thay đổi store (mới nhất trên)
| Ngày | Ai | Việc |
|---|---|---|
| 2026-11-21 | Claude (brain) | Tạo trang này từ [`shop-profile.md`](../00-context/shop-profile.md) + `04-listings/2026-11-2*-shopify-*`. Không đổi gì trên store |
| 2026-11-21 | Claude | Đợt 2: 143 sản phẩm (127 ACTIVE + 16 DRAFT); đổi tên 159 ảnh; bỏ collection trống khỏi menu; lưu logo vào Dawn (chưa publish) |
| 2026-11-20 | Claude | Đợt 1: 10 sản phẩm Christmas; Terms 14 mục; logo + hero lên Horizon; cài Dawn 16.2.0 |
| 2026-11-19 | Claude | Setup store: trang, collection, menu, theme Horizon, chính sách |
