---
updated: 2026-11-21
owner: Product
sources:
  - "CLAUDE.md"
  - "templates/"
  - "02-ideas/"
---

# SOP — Idea → listing (pipeline sản phẩm)

> Chủ: **Product**. Cập nhật 2026-11-21. Nguồn: [`CLAUDE.md`](../../CLAUDE.md) §4, [`templates/`](../../templates/), các file [`02-ideas/daily/`](../../02-ideas/daily/).

```
01 Research → 02 Ideas → 03 Ảnh/brief → Trello → 04 Listing → bán → 05 Results
```

1. **Research** ([`01-research/`](../../01-research/)): quét đối thủ + từ khoá bằng Chrome + HeyEtsy theo [[etsy-scanning]]. Mỗi lô idea phải có số thật (decision 2026-11-17). Đi trước mùa 4–8 tuần ([`01-research/2026-11-12-holiday-calendar.md`](../../01-research/2026-11-12-holiday-calendar.md)).
2. **Idea** (`02-ideas/daily/YYYY-MM-DD-<chu-de>.md` + [`02-ideas/backlog.md`](../../02-ideas/backlog.md)):
   - Format [`templates/idea-card.md`](../../templates/idea-card.md), chấm /20. Ghi rõ **shop** (Paola / Kyra / EmbroThread) — đừng để `[?]`.
   - Luật: bundle ≤ 20 · Christian được làm · Mahjong đã bật lại (2026-10-24) · trộn winner + khoảng trống + đúng mùa. Xem [[decisions]].
   - Lọc IP theo [[trademark-ip-check]]; lọc kỹ thuật theo [`00-context/embroidery-specs.md`](../../00-context/embroidery-specs.md).
3. **Anh Nam duyệt** (thường duyệt cả lô).
4. **Ảnh mockup** theo [[mockup-generation]] + [`00-context/image-style-guide.md`](../../00-context/image-style-guide.md). Ghi file `-images.md` (chat id, ghi chú từng ảnh).
5. **Trello**: card lên board VP-EMBROIDERY (mã `VPE<yymmdd><stt>`, cột IDEA RAW → Cần Design → Cần Listing / cột chủ đề). Board EMBN và EmbroT xem [[INDEX]] §4.
6. **Listing**:
   - Etsy: title + 13 tag + mô tả, ghi `04-listings/YYYY-MM-DD-<...>.md`; có khi đăng vào comment card Trello (chỉ khi anh cho phép).
   - Shopify: theo [[shopify-listing]].
7. **Có đơn → digitize → giao file**: [[order-digitize-delivery]].
8. **Kết quả**: số bán/views/fav → [`05-results/`](../../05-results/) (đang trống `[?]`) và [[brain/metrics/README]]; bài học → [[lessons]].
