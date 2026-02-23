# library_project

# 📚 Library Management System API

Build a robust and production-ready Library REST API using **Django** and **Django REST Framework (DRF)**. This project implements full CRUD operations, advanced filtering, and performance optimizations.

## 🎯 Features

- **Full CRUD**: Manage both Authors and Books with ease.
- **Advanced Filtering**: Combine multiple query parameters (price, date, availability, etc.) using Django ORM.
- **Dynamic Ordering**: Sort results by specific fields (e.g., price, date, surname).
- **Fault-Tolerant**: Global error handling ensures the API never crashes on invalid inputs.
- **Optimized Queries**: Uses `select_related` to eliminate N+1 query issues.
- **Advanced Extras**: 
    - **Pagination**: Results limited to 10 items per page.
    - **Caching**: 60-second cache for high-traffic endpoints.
    - **Statistics**: Aggregated insights via `/api/books/stats/`.

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd library-api

# Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies:
pip install django djangorestframework

# Prepare the database:
python manage.py migrate

# Launch the server:
python manage.py runserver

### 3. API Endpoints Cədvəli
```markdown
## 🌐 API Endpoints

### 📖 Books (`/api/books/`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/api/books/` | List all books (Supports filtering & ordering) |
| **POST** | `/api/books/` | Create a new book |
| **GET** | `/api/books/<id>/` | Retrieve specific book details |
| **PUT** | `/api/books/<id>/` | Fully update a book |
| **DELETE** | `/api/books/<id>/` | Remove a book from the library |
| **GET** | `/api/books/stats/` | **Bonus:** Get total books, available count, and avg price |

### ✍️ Authors (`/api/authors/`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/api/authors/` | List all authors |
| **POST** | `/api/authors/` | Register a new author |
| **GET** | `/api/authors/<id>/` | Retrieve author profile |
| **DELETE** | `/api/authors/<id>/` | Delete an author |

## 🔎 Filtering & Ordering Guide

### Books Filtering
- **By Author:** `?author_id=1`
- **By Availability:** `?is_available=true`
- **By Price:** `?min_price=20&max_price=100` (uses `price__gte` and `price__lte`)
- **By Year:** `?year=2024`
- **Search Title:** `?search=django` (uses `title__icontains`)

### Authors Filtering
- **By Country:** `?country=Germany`
- **By Birth Year:** `?birth_year=1980`

### ↕️ Ordering
- **Ascending:** `?ordering=price`
- **Descending:** `?ordering=-published_date`
- **Author Sort:** `?ordering=last_name`

## ⚠️ Requirements & Error Handling

- **Crash Prevention**: Invalid filters or ordering fields do not break the server.
- **Status Codes**: 
    - `200 OK` for success.
    - `201 Created` for successful POST.
    - `400 Bad Request` for invalid parameters.
    - `404 Not Found` for non-existent objects.
- **Empty Results**: Returns `[]` if no matches are found (Status 200).

## 🛠 Tech Stack
- **Framework**: Django 6.x
- **Toolkit**: Django REST Framework
- **Language**: Python 3.10+
- **Database**: SQLite (Development)