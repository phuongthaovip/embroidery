---
updated: 2026-11-21
owner: Product
sources:
  - "00-context/shopify-listing-standard.md"
  - "tools/shopify_prep.py"
  - "tools/badges.py"
---

# SOP — Làm lại ảnh (WebP / đổi tên / Canva)

> Chủ: **Product**. Cập nhật 2026-11-21. Chuẩn: [`00-context/shopify-listing-standard.md`](../../00-context/shopify-listing-standard.md) §3, §3b.

## A. Đổi ảnh cũ sang WebP (sản phẩm đã list)
1. Lấy ảnh gốc (không dùng preview Trello 600px).
2. WebP rộng 1000px, q80, RGB, xoá EXIF ([`tools/shopify_prep.py`](../../tools/shopify_prep.py)).
3. Thay ảnh trên sản phẩm; tên file `<handle>[-role].webp`, alt riêng từng ảnh.
4. Chỉ đổi tên/alt (không upload lại) → `fileUpdate` (`filename` + `alt`). Đã làm cho 159 ảnh ngày 2026-11-21.
5. **Không đổi handle đã publish**; bắt buộc đổi → `productUpdate` + `redirectNewHandle: true`.

## B. Ảnh có badge "Instant Download" / logo shop khác / chỉ clip-art (anh chốt 2026-11-21)
1. Làm lại ảnh bằng **Canva** (xoá badge/logo, thêm badge EmbroThread bằng [`tools/badges.py`](../../tools/badges.py) nếu cần).
2. Có ảnh mới → list như card sạch ([[shopify-listing]]).
3. Hàng đợi hiện tại: 123 card cột Christmas VP (xem [[store-state]]).
4. Đẩy ảnh mới lên Trello chỉ khi anh cho phép ([`tools/trello_push.py`](../../tools/trello_push.py), `trello_replace.py`).
