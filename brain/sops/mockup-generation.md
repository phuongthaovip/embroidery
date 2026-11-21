---
updated: 2026-11-21
owner: Product
sources:
  - "CLAUDE.md"
  - "00-context/image-style-guide.md"
  - "templates/image-prompt.md"
  - "02-ideas/daily/"
---

# SOP — Gen ảnh mockup

> Chủ: **Product**. Cập nhật 2026-11-21. Nguồn: [`CLAUDE.md`](../../CLAUDE.md) §6 (Gavana), [`00-context/image-style-guide.md`](../../00-context/image-style-guide.md), file `02-ideas/daily/*-images.md`, [`00-context/shop-profile.md`](../../00-context/shop-profile.md) (Magnific).

## Phong cách (đọc trước khi gen)
- Mockup chính: [`00-context/image-style-guide.md`](../../00-context/image-style-guide.md) (chốt 2026-11-18): vải linen kem, chỉ dày, 6–10 màu, nhánh A nhân vật / B botanical. Không khung thêu, không viền bao, chữ đúng chính tả.
- ⚠️ [`templates/image-prompt.md`](../../templates/image-prompt.md) (nền trắng, ≤6 màu) cũ hơn style guide. Nhiều lô áo vẫn gen **nền trong suốt** (Krampus 11-16, Teacher 11-18). Khi lô không nói rõ → hỏi anh `[?]`.
- Mẫu chữ: 2 bản áo sáng + áo tối. Filigree: vải trắng, chỉ nâu espresso. Bundle: gen sheet rồi tách ảnh lẻ.
- Ảnh phải **digitize được giống mockup**.

## Công cụ
| Tool | Dùng khi | Lưu ý |
|---|---|---|
| **ChatGPT project "Thaonie"** (Chrome NIENVP) | Đường chính cho mockup từ 2026-10-26 | Mỗi idea 1 chat; ghi chat id vào file `-images.md`; được chạy 3 tab song song (2026-11-17); kiểm alpha góc = 0 khi cần nền trong suốt; ảnh 1254×1254 |
| **Gavana** canvas "nam embroidery" | Dự phòng | Chỉ model **GPT Image (ChatGPT plan)**, chạy qua máy H Mac (offline → "Queued"). Tạo từng node "Generate image" → prompt → 1:1 → model tab ChatGPT plan → gen, ~1–2 phút/ảnh. **Không dùng "List / Create batch"** (crash + sai prompt, 2026-10-18). Không bấm vùng gen/Stop node đang chạy (ghi đè ảnh) |
| **Magnific** (project Personal) | Ảnh banner/hero store | Hero coastal 2026-11-20 làm ở đây; bản mở rộng sang trái từng lỗi (vẽ thêm máy) → kiểm kỹ ảnh expand |
| **Canva** | Sửa ảnh có badge/logo lạ | [[image-webp-redo]] |

## Sau khi gen
- Kiểm chính tả chữ, IP, số màu, dáng gọn.
- Ghi trạng thái từng ảnh trong `02-ideas/daily/<lô>-images.md`.
