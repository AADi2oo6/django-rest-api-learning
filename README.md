# 📘 Django REST API Learning Journey  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python) ![Django](https://img.shields.io/badge/Django-4.x-green?logo=django) ![DRF](https://img.shields.io/badge/DRF-3.x-red?logo=django)  ![License](https://img.shields.io/badge/License-MIT-yellow?logo=open-source-initiative) ![GitHub repo size](https://img.shields.io/github/repo-size/AADi2oo6/django-rest-api-learning) ![GitHub last commit](https://img.shields.io/github/last-commit/AADi2oo6/django-rest-api-learning)  

---

Welcome to my **Django REST Framework (DRF)** learning repository! 🚀  
This repo holds my code experiments, projects, and exercises as I explore Django REST API.  

---

## 📝 Learning Notes  

I’m maintaining all my **detailed notes, explanations, and summaries** in **Notion** for better organization.  

👉 [Check out my Notion Notes here](https://www.notion.so/Django-REST-API-Learning-Template-f11a2c45ba994632860f5c248f978841?source=copy_link)  

---

## 📂 Project Structure  

Here’s the current structure of my project:  

```
django-rest-api-learning/
├── backend/                # Main backend folder
│   ├── api/                # Django app for APIs
│   │   ├── migrations/     # Database migrations
│   │   ├── admin.py        # Admin panel config
│   │   ├── apps.py         # App configuration
│   │   ├── models.py       # Database models
│   │   ├── tests.py        # Unit tests
│   │   ├── urls.py         # API URLs
│   │   └── views.py        # API views (logic)
│   │
│   ├── cfehome/            # Main Django project
│   │   ├── settings.py     # Project settings
│   │   ├── urls.py         # Root URL configs
│   │   ├── wsgi.py         # WSGI config
│   │   └── asgi.py         # ASGI config
│   │
│   ├── db.sqlite3          # SQLite database (dev only)
│   └── manage.py           # Django management script
│
├── py_client/              # Python client for testing APIs
│   ├── basic.py
│   └── basic1.py
│
├── venv/                   # Virtual environment (ignored in git)
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

---

## 🚀 Quick Start  

Follow these steps to run the project locally:  

```bash
# Clone the repository
git clone https://github.com/your-username/django-rest-api-learning.git
cd django-rest-api-learning

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Server will be available at 👉 `http://127.0.0.1:8000/`  

---

## 📈 Progress Tracker  

- [x] Setup GitHub repo ✅  
- [x] Installed Django & Django REST Framework ✅  
- [ ] Build first API endpoint 🔄  
- [ ] Learn about Serializers  
- [ ] Learn about ViewSets & Routers  
- [ ] Authentication & Permissions  
- [ ] API Documentation with Swagger/OpenAPI  

---

## 🎯 Goal  

By the end of this journey, I want to be confident in:  
- Building REST APIs with Django REST Framework  
- Handling authentication & permissions  
- Designing clean, maintainable API projects  
- Documenting APIs with Swagger/OpenAPI  

---

⭐ If you’re also learning DRF, feel free to follow along or fork this repo!  
