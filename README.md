# 🍔 Smart Web-Based Online Food Ordering System

A full-stack, intelligent web application built with **Django** and **Machine Learning** that provides a seamless food ordering experience for Customers, Restaurants, and Administrators.

---

## 🌟 Key Features

### 👤 Multi-Role Architecture
- **Customer / User**: Browse menu items, add to cart, place orders, track order status in real time, and submit restaurant reviews.
- **Restaurant Manager**: Manage food categories, add/update menu items with images, set availability, and manage incoming orders.
- **Administrator**: Oversee platform activities, users, restaurants, and system operations.

### 🤖 Machine Learning Recommendation System
- Built-in collaborative filtering engine using **Cosine Similarity** (`scikit-learn` & `pandas`).
- Dynamically analyzes user order history to suggest personalized food items to customers.

### 🛒 Ordering & Cart Management
- Dynamic shopping cart with real-time quantity adjustments and total calculation.
- Comprehensive order lifecycle tracking: `Pending` $\rightarrow$ `Preparing` $\rightarrow$ `Out for Delivery` $\rightarrow$ `Delivered` / `Cancelled`.

### ⭐ Feedback & Ratings
- Customers can leave ratings (1–5 stars) and detailed reviews for restaurants.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.11+, Django 4.2
- **Machine Learning**: Pandas, Scikit-learn, NumPy
- **Static Assets**: WhiteNoise
- **WSGI / Web Server**: Gunicorn (Render) / Serverless Python (Vercel)
- **Database**: PostgreSQL / MySQL / SQLite
- **Deployment**: Vercel & Render Ready

---

## 📁 Project Structure

```text
food_delivery_project/
├── mainapp/                  # Primary Django application module
│   ├── ml/                   # Machine learning recommendation logic
│   │   └── recommendation.py
│   ├── models.py             # User, FoodItem, Cart, Order, Feedback models
│   ├── views.py              # Application views & controllers
│   ├── urls.py               # Application routing
│   └── templates/            # HTML UI templates
├── food_delivery_project/    # Project configuration & settings
│   ├── settings.py           # Production & development settings
│   ├── urls.py               # Root URL configuration
│   └── wsgi.py               # WSGI entry point
├── static/                   # Static CSS / JS assets
├── media/                    # Uploaded food item images
├── build_files.sh            # Vercel build script
├── build.sh                  # Render build script
├── Procfile                  # Process manager config
├── render.yaml               # Render Blueprint config
├── vercel.json               # Vercel deployment config
├── requirements.txt          # Python dependencies
└── manage.py                 # Django management CLI
```

---

## 🚀 Local Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/meg-hana0507/Smart_Web_Based_Online_Food_Ordering_System.git
cd Smart_Web_Based_Online_Food_Ordering_System
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 6. Start Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` in your web browser.

---

## ⚡ Deployment Options

### 📐 Vercel (Instant UI Deployment)
1. Import repository on [Vercel](https://vercel.com/).
2. Keep Framework Preset as **Other**.
3. Click **Deploy**. Vercel will automatically use `vercel.json` and deploy instantly.

### 🔷 Render Deployment
1. Connect repository on [Render](https://render.com/).
2. Select **Blueprint** deployment using `render.yaml` or create a **Web Service** with build command `./build.sh` and start command `gunicorn food_delivery_project.wsgi:application`.

---

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.
