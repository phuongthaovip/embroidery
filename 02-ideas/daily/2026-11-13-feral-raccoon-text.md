# Feral raccoon: chuyển mẫu 2D bán chạy sang file thêu (2026-11-13)

- **Nguồn:** 8 ảnh 2D bán chạy của shop cũ anh Nam, thư mục `D:\1KHOKANG\CreF\VP IDEA\EMBROIDERY\demo\5437548`.
- **Cách làm:** giữ nguyên câu chữ của từng ảnh. Đổi hình gấu mèo vẽ chì (nét gạch dày, lông sợi, không thêu được giống) sang kiểu thêu.
- **IP:** câu chữ và hình meme gấu mèo là của anh, không dính nhân vật hay thương hiệu nào. Ổn.

## Hướng thêu chung

- **Màu:** 1 màu chính nâu đen (giống bản in gốc). Muốn nổi hơn thì thêm 1–2 màu: xám cho thân, trắng kem cho mặt.
- **Gấu mèo:**
  - Nét viền satin kết hợp mảng fill phẳng: mặt nạ đen, đuôi khoang, bụng trắng.
  - Không có lông sợi. Có thể giữ vài nét running stitch ngắn cho chất vintage.
- **Tư thế:** giữ dáng giống ảnh gốc (theo [[feedback-match-reference-silhouette]]): nằm ngửa giơ 1 chân lên trời, đầu ngoảnh nhìn.
- **Chữ:**
  - Giữ font kiểu retro serif / script như bản gốc.
  - Dòng chữ nhỏ (EST., Exclusive Members Only) phải cao ≥ 0.25".
- **Sao trang trí:** sao 4 cánh làm bằng satin, giữ khoảng 6–8 cái.
- **Size:** 4–7" (thêu ngực áo / áo sweatshirt). Có thể thêm bản left chest 3.5" chỉ gồm gấu mèo và chữ ngắn.

## Bảng idea

| ID | Ảnh gốc | Câu chữ (giữ nguyên) | Hình gấu mèo bản thêu | Phụ kiện |
|---|---|---|---|---|
| FR-01 | Feral And Pregnant Don't Touch Me.png | Feral & Pregnant / Don't Touch Me | Ngồi ôm bụng bầu tròn | Bụng trắng to, sao |
| FR-02 | 141825 | Feral & Pregnant / Don't Touch Me | Nằm ngửa giơ chân, bụng tròn | Sao |
| FR-03 | 141503 | FERAL AUNTS / EST. 2025 / Social Club / EXCLUSIVE MEMBERS ONLY | Nằm ngửa giơ chân | Bố cục logo club |
| FR-04 | 141751 | FERAL & ENGAGED | Nằm ngửa giơ chân, ôm nhẫn kim cương | Nhẫn kim cương to, sao |
| FR-05 | 141759 | UNDIAGNOSED / But Something Aint Right | Nằm ngửa giơ chân | Sao |
| FR-06 | 141808 | GIRLS GONE Feral / EST. 2026 / [NAME]'S BACHELORETTE / [City, State] | Nằm ngửa giơ chân, đội voan cô dâu | Voan ngắn, sao. Phần tên và địa điểm để khách đổi (personalized) |
| FR-07 | 141816 | In My Feral / BRIDE ERA | Nằm ngửa giơ chân, đội voan | Voan, sao |
| FR-08 | 141857 | Feral & / STERILE | Nằm ngửa giơ chân | Sao |

**Gợi ý thêm (từ cùng ảnh):**
- **Bundle cưới:** gộp FR-04 Engaged, FR-06 Bachelorette và FR-07 Bride Era thành "Feral Bride Bundle 3 designs". Dùng cho tiệc bachelorette, cả nhóm bạn mặc chung nên dễ bán theo set.
- **FR-06 bản cố định:** thay tên và địa điểm bằng chữ chung "BRIDE SQUAD / Bachelorette Party". Như vậy không cần làm lại file cho từng khách.

## Prompt ảnh (ChatGPT Thaonie, 1 chat / idea)

Phần style chung, ghép sau mỗi prompt:

> Style: machine embroidery design mockup, realistic satin and fill stitch texture, vintage retro t-shirt look, only 2 thread colors (dark espresso brown and light grey) plus cream for the belly and face, flat colors, no gradients, no shading, no fur strand texture, clean bold outlines, easy to digitize. The raccoon is drawn with simple satin outlines and flat fill areas (black eye mask, striped ringed tail, light belly), only a few short running-stitch accent lines. Small 4-point satin sparkle stars around the raccoon. Text in the same dark brown, crisp satin lettering, spelled exactly as written. No outer border, no patch edge. Fully transparent background (PNG with alpha channel), no shirt, no fabric, no shadow.

| ID | Prompt nội dung |
|---|---|
| FR-01 | Create a square 1:1 image. Top text in two lines: "Feral &" small retro serif, "Pregnant" big bold retro serif. Center: a chubby raccoon sitting upright, holding its big round pregnant belly with both paws, smug face. Bottom text in a playful retro script: "Don't Touch Me". |
| FR-02 | Create a square 1:1 image. Top text: "Feral &" small retro serif above "Pregnant" big bold retro serif. Center: a raccoon lying dramatically on its back, round pregnant belly up, one hind leg kicked straight up in the air, head turned looking at the viewer. Bottom text in playful retro script: "Don't Touch Me". |
| FR-03 | Create a square 1:1 image. A vintage social club logo layout: big arched condensed serif text "FERAL AUNTS" at the top, "EST." on the left and "2025" on the right of the center image, center: a raccoon lying dramatically on its back with one leg kicked up in the air, head turned to the viewer. Below: elegant script "Social Club", and a small line of serif caps "EXCLUSIVE MEMBERS ONLY". |
| FR-04 | Create a square 1:1 image. Top text: big bold retro serif "FERAL" with a large decorative script ampersand "&" on the right. Center: a raccoon lying dramatically on its back with one leg kicked up, hugging a big diamond engagement ring. Bottom text: big bold retro serif "ENGAGED". |
| FR-05 | Create a square 1:1 image. Top text: condensed bold retro serif "UNDIAGNOSED". Center: a raccoon lying dramatically on its back with one leg kicked up in the air, head turned to the viewer, slightly unhinged expression. Bottom text in two lines of playful retro script: "But Something" and "Aint Right". |
| FR-06 | Create a square 1:1 image. Top text: big classic serif "GIRLS GONE" with script "Feral" under it. "EST." on the left and "2026" on the right of the center image. Center: a raccoon lying on its back with one leg kicked up, wearing a short bridal veil. Bottom: serif caps "OLIVIA'S BACHELORETTE" and elegant script "New Orleans, Louisiana". |
| FR-07 | Create a square 1:1 image. Top text: playful retro serif "In My Feral". Center: a raccoon lying dramatically on its back with one leg kicked up, wearing a short bridal veil, head turned to the viewer. Bottom text: big bold retro serif "BRIDE ERA". |
| FR-08 | Create a square 1:1 image. Top text: big bold retro serif "Feral" with a large decorative script "&" on the right. Center: a raccoon lying dramatically on its back with one leg kicked up in the air, head turned to the viewer. Bottom text: big bold retro serif "STERILE". |

**Ghi chú FR-06:** tên "Olivia" và "New Orleans" chỉ là chữ mẫu trên ảnh. Listing cần ghi rõ "custom name & city".
