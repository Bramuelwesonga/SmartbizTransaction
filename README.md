# 💼 SmartBizTransaction

SmartBizTransaction is a simple Django-based web application designed to help small business owners efficiently manage their income and expenses. It allows users to record, view, and categorize financial transactions with optional receipt uploads in a clean and responsive interface.

---

## 🚀 Features

- 📥 Add income and expense transactions  
- 📅 Automatically records the transaction date  
- 📝 Add descriptions for each transaction  
- 🖼️ Upload optional receipt images for transactions  
- 📊 View total income, total expenses, and current balance  
- 📃 Clean and responsive UI built with Bootstrap 5  
- 🏠 Simple and intuitive dashboard interface  

---

## 🧱 Tech Stack

- **Backend:** Django 5.x  
- **Frontend:** HTML5, Bootstrap 5  
- **Database:** SQLite3 (default with Django)  

---

## 📂 Project Structure

smartbiz/
├── smartbiz/ # Django project settings
├── tracker/ # Main app for transactions
│ ├── migrations/
│ ├── templates/
│ │ ├── add_transaction.html
│ │ └── dashboard.html
│ ├── static/ # Static files (optional)
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── forms.py
├── media/ # Uploaded receipt images
├── db.sqlite3 # SQLite database file
└── manage.py

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/SmartBizTransaction.git
cd SmartBizTransaction
Create a virtual environment and activate it

bash
Copy
Edit
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, install Django manually:

bash
Copy
Edit
pip install django
Apply migrations

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Run the development server

bash
Copy
Edit
python manage.py runserver
Open your browser and navigate to:

cpp
Copy
Edit
http://127.0.0.1:8000/

📄 Forms
The transaction form includes the following fields:

transaction_type (Income / Expense)

amount

description (optional)

date (auto-set)

receipt_image (optional upload)

📦 Future Improvements
Add user authentication and personalized accounts

Filter transactions by date range and categories

Export data to PDF or Excel formats

Integrate voice or photo input for mobile convenience

🧑‍💻 Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

Please make sure to update tests as appropriate and write clear commit messages.

