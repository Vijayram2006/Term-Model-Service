# Term Model Service

A backend REST API built using FastAPI and PostgreSQL to manage terms,
their selfsame identifiers, and synonyms.

---

## Features
- CRUD operations for Terms
- Term Selfsame & Synonym management
- Input validation and error handling
- Safe delete with foreign key handling
- Pagination and filtering
- Automated tests

---

## Tech Stack
- Python
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Docker
- Pytest

---

## Project Structure
term-model-service/
│
├── app/
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   ├── dependencies.py
│   │
│   └── routers/
│       ├── auth.py
│       ├── terms.py
│       ├── term_selfsame.py
│       └── term_synonym.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

---> Architecture Diagram (Logical);

Client (Browser / Swagger / App)
        |
        | HTTP / JSON
        v
FastAPI Application (Term Model Service)
        |
        | SQLAlchemy ORM
        v
PostgreSQL Database
              ----------

-->> Security Architecture;

User → Login → JWT Token → API Calls → Token Verified

              --------------

---->>> Deployment Architecture (Cloud);

User
 ↓
Google Cloud Run (Container)
 ↓
Cloud SQL (PostgreSQL)              
                   ---------

                   
                   
![alt text](<solution architecture image format.png>)