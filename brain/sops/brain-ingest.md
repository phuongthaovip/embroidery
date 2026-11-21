---
updated: 2026-11-21
owner: bot tạo nguồn
sources:
  - "brain/README.md"
---

# SOP — Ingest: đưa nguồn mới vào brain

> Chủ: bot tạo ra nguồn đó (Product cho idea/listing, Shopify cho store, CEO cho số liệu…). Cập nhật 2026-11-21.

Khi nào: có file mới trong lớp nguồn ([`01-research/`](../../01-research/), [`02-ideas/`](../../02-ideas/), [`04-listings/`](../../04-listings/), [`00-context/`](../../00-context/), ảnh/scan trong [`raw/`](../../raw/)), anh Nam nói gì mới, hoặc vừa kiểm/đổi store.

1. **Không sửa nguồn để khớp brain.** Nguồn là chỉ-đọc (lớp 1, xem [[INDEX]]).
2. Đọc nguồn, liệt kê **mọi trang brain nó chạm** — thường 3–8 trang:
   - fact store → [[store-state]] (ghi ngày kiểm + cách kiểm)
   - anh chốt / chọn / nói → 1 dòng đầu [[decisions]]; quyết định cũ bị thay → gạch + `SUPERSEDED <ngày>`
   - bài học, số liệu thắng/thua → [[lessons]]
   - số tuần → [[brain/metrics/README]]
   - quy trình đổi → SOP tương ứng trong `brain/sops/`
   - ai làm gì đổi → [[team]]
3. Sửa từng trang: tóm 1–3 dòng + **link tới nguồn**, không chép nguyên văn. Cập nhật `updated:` và `sources:` trong frontmatter.
4. File nguồn mới → thêm 1 dòng vào [[INDEX]] (mục chủ đề + nhãn PARA).
5. Thấy mâu thuẫn với trang cũ → ghi `⚠️ mâu thuẫn:` kèm 2 nguồn, không tự chọn bên. Cần anh → thêm vào "Câu hỏi đang chờ" trong [[decisions]].
6. **Log**: 1 dòng cuối [[log]]: ngày | ai | đổi gì | file.
7. Chưa kịp xếp → để ở [[inbox]] (có ngày), không bỏ.
