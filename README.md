# TradeFair Management System

📌 A FastAPI-based system under development to manage trade fairs, connecting organizers, exhibitors, and visitors on a single platform.

---

## 📖 About
This project aims to build a system that centralizes the management of trade fairs.  
It will allow organizers, exhibitors, and visitors to interact within a unified platform.

---

## ✅ Planned Features
- User management (organizers, exhibitors, visitors)  
- Stand management  
- Visitor and event registration  
- Participation reports  
- Different access profiles with authentication  

---

## 🛠️ Planned Technologies
- Python 3.12  
- FastAPI  
- SQLite (initial database, may evolve to PostgreSQL)  
- SQLAlchemy  

---

## 🚀 Status
📌 **In development** — this project is in the initial modeling and implementation phase.  

---

## Database Schema (Initial Subset)

### Entities
- **User** (base entity)
- **Role** (linked to User)
- **Client** (specialization of user)
- **Admin** (specialization of user)
- **Exhibitor** (specialization of user)
- **Product** (linked to exhibitor)
- **Tradefair** (main event entity)

### Intermediate Tables
- **admins_tradefairs** → admins that manage a tradefair
- **booth** → exhibitors that participate in a tradefair
- **attendance** → clients that attend a tradefair
---

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
