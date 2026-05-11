# 🌐 Network Tracker 🌐

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Async_API-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI_Server-222222?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active_Development-orange?style=for-the-badge)

A scalable network asset tracking and monitoring platform built with FastAPI and MongoDB.

</div>

---

# 📖 Overview 📖

Network Tracker is a backend-driven infrastructure management platform designed to track:

- Network sites
- Devices
- IP addresses
- Rack locations
- Device uptime
- Connectivity status

The project is designed to evolve into a full monitoring and visualization platform with:
- topology mapping
- historical uptime graphing
- outage tracking
- subnet discovery
- SNMP monitoring
- real-time device health
- geographic visualization

---

# ✨ Current Features ✨

## ✅ Site Management ✅
- Create sites
- Update sites
- Delete sites
- Retrieve individual sites
- Retrieve all sites

## ✅ Device Management ✅
- Create devices
- Update devices
- Delete devices
- Retrieve devices
- Link devices to sites

## ✅ Monitoring ✅
- Automated asynchronous ping checks
- Scheduled device polling
- Per-device online/offline status
- Ping success tracking
- Last checked timestamps

## ✅ Backend Architecture ✅
- FastAPI async backend
- MongoDB integration
- APIRouter route separation
- Pydantic response validation
- Background monitoring services
- Structured service architecture

---

# 🚀 Tech Stack 🚀

| Technology | Purpose |
|---|---|
| FastAPI | Backend API framework |
| MongoDB | Database |
| Motor | Async MongoDB driver |
| Pydantic | Validation & serialization |
| Uvicorn | ASGI server |
| Python AsyncIO | Background scheduling & async tasks |

---

# 🔌 API Endpoints 🔌

## 🌐 Sites 🌐

| Method | Endpoint |
|---|---|
| GET | `/sites` |
| GET | `/sites/{site_id}` |
| POST | `/sites` |
| PUT | `/sites/{site_id}` |
| DELETE | `/sites/{site_id}` |

---

## 💻 Devices 💻

| Method | Endpoint |
|---|---|
| GET | `/devices` |
| GET | `/devices/{device_id}` |
| GET | `/sites/{site_id}/devices` |
| POST | `/devices` |
| PUT | `/devices/{device_id}` |
| DELETE | `/devices/{device_id}` |

---

# 📡 Monitoring System 📡

The backend includes a background monitoring service that:

- Periodically pings known devices
- Updates connectivity state
- Tracks successful ping attempts
- Stores last-known status

Future improvements include:
- latency tracking
- packet loss
- uptime percentages
- historical graphing
- outage detection
- notification systems

---

# 🛠️ Local Development 🛠️

## 📥 Clone Repository 📥

```bash
git clone git@github.com:YOUR_USERNAME/network-tracker.git
cd network-tracker