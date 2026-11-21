# INDEX — bản đồ repo theo chủ đề

> Cập nhật 2026-11-21. Cột "Ngày" = ngày commit gần nhất (mọi file nhập lần đầu được commit 2026-11-18, nên ngày trong tên file chính xác hơn).
> "chưa commit" = file đang có ở checkout chính (`main`) nhưng chưa commit lúc tạo brain. Thêm file mới vào repo → thêm 1 dòng ở đây.

## 0. Brain
| File | Nội dung | Ngày |
|---|---|---|
| `brain/README.md` | Brain là gì, thứ tự đọc, luật ghi | 2026-11-21 |
| `brain/store-state.md` | Dashboard trạng thái EmbroThread.com + việc mở | 2026-11-21 |
| `brain/team.md` | Bot/phiên, phạm vi, luật bàn giao | 2026-11-21 |
| `brain/decisions.md` | Log quyết định của anh Nam, mới nhất trên đầu | 2026-11-21 |
| `brain/lessons.md` | Bài học đúc kết | 2026-11-21 |
| `brain/inbox.md` | Ghi chú thô chờ xếp | 2026-11-21 |
| `brain/metrics/README.md`, `brain/metrics/2026-11-21.md` | Format snapshot tuần + snapshot đầu | 2026-11-21 |
| `brain/sops/*.md` | 7 SOP (xem mục 5) | 2026-11-21 |

## 1. Hướng dẫn cho agent
| File | Nội dung | Ngày |
|---|---|---|
| `CLAUDE.md` | Context cho Claude: mục tiêu, shop, quy trình, ràng buộc idea, tool (Gavana, Trello) | 2026-11-20 (+ sửa chưa commit ở main) |
| `AGENTS.md` | Bản cho Codex, nội dung gần như trùng `CLAUDE.md` | chưa commit |
| `2026-10-18-lich-su-chat.html` | Lịch sử chat dự án ngày đầu (HTML) | 2026-11-18 |

## 2. Shop & store (context)
| File | Nội dung | Ngày |
|---|---|---|
| `00-context/shop-profile.md` | Hồ sơ PaolaCraftGifts, KyraGiftsCo; log setup Shopify 11-19→11-21 (phần Shopify nay trỏ sang `brain/store-state.md`) | 2026-11-20 (+ sửa chưa commit) |
| `00-context/2026-11-19-shopify-policies.md` | Refund / Shipping / Terms (14 mục) đã đăng lên store | 2026-11-20 |
| `00-context/shopify-listing-standard.md` | **Chuẩn listing Shopify**: chọn card, trạng thái, WebP, handle/tên file/alt, title, mô tả, tag, bảng giá | chưa commit (2026-11-21) |
| `logo.png`, `logo-inverse.png`, `icon-embrothread.png` | Logo EmbroThread (navy, bản kem, favicon chữ E) | 2026-11-19 |

## 3. Design / ảnh / thêu
| File | Nội dung | Ngày |
|---|---|---|
| `00-context/image-style-guide.md` | Phong cách mockup chốt 2026-11-18: nền linen kem, chỉ dày, 2 nhánh A/B + prompt mẫu | 2026-11-18 |
| `00-context/embroidery-specs.md` | Khung hoop, quy tắc chữ/nét/màu (nhiều `[?]`) | 2026-11-18 |
| `templates/image-prompt.md` | Prompt gen ảnh cũ (nền trắng, ≤6 màu) — ⚠️ cũ hơn style guide | 2026-11-18 |
| `templates/idea-card.md` | Mẫu idea card + chấm điểm /20 | 2026-11-18 |

