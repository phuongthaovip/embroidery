---
updated: 2026-11-21
owner: CEO / anh Nam
sources:
  - "Orca task 2026-11-21"
  - "CLAUDE.md"
---

# Team — bot, phiên làm việc, ai giữ gì

> Cập nhật 2026-11-21. Bot nào đổi phạm vi thì sửa dòng của mình, ghi ngày. `[?]` = chưa rõ, hỏi anh Nam.

## Người
| Ai | Vai trò |
|---|---|
| **Anh Nam** | Chủ 3 kênh. Duyệt idea, chốt quyết định, làm việc cần danh tính (Shopify Payments, giấy tờ, ngân hàng). |
| Chị (chủ KyraGiftsCo) | Shop Etsy thứ 2, cùng nhà, dùng chung idea machine. |
| Designer(s) | Digitize file khi có đơn. Board "Designer Online - Nguyen Hop" (EMBN). Danh sách người `[?]` |

## Bot (EmbroThread team)
Đang có: CEO, Product, QA, Ads. Sẽ thêm: Shopify, SEO, Social, Email, CS. Cho tới khi bot "sẽ thêm" chạy, việc của nó do **CEO giao lại** (thường cho Product hoặc phiên Claude), không ai tự nhận.

| Bot | Việc | Sở hữu (chỉ bot này ghi) | Không được đụng | Báo cáo về |
|---|---|---|---|---|
| **CEO** | Ưu tiên, giao việc, báo cáo cho anh Nam | [[brain/metrics/README]] (snapshot tuần), lint brain hàng tuần ([[brain-lint]]), dọn [[inbox]], cột "Chủ" trong [[store-state]] | Không tự sửa sản phẩm/theme/ads; không chốt thay anh Nam | anh Nam |
| **Product** | Idea, ảnh mockup, listing (Etsy + Shopify) | [`02-ideas/`](../02-ideas/), [`03-briefs/`](../03-briefs/), [`04-listings/`](../04-listings/), tạo/sửa sản phẩm Shopify theo [`shopify-listing-standard.md`](../00-context/shopify-listing-standard.md), [[idea-to-listing]], [[shopify-listing]], [[mockup-generation]], [[image-webp-redo]] | Theme, menu, giá chung, ads, email | CEO |
| **QA** | Kiểm file thêu + listing trước/sau khi lên | Báo cáo QA (ghi vào [[inbox]] hoặc file `05-results/YYYY-MM-DD-qa-*.md`), [[trademark-ip-check]] | Không tự sửa listing — gửi lỗi cho Product | CEO |
| **Ads** | Quảng cáo trả tiền (Etsy Ads, Google/Meta khi có) | Chiến dịch ads, số ads trong [[brain/metrics/README]] | Không đổi giá, sản phẩm, theme | CEO |
| **Shopify** *(sắp có)* | Theme, trang, menu, collection, conversion | Theme, menu, trang, collection, app setting; cập nhật [[store-state]] | Nội dung sản phẩm (Product), policies cần anh dán/duyệt | CEO |
| **SEO** *(sắp có)* | Tìm kiếm (Google + Etsy search) | Meta trang/collection, chuẩn keyword; góp ý title/tag cho Product | Không đổi handle đã publish trừ khi có redirect 301 | CEO |
| **Social** *(sắp có)* | Mạng xã hội organic (Pinterest, IG, FB…) | Lịch post, tài khoản social | Không chạy ads (Ads), không đổi store | CEO |
| **Email** *(sắp có)* | Email marketing (signup, flow, newsletter) | Danh sách + flow email | Không gửi email giao file đơn hàng (CS) | CEO |
| **CS** *(sắp có)* | Khách hàng: đơn, giao file, hỏi đáp, hoàn tiền theo policy | Hộp thư khách, [[order-digitize-delivery]] | Không đổi policy, giá | CEO |

## Phiên / máy làm việc
| Phiên | Đọc file gì | Dùng cho | Ghi chú |
|---|---|---|---|
| Claude (Claude Code / Orca) | [`CLAUDE.md`](../CLAUDE.md) | Research, idea, SEO, Shopify (MCP + CLI), Trello MCP | Máy Mac của anh, checkout `~/Downloads/Ecom-Project/embroidery` |
| Codex | [`AGENTS.md`](../AGENTS.md) | Như Claude | AGENTS.md gần trùng CLAUDE.md |
| **H Mac** | — | Chạy GPT Image (ChatGPT plan) cho Gavana; offline → ảnh nằm "Queued" | [`CLAUDE.md`](../CLAUDE.md) §6 |
| Phiên Windows (Chrome **NIENVP**, ChatGPT project **Thaonie**) | — | Gen ảnh mockup từ 2026-10-26 trở đi; giữ các memory `feedback-*` | Đường dẫn `D:\1KHOKANG\...`, `C:\Users\vutha\...` trong file idea là của máy này `[?]` |
| Orca coordinator + worker | `brain/` | Chia việc nhiều agent | Worker làm trong worktree riêng, merge về `main` |

## Luật bàn giao (handoff)
1. **Trước khi đổi store hoặc file dùng chung** ([`CLAUDE.md`](../CLAUDE.md), [`AGENTS.md`](../AGENTS.md), `00-context/*`, `brain/*`, Trello, Shopify): đọc [[store-state]] + file này. Việc đó có chủ khác → hỏi chủ / CEO, đừng làm chồng.
2. Đang làm 1 việc dài → ghi 1 dòng "đang làm" vào [[store-state]] (Việc đang mở) hoặc [[inbox]], kèm ngày + tên bot, để bot khác không làm trùng.
3. **Làm xong → log**: sửa fact trong [[store-state]] (có ngày kiểm), thêm dòng vào "Log thay đổi store"; quyết định mới của anh → [[decisions]]; 1 dòng cuối [[log]]. Nguồn mới → theo [[brain-ingest]].
4. Không ghi lên Trello / Etsy / Shopify thứ anh chưa cho phép ([`shopify-listing-standard.md`](../00-context/shopify-listing-standard.md) §8).
5. Không lưu secret ở bất kỳ file nào (xem [[brain/README]]).
