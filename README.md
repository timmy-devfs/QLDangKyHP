<<<<<<< HEAD
# QLDangKyHP
git clone https://github.com/timmy-devfs/QLDangKyHP.git
cd QLDangKyHP
npm install
copy .env.example .env
:: Mở .env và điền DB_PASSWORD + JWT_SECRET
=======
🌿 BICAP System

Blockchain Integration in Clean Agricultural Production

Hệ thống truy xuất nguồn gốc nông sản sạch tích hợp nền tảng Blockchain VeChainThor.

Học phần: Xây dựng phần mềm hướng đối tượng (OOAD) | Học kỳ: 2 — Năm học 2024–2025

📋 Mục lục

Kiến trúc tổng quan

Công nghệ sử dụng

Đội ngũ phát triển

Hướng dẫn cài đặt nhanh

Cấu trúc thư mục

Quy trình làm việc (Git)

🏗️ Kiến trúc tổng quan

Hệ thống được thiết kế theo kiến trúc Microservices hiện đại, đảm bảo tính đóng gói và khả năng mở rộng.

                     [ Client Layer: Web / Mobile ]
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  API Gateway :8080│ ◄─── JWT Auth (Identity Service)
                         └─────────┬─────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          ▼                        ▼                        ▼
    [ Identity :8081 ]      [ Farm :8082 ]           [ Retailer :8083 ]
    [ Shipping :8084 ]      [ Notify :8085 ]         [ Payment :8086 ]
    [ IoT :8087 ]           [ Report :8088 ]         [ Guest :8089 ]
    [ Blockchain :8090 ]    


Event Bus: Apache Kafka (Asynchronous Communication)

Cache: Redis (Performance Optimization)

Database: SQL Server 2022 (Persistence)

🛠️ Tech Stack

Thành phần

Công nghệ chính

Backend (10 Services)

Java 17 + Spring Boot 3.x

Blockchain Service

NodeJS 18 + TypeScript + VeChainThor SDK

Frontend Web

NextJS 14 (App Router) + TailwindCSS

Mobile App

React Native + Expo

Message Broker

Apache Kafka

Caching

Redis 7

Database

SQL Server 2022

DevOps / Infra

Docker + Docker Compose + Nginx

Data Pipeline

Apache NiFi

👥 Team

Role

Thành viên

Phụ trách chính

DEV-01

Team Lead

API Gateway, Identity Service, Web Admin

DEV-02

Backend Dev

Farm Service, IoT Service, Web Farm

DEV-03

Backend Dev

Retailer Service, Payment Service, Web Retailer

DEV-04

Backend Dev

Shipping Service, Report Service, Web Shipping, Web Public

DEV-05

Backend Dev

Blockchain Service, Notification Service, Guest Service, Mobile Driver

🚀 Quick Start

📋 Yêu cầu hệ thống

Docker Desktop (đã khởi chạy)

Git CLI

Java 17+ & NodeJS 18+ (cho môi trường local dev)

⚙️ Cài đặt & Khởi động

# 1. Clone source code
git clone https://github.com/timmy-devfs/bicap-system.git
cd bicap-system

# 2. Cấu hình biến môi trường
cp .env.example .env
# Chỉnh sửa .env để khớp với thông tin kết nối local

# 3. Khởi động hạ tầng (Infrastructure)
make up

# 4. Kiểm tra trạng thái các containers
make ps


🔗 Địa chỉ truy cập mặc định

Kafka Cluster: localhost:9092

Redis Cache: localhost:6379

SQL Server: localhost:1433

NiFi Dashboard: https://localhost:8443

📁 Cấu trúc dự án

bicap-system/
├── services/          # 11 Microservices (Java Spring & NodeJS)
├── contracts/         # Kafka Avro Schemas & OpenAPI Specification
├── frontend/          # 5 Web Apps & 2 Mobile Apps (Monorepo style)
├── infrastructure/    # Cấu hình Docker, Kafka, Redis, Nginx, NiFi
└── docs/              # Tài liệu phân tích thiết kế & HDSD


🌿 Branch Strategy

Chúng tôi tuân thủ quy trình Git Flow cơ bản để quản lý mã nguồn:

Nhánh

Mục đích

Chính sách

main

Production-ready

Bảo vệ nghiêm ngặt, chỉ nhận qua Pull Request

develop

Integration branch

Nơi tích hợp các tính năng mới

feature/BIC-xxx

Task-based branch

Mỗi tính năng/fix là một nhánh riêng

Luồng làm việc chuẩn:

# Cập nhật mã nguồn mới nhất
git checkout develop && git pull origin develop

# Tạo nhánh cho tính năng mới
git checkout -b feature/BIC-001-init-monorepo

# Sau khi hoàn tất: commit và push
git add .
git commit -m "feat: initialize project structure"
git push origin feature/BIC-001-init-monorepo

# Thực hiện Pull Request (PR) trên GitHub vào nhánh develop


© 2024 BICAP System Project - Một sản phẩm của sinh viên ngành Kỹ thuật Phần mềm.
>>>>>>> 62f43ad1dccfae203cc46be8617690d2387de668