## 4. Tool & dữ liệu thô (chưa commit, ở checkout chính)
| File | Nội dung |
|---|---|
| `tools/shopify_prep.py` | Đổi ảnh sang WebP 1000px, đặt handle/tên file/alt, xuất `manifest.json` |
| `tools/badges.py` | Thêm 2 hàng badge navy (định dạng file + hãng máy) vào đáy mockup |
| `tools/trello_pull.py` | Tải attachment card list "Đã duyệt" (board **EmbroT**) về `raw/<mã>/` |
| `tools/trello_push.py` | Đẩy `raw/<mã>/out/*.webp` lên card, chuyển sang list "Listing Shopify" |
| `tools/trello_replace.py` | Thay attachment `<mã>-N.webp` trên card EmbroT |
| `raw/` | Ảnh gốc theo mã card (EMBN…) + `cards.json` |
> Token Trello đọc từ `~/.config/embroidery/trello.env` (ngoài repo). Không chép vào brain.

## 5. Quy trình (SOP)
| File | Nội dung |
|---|---|
| `brain/sops/idea-to-listing.md` | Research → idea → ảnh → Trello → listing → kết quả |
| `brain/sops/shopify-listing.md` | Tóm + link tới `00-context/shopify-listing-standard.md` |
| `brain/sops/image-webp-redo.md` | Làm lại ảnh (WebP, đổi tên, Canva cho ảnh có badge/logo lạ) |
| `brain/sops/mockup-generation.md` | Gen mockup: ChatGPT Thaonie, Gavana, Magnific |
| `brain/sops/order-digitize-delivery.md` | Có đơn → digitize → gửi file qua email 1–3 ngày |
| `brain/sops/etsy-scanning.md` | Quét Etsy bằng Chrome + HeyEtsy, giới hạn 429 |
| `brain/sops/trademark-ip-check.md` | Lọc rủi ro IP/trademark |

## 6. Research
| File | Nội dung | Ngày |
|---|---|---|
| `01-research/2026-10-17-shop-competitor-analysis.md` | Quét Paola + 3 đối thủ: 80% listing không bán, top 10 = 75%, bundle = 56%, faith gap | 2026-11-18 |
| `01-research/2026-10-22-amazon-merch-christmas-scan.md` | Quét Amazon Merch Christmas — không ra kết quả, bài học | 2026-11-18 |
| `01-research/2026-11-12-holiday-calendar.md` | Lịch lễ 11/2026→4/2027 + số YTrends | 2026-11-18 |
| `01-research/2026-11-13-measles-vaccine-niche.md` | Niche sởi/vaccine: keyword, shop, rủi ro | 2026-11-18 |
| `01-research/2026-11-20-store-design-benchmark.md` | Học giao diện 5 store thêu lớn → áp cho embrothread.com | 2026-11-20 |
| `01-research/2026-11-21-valentine-competitor-scan.md` | Quét Valentine + đề xuất 14 idea V1–V14 (chờ duyệt) | chưa commit |

