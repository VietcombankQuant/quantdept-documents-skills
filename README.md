# Skill: Lập & rà soát văn bản / trang trình chiếu cho Phòng Quant (Vietcombank)

Đây là một skill dành cho Claude (và các agent hỗ trợ định dạng skill tương tự). Skill này giúp agent soạn thảo, chỉnh sửa và kiểm tra văn bản hành chính tiếng Việt — tờ trình, báo cáo, giải trình, công văn, thư điện tử — cũng như trang trình chiếu PowerPoint cho Phòng Mô hình và Công cụ Quản trị Rủi ro (Phòng Quant), Vietcombank.

Kết quả đầu ra được chuẩn hoá theo hai tiêu chí:

- **Văn phong hành chính - chính luận**: không dùng văn nói, không dùng từ mơ hồ kiểu "có thể", "hơi hơi"; không trộn tiếng Anh tuỳ tiện; trích dẫn quy định Basel / EBA / ECB / NHNN đúng chuẩn; bố cục rõ ràng theo luận điểm → luận cứ → kết luận.
- **Nhận diện thương hiệu Vietcombank**: bảng màu chính thức, cách dùng biểu trưng, và định dạng slide chuẩn của ngân hàng.

> File README này là ghi chú cho **người bảo trì skill**, không phải nội dung agent đọc. Hướng dẫn agent thực thi nằm trong [`SKILL.md`](SKILL.md).

## Cài đặt & sử dụng

### Với Claude Code (dòng lệnh)

Copy nguyên thư mục skill vào thư mục skills của Claude (thường là `~/.claude/skills/`). Để tên thư mục đúng nguyên `quantdept-documents-skills`:

```bash
cp -r quantdept-documents-skills ~/.claude/skills/
```

### Với Claude Web (claude.ai)

Tải file `.zip` từ trang GitHub của repo này: vào **Code** → **Download ZIP**. Sau đó mở **claude.ai** → **Settings** → **Capabilities** → **Skills**, upload file vừa tải lên. Người dùng có thể gắn skill vào một **Project** để dùng lại cho nhiều hội thoại khác nhau.

### Sau khi cài

Agent sẽ tự nhận biết và gọi skill khi người dùng yêu cầu soạn, sửa, hay kiểm tra văn bản, tờ trình, báo cáo, email, slide, hoặc kiểm tra văn phong / màu thương hiệu. Xem thêm danh sách từ khoá kích hoạt trong [`SKILL.md`](SKILL.md).

## Cấu trúc thư mục

```plaintext
quantdept-documents-skills/
├── SKILL.md                 # Bắt buộc. Chứa tên skill, mô tả, và hướng dẫn agent.
├── README.md                # File này — ghi chú cho người bảo trì.
├── references/              # Tài liệu chi tiết, agent load khi cần.
│   ├── quy-tac-van-ban.md       # Quy tắc văn phong + checklist 15 điểm + bảng viết tắt.
│   ├── quy-tac-viet-to-trinh.md # Cấu trúc & bố cục tờ trình + checklist 12 điểm.
│   ├── quy-tac-lam-slide.md     # Quy tắc làm slide + checklist 12 điểm.
│   └── quy-tac-mau-sac.md       # Bảng màu thương hiệu, màu theo mục đích, cách chọn logo.
├── assets/                  # Mẫu slide, logo.
│   ├── Slide mẫu Phòng Quant - Mẫu khách hàng thông thường.pptx   # Mẫu cho khách hàng phổ thông.
│   ├── Slide mẫu Phòng Quant - Mẫu khách hàng cao cấp (priority).pptx   # Mẫu cho khách hàng cao cấp / ưu tiên.
│   └── logo-vietcombank/    # 11 biến thể logo chính thức (xanh/trắng/đen/vàng, có/không slogan, ngang/dọc).
└── scripts/
    └── validate.py          # Script kiểm tra format SKILL.md.
```

## Kiểm tra

```bash
python scripts/validate.py
```

Script này xác nhận `SKILL.md` có phần khai báo đầu file đúng chuẩn — tên skill đúng định dạng (chữ thường, số, gạch nối, tối đa 64 ký tự) và mô tả không quá 1024 ký tự.

## Triết lý thiết kế

- **Load dần khi cần.** `SKILL.md` giữ ngắn; chi tiết nằm trong `references/`, agent chỉ đọc phần liên quan đến việc đang làm.
- **Code ở trong file script, không phải trong văn bản skill.** Mọi logic cho vào `scripts/` thay vì nhồi code block dài vào `SKILL.md`.
- **Mô tả điều kiện skill được sử dụng** Viết bằng đúng từ ngữ người dùng sẽ nói, và nói rõ *khi nào* thì dùng skill.

## Quy ước đặt tên (hầu hết loader đều yêu cầu)

- **Tên thư mục**: chữ thường, số, gạch nối.
- **Tên skill**: trùng tên thư mục, tối đa 64 ký tự.
- **Mô tả skill**: tối đa 1024 ký tự, viết ở ngôi thứ ba, mô tả rõ điều kiện kích hoạt.
