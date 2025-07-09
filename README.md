# SE334.P22---Cinestream
Đồ án SE334.P22 của nhóm chủ đề số 3:
                                      23520582-Võ Phi Hùng. 
                                      21521657-Trần Khiết Tường.
# CINESTREAM - Ứng dụng đặt vé xem phim
*Hệ thống đặt vé xem phim đa nền tảng*

CINESTREAM cho phép người xem phim duyệt lịch chiếu, chọn chỗ ngồi và thanh toán an toàn từ ứng dụng Android trong khi nhân viên rạp chiếu phim quản lý phim, lịch chiếu và doanh số bán hàng thông qua cổng thông tin quản trị.
Giải pháp được chia thành **Python + Flask REST API** (có MySQL) và **ứng dụng khách Android (Java)** gốc, do đó bạn có thể chạy máy chủ ở bất kỳ đâu và trỏ nhiều ứng dụng đến đó.

---
## ✨ Các tính năng chính
| Dành cho người dùng | Dành cho quản trị viên |
|-------------|--------------|
| 🔍 Tìm kiếm & lọc phim theo thể loại, ngày và rạp chiếu phim | 🎞️ Phim CRUD, lịch chiếu & phòng chiếu |
| 🪑 Logic chọn chỗ ngồi & giữ chỗ theo thời gian thực | 🎫 Xem, xác nhận hoặc hủy đặt chỗ |
| 💳 Luồng đặt chỗ & thanh toán trong ứng dụng | 📊 Bảng thông tin doanh thu hàng ngày |
| 📜 Lịch sử đơn hàng & vé điện tử | 👤 Tài khoản theo vai trò (quản trị viên/người dùng) |

---
📋 Yêu cầu
Trước khi bắt đầu, hãy đảm bảo rằng bạn đã cài đặt những phần mềm sau trên hệ thống của mình:

## Java Development Kit (JDK)

Phiên bản bắt buộc: JDK 17 hoặc JDK 21

Tải xuống: Oracle JDK hoặc OpenJDK

## Python

Phiên bản bắt buộc: Python 3.12 hoặc Python 3.13

Tải xuống: Tải xuống Python

🔍 Xác minh cài đặt
Kiểm tra phiên bản đã cài đặt của bạn:

```bash
java --version
python --version
```
## 📦 Cài đặt & thiết lập dự án
1️⃣ Sao chép dự án

```bash
git clone https://github.com/huypro2005/se114_nmdd.git
```

🖥️ Thiết lập phần phụ trợ (Python)
➡️ Tạo và kích hoạt môi trường ảo

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

➡️ Cài đặt Dependencies
```bash
cd backend_python
pip install -r requirements.txt
```

➡️ Cấu hình Biến môi trường
Chỉnh sửa tệp ./backend_python/.env và cập nhật các giá trị sau:
```bash
KEY='restfull_api'
DB_HOST={HOST}
DB_PORT={PORT}
DB_USER={USER}
DB_PASSWORD={PASSWORD}
DB_NAME='firmmanagement'
```

📌 Thay thế {HOST}, {PORT}, {USER}, {PASSWORD} bằng thông tin kết nối MySQL thực tế của bạn.

➡️ Tạo Cơ sở dữ liệu trong MySQL
Mở máy khách MySQL của bạn và chạy:
```bash
CREATE DATABASE firmmanagement;
```

Sau đó nhập dữ liệu từ tệp backup_data.sql được cung cấp.

➡️ Chạy Backend Server

```bash
cd backend_python
python run.py
```

✅ Nếu thành công, bạn sẽ thấy:
```bash
Checking if database tables exist...
Database tables created successfully.
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.8:5000
Press CTRL+C to quit
 * Debugger is active!
```

📱 Thiết lập giao diện người dùng (Android)
➡️ Mở dự án
Mở thư mục frontend_java trong Android Studio.

➡️ Cấu hình URL Backend
Chỉnh sửa tệp frontend_java/local.properties và thêm:

```bash
BASE_URL=http://192.168.1.8:5000
```

📌 Đảm bảo thay thế 192.168.1.8 bằng địa chỉ IP cục bộ thực tế của bạn (cùng IP nơi backend đang chạy).

## Tài khoản
```bash
- Người dùng:

tên người dùng: người dùng
mật khẩu: 123456

- Quản trị viên
tên người dùng: quản trị viên
mật khẩu: quản trị viên
```

✅ Lưu ý
Đảm bảo cơ sở dữ liệu được tạo trước khi chạy backend.

Backend này sử dụng máy chủ phát triển Flask — để sử dụng trong sản xuất, hãy cân nhắc triển khai với máy chủ WSGI như gunicorn hoặc uWSGI.

Frontend được xây dựng bằng Java + Android Studio.
