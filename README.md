# Pawventory-Django

A Django-based web application for managing a dog shop inventory and e-commerce transactions.

## Features
- **User Accounts:** Custom user registration, login, logout, and session-based user authentication.
- **Shop & Inventory:** Browse products by category, add/remove items to/from a shopping cart, and place orders.
- **Contact Form:** Contact submissions saved directly to the database.
- **REST Endpoints:** Basic JSON APIs to retrieve products and categories list.

## App Structure
- `Core` - Handles custom user registration, login, session management, and the homepage.
- `Shop` - Handles product catalog, shopping cart, order placement, and API endpoints.
- `Contact` - Simple contact form database model and views.
- `Pages` - Holds static views like the About Us page.

## Setup Instructions

### 1. Setup Environment
Ensure Python 3.10+ is installed.

```bash
# Clone the repository
git clone https://github.com/bhavyamotiyani/Pawventory-Django.git
cd Pawventory-Django

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows run: .venv\Scripts\activate
```

### 2. Install Django
```bash
pip install django
```

### 3. Database & Migrations
Run the migrations to create the database schemas:
```bash
python manage.py migrate
```

### 4. Create Superuser (Admin)
To manage products and categories via the Django Admin panel:
```bash
python manage.py createsuperuser
```

### 5. Run the Server
```bash
python manage.py runserver
```
Open `http://127.0.0.1:8000/` in your browser.

## API Endpoints
- **Get Products:** `GET /api/shop/products/`
- **Get Categories:** `GET /api/shop/categories/`
