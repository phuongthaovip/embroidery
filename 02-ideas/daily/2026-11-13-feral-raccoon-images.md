# Ảnh gen Feral raccoon (2026-11-13)

- Gen trong ChatGPT, project Thaonie, mỗi mẫu 1 chat.
- Link chat: https://chatgpt.com/g/g-p-6acf585d89cc819185cfb3a3832d45e7-thaonie/c/<chat id>
- Theo yêu cầu của anh Nam, mỗi mẫu có 2 bản:
  - **Áo sáng:** chỉ nâu đậm, xám, kem. Là ảnh đầu tiên trong chat.
  - **Áo tối:** chữ và viền kem/trắng, thân gấu xám nhạt, mặt nạ xám than. Là ảnh cuối cùng trong chat.
- Cả 2 bản đều nền trong suốt.
- **Đã kiểm tra:** alpha ở 4 góc ảnh bằng 0. Đã ghép thử ảnh lên nền trắng và nền đen để chắc mặt nạ, sọc đuôi không bị xóa theo nền.

## Bài học khi làm bản áo tối
- Sửa bản áo sáng sang bản áo tối thì ChatGPT hay làm mất nền trong suốt.
- Nếu trong prompt có chữ "transparent", máy gen ảnh vẽ luôn hình bàn cờ vào ảnh. Dùng Python xóa bàn cờ sau đó vẫn sót chấm ô vuông ở mép và trong lòng chữ.
- Bảo gen trên nền xanh lá #00FF00 cũng không được, máy vẫn vẽ bàn cờ.
- **Cách sạch nhất:**
  1. Gen trên nền đen đặc #000000, ghi trong prompt là "bản xem trước thêu trên áo đen".
  2. Nhờ ChatGPT dùng Python xóa nền đen bằng flood fill từ mép ảnh.
  3. Mặt nạ và sọc đuôi có viền kem bao quanh nên không bị xóa theo.
  - FR-02, 03 và 08 làm theo cách này đều sạch.

| ID | Chat id | Áo sáng | Áo tối |
|---|---|---|---|
| FR-01 | 6af6bac6-b348-83ec-a876-c0633b9f67ae | OK. ChatGPT cho chọn A/B, em chọn ảnh 1 (gấu ngồi ôm bụng) | OK sau khi xuất lại (lần đầu bị vẽ bàn cờ cứng vào ảnh) |
| FR-02 | 6af6bac5-35ec-83ec-a714-fbf60ce89fd5 | OK (gấu nằm giơ chân, bụng tròn) | OK sau khi xuất lại (lần đầu ra nền đen) |
| FR-03 | 6af6bac7-dc40-83ec-b95b-bcb2aed87d35 | OK, đủ chữ | OK sau khi xuất lại (lần đầu ra nền đen) |
| FR-04 | 6af6bd40-8228-83ec-b064-71144f496e97 | OK (ôm nhẫn kim cương) | OK. Ảnh cuối trong chat: feral_engaged_edge_flood_transparent.png. Gen trên nền đen rồi flood fill; bản đầu thân gấu đen, đã sửa sang xám |
| FR-05 | 6af6bd40-8dbc-83ec-8f29-d9b0cade78cb | OK | OK ngay lần đầu |
| FR-06 | 6af6bd42-03f8-83ec-8fbb-e1f29edcfa49 | OK (voan cô dâu, Olivia's Bachelorette / New Orleans) | OK sau khi xuất lại |
| FR-07 | 6af6befe-566c-83ec-8179-ec08f026e0d6 | OK (voan + hoa) | OK. Ảnh cuối trong chat: feral_bride_era_edge_flood_transparent.png. Gen trên nền đen rồi flood fill |

**Lưu ý bản áo tối làm bằng flood fill (FR-04, 07, 08 và có thể cả 02, 03):**
- Lỗ kín bên trong chữ (lòng chữ B, R, D, A, chữ &) vẫn còn màu đen, vì flood fill đi từ mép ảnh không chạm tới được.
- Thêu trên áo đen thì không thấy gì. Lúc digitize thì bỏ qua phần này.
- Nếu muốn nền sạch hoàn toàn: nhờ ChatGPT xóa thêm các vùng đen nằm trong lòng chữ.
| FR-08 | 6af6bfe3-5740-83ec-8782-29c58199f8d4 | OK | OK (gen ra nền đen, flood fill sạch) |
