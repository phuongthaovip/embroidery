# Lessons — cái chạy / cái không

> Mỗi bài học có ngày + nguồn. Mới thêm lên đầu mục. Số "sold" từ extension là ước tính.

## Sản phẩm & thị trường
- **80% listing không bán; top 10 = 75% doanh số** (Paola, 565 listing, 2026-10-17) → lọc idea mạnh trước khi list, không chỉ sinh nhiều. `01-research/2026-10-17-shop-competitor-analysis.md`
- **Bundle = 23% listing nhưng 56% doanh số** (Paola). Đối thủ bán mega bundle $13–17; mình giữ ≤20 mẫu vì sức designer. (nguồn trên)
- **Winner của Paola**: preppy/coastal animal bundle (fish TB 24.4 sold/listing), frog, funny + con vật, ITH bag charm/bag tie. Công thức nên nhân bản. (nguồn trên)
- **Christian/faith = 19–30% doanh số của 3 đối thủ**, Paola 0% → khoảng trống lớn. (nguồn trên)
- **Font/monogram = 66% doanh số KVFlorida** — Paola 0%. (nguồn trên)
- **Mahjong yếu hơn cảm nhận** ở Paola: 50 listing → 104 sold, gần hết từ 1 mẫu (2026-10-17). Anh vẫn bật lại 2026-10-24 → cần đo lại kết quả các lô Mahjong `[?]`.
- **Christmas/Halloween/Easter/Thanksgiving của Paola rất thấp** (≤0.5 sold/listing) mùa trước — có thể do shop mới mở. Xem lại sau tháng 12. (nguồn trên)
- Người mua file thêu mua **sớm hơn 2–4 tuần** so với người mua quà làm sẵn; Christmas file bán mạnh tới ~10–15/12; Valentine nên list trước ~15/12. `01-research/2026-11-12-holiday-calendar.md`
- Valentine: tim mini/scallop bán nhiều nhưng rẻ; love letter, coquette bow, con vật + tim, đồ trẻ em là cụm rõ; faith/coastal/ITH Valentine còn trống (2026-11-21). `01-research/2026-11-21-valentine-competitor-scan.md`
- Niche sởi/vaccine: có cầu nhỏ, file thêu gần như trống, nhưng rủi ro chính trị/y tế/IP; anh đã dừng lô (2026-11-13). `01-research/2026-11-13-measles-vaccine-niche.md`

## Công cụ & quy trình
- **Gavana "List / Create batch" hỏng**: crash khi nhập prompt, batch ra ảnh sai prompt (2026-10-18). Gen từng node một. `CLAUDE.md` §6
- Gavana phụ thuộc máy H Mac online; thực tế chuyển sang ChatGPT project Thaonie từ 2026-10-26, chạy 3 tab song song không treo (2026-11-17).
- **Etsy chặn quét nhanh** (429 / trang kiểm tra bot): ≤4 trang/lượt, nghỉ giữa lượt; Etsy chặn WebFetch (403) → dùng Chrome. `CLAUDE.md` §4b
- YTrends/EverBee dữ liệu embroidery rất mỏng (2–8 listing/keyword); EverBee về gói Hobby từ 2026-11-11 → nguồn chính là quét Etsy + HeyEtsy.
- **Amazon Merch** quét Newest từng trang: tốn công, 0 kết quả, bị chặn 3 lần (2026-10-22) → dùng Hot New Releases.
- AI hay viết sai chính tả chữ trên ảnh → luôn kiểm trước khi list. `templates/image-prompt.md`
- Magnific "expand" ảnh hero vẽ thêm máy thêu thứ 2 (2026-11-20) → kiểm kỹ ảnh mở rộng.
- Shopify MCP: không sửa được Policies (thiếu quyền), chặn bulk mutation → dán tay / Chrome cho policy, Shopify CLI `store execute` cho việc hàng loạt (2026-11-20/21).
- WebP 1000px q80: ảnh 3.3–3.7 MB → 254–277 KB (~92% nhẹ hơn) (2026-11-21). `00-context/shopify-listing-standard.md`
- Mã card không phải keyword → tên file ảnh/handle theo title, không theo mã (2026-11-21).
- Link menu tới collection trống làm store nhìn rỗng → chỉ hiện collection có sản phẩm (2026-11-21).

## Store
- Store lớn (Urban Threads, Emb Library, JuJu, Kara): hero là mẫu thêu/ưu đãi, chữ "machine embroidery" khắp nơi, menu theo cách khách tìm (ITH, hoop size, mùa), mẫu free đổi email (2026-11-20). `01-research/2026-11-20-store-design-benchmark.md`
- Có traffic mà không có cổng thanh toán = 0 đơn (66 sessions, 0 orders, 30 ngày tới 2026-11-21). `brain/metrics/2026-11-21.md`
