SQL Injection Detection using NLP & Streamlit
Dự án này là một ứng dụng web được xây dựng bằng Streamlit, sử dụng mô hình học máy (Machine Learning) và Xử lý ngôn ngữ tự nhiên (NLP) để phát hiện các cuộc tấn công SQL Injection. Người dùng có thể nhập một chuỗi truy vấn, và ứng dụng sẽ dự đoán xem chuỗi đó có độc hại hay không.

Đây là sản phẩm của đồ án môn học An toàn Máy tính (CT201H) tại Trường Đại học Cần Thơ.

✨ Tính năng
Phân tích thời gian thực: Phân tích các chuỗi truy vấn do người dùng nhập vào ngay lập tức.

Mô hình NLP: Sử dụng TF-IDF và Logistic Regression để phân loại văn bản.

Giao diện trực quan: Giao diện người dùng đơn giản, sạch sẽ được xây dựng bằng Streamlit.

Hiển thị kết quả rõ ràng: Kết quả được hiển thị với màu sắc (Đỏ cho độc hại, Xanh cho an toàn) và điểm tin cậy của mô hình.

Dễ dàng triển khai: Có thể được triển khai dễ dàng lên Streamlit Community Cloud.

🚀 Demo
Dưới đây là giao diện của ứng dụng khi phân tích các loại truy vấn khác nhau.

Trường hợp 1: Phát hiện truy vấn độc hại (Malicious)

Trường hợp 2: Xác nhận truy vấn an toàn (Benign)

🛠️ Cài đặt và Chạy cục bộ
Để chạy dự án này trên máy của bạn, hãy làm theo các bước sau.

1. Yêu cầu
Python 3.8+

Git

2. Cài đặt
a. Clone repository:
Mở terminal và chạy lệnh sau để sao chép mã nguồn về máy:

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

b. Tạo và kích hoạt môi trường ảo:
Môi trường ảo giúp quản lý các thư viện của dự án một cách độc lập.

# Tạo môi trường ảo
python -m venv .venv

# Kích hoạt môi trường ảo (trên Windows)
.\.venv\Scripts\activate

# Kích hoạt môi trường ảo (trên macOS/Linux)
# source .venv/bin/activate

c. Cài đặt các thư viện cần thiết:
Cài đặt tất cả các gói phụ thuộc từ file requirements.txt.

pip install -r requirements.txt

📈 Sử dụng
Dự án bao gồm hai kịch bản chính: huấn luyện mô hình và chạy ứng dụng.

1. Huấn luyện mô hình (Tùy chọn)
Mô hình đã được huấn luyện và lưu sẵn trong thư mục model/. Tuy nhiên, nếu bạn muốn huấn luyện lại mô hình với dữ liệu mới, hãy chạy lệnh sau:

python train.py

Lệnh này sẽ:

Đọc dữ liệu từ data/sqli_dataset.csv.

Xử lý, làm sạch dữ liệu.

Huấn luyện một mô hình Logistic Regression mới.

Lưu mô hình và vectorizer đã huấn luyện vào thư mục model/.

2. Chạy ứng dụng Web
Để khởi chạy giao diện web, hãy chạy lệnh sau:

streamlit run app.py

Một tab mới trên trình duyệt sẽ tự động mở ra, hiển thị ứng dụng của bạn. Bây giờ bạn có thể nhập các truy vấn để kiểm tra.

📂 Cấu trúc thư mục
.
├── data/
│   └── sqli_dataset.csv      # Tập dữ liệu dùng để huấn luyện
├── model/
│   ├── model.pkl             # File mô hình đã huấn luyện
│   └── vectorizer.pkl        # File vectorizer TF-IDF đã lưu
├── .venv/                      # Thư mục môi trường ảo
├── app.py                      # Mã nguồn ứng dụng Streamlit
├── train.py                    # Kịch bản để huấn luyện mô hình
├── requirements.txt            # Danh sách các thư viện cần thiết
└── README.md                   # File hướng dẫn này

💻 Công nghệ sử dụng
Python: Ngôn ngữ lập trình chính.

Scikit-learn: Dùng để xây dựng và huấn luyện mô hình Logistic Regression.

Pandas: Dùng để xử lý và thao tác dữ liệu.

NLTK: Dùng để xử lý ngôn ngữ tự nhiên (ví dụ: loại bỏ stopword).

Streamlit: Dùng để xây dựng giao diện web tương tác.

Joblib: Dùng để lưu và tải mô hình đã huấn luyện.

🙏 Lời cảm ơn
Dự án này được phát triển dựa trên ý tưởng và tập dữ liệu từ repository SQL-Injection-Detection-Using-Machine-Learning-for-NLP của tác giả Shaffaprawira.
