# **📚 Online Book Store with Recommendation System**

⚠ **THE AUTHOR IS NO LONGER UPDATING THIS REPOSITORY** ⚠

## **📖 About This Project**
This project is an **e-commerce website for buying books online**, featuring a **Recommendation System** that suggests books based on user ratings.

### **🔹 Features**
- 📚 **Book Catalog** – Browse and search books by category.
- 🛒 **Shopping Cart** – Add books and proceed to checkout.
- ⭐ **Recommendation System** – Get book recommendations using **Collaborative Filtering** (Matrix Factorization).
- 🔒 **User Authentication** – Sign up, log in, and manage your profile.
- 🛠 **Built With** – **Python, Django, MySQL, HTML, CSS, Bootstrap, JavaScript.**

### **🔹 Running the Project**
```powershell
python manage.py runserver
```
Then open **http://127.0.0.1:8000/** in your browser.

---

# **🚀 Setup Guide**
If you are **forking or downloading this repository**, follow these steps to **avoid common setup issues**.

---

## 📌 **Step 1: Install MySQL**
### **1️⃣ Install MySQL**
- **Download MySQL**: [MySQL Community Server](https://dev.mysql.com/downloads/mysql/)
- Choose **"Server Only"** during installation.
- Set a **root password** (remember it).

### **2️⃣ Verify MySQL is Running**
Run:
```powershell
Get-Service | Where-Object { $_.DisplayName -like "*MySQL*" }
```
- If MySQL is **stopped**, start it:
  ```powershell
  Start-Service MySQL
  ```
- If using **XAMPP**, start MySQL manually.

---

## 📌 **Step 2: Add MySQL to System PATH**
If `mysql` is not recognized as a command, add it to **System PATH**:

1. Open **Environment Variables** (`Win + R` → type `sysdm.cpl` → "Advanced" → "Environment Variables").
2. Find **"Path"** under **System Variables** → Click **Edit**.
3. Click **New** → Add:
   ```
   C:\Program Files\MySQL\MySQL Server 8.0\bin
   ```
4. Click **OK** and **Restart your PC**.

Test MySQL:
```powershell
mysql --version
```
✅ **If you see a version number, MySQL is working!**

---

## 📌 **Step 3: Set Up MySQL Database**
### **1️⃣ Open MySQL Shell**
```powershell
mysql -u root -p
```
Enter your **MySQL root password**.

### **2️⃣ Create a Database and User**
Run:
```sql
CREATE DATABASE bookstore CHARACTER SET UTF8;
CREATE USER 'bookadmin'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON bookstore.* TO 'bookadmin'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
✅ **Your MySQL setup is now ready!**

---

## 📌 **Step 4: Clone the Repository**
Navigate to your project folder and clone the GitHub repository:
```powershell
cd D:\GitHub
git clone https://github.com/kapeed54/Online-Book-Store-With-Recommendation-System.git
cd Online-Book-Store-With-Recommendation-System
```

---

## 📌 **Step 5: Set Up a Virtual Environment**
Create and activate a virtual environment:
```powershell
python -m venv env
.\env\Scripts\Activate
```

---

## 📌 **Step 6: Install Dependencies**
Install all required Python packages:
```powershell
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```
✅ **If `requirements.txt` is missing, install dependencies manually**:
```powershell
pip install django mysqlclient numpy scipy pandas scikit-learn Pillow django-bootstrap4 gunicorn
```

---

## 📌 **Step 7: Configure Database in Django**
Open **`bookstore/settings.py`**, update the `DATABASES` section:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookstore',  # Database name
        'USER': 'bookadmin',  # MySQL username
        'PASSWORD': 'yourpassword',  # MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
✅ **Save the file.**

---

## 📌 **Step 8: Apply Migrations**
Run:
```powershell
python manage.py makemigrations
python manage.py migrate
```
✅ **Now, your database is connected!**

---

## 📌 **Step 9: Create a Superuser for Django Admin**
To manage books and users via Django Admin, create a **superuser**:
```powershell
python manage.py createsuperuser
```
- Enter **Username, Email, and Password**.
- Log in at **[`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/)**.

---

## 📌 **Step 10: Load Sample Data (If Needed)**
### **1️⃣ Add Books via Django Admin**
- Go to: **[`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/)**
- Log in and manually **add some books**.

### **2️⃣ Or Use the Django Shell**
Run:
```powershell
python manage.py shell
```
Then enter:
```python
from shop.models import Product, Myrating, User

# Get an existing user
user = User.objects.first()
if not user:
    print("No users found. Please create a user first via admin panel.")
    exit()

# Add sample books if none exist
if not Product.objects.exists():
    Product.objects.create(name="The Great Gatsby", price=20, description="A classic novel", stock=10)
    Product.objects.create(name="1984", price=25, description="A dystopian novel", stock=5)
    Product.objects.create(name="To Kill a Mockingbird", price=30, description="A novel by Harper Lee", stock=8)
    print("Sample books added!")

# Add sample ratings
if not Myrating.objects.exists():
    Myrating.objects.create(user=user, product=Product.objects.first(), rating=5)
    Myrating.objects.create(user=user, product=Product.objects.last(), rating=4)
    print("Sample ratings added!")

exit()
```
✅ **Now your project has books and ratings!**

---

## 📌 **Step 11: Run the Development Server**
```powershell
python manage.py runserver
```
Open:
- **Homepage:** [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)
- **Admin Panel:** [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/)
- **Get Recommendations:** [`http://127.0.0.1:8000/recommend/`](http://127.0.0.1:8000/recommend/)

✅ **Your project is now running successfully!** 🎉

---

## 📌 **Troubleshooting**
### **1️⃣ If MySQL Connection Fails**
```powershell
Get-Service | Where-Object { $_.DisplayName -like "*MySQL*" }
Start-Service MySQL
```
### **2️⃣ If `pip install` Fails**
```powershell
python -m pip install --upgrade pip
```
### **3️⃣ If Recommendations Don’t Work**
Ensure users have **rated books** before trying recommendations.

---

🚀 **Now the setup steps are logically ordered and easier to follow!**  

This **README format is perfect for GitHub** and blends the original **project introduction** with the **updated setup instructions**.  

Let me know if you want any final tweaks before committing this! 🎯
          


  

