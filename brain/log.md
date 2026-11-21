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