## 7. Ideas (pipeline sản phẩm)
| File | Nội dung | Ngày |
|---|---|---|
| `02-ideas/backlog.md` | Backlog idea + điểm /20 + trạng thái (mới nhất trên đầu) | 2026-11-18 |
| `02-ideas/daily/2026-10-18-paola.md` | Idea ngày 2026-10-18 (Chủ nhật) — 14 đề xuất, mục tiêu duyệt 10 | 2026-11-18 |
| `02-ideas/daily/2026-10-22-thanksgiving.md` | Lô 10 idea thêu Thanksgiving (2026-10-22) | 2026-11-18 |
| `02-ideas/daily/2026-10-23-ith-frames.md` | Lô 10 idea: khung ITH applique trống ở giữa (frame), 2026-10-23 | 2026-11-18 |
| `02-ideas/daily/2026-10-23-ith.md` | Lô 10 idea ITH (In The Hoop), 2026-10-23 | 2026-11-18 |
| `02-ideas/daily/2026-10-23-yule-cat-2.md` | Lô 10 idea Yule Cat, đợt 2 (2026-10-23) | 2026-11-18 |
| `02-ideas/daily/2026-10-23-yule-cat.md` | Lô 10 idea: Yule Cat (Jólakötturinn), 2026-10-23 | 2026-11-18 |
| `02-ideas/daily/2026-10-24-mahjong.md` | Idea Mahjong — 2026-10-24 (anh Nam duyệt cả 10) | 2026-11-18 |
| `02-ideas/daily/2026-10-24-yule-cat-3.md` | Lô 10 idea Yule Cat, đợt 3 (2026-10-24) | 2026-11-18 |
| `02-ideas/daily/2026-10-24-yule-cat-4.md` | Lô 10 idea Yule Cat, đợt 4: thêu đơn giản (2026-10-24) | 2026-11-18 |
| `02-ideas/daily/2026-10-24-yule-lads.md` | Lô 10 idea Yule Lads, 13 chú Yule Lad Iceland (2026-10-24) | 2026-11-18 |
| `02-ideas/daily/2026-10-26-black-cat-christmas.md` | Lô 10 idea Black Cat Christmas (2026-10-26) | 2026-11-18 |
| `02-ideas/daily/2026-10-26-first-christmas-baby.md` | Baby's First Christmas — 10 bundle idea (2026-10-26) | 2026-11-18 |
| `02-ideas/daily/2026-10-26-mahjong-christmas.md` | Mahjong Christmas — 10 idea (2026-10-26) | 2026-11-18 |
| `02-ideas/daily/2026-10-26-santa-reindeer.md` | Santa & Reindeer Christmas — 10 idea (2026-10-26) | 2026-11-18 |
| `02-ideas/daily/2026-10-26-yule-cat-5.md` | Lô 20 idea Yule Cat, đợt 5: theo từ khóa (2026-10-26) | 2026-11-18 |
| `02-ideas/daily/2026-10-27-book-lover-christmas.md` | Book Lover Christmas — 10 idea (2026-10-27) | 2026-11-18 |
| `02-ideas/daily/2026-10-27-mahjong-christmas-funny.md` | Mahjong Christmas FUNNY — 10 ý tưởng (2026-10-27) | 2026-11-18 |
| `02-ideas/daily/2026-10-28-believe-christmas.md` | Believe Christmas — 10 ý tưởng (2026-10-28) | 2026-11-18 |
| `02-ideas/daily/2026-10-28-christian.md` | Christian — 10 ý tưởng (2026-10-28) | 2026-11-18 |
| `02-ideas/daily/2026-10-28-classic-christmas.md` | Classic Christmas — 10 ý tưởng (2026-10-28) | 2026-11-18 |
| `02-ideas/daily/2026-11-02-coquette-first-christmas.md` | Coquette "My First Christmas" — 10 idea mẫu lẻ (2026-11-02) | 2026-11-18 |
| `02-ideas/daily/2026-11-03-kyra-christmas-bundle-12.md` | Kawaii Christmas bundle 12 mẫu: thêm 8 idea (2026-11-03) | 2026-11-18 |
| `02-ideas/daily/2026-11-03-kyra-christmas-food.md` | Kawaii Christmas Food: chuyển từ bundle Thanksgiving (2026-11-03) | 2026-11-18 |
| `02-ideas/daily/2026-11-04-christmas-winners-remix.md` | Christmas — 10 idea lấy từ mẫu bán chạy và nhiều fav (2026-11-04) | 2026-11-18 |
| `02-ideas/daily/2026-11-04-mahjong-christmas-funny-2.md` | Mahjong Funny Christmas — lô 2, 10 idea (2026-11-04) | 2026-11-18 |
| `02-ideas/daily/2026-11-09-first-christmas-pink-green.md` | First Christmas màu hồng + xanh lá: lô 10 idea (2026-11-09) | 2026-11-18 |
| `02-ideas/daily/2026-11-09-yule-cat-folk.md` | Yule Cat theo phong cách lô đầu: lô 10 idea (2026-11-09) | 2026-11-18 |
| `02-ideas/daily/2026-11-09-yule-cat-winners.md` | Yule Cat theo mẫu bán tốt: lô 10 idea (2026-11-09) | 2026-11-18 |
| `02-ideas/daily/2026-11-09-yule-krampus.md` | Yule Cat, Yule Christmas, Krampus: lô 10 idea (2026-11-09) | 2026-11-18 |
| `02-ideas/daily/2026-11-11-floral-leaf-animals.md` | Con vật và côn trùng ghép từ hoa lá: lô 20 idea (2026-11-11) | 2026-11-18 |
| `02-ideas/daily/2026-11-12-holiday-4-events-images.md` | Ảnh gen, lô 4 dịp (2026-11-12) | 2026-11-18 |
| `02-ideas/daily/2026-11-12-holiday-4-events.md` | Idea 4 dịp: Thanksgiving, Black Friday/Cyber, Hanukkah, Christmas | 2026-11-18 |
| `02-ideas/daily/2026-11-13-blue-wave-images.md` | Ảnh gen Blue Wave 2026 (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-blue-wave.md` | Lô Blue Wave 2026: file thêu máy (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-christmas-wreath-frames-images.md` | Ảnh gen khung vòng Christmas (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-christmas-wreath-frames.md` | Lô 10 khung vòng Christmas (2026-11-13, bản 2 sau khi anh thêm ảnh) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-feral-raccoon-images.md` | Ảnh gen Feral raccoon (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-feral-raccoon-text.md` | Feral raccoon: chuyển mẫu 2D bán chạy sang file thêu (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-filigree-b2-images.md` | Ảnh gen lô Filigree đợt 2 (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-filigree-b2.md` | Lô Filigree đợt 2: 20 ý tưởng Christmas và Thanksgiving (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-linework-glow-images.md` | Ảnh gen lô Linework Glow (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-linework-glow.md` | Lô thêu nét phát sáng (linework glow), Christmas và Thanksgiving (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-peeking-animal-bundles-images.md` | Ảnh gen bundle thú peeking (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-peeking-animal-bundles.md` | Bundle thú "peeking" theo mẫu Feral & Engaged (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-13-pro-science-b2.md` | Lô Pro-Science đợt 2 (2026-11-13), ý tưởng lấy từ shop đối thủ | 2026-11-18 |
| `02-ideas/daily/2026-11-13-public-health-images.md` | Ảnh gen lô Public Health (2026-11-13), ĐÃ DỪNG theo yêu cầu anh Nam | 2026-11-18 |
| `02-ideas/daily/2026-11-13-public-health.md` | Lô Public Health / Pro-Vaccine (2026-11-13) | 2026-11-18 |
| `02-ideas/daily/2026-11-14-christmas-monogram-font-b2-images.md` | Ảnh gen Christmas Monogram Font đợt 2 (2026-11-14) | 2026-11-18 |
| `02-ideas/daily/2026-11-14-christmas-monogram-font-b2.md` | Christmas Monogram Font đợt 2: 10 ý tưởng (2026-11-14) | 2026-11-18 |
| `02-ideas/daily/2026-11-14-christmas-monogram-font.md` | 10 ý tưởng Christmas Monogram Font (2026-11-14) | 2026-11-18 |
| `02-ideas/daily/2026-11-14-filigree-b3-images.md` | Ảnh gen lô Filigree đợt 3 + Christmas Monogram Font (2026-11-14) | 2026-11-18 |
| `02-ideas/daily/2026-11-14-filigree-b3.md` | Lô Filigree đợt 3: 20 ý tưởng Christmas và Thanksgiving (2026-11-14) | 2026-11-18 |
| `02-ideas/daily/2026-11-14-filigree-monogram-font.md` | Filigree Christmas Monogram Font: 10 ý tưởng (2026-11-14) | 2026-11-18 |
| `02-ideas/daily/2026-11-16-krampus-black-cat-images.md` | Ảnh gen lô Krampus × mèo đen (2026-11-16) | 2026-11-18 |
| `02-ideas/daily/2026-11-16-krampus-black-cat.md` | Krampus và nhân vật truyền thuyết mix mèo đen: lô 20 ý tưởng (2026-11-16) | 2026-11-18 |
| `02-ideas/daily/2026-11-17-christmas-b2-images.md` | Ảnh gen lô Christmas đợt 2 XN (2026-11-17) | 2026-11-18 |
| `02-ideas/daily/2026-11-17-christmas-b2.md` | Christmas đợt 2 từ spy Etsy + HeyEtsy: lô 20 ý tưởng (2026-11-17, bản làm lại) | 2026-11-18 |
| `02-ideas/daily/2026-11-17-christmas-bestsellers-images.md` | Ảnh gen lô Christmas bestseller XS (2026-11-17) | 2026-11-18 |
| `02-ideas/daily/2026-11-17-christmas-bestsellers.md` | Christmas từ mẫu bán chạy trên Etsy: lô 20 ý tưởng (2026-11-17) | 2026-11-18 |
| `02-ideas/daily/2026-11-18-christmas-sheep-ref.md` | Ref anh gửi: Christmas Sheep cocoa (2026-11-18) | 2026-11-18 |
| `02-ideas/daily/2026-11-18-kw-embroidery-design-b2-images.md` | Ảnh gen lô KN, phong cách mới (2026-11-18) | 2026-11-18 |
| `02-ideas/daily/2026-11-18-kw-embroidery-design-b2.md` | Lô 2 từ khóa "embroidery design": 10 ý tưởng (2026-11-18) | 2026-11-18 |
| `02-ideas/daily/2026-11-18-kw-embroidery-design-images.md` | Ảnh gen KW, phong cách mới (2026-11-18) | 2026-11-18 |
| `02-ideas/daily/2026-11-18-kw-embroidery-design.md` | Từ khóa "embroidery design": quét Etsy và ý tưởng (2026-11-18) | 2026-11-18 |
| `02-ideas/daily/2026-11-18-teacher-christmas-images.md` | Ảnh gen lô Teacher Christmas TT (2026-11-18) | 2026-11-18 |
| `02-ideas/daily/2026-11-18-teacher-christmas.md` | Teacher Christmas: lô 20 ý tưởng (2026-11-18) | 2026-11-18 |

## 8. Listings (SEO Etsy + Shopify)
| File | Nội dung | Ngày |
|---|---|---|
| `04-listings/2026-10-22-kyra-thanksgiving-seo.md` | SEO Etsy: Thanksgiving, KyraGiftsCo (Trello VP-EMBROIDERY, cột IDEA RAW), 2026-10-22 | 2026-11-18 |
| `04-listings/2026-10-23-kyra-can-designer-seo.md` | SEO Etsy: KyraGiftsCo, Trello VP-EMBROIDERY cột Cần Designer, 2026-10-23 | 2026-11-18 |
| `04-listings/2026-10-23-kyra-yule-cat-seo.md` | SEO Etsy: Yule Cat, Trello VP-EMBROIDERY cột Cần Designer, 2026-10-23 | 2026-11-18 |
| `04-listings/2026-10-24-vpembroidery-black-cat-christmas-can-design.md` | SEO Listings — cột "Cần Design" (board VP-EMBROIDERY) | 2026-11-18 |
| `04-listings/2026-10-25-vpembroidery-mahjong-can-design.md` | SEO Listings — mẫu mới cột "Cần Design" (VP-EMBROIDERY) — Mahjong | 2026-11-18 |
| `04-listings/2026-10-26-vpembroidery-can-design.md` | SEO Listings: cột "Cần Design" (VP-EMBROIDERY), ngày 2026-10-26 | 2026-11-18 |
| `04-listings/2026-10-27-vpembroidery-idea-raw.md` | SEO VP-EMBROIDERY — cột IDEA RAW (2026-10-27) | 2026-11-18 |
| `04-listings/2026-10-28-vpe-281-287.md` | SEO — cột Cần Design VP-EMBROIDERY (VPE2610281–287) | 2026-11-18 |
| `04-listings/2026-10-28-vpembroidery-idea-raw-276-279.md` | VP-EMBROIDERY — IDEA RAW: SEO 4 mẫu còn lại (VPE2610276–279) | 2026-11-18 |
| `04-listings/2026-10-30-vpe-301-308.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE2610301–308) | 2026-11-18 |
| `04-listings/2026-10-31-vpe-031-038.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE261031–038) | 2026-11-18 |
| `04-listings/2026-11-01-vpe-2611011-018.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE2611011–018) | 2026-11-18 |
| `04-listings/2026-11-02-vpe-2611021-029-first-christmas.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE2611021–029), Coquette My First Christmas | 2026-11-18 |
| `04-listings/2026-11-03-vpe-2611031-041-kawaii-christmas-bundles.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE2611031–041), bundle Christmas kawaii | 2026-11-18 |
| `04-listings/2026-11-04-vpe-idea-raw-271-277-035.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE2610271–277 bản mới + VPE2611035) | 2026-11-18 |
| `04-listings/2026-11-09-vpe-idea-raw-2611091-101.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE2611091–099, VPE2611101) | 2026-11-18 |
| `04-listings/2026-11-09-ycf-yule-cat-folk.md` | SEO — Yule Cat folk (YCF-1109-01..10) | 2026-11-18 |
| `04-listings/2026-11-11-fla-floral-leaf-animals.md` | SEO — lô con vật, côn trùng ghép hoa lá FLA-1111-01..20 (KyraGiftsCo) | 2026-11-18 |
| `04-listings/2026-11-11-vpe-idea-raw-fla.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE2611111–117, lô FLA ghép hoa lá) | 2026-11-18 |
| `04-listings/2026-11-11-vpe-idea-raw-mahjong-xmas.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE2609198, VPE2611101–106) | 2026-11-18 |
| `04-listings/2026-11-12-vpe-idea-raw-holiday.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE26111201–17, lô 4 dịp lễ) | 2026-11-18 |
| `04-listings/2026-11-13-vpe-idea-raw-feral-peeking.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE26111317–25) | 2026-11-18 |
| `04-listings/2026-11-13-vpe-idea-raw-filigree.md` | SEO, mẫu Filigree lên Trello IDEA RAW (VPE26111326–52) | 2026-11-18 |
| `04-listings/2026-11-13-vpe-idea-raw-wreath.md` | SEO — cột IDEA RAW VP-EMBROIDERY (VPE26111301–16) | 2026-11-18 |
| `04-listings/2026-11-16-vpe-idea-raw-filigree-b3.md` | SEO Filigree đợt 3, thư mục 5size (2026-11-16) | 2026-11-18 |
| `04-listings/2026-11-16-vpe-idea-raw-krampus-cat.md` | SEO lô Krampus × mèo đen lên Trello IDEA RAW (VPE26111612–21) | 2026-11-18 |
| `04-listings/2026-11-17-vpe-idea-raw-christmas-xs.md` | SEO 8 mockup Christmas lên Trello IDEA RAW (VPE26111701–VPE26111708) | 2026-11-18 |
| `04-listings/2026-11-20-shopify-christmas-batch1.md` | Shopify listing — Christmas (VP-EMBROIDERY) — đợt thử 2026-11-20 | 2026-11-20 |
| `04-listings/2026-11-21-shopify-christmas-batch2.md` | Shopify listing — Christmas (VP-EMBROIDERY) — đợt 2, 2026-11-21 | chưa commit |
| `04-listings/filigree-shared-description.md` | Đoạn mô tả dùng chung dòng Filigree Embroidery Design | 2026-11-18 |

## 9. Kết quả / số liệu
| File | Nội dung | Ngày |
|---|---|---|
| `05-results/` | Trống (chỉ `.gitkeep`) — chưa có số bán ghi lại `[?]` | — |
| `brain/metrics/2026-11-21.md` | Snapshot đầu tiên EmbroThread | 2026-11-21 |
| `03-briefs/` | Trống — chưa dùng bước brief riêng | — |
