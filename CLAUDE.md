# Embroidery Idea Machine — Context cho Claude

> Claude đọc file này mỗi phiên làm việc. Giữ ngắn gọn, cập nhật khi có thay đổi.
> Chỗ có `[?]` = chưa xác nhận, Claude phải hỏi lại anh Nam thay vì tự đoán.

> **Second brain:** đọc `brain/README.md` và `brain/store-state.md` trước; ghi quyết định mới vào `brain/decisions.md`. Mọi thay đổi brain ghi 1 dòng vào `brain/log.md`. File này là lớp *schema*; `brain/` là wiki; các thư mục 00–05 là nguồn thô. (Thêm 2026-11-21)

## 1. Người làm việc cùng
- **Anh Nam** — chủ shop Etsy bán machine embroidery design.
- Giao tiếp bằng **tiếng Việt**. Thuật ngữ Etsy/SEO/embroidery giữ nguyên tiếng Anh.
- Keyword, title, tags, mô tả listing luôn viết bằng **tiếng Anh** (thị trường Etsy).

## 2. Mục tiêu dự án
Xây một quy trình lặp lại được ("idea machine") để:
1. Tìm idea design thêu máy có nhu cầu thật trên Etsy.
2. Lọc và chấm điểm idea trước khi tốn công làm design.
3. Biến idea thành brief rõ ràng cho khâu làm design / digitize.
4. Viết listing (title, tags, description) chuẩn SEO.
5. Theo dõi kết quả bán hàng để quay lại cải thiện bước 1–2.

## 3. Shop & sản phẩm — chi tiết ở `00-context/shop-profile.md`
- Shop: **PaolaCraftGifts** (có "s"). Bán **file thêu kỹ thuật số**. 2.4k sales, 565 listing, mở khoảng 11/2025.
- Mô hình: **AI gen ảnh → list trước → khi có đơn mới digitize**. ~50 mẫu mới/tuần.
  ⇒ Mọi idea/prompt phải cho ra ảnh **digitize được giống mockup** (ít màu, nét rõ, không gradient kiểu ảnh chụp).
- Khâu nghẽn: **tìm idea** (hiện dùng Pinterest + xem shop đối thủ).
- Đối thủ: EmbCharlotte, KVFlorida, GagaEmbroidery, HuongboutiqueCo, TaraTranCo, Nancyembcraft, TunezzArt.
- Shop thứ 2 (cùng nhà, KHÔNG phải đối thủ): **KyraGiftsCo** — shop của chị, **cũng bán file thêu máy**, dùng **chung quy trình idea machine**. Idea machine giờ phục vụ 2 shop. Số liệu/winner riêng của shop chị: `[?]` chưa quét. Chi tiết ở `00-context/shop-profile.md`.
- Kết quả phân tích mới nhất: `01-research/2026-10-17-shop-competitor-analysis.md`. Ý chính:
  80% listing không bán, top 10 = 75% doanh số; bundle = 56% doanh số; winner là preppy/coastal animal bundle + ITH + funny animal;
  Christian/faith chiếm 19–30% doanh số đối thủ nhưng shop anh chưa làm; Mahjong yếu hơn anh nghĩ.

## 4. Quy trình (bản nháp — sẽ tinh chỉnh cùng anh)
```
01 Research  →  02 Ideas  →  03 Brief/Prompt  →  04 Listing  →  05 Results
 (đối thủ,        (backlog,     (prompt ảnh AI      (SEO title,     (sales, views,
  trend,           chấm điểm,    + note cho          13 tags,        favorites → học
  winner cũ)       lọc mạnh)     designer)           mô tả)          ngược lại)
```
Quản lý pipeline trên **Trello** (anh đã chọn). Mỗi bước có thư mục riêng cùng số thứ tự. Template ở `templates/`.

### Nhịp làm việc THEO NGÀY (anh Nam chốt 2026-10-17)
- Mục tiêu: **~70 mẫu được duyệt / tuần ≈ 10 mẫu/ngày**. Claude đề xuất **~14 idea/ngày** để anh lọc còn 10.
- **2 shop, mỗi shop MỘT bộ idea riêng** (anh Nam chốt 2026-10-18): mỗi ngày làm ~14 idea cho PaolaCraftGifts **và** ~14 idea cho KyraGiftsCo, dựa trên winner riêng của từng shop.
- Mỗi ngày tạo **1 file / shop**: `02-ideas/daily/YYYY-MM-DD-paola.md` và `02-ideas/daily/YYYY-MM-DD-kyra.md`. Mỗi file gồm: bảng tóm tắt (idea, loại, bằng chứng, điểm) + chi tiết (keyword, prompt ảnh).
- Đưa idea lên Trello (cột "Idea mới"), anh duyệt → gen ảnh → list → có đơn → digitize.
- Idea được duyệt → Claude viết listing SEO (title, 13 tags, mô tả) vào `04-listings/`.
- Mỗi tuần: quét lại shop đối thủ (đi chậm) + shop anh để cập nhật winner, ghi vào `01-research/`.

