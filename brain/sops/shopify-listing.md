---
updated: 2026-11-21
owner: Product
sources:
  - "00-context/shopify-listing-standard.md"
---

# SOP — List sản phẩm lên EmbroThread (Shopify)

> Chủ: **Product** (QA kiểm). Cập nhật 2026-11-21.
> **Chuẩn đầy đủ: [`00-context/shopify-listing-standard.md`](../../00-context/shopify-listing-standard.md)** — file đó là nguồn duy nhất, sửa chuẩn thì sửa ở đó.

Tóm tắt 1 đợt list:
1. Đọc [[store-state]] (giá, số đang có, việc mở) — tránh list trùng.
2. Lọc card (chuẩn §1–2): có mockup đã thêu, không IP, không trùng. Ảnh có badge "Instant Download"/logo shop khác → chờ Canva ([[image-webp-redo]]). Cá nhân hoá → DRAFT.
3. Tải ảnh gốc Trello về `raw/<mã>/` ([`tools/trello_pull.py`](../../tools/trello_pull.py) cho board EmbroT).
4. Gán `role` cho từng ảnh → `input.json` → `python3 tools/shopify_prep.py input.json out/<dot>` (WebP 1000px, handle ≤60, tên file + alt). Badge: [`tools/badges.py`](../../tools/badges.py).
5. Kiểm: handle không trùng, ảnh < 400 KB, alt khác nhau.
6. Tạo sản phẩm (MCP cho lẻ, `shopify store execute` cho hàng loạt). Giá theo bảng §7. Tag collection đúng (`bundle`, `ith`, `faith`, `animals`, `coastal`, `alphabet`). `requiresShipping=false`.
7. Ghi kết quả `04-listings/YYYY-MM-DD-shopify-<chu-de>.md`; cập nhật số + log trong [[store-state]].
8. Collection mới có sản phẩm → báo Shopify bot thêm lại vào menu.
