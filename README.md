# Flask User Management Mini-Project

This mini-project is a **simple sketchy user management system** built using **Flask**. It took just a few hours to put together, but the lessons learned during the process are valuable—especially for anyone transitioning from raw mechanical programming to structured software engineering.

---

## 🚀 Key Takeaways

### 🐞 Debug First, Code Later
In real-world software engineering, the key isn’t just getting an app to run—**it’s reading errors, debugging them, and understanding what the terminal tells you before even launching the app**. That mindset shift is what separates quick hacks from real development.

---

## 🧩 Technologies & Concepts Used

- **Flask** – the core micro web framework
- **Flask-WTF** – for building forms in Python (and rendering them with Jinja2 templates in HTML)
- **Jinja2** – used in HTML templates to embed dynamic content
- **Hashlib** – used to hash passwords instead of `werkzeug.security`, which is more tailored for production setups
- **Flask-Login** – for session and user login management
- **SQLAlchemy** – used for ORM-based database schema modeling (tables as classes and rows as objects)
- **MySQL + PyMySQL** – for relational database handling and connection
- **Flash Messaging** – to display helpful alerts throughout the app (pending full styling)

---

## 📝 Features

- ✅ Sign up with hashed password storage  
- ✅ Log in with hashed password check  
- ✅ Jinja2-based form rendering  
- ✅ SQLAlchemy-based schema modeling  
- ✅ Flask-WTF for form validation  
- ✅ Flask-Login for user session management  
- ⚠️ Admin check route exists but is minimal  
- ⚠️ Routes are mostly responsive, but **not fully implemented**

---

## 🧠 What I Learned

> "This small app might look like a simple experiment, but it’s **deep in concepts** and covers the essentials of full-stack Flask development."

- Structuring an app using modular Flask design
- Handling form submissions and validations using Python
- Understanding WSGI, live servers, and HTML/Jinja templating
- Working with relational databases via ORM (SQLAlchemy)
- Secure session and login management
- Navigating and fixing issues via the debugger and terminal logs

---

## 📌 Final Thoughts

This app is far from production-ready, but that's not the point. It’s a **functional mini-lab for Flask learners**. The code might be sketchy, the features half-done, but the depth of learning here speaks volumes about how powerful Flask can be when explored even at surface level.

---

## 👨‍💻 Author

Built by a curious developer[Dancan Mungafu] pushing boundaries, one bug at a time.

