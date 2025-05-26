💼 SmartBizTransaction
SmartBizTransaction is a simple Django-based web application designed to help small business owners manage their income and expenses efficiently. It allows users to record, view, and categorize financial transactions with optional receipt uploads.

🚀 Features
📥 Add income and expense transactions

📅 Automatically records the transaction date

📝 Add descriptions for each transaction

🖼️ Upload optional receipt images

📊 View total income, expenses, and balance

📃 Clean and responsive Bootstrap 5 UI

🏠 Simple dashboard interface

🧱 Tech Stack
Backend: Django 5.x

Frontend: HTML5, Bootstrap 5

Database: SQLite3 (default)

📂 Project Structure
php
Copy
Edit
smartbiz/
├── smartbiz/               # Project settings
├── tracker/                # Main app for transactions
│   ├── migrations/
│   ├── templates/
│   │   ├── add_transaction.html
│   │   └── dashboard.html
│   ├── static/             # Static files (optional)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
├── media/                  # Uploaded receipt images
├── db.sqlite3              # SQLite database
└── manage.py
🛠️ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/SmartBizTransaction.git
cd SmartBizTransaction
2. Create a virtual environment and activate it
bash
Copy
Edit
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, manually install Django:

bash
Copy
Edit
pip install django
4. Apply migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. Run the development server
bash
Copy
Edit
python manage.py runserver
Then open your browser at:
🌐 http://127.0.0.1:8000/

📸 Screenshots
Dashboard
View total income, expense, balance, and a list of all transactions.

Add Transaction
Form to create a new income or expense, with support for descriptions and image receipts.

📄 Forms
Transaction form includes:

transaction_type (Income/Expense)

amount

description (optional)

date (auto-set)

receipt_image (optional)

📦 Future Improvements
 Add user authentication

 Filter transactions by date range

 Export data to PDF or Excel

 Voice/photo input integration (for mobile)

🧑‍💻 Contributing
Feel free to fork this project and contribute. Pull requests are welcome!

