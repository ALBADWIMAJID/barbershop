
# 💈 Barbershop Legend

A modern and elegant barbershop website built with Django. This platform allows customers to easily book appointments, explore services, and learn more about the barbershop's offerings and atmosphere.

🌐 **Live Demo**: [barbershop-7ncw.onrender.com](https://barbershop-7ncw.onrender.com)

---

## 🚀 Features

- ✅ **User Registration & Login**
- 📅 **Online Booking System** (Date & Time selection)
- ✂️ **Service Listing with Images, Prices, and Duration**
- 🌍 **Multilingual Support** (Arabic, English, Russian)
- 📷 **About Page with Real Images**
- 📬 **Contact Page**
- 🔐 **Admin Panel for managing bookings and content**
- 📱 **Responsive Design (Mobile-Friendly)**

---

## 🛠️ Tech Stack

- **Backend**: Django 4+
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (default, easily switchable)
- **Hosting**: [Render](https://render.com)
- **Language Support**: i18n via `gettext` and Django translations

---

## 📷 Screenshots

<img src="https://f1.dikidi.net/c4/v3497/37106hqbh7.jpg?size=m" width="400"/>

---

## 🔧 Installation

```bash
# Clone the repo
git clone https://github.com/ALBADWIMAJID/barbershop.git
cd barbershop

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver
```

---

## 🌐 Language Translation

To compile translation messages:

```bash
django-admin makemessages -l ar
django-admin compilemessages
```

All translation files are located in `locale/`.

---

## 📩 Contact

**Developer**: Majid Albadwi  
📧 Email: albadwimajid755@gmail.com  
🐙 GitHub: [@ALBADWIMAJID](https://github.com/ALBADWIMAJID)

---

## 📄 License

This project is licensed under the MIT License.
