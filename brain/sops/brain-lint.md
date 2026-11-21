---
updated: 2026-11-21
owner: CEO
sources:
  - "brain/README.md"
---

# SOP — Lint: kiểm sức khoẻ brain hàng tuần

> Chủ: **CEO** (giao QA nếu cần). Mỗi tuần, cùng lúc làm snapshot [[brain/metrics/README]]. Cập nhật 2026-11-21.

Kiểm, sửa được thì sửa, không sửa được thì ghi vào [[inbox]]; cuối cùng 1 dòng [[log]] ("lint tuần YYYY-MM-DD: N lỗi, M đã sửa").

1. **Mâu thuẫn**: grep `⚠️` trong `brain/`; so [[store-state]] với file listing mới nhất và [`00-context/shop-profile.md`](../../00-context/shop-profile.md); so [[decisions]] với [`CLAUDE.md`](../../CLAUDE.md)/[`AGENTS.md`](../../AGENTS.md) (vd. Mahjong). Cái nào anh đã chốt → sửa; chưa → đưa vào "Câu hỏi đang chờ" trong [[decisions]].
2. **Fact cũ**: mọi dòng trong [[store-state]] có ngày kiểm **cũ hơn 14 ngày** → kiểm lại (Shopify MCP/CLI/Chrome) hoặc đánh dấu `(cũ)`.
3. **Trang mồ côi**: trang trong `brain/` không được trang nào link tới, hoặc không có trong [[INDEX]] → thêm link.
4. **Link thiếu / hỏng**: `[[...]]` trỏ tới trang không tồn tại; link tương đối tới file đã đổi tên; file mới trong repo chưa có trong [[INDEX]] (so `git ls-files` với INDEX).
5. **`[?]` chưa giải**: đếm `[?]` trong `brain/`; cái nào đã có câu trả lời trong nguồn mới → điền; còn lại gom lên CEO hỏi anh.
6. **Inbox**: dọn [[inbox]] — chuyển từng dòng vào trang đúng, gạch dòng đã chuyển.
7. **Frontmatter**: trang nào `updated:` không khớp lần sửa cuối → sửa.
