---
updated: 2026-11-21
owner: Product
sources:
  - "CLAUDE.md"
  - "01-research/2026-10-17-shop-competitor-analysis.md"
---

# SOP — Quét dữ liệu Etsy

> Chủ: **Product** (SEO dùng chung). Cập nhật 2026-11-21. Nguồn: [`CLAUDE.md`](../../CLAUDE.md) §4b, [`01-research/2026-10-17-shop-competitor-analysis.md`](../../01-research/2026-10-17-shop-competitor-analysis.md), các file idea 11-17/18.

1. **Dùng Chrome** của anh (Etsy chặn WebFetch 403). Extension **HeyEtsy** hiện sold / views / favorites / ngày tạo trên từng listing — đọc số trên **mọi trang** đã quét.
2. **Chậm**: tối đa ~4 trang mỗi lượt, nghỉ giữa các lượt. Quét nhanh → 429 hoặc trang kiểm tra bot (đã gặp 2026-10-17, 2026-11-18) → dừng, không cố.
3. Doanh thu hiện VND (shop anh) hoặc USD (đối thủ) → regex bắt mọi mã tiền tệ.
4. Trang 2 của search đôi khi trả lại trang 1 (ITH, 2026-10-23) → kiểm trùng.
5. Dữ liệu thô quét shop từng lưu ở localStorage etsy.com, key `emb_<shop>`.
6. Ghi kết quả: `01-research/YYYY-MM-DD-<chu-de>.md` hoặc phần "Nguồn" của lô idea. Luôn ghi nguồn + ngày; "sold" là **ước tính của extension**, không phải số Etsy.
7. YTrends/EverBee: dữ liệu embroidery rất mỏng (YTrends 2–8 listing/keyword; EverBee về gói Hobby từ 2026-11-11) → chỉ tham khảo.
8. Amazon Merch: dùng Hot New Releases, không quét Newest từng trang ([`01-research/2026-10-22-amazon-merch-christmas-scan.md`](../../01-research/2026-10-22-amazon-merch-christmas-scan.md)).
