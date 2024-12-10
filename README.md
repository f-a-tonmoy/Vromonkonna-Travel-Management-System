## 📝 Project Overview

**Vromonkonna** is a travel management platform that caters primarily to female travelers, ensuring a secure, user-friendly environment. The system provides travel package booking, hotel collaborations, travel blogs, and administrative controls. Designed with usability and security in mind, it supports users, hotels, and admins with tailored features.

---

## 📂 Project Structure

```plaintext
├── Vromonkonna/                    # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── blogs/                          # App for managing travel blogs
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── pkg/                            # Core app for travel package management
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── pkgbooking/                     # App for booking travel packages
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── users/                          # App for user authentication and profiles
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/                         # Static assets (CSS, JS, images)
├── templates/                      # HTML templates for rendering pages
├── manage.py                       # Django's CLI manager
├── db.sqlite3                      # SQLite database for development
```

---

## 🚀 Features

### For Female Travelers
- Browse and book travel packages.
- Share travel experiences through blogs.
- View hotel and tourist attraction details.
- Manage user profiles and travel history.
- Provide feedback and rate packages.

### For Hotel Representatives
- Register and manage hotel accounts.
- Add, update, or delete travel packages.
- View and organize bookings.
- Manage hotel information and track user feedback.

### For Admins
- Monitor the overall system via an admin dashboard.
- Evaluate user profiles and hotel statuses.
- Manage system-wide data and resolve issues.

---

## 💡 Motivation
The system is designed to address the specific challenges faced by women travelers in Bangladesh, ensuring their safety, convenience, and comfort while exploring new destinations.

---

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Framework**: Django
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite (development), MySQL (production-ready)
- **IDE**: PyCharm, VS Code

---

## 🔍 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/f-a-tonmoy/Vromonkonna-Travel-Management-System.git
   cd Vromonkonna-Travel-Management-System
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Access the application at:
   ```
   http://127.0.0.1:8000/
   ```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💬 Contact

For inquiries or feedback:
- **Fahim Ahamed (Tonmoy)**: [f.a.tonmoy00@gmail.com](mailto:f.a.tonmoy00@gmail.com)
- GitHub: [f-a-tonmoy](https://github.com/f-a-tonmoy)
```
