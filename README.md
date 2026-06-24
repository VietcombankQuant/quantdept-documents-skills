# Skill: Lập & rà soát văn bản / trang trình chiếu cho Phòng Quant (Vietcombank)

Skill dành cho agent Claude (và các agent khác hỗ trợ định dạng skill) giúp
**tạo, chỉnh sửa và rà soát** văn bản hành chính tiếng Việt (tờ trình, báo cáo,
giải trình, công văn, thư điện tử) và trang trình chiếu PowerPoint cho **Phòng Mô
hình và công cụ quản trị rủi ro (Phòng Quant), Vietcombank**.

Skill chuẩn hoá kết quả đầu ra theo hai bộ quy tắc đã được phê duyệt:

- **Văn phong hành chính - chính luận** — loại bỏ văn nói, lượng từ mơ hồ, trộn
  lẫn Anh - Việt; trích dẫn quy định Basel/EBA/ECB/NHNN đúng chuẩn; cấu trúc
  luận điểm → luận cứ → kết luận.
- **Nhận diện thương hiệu Vietcombank** — bảng mầu, biểu trưng, định dạng trang
  trình chiếu.

> Tệp README này là ghi chú dành cho **người bảo trì skill**, không phải nội
> dung agent đọc. Hướng dẫn mà agent thực thi nằm trong [`SKILL.md`](SKILL.md).

## Cách cài đặt / sử dụng

### Trên Claude Code (dòng lệnh)

Sao chép thư mục này vào thư mục skill của Claude (ví dụ `~/.claude/skills/`),
giữ nguyên tên thư mục `quantdept-documents-skills`:

```bash
cp -r quantdept-documents-skills ~/.claude/skills/
```

### Trên Claude Web (claude.ai)

Nén toàn bộ thư mục skill (giữ `SKILL.md` ở thư mục gốc của tệp nén) thành một
tệp `.zip`:

```bash
zip -r quantdept-documents-skills.zip quantdept-documents-skills
```

Sau đó mở **claude.ai**, vào **Cài đặt** (Settings) → **Năng lực**
(Capabilities) → mục **Kỹ năng** (Skills) rồi tải tệp `.zip` vừa nén lên. Bạn
cũng có thể gắn skill vào một **Dự án** (Project) để dùng lại cho nhiều cuộc trò
chuyện.

### Sau khi cài đặt

Ở cả hai môi trường, agent sẽ tự nhận diện và gọi skill khi người dùng yêu cầu
soạn / viết / biên tập / rà soát văn bản, tờ trình, báo cáo, thư điện tử, trang
trình chiếu, hoặc kiểm tra văn phong, định dạng, mầu thương hiệu (xem phần mô tả
trong [`SKILL.md`](SKILL.md) để biết đầy đủ các từ khoá kích hoạt).

## Bố cục thư mục

```plaintext
quantdept-documents-skills/
├── SKILL.md                 # Bắt buộc. Phần khai báo đầu tệp (tên + mô tả) và hướng dẫn cho agent.
├── README.md                # Tệp này — ghi chú cho người bảo trì.
├── references/              # Tài liệu chi tiết, agent đọc khi cần (đọc dần để giảm tải).
│   ├── quy-tac-van-ban.md   # Bộ quy tắc văn phong + danh mục tự rà soát 15 điểm + bảng viết tắt.
│   └── quy-tac-mau-sac.md   # Bảng mầu thương hiệu, mầu theo mục đích, hướng dẫn chọn biểu trưng.
├── assets/                  # Mẫu, biểu trưng, tài nguyên dùng kèm.
│   ├── Slide mẫu Phòng Quant.pptx   # Mẫu PowerPoint 16:9, 17 bố cục có sẵn ô giữ chỗ.
│   └── logo-vietcombank/    # 11 biến thể biểu trưng chính thức (xanh/trắng/đen/vàng, có/không khẩu hiệu, ngang/dọc).
└── scripts/
    └── validate.py          # Kiểm tra SKILL.md hợp lệ (tên + mô tả).
```

## Kiểm tra

Chạy đoạn lệnh sau để kiểm tra phần khai báo đầu tệp của SKILL.md đúng quy ước:

```bash
python scripts/validate.py
```

Đoạn lệnh xác nhận SKILL.md có phần khai báo đầu tệp, có tên skill đúng định dạng
(chữ thường - số - gạch nối, không quá 64 ký tự) và phần mô tả không quá 1024 ký
tự.

## Nguyên tắc thiết kế skill

- **Đọc dần khi cần.** `SKILL.md` giữ ngắn gọn; đẩy chi tiết sang `references/`
  và để agent chỉ đọc phần cần dùng.
- **Mã nguồn nằm trong tệp, không nằm trong lời văn.** Đặt đoạn lệnh trong
  `scripts/` thay vì dán khối mã lớn vào `SKILL.md`.
- **Phần mô tả quyết định việc định tuyến.** Viết bằng đúng những từ người dùng
  sẽ nói, ghi rõ *khi nào* dùng skill.
- **Một skill, một nhiệm vụ.**

## Quy tắc đặt tên (đa số trình nạp bắt buộc)

- **Tên thư mục** — chữ thường, chữ số, gạch nối.
- **Tên skill** — trùng tên thư mục, không quá 64 ký tự.
- **Phần mô tả** — không quá 1024 ký tự, viết ở ngôi thứ ba, nêu rõ điều kiện
  kích hoạt.
