# Second brain — Embroidery / EmbroThread

> Tạo 2026-11-21. Đây là **chỗ đọc đầu tiên** cho mọi người và mọi bot làm việc trong repo này
> (anh Nam, bot EmbroThread CEO / Product / QA / Ads / …, các phiên Claude và Codex).

## Brain là gì
Repo này điều hành 3 kênh bán file thêu máy từ một thư mục: 2 shop Etsy (**PaolaCraftGifts**, **KyraGiftsCo**) và store Shopify **EmbroThread.com**.
Kiến thức nằm rải rác ở `AGENTS.md`, `CLAUDE.md`, `00-context/` (nhất là `shop-profile.md`), research, idea, listing.
`brain/` gom lại thành **trạng thái hiện tại + quyết định + ai làm gì + cách làm**, và **trỏ về file nguồn** thay vì chép lại.

## Thứ tự đọc
1. `brain/README.md` (file này) — luật ghi.
2. `brain/store-state.md` — EmbroThread.com đang ở trạng thái nào, việc đang mở, ai giữ.
3. `brain/team.md` — bot/phiên nào làm gì, không được đụng gì, báo cáo về đâu.
4. `brain/decisions.md` — anh Nam đã chốt gì (mới nhất ở trên). **Quyết định ở đây thắng ghi chú cũ trong file khác.**
5. `brain/sops/` — quy trình lặp lại (đọc SOP đúng việc mình sắp làm).
6. `brain/INDEX.md` — bản đồ mọi file trong repo, khi cần tìm nguồn.
7. Khi cần: `brain/lessons.md` (bài học), `brain/metrics/` (số liệu tuần), `brain/inbox.md` (ghi chú thô chưa xếp).

## Luật ghi (ai cũng phải theo)
1. **Ghi ngày mọi mục**: `YYYY-MM-DD`. Fact về store/shop ghi kèm "kiểm tra ngày nào, bằng gì" (Shopify MCP, CLI, Chrome, anh nói).
2. **Trỏ link, không chép.** Nếu đã có file đầy đủ (vd. `00-context/shopify-listing-standard.md`) thì brain chỉ tóm 1–3 dòng + link. Sửa chuẩn thì sửa ở file nguồn.
3. **Không bao giờ lưu secret**: mật khẩu, token, API key, App Password, mã 2FA, số thẻ/ngân hàng. Chỉ ghi *chỗ để* (vd. "token Trello ở `~/.config/embroidery/trello.env`, ngoài repo").
4. **Giữ `[?]` cho chỗ chưa biết.** Không đoán số liệu. Chỗ mâu thuẫn ghi `⚠️ mâu thuẫn:` kèm 2 nguồn.
5. **Quyết định mới của anh Nam** → thêm 1 dòng lên đầu `decisions.md` (ngày | quyết định | phạm vi | nguồn). Quyết định cũ bị thay → đánh dấu `~~gạch~~ SUPERSEDED <ngày>`, không xoá.
6. **Trước khi đổi store hoặc file dùng chung**: đọc `store-state.md` + `team.md`, kiểm việc đó có chủ chưa. Làm xong → cập nhật `store-state.md` (hoặc file trạng thái liên quan) + ghi 1 dòng log.
7. Không chắc xếp vào đâu → thả vào `inbox.md`, có ngày + tên người/bot ghi.

## Ai ghi file nào
| File | Ai ghi chính | Ai được bổ sung |
|---|---|---|
| `store-state.md` | Bot đổi store vừa làm xong việc (Shopify, Product, CEO) | Mọi bot, sau khi kiểm thực tế |
| `decisions.md` | Ai nghe anh Nam chốt thì ghi | — |
| `team.md` | CEO / anh Nam | Bot tự sửa dòng của mình nếu phạm vi đổi (ghi ngày) |
| `sops/*` | Bot giữ quy trình đó (xem `team.md`) | QA góp ý |
| `metrics/` | CEO (snapshot tuần) | Ads, SEO, Email thêm số kênh mình |
| `lessons.md` | Ai rút ra bài học, có nguồn | — |
| `inbox.md` | Ai cũng được | CEO dọn hàng tuần |
| `INDEX.md` | Ai thêm file mới vào repo | — |

## Quy ước chung của repo (giữ nguyên)
- Văn xuôi tiếng Việt; keyword, title, tag, mô tả listing bằng tiếng Anh.
- Tên file có ngày: `YYYY-MM-DD-<chu-de>.md`.
- Không làm idea vướng IP/trademark (xem `sops/trademark-ip-check.md`).