### Ràng buộc idea (anh Nam chốt)
- **Bundle ≤ 20 mẫu.** Không làm mega bundle 100+ (designer không kịp), kể cả ITH.
- **Mahjong: đã bật lại** (anh Nam bật lại 2026-10-24, nguồn `02-ideas/daily/2026-10-24-mahjong.md`; trước đó tạm bỏ). Data 2026-10-17 cho thấy Mahjong yếu, nên đo kết quả các lô Mahjong.
- **Christian/faith: được làm.**
- Mỗi ngày nên trộn: nhân bản công thức winner của shop (preppy/coastal animal bundle, ITH, funny animal) + khoảng trống từ đối thủ (Christian, ITH tag, mini icon ≤20) + đúng mùa (đi trước mùa 4–8 tuần).
- Prompt ảnh theo `templates/image-prompt.md` (cho ChatGPT / Gavana).

## 4b. Cách quét dữ liệu Etsy
- Etsy chặn WebFetch (403) → dùng Chrome. Chrome của anh có extension hiện số sold/views/favorites/ngày tạo trên từng listing.
- Etsy trả lỗi **429 nếu quét nhanh**: tối đa ~4 trang mỗi lượt, nghỉ giữa các lượt.
- Doanh thu hiển thị bằng VND (shop anh) hoặc USD (đối thủ), nên regex phải bắt được mọi mã tiền tệ.

## 5. Quy tắc khi làm việc
- **Không đoán số liệu.** Số liệu thị trường phải lấy từ tool (YTrends…) hoặc anh cung cấp, và ghi rõ nguồn + ngày lấy.
- **Bản quyền:** Không đề xuất idea dùng nhân vật, logo, thương hiệu, tên đội thể thao, lời bài hát… có bản quyền/trademark. Gắn cờ ⚠️ nếu idea có rủi ro IP.
- **Ràng buộc kỹ thuật thêu** phải được xét khi đề xuất idea (kích thước khung, chữ quá nhỏ, chi tiết quá mảnh, mật độ mũi…). Xem `00-context/embroidery-specs.md`.
- Idea mới luôn ghi vào `02-ideas/backlog.md` theo format trong `templates/idea-card.md`.
- Đặt tên file có ngày: `YYYY-MM-DD-<chu-de>.md`.

## 6. Công cụ có sẵn trong phiên Claude
- **YTrends** — dữ liệu về embroidery **rất mỏng** (chỉ 4–7 listing mỗi keyword), chỉ dùng tham khảo. Nguồn chính là quét shop đối thủ bằng Chrome.
- **AI gen ảnh: Gavana**: canvas "nam embroidery" https://app.gavana.ai/canvas/wTsyZjqBV73EHhs3laPF6?owner=ml9jM2PfjuYINbenNKieFTuJUAC3
  - Model dùng được DUY NHẤT: **GPT Image (ChatGPT plan)**. Model này chạy qua máy **H Mac** (Codex + gói ChatGPT). H Mac offline thì ảnh nằm ở "Queued" chờ. Các model "Gavana credit" đều Unavailable.
  - Cách làm chạy được: tạo từng node "Generate image" → gõ prompt → chọn 1:1 → chọn model (tab ChatGPT plan) → bấm gen. Mỗi ảnh ~1–2 phút, chạy lần lượt.
  - **KHÔNG dùng "List / Create batch"**: trang hay crash khi nhập prompt, và batch ra ảnh sai prompt (ngày 2026-10-18).
  - Khi chờ gen, khung nhìn có thể tự zoom/đổi vị trí. Đừng bấm vào vùng nút gen/Stop của node đang chạy, vì gen lại sẽ ghi đè ảnh cũ.
- **Trello** — board đang dùng: **VP-EMBROIDERY** https://trello.com/b/8ImjXI5V/vp-embroidery (kết nối được, 2026-11-20). Cột theo chủ đề (CHRISTMAS, Halloween, Animal Lover, Mahjong…) + IDEA RAW, Cần Design, Cần Listing. Mỗi card = 1 mẫu, tên là mã `VPE<yymmdd><stt>`, ảnh mockup đính kèm. Board cũ duy-nam: tài khoản arronvu chưa có quyền.
  Board thứ 2: **Designer Online - Nguyen Hop** https://trello.com/b/ztGSbKOs/designer-online-nguyen-hop (riêng tư, đọc qua Trello MCP; mã `EMBN…`, card có sẵn title + tag Etsy).
- **Google Drive** — lưu trữ / chia sẻ file. [?]
- Chrome — xem trực tiếp Etsy, shop đối thủ.

## 7. Bản đồ thư mục
| Thư mục | Nội dung |
|---|---|
| `00-context/` | Thông tin shop, niche, khách hàng, spec thêu, brand style |
| `01-research/` | Báo cáo trend, keyword, phân tích đối thủ |
| `02-ideas/` | Backlog idea + điểm số |
| `03-briefs/` | Brief chi tiết cho từng design được chọn |
| `04-listings/` | Nội dung listing SEO |
| `05-results/` | Số liệu bán hàng, bài học rút ra |
| `templates/` | Mẫu dùng chung |
| `tools/` | Script: `shopify_prep.py` chuẩn hoá ảnh/handle/tên file/alt trước khi list Shopify |
