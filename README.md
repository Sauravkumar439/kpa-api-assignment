# KPA API Assignment – Django REST Framework

This project implements two RESTful APIs as per the KPA assignment requirements:

1. **POST /api/user/login/** – Login using phone number and password  
2. **POST /api/kpa/form_data/** – Submit a KPA form (requires authentication)

## Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- PostgreSQL
- Token Authentication (DRF built-in)


## API Credentials for Testing

Use the following credentials (provided in assignment):

Phone number: 7760873976
Password: to_share@123


---

## Installation & Setup

### 1. Clone the repo & activate virtual environment

git clone https://github.com/Sauravkumar439/kpa-api-assignment.git
cd kpa-api-assignment
python -m venv venv
venv\Scripts\activate  # For Windows

### 2. Install dependencies

pip install -r requirements.txt

### 3. Configure PostgreSQL

Create a PostgreSQL database called kpa_db and update this in core/settings.py:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kpa_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


### 4. Run migrations and create superuser

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 5. Start the development server

python manage.py runserver

### API Endpoints

POST /api/user/login/

### Request Body:

    json
    Copy
    Edit
    {
    "phone_number": "7760873976",
    "password": "to_share@123"
    }


### Response:

{
  "token": "your_token_here"
}


### POST /api/kpa/form_data/
### Headers:

pgsql
Copy
Edit
Authorization: Token your_token_here
Content-Type: application/json

### Request Body:

json
Copy
Edit
{
  "department": "Engineering",
  "kpa_title": "Performance and Delivery",
  "score": 9
}

### Response:

json
Copy
Edit
{
  "id": 1,
  "user": 1,
  "department": "Engineering",
  "kpa_title": "Performance and Delivery",
  "score": 9,
  "created_at": "2025-07-12T16:41:09.928087Z"
}

### Postman Collection

Included in the repository as:
kpa_assignment.postman_collection.json

### Video Demo
Watch the screen recording demo here:
Project Demo – https://drive.google.com/file/d/1fWCjWmMKWu9s8JCs-tI_H7Ht7chqhn62/view?usp=sharing
