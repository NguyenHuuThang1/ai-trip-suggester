Cấu trúc dự án:
backend-python/ — FastAPI server cung cấp API gợi ý dựa trên mô hình embedding
backend-springboot/ — Spring Boot backend trung gian, nhận request từ frontend và gọi FastAPI
frontend-react/ — Ứng dụng ReactJS giao diện người dùng

Yêu cầu cài đặt:
Python 3.8+ (cho FastAPI)
Java 11+ và Maven (cho Spring Boot)
Node.js + npm (cho ReactJS)
Virtual environment cho Python

1. Chuẩn bị FastAPI backend(cd tripassistant-FE+Model): chạy lệnh : uvicorn main:app --reload 
2. Chuẩn bị Spring Boot backend(cd tripassistant-BE): chạy lệnh mvn spring-boot:run
3. Chuẩn bị React frontend(cd tripassistant-FE+Model/frontend-react): chạy lệnh: npm run dev
