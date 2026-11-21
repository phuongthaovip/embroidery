---
updated: 2026-11-21
owner: anh Nam / CEO
sources:
  - "CLAUDE.md"
  - "AGENTS.md"
---

# Second brain — Embroidery / EmbroThread

> Tạo 2026-11-21. Đây là **chỗ đọc đầu tiên** cho mọi người và mọi bot làm việc trong repo này
> (anh Nam, bot EmbroThread CEO / Product / QA / Ads / …, các phiên Claude và Codex).

## Brain là gì
Repo này điều hành 3 kênh bán file thêu máy từ một thư mục: 2 shop Etsy (**PaolaCraftGifts**, **KyraGiftsCo**) và store Shopify **EmbroThread.com**.
Kiến thức nằm rải rác ở [`AGENTS.md`](../AGENTS.md), [`CLAUDE.md`](../CLAUDE.md), [`00-context/`](../00-context/) (nhất là [`shop-profile.md`](../00-context/shop-profile.md)), research, idea, listing.
`brain/` gom lại thành **trạng thái hiện tại + quyết định + ai làm gì + cách làm**, và **trỏ về file nguồn** thay vì chép lại.

## Ba lớp
1. **Nguồn thô** (chỉ đọc): [`01-research/`](../01-research/), [`02-ideas/`](../02-ideas/), [`04-listings/`](../04-listings/), [`00-context/`](../00-context/), [`raw/`](../raw/), [`tools/`](../tools/), lịch sử chat, Trello/Etsy/Shopify. Nằm yên chỗ cũ, liệt kê trong [[INDEX]].
2. **Wiki** = `brain/`: trang đã biên soạn, link về nguồn.
3. **Schema** = [`CLAUDE.md`](../CLAUDE.md), [`AGENTS.md`](../AGENTS.md) (+ file này): luật cho agent.

## Ba việc với brain
- **Ingest** — nguồn mới → cập nhật mọi trang nó chạm + log: [[brain-ingest]].
- **Query** — trả lời từ brain kèm link nguồn; câu trả lời tốt → thành trang: [[brain-query]].
- **Lint** — hàng tuần: mâu thuẫn, fact >14 ngày, trang mồ côi, link thiếu, `[?]`: [[brain-lint]].

## Thứ tự đọc
1. [[brain/README]] (file này) — luật ghi.
2. [[store-state]] — EmbroThread.com đang ở trạng thái nào, việc đang mở, ai giữ.
3. [[team]] — bot/phiên nào làm gì, không được đụng gì, báo cáo về đâu.
4. [[decisions]] — anh Nam đã chốt gì (mới nhất ở trên). **Quyết định ở đây thắng ghi chú cũ trong file khác.**
5. `brain/sops/` — quy trình lặp lại (đọc SOP đúng việc mình sắp làm).
6. [[INDEX]] — bản đồ mọi file trong repo, khi cần tìm nguồn.
7. Khi cần: [[lessons]] (bài học), [[brain/metrics/README]] (số liệu tuần), [[inbox]] (ghi chú thô chưa xếp), [[log]] (ai đổi gì, khi nào).

## Luật ghi (ai cũng phải theo)
1. **Ghi ngày mọi mục**: `YYYY-MM-DD`. Fact về store/shop ghi kèm "kiểm tra ngày nào, bằng gì" (Shopify MCP, CLI, Chrome, anh nói).
2. **Trỏ link, không chép.** Nếu đã có file đầy đủ (vd. [`00-context/shopify-listing-standard.md`](../00-context/shopify-listing-standard.md)) thì brain chỉ tóm 1–3 dòng + link. Sửa chuẩn thì sửa ở file nguồn.
3. **Không bao giờ lưu secret**: mật khẩu, token, API key, App Password, mã 2FA, số thẻ/ngân hàng. Chỉ ghi *chỗ để* (vd. "token Trello ở `~/.config/embroidery/trello.env`, ngoài repo").
4. **Giữ `[?]` cho chỗ chưa biết.** Không đoán số liệu. Chỗ mâu thuẫn ghi `⚠️ mâu thuẫn:` kèm 2 nguồn.
5. **Quyết định mới của anh Nam** → thêm 1 dòng lên đầu [[decisions]] (ngày | quyết định | phạm vi | nguồn). Quyết định cũ bị thay → đánh dấu `~~gạch~~ SUPERSEDED <ngày>`, không xoá.
6. **Trước khi đổi store hoặc file dùng chung**: đọc [[store-state]] + [[team]], kiểm việc đó có chủ chưa. Làm xong → cập nhật [[store-state]] (hoặc file trạng thái liên quan) + ghi 1 dòng log.
7. Không chắc xếp vào đâu → thả vào [[inbox]], có ngày + tên người/bot ghi.
8. **Mọi thay đổi trong brain → 1 dòng cuối [[log]]** (append-only): ngày | ai | đổi gì | file.
9. **Định dạng trang** (mở repo bằng Obsidian để xem graph): mỗi trang có frontmatter YAML `updated`, `owner`, `sources`; link giữa trang brain dùng `[[wikilink]]` (tên file không đuôi; README dùng `[[brain/README]]`); link tới file repo dùng link markdown tương đối, vd. `[shop-profile](../00-context/shop-profile.md)`.
10. Markdown thuần. Không embeddings/RAG lúc này — [[INDEX]] + grep là đủ.

## Ai ghi file nào
| File | Ai ghi chính | Ai được bổ sung |
|---|---|---|
| [[store-state]] | Bot đổi store vừa làm xong việc (Shopify, Product, CEO) | Mọi bot, sau khi kiểm thực tế |
| [[decisions]] | Ai nghe anh Nam chốt thì ghi | — |
| [[team]] | CEO / anh Nam | Bot tự sửa dòng của mình nếu phạm vi đổi (ghi ngày) |
| `sops/*` | Bot giữ quy trình đó (xem [[team]]) | QA góp ý |
| [[brain/metrics/README]] | CEO (snapshot tuần) | Ads, SEO, Email thêm số kênh mình |
| [[lessons]] | Ai rút ra bài học, có nguồn | — |
| [[inbox]] | Ai cũng được | CEO dọn hàng tuần |
| [[log]] | Ai đổi brain thì thêm dòng (chỉ thêm, không sửa) | — |
| [[INDEX]] | Ai thêm file mới vào repo | — |

## Quy ước chung của repo (giữ nguyên)
- Văn xuôi tiếng Việt; keyword, title, tag, mô tả listing bằng tiếng Anh.
- Tên file có ngày: `YYYY-MM-DD-<chu-de>.md`.
- Không làm idea vướng IP/trademark (xem [[trademark-ip-check]]).
