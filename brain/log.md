---
updated: 2026-11-21
owner: mọi bot (append-only)
sources: []
---

# Log — mọi lần ingest / thay đổi brain

> **Append-only**: chỉ thêm dòng mới ở **cuối** bảng, không sửa/xoá dòng cũ (ghi sai → thêm dòng đính chính).
> Mỗi lần [[brain-ingest]], sửa trang brain, hay đổi store đã ghi vào [[store-state]] → 1 dòng ở đây.
> Định dạng: `| YYYY-MM-DD | ai (bot / phiên) | đổi gì | file |`

| Ngày | Ai | Đổi gì | File |
|---|---|---|---|
| 2026-11-21 | Claude (Orca worker, task_39e80db6cc31) | Tạo brain: ingest toàn bộ [`AGENTS.md`](../AGENTS.md), [`CLAUDE.md`](../CLAUDE.md), [`00-context/`](../00-context/), [`01-research/`](../01-research/), [`02-ideas/`](../02-ideas/), [`04-listings/`](../04-listings/), [`tools/`](../tools/), git log | brain/README, INDEX, decisions (44), store-state, team, sops/ (7), metrics/, lessons, inbox |
| 2026-11-21 | Claude (Orca worker, task_39e80db6cc31) | Thêm mô hình 3 lớp + PARA vào INDEX; thêm SOP ingest/query/lint; thêm log; frontmatter + `[[wikilink]]` cho mọi trang | brain/INDEX, sops/brain-ingest, sops/brain-query, sops/brain-lint, log, mọi trang brain |
| 2026-11-21 | Claude (Orca worker, task_39e80db6cc31) | Thêm dòng trỏ tới brain ở đầu [`CLAUDE.md`](../CLAUDE.md), [`AGENTS.md`](../AGENTS.md); mục Shopify của [`shop-profile.md`](../00-context/shop-profile.md) trỏ sang store-state | CLAUDE.md, AGENTS.md, 00-context/shop-profile.md |
| 2026-11-21 | Claude (Orca worker, task_39e80db6cc31) | Sửa dòng "Tạm bỏ Mahjong" trong CLAUDE.md/AGENTS.md thành "đã bật lại 2026-10-24" (nguồn có ngày: `02-ideas/daily/2026-10-24-mahjong.md`) | CLAUDE.md, AGENTS.md, brain/decisions |
| 2026-11-21 | Claude (phiên embroidery) | Sửa danh sách bot trong team cho khớp `orca bot list`: có CEO, Product, QA, Shopify, Email; Ads/SEO/Social/CS chưa có bot; thêm cách gọi bot qua Orca | brain/team.md |
| 2026-11-21 | EmbroThread CEO | Lên kế hoạch tuần 23–29/11 (nháp, chờ anh duyệt, chưa giao việc); cập nhật chủ việc BF→CM trong store-state | 05-results/2026-11-23-weekly-plan.md, brain/store-state.md |
| 2026-11-21 | EmbroThread Email | Soạn nháp form thu email (Shopify Forms, thẻ bf-2026), 3 email BF→CM, mẫu mail giao file, phương án B Cyber Week 1–3/12. Chưa đổi gì trên store | 05-results/2026-11-25-email-drafts.md |
| 2026-11-21 | EmbroThread Shopify | Chuẩn bị tuần 23/11 (chưa ghi store): kiểm collection/menu/theme, đề xuất menu + ảnh collection, checklist sale BF→CM, bước logo. Sửa store-state: theme live là Horizon, logo đã live, múi giờ Phoenix, 154 SP (137/17), giá lẫn $3.23/$3.99 | 05-results/2026-11-24-shopify-prep.md, brain/store-state.md |
| 2026-11-21 | EmbroThread QA | Đếm lại trên Admin (chỉ đọc): 154 = 153 thật (137 ACTIVE / 16 DRAFT) + 1 [SAMPLE] DRAFT; lỗi nặng: 22 ACTIVE ảnh nền đen, 10 giá $3.99, sample còn trong Admin; thêm dòng chốt số dưới ⚠️ mâu thuẫn | 05-results/2026-11-23-qa-count.md, brain/store-state.md |
| 2026-11-21 | EmbroThread CEO | Đề xuất cấu trúc giá mới (chờ anh duyệt, chưa đổi store) | 05-results/2026-11-21-pricing-structure.md |
| 2026-11-21 | EmbroThread CEO | Ghi quyết định giá mới; giao Product, Shopify, Email, QA/QC áp dụng | brain/decisions.md |
