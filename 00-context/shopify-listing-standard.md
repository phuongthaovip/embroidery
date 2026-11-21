# Tiêu chuẩn listing Shopify — EmbroThread (cập nhật 2026-11-21)

> Áp dụng cho mọi sản phẩm đưa lên embrothread.com, từ cả 2 board Trello:
> **VP-EMBROIDERY** (mã `VPE…`) và **Designer Online - Nguyen Hop** (mã `EMBN…`).
> Mục có `[?]` = chờ anh Nam chốt.

## 1. Card nào được list
- Có **ảnh mockup đã thêu** (thiết kế trên vải, có badge size/định dạng). Chỉ có clip-art phẳng hoặc ảnh chụp phần mềm digitize → **không list**.
- **Không list nếu rủi ro IP**: nhân vật, thương hiệu, logo, đội thể thao, lời bài hát, phim/truyện, người nổi tiếng (Grinch, Snoopy, Disney, Pac-Man, "Santa Baby"…). Santa, tuần lộc, elf, người tuyết, Krampus, giáng sinh Kitô giáo, gnome = được.
- Card trùng mẫu với card khác → chỉ list 1 lần.
- Card phải đúng chủ đề của cột. Mẫu lạc đề (vd. charm bóng bầu dục ở cột Christmas) → list nhưng **không gắn tag mùa sai**.

## 2. Trạng thái
| Trường hợp | Trạng thái |
|---|---|
| Sạch, không vướng gì | **ACTIVE** + publish lên Online Store |
| Ảnh có chữ "Instant Download" hoặc logo shop khác (KyraGiftsCo, HedgehogPrintGifts…) | **Chờ làm lại ảnh bằng Canva** (anh chốt 2026-11-21), chưa list. Có ảnh mới thì list như card sạch |
| Mẫu cá nhân hoá (tên/năm mẫu) | DRAFT, tính sau (anh chốt 2026-11-21) |
| Không chắc (lạc mùa, nghi IP nhẹ, badge sai) | DRAFT, ghi lý do |

## 3. Ảnh — **bắt buộc WebP**
- Tải **ảnh gốc** từ Trello (không dùng preview 600px, quá nhỏ để zoom).
- Chuyển sang **WebP**: chiều rộng **1000px** (anh chốt 2026-11-21), chất lượng **80**, nền RGB (bỏ alpha).
  - Thử thực tế 3 ảnh 2000×2000: **3.3–3.7 MB → 254–277 KB** (nhẹ hơn ~92%).
  - Toàn bộ ảnh cột Christmas VP: ~1.1 GB gốc → ước ~90–110 MB webp.
- Tên file và alt: theo **mục 3b** (bỏ kiểu cũ `<ma>-<stt>.webp`, vì mã card không phải keyword).
- Thứ tự: mockup chính trước → ảnh "download includes N designs" → ảnh lifestyle cùng mẫu.
- Ảnh vuông 1:1, nền trắng hoặc nền vải sáng, mẫu chiếm ~70–80% khung. Xoá metadata (EXIF).
- Bỏ: ảnh tham khảo/idea, ảnh phần mềm digitize, ảnh gần trùng, ảnh của sản phẩm khác.
- **Không giới hạn số ảnh**/sản phẩm (anh chốt 2026-11-21): giữ mọi ảnh dùng được.
- Upload lên Shopify Files (staged upload) rồi gắn vào sản phẩm. Không dẫn link Trello trực tiếp nữa.
- 10 sản phẩm đã list ngày 2026-11-20 (ảnh PNG/JPG) → **thay lại bằng webp**.

## 3b. Chuẩn SEO: handle (URL), tên file ảnh, alt (thêm 2026-11-21)
Làm **trước khi upload**, bằng `tools/shopify_prep.py` (đổi ảnh sang webp + đặt tên + viết alt + xuất `manifest.json`).

**Handle (URL sản phẩm)** — `embrothread.com/products/<handle>`
- Lấy từ title: chữ thường, không dấu, chỉ `a-z 0-9 -`, bỏ dấu nháy (`santa's` → `santas`).
- **≤ 60 ký tự**, keyword chủ thể ở đầu, luôn kết thúc bằng đuôi loại: `-machine-embroidery-design` / `-embroidery-design` / `-embroidery-bundle` / `-embroidery-font`.
- Bundle **bỏ số lượng** (`, 20 Designs`): số mẫu có thể đổi, URL thì không nên đổi.
- Quá 60 ký tự → bỏ stop word (a, the, and, with, of, for, in, on, to) → bỏ `machine` → cắt bớt từ mô tả cuối.
- Không mã card, không năm, không chữ "best/sale/new" trong handle. Trùng handle → thêm mã card ở cuối.
- **Đã publish thì không đổi handle.** Bắt buộc đổi → `productUpdate` với `redirectNewHandle: true` (tạo redirect 301).

