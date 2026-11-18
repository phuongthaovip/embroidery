# Ảnh gen bundle thú peeking (2026-11-13)

- Gen trong ChatGPT, project Thaonie. Mỗi bundle 1 chat.
- Link chat: https://chatgpt.com/g/g-p-6acf585d89cc819185cfb3a3832d45e7-thaonie/c/<chat id>
- **Bản áo sáng:** ảnh đầu tiên trong chat. Viền nâu đậm. Gen trên nền trong suốt, lần đầu đã đạt.
- **Bản áo tối:** ảnh cuối trong chat (file *_dark_fabric_transparent.png). Viền và chữ màu kem. Làm 2 bước:
  1. Gen trên nền đen đặc.
  2. Dùng Python flood fill xóa nền đen.
- **Đã kiểm tra:** alpha 4 góc = 0. Ghép ảnh lên nền trắng và nền đen thì sạch, các phần màu than (gấu đen, Lab đen, đốm bò) vẫn còn nguyên.

| ID | Chat id | Áo sáng | Áo tối |
|---|---|---|---|
| PK-01 Woodland 9 con | 6af6caa8-3468-83ec-abc0-fc1d53deceaa | OK. Đủ 9 chữ, đúng chính tả: Feral, Unhinged, Stinky, Sly, Nuts, Busy, Armored, Prickly, Grumpy | OK, đã xóa luôn lỗ đen trong lòng chữ |
| PK-02 Dog breeds 12 con | 6af6caaa-7fd0-83ec-8fb0-61b9b80025da | OK, 12 giống chó đúng màu | OK |
| PK-03 Farm 9 con | 6af6caac-6538-83ec-bc2d-6b4330d96a85 | OK. Highland cow, bò sữa, heo, dê, cừu, gà, ngựa, lừa, vịt | OK |
| PK-04 Christmas 9 con | 6af6cd3d-d8f4-83ec-b3cc-8680dcd0cce1 | OK, 9 chữ đúng: Feral, Jolly, Unhinged, Sleigh, Chill, Merry, Moo-ry, Festive, Lit | OK (christmas_critters_dark_fabric_transparent.png) |
| PK-05 Cats 12 con | 6af6ce7c-c578-83ec-b613-5d5a93a94c5a | OK, 12 chữ đúng: Chaos, Void, Fancy, Spicy, Drama, Grumpy, Judging, Floof, Naked, Clingy, Tortitude, Chonk | OK (cat_bundle_dark_fabric_transparent.png) |
