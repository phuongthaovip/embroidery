---
updated: 2026-11-21
owner: mọi bot
sources:
  - "brain/README.md"
---

# SOP — Query: trả lời câu hỏi từ brain

> Mọi bot / phiên. Cập nhật 2026-11-21.

1. Bắt đầu từ [[INDEX]] và trang brain liên quan ([[store-state]], [[decisions]], [[team]], [[lessons]], SOP). Không có embeddings/RAG — index + grep là đủ ở quy mô này.
2. Trả lời **kèm link nguồn** (trang brain + file nguồn lớp 1). Fact có ngày kiểm cũ hơn 14 ngày → nói rõ "đã cũ, kiểm ngày …" hoặc kiểm lại thực tế trước.
3. Brain không có / mâu thuẫn → đọc file nguồn; vẫn không rõ → trả lời `[?]` và hỏi anh Nam, **không đoán**.
4. **Câu trả lời tốt, sẽ còn được hỏi lại** (so sánh, tổng hợp nhiều nguồn, kết luận) → lưu thành trang mới `brain/<chu-de>.md` (có frontmatter, link nguồn), thêm vào [[INDEX]], ghi [[log]].
5. Câu trả lời làm lộ thông tin sai/cũ trong brain → sửa trang đó theo [[brain-ingest]].