**Tên file ảnh** — theo handle + vai trò ảnh (Shopify giữ nguyên tên file trong link CDN):
| Vai trò (`role`) | Tên file |
|---|---|
| `main` mockup chính | `<handle>.webp` |
| `included` ảnh "N designs" | `<handle>-included.webp` |
| `hoop-sizes` bảng size/định dạng | `<handle>-hoop-sizes.webp` |
| `detail` cận cảnh mũi thêu | `<handle>-detail.webp` |
| `on-<đồ vật>` lifestyle | `<handle>-on-sweatshirt.webp`, `-on-tote-bag.webp`… |
Cùng vai trò có nhiều ảnh → thêm `-2`, `-3`.

**Alt text** — mỗi ảnh **một alt riêng**, tả đúng ảnh đó, ≤ 125 ký tự, tiếng Anh:
- main = title · included = `All 12 designs included in the <title>` · lifestyle = `<chủ thể> embroidery design stitched on a sweatshirt` · detail = `Close-up stitch detail of the <chủ thể> embroidery design`.
- Không nhồi keyword, không lặp nguyên title cho mọi ảnh.

**Quy trình 1 đợt list**
1. Lọc card theo mục 1–2, tải ảnh gốc Trello về `raw/<ma>/`.
2. Claude xem từng ảnh, gán `role` (+ `count` cho ảnh included), bỏ ảnh xấu → tạo `input.json`.
3. Chạy `python3 tools/shopify_prep.py input.json out/<dot>` → ra webp đã đặt tên + `manifest.json`.
4. Kiểm nhanh: handle ≤ 60, không trùng, mỗi ảnh < 400 KB, alt khác nhau.
5. Staged upload ảnh (giữ tên file) → tạo sản phẩm với `handle` + `alt` từ manifest.
6. Ghi bảng kết quả vào `04-listings/` (mục 8).

**Sản phẩm đã list (153 cái, 2026-11-20/21):** **đã đổi xong** (2026-11-21) 159 ảnh từ `VPE…-1.webp` sang tên theo handle + alt theo vai trò, dùng `fileUpdate` (`filename` + `alt`), không upload lại. Handle cũ giữ nguyên (bundle vẫn còn số lượng trong handle, ví dụ `…-bundle-20-designs`).

## 4. Title (tiếng Anh, ≤ 70 ký tự)
- Lẻ: `<Mô tả mẫu> Machine Embroidery Design` hoặc `<Mô tả> Embroidery Design, <chi tiết>`.
- Bundle: `<Chủ đề> Embroidery Design Bundle, <N> Designs`.
- Font: `<Style> Christmas Embroidery Alphabet Font`.
- Chỉ tả cái nhìn thấy. Không hype (best, perfect, stunning), không "instant", không nhồi "PES file".
- Không trùng title trong store. Nếu trùng → thêm `(<mã>)`.
- Card EMBN đã có title Etsy dài (~150 ký tự) → **rút gọn** theo quy tắc trên, không copy nguyên.

## 5. Mô tả (HTML, cùng 1 khung)
1. **Intro** 1–2 câu: tả đúng mẫu, chữ thêu trích nguyên văn. Bundle: nói bộ gồm gì.
2. **What you get**: số mẫu (bundle) · size (theo badge, không có thì "Multiple hoop sizes") · định dạng (mặc định CSD, DST, EXP, HUS, JEF, PES, PCS, VP3).
3. **How you receive it**: file số, gửi qua email trong **1–3 business days**, không ship hàng.
4. **Good to know**: cần máy thêu + cách chuyển file · ảnh là preview, kết quả thay đổi theo vải/chỉ · *được bán sản phẩm đã thêu, không chia sẻ/bán lại file* (anh chốt giữ, 2026-11-21).

SEO description ≤ 155 ký tự, câu thường. SEO title = title.

## 6. Tag (chữ thường)
- Luôn có: tag mùa (`christmas`…), `digital download`, mã card.
- Tag collection (gắn đúng để sản phẩm vào collection): `animals` (con vật là chủ thể) · `bundle` · `faith` · `ith` · `coastal` · `alphabet`.
- Thêm 2–4 tag chủ đề cụ thể (gingerbread, snowman, cardinal…).
- Tổng 5–9 tag. Không lấy 13 tag Etsy nguyên bộ.

## 7. Giá & biến thể
- Bảng giá (anh chốt 2026-11-21):

  | Loại | Giá |
  |---|---|
  | Lẻ (1 mẫu) | $3.23 |
  | Bundle 2–5 mẫu | $5.99 |
  | Bundle 6–10 mẫu | $8.99 |
  | Bundle 11–15 mẫu | $11.99 |
  | Bundle 16–20 mẫu | $14.99 |
  | Alphabet / font | $9.99 |

  Bundle tối đa 20 mẫu.
- 1 variant "Default Title". SKU = mã card. Không ship (`requiresShipping=false`), không theo dõi tồn kho, có tính thuế.
- Vendor `EmbroThread` · Product type `Machine Embroidery Design`.

## 8. Sau khi list
- Ghi danh sách (mã, title, trạng thái, handle) vào `04-listings/YYYY-MM-DD-shopify-<chu-de>.md`.
- Không ghi gì lên Trello nếu anh chưa cho phép.
