_**THE AUTHOR IS NO LONGER UPDATING THIS REPOSITORY **_

# Online-Book-Store-With-Recommendation-System
This project deals with developing an e-commerce website for Online Book Sale. It provides the user with a catalog of different books available for purchase in the store. In order to facilitate online purchase a shopping cart is provided to the user. The users are recommended on the basis of previous users rating.
To run this project:
open command line and enter:
python manage.py runserver

## Dont Forget to Read the documentation provided

- Online shopping is the process whereby consumers directly buy goods or services from a seller in real-time, without an intermediary service, over the Internet. 
- The process is called Business-to-Consumer (B2C) online shopping.  
- The developed system is a “Recommendation System Using Collaborative Filtering” which deals with developing an e-commerce website for a bookstore for both walk-in customers and online customers.
- The customer can browse by catalog, search, buy and get a recommendation of books in the store. 
- To facilitate online purchase a shopping cart is provided to the user. 
- The users are recommended based on previous users rating using **matrix factorization technique**.
- To develop an e-commerce website, several Technologies was studied and understood. 
- These include server and client-side scripting techniques, implementation technologies such as Python, Django, HTML, CSS, Bootstrap, JavaScript, and MySQL for database 
handling.  
          
**Step 1: Downloading and Setting Up MySQL**
You can skip this step if you already have MySQL set up on your computer.
First, we will download and set up MySQL using . Make sure to save the temporary root password they give you! Once MySQL is installed, we will set up a launch daemon that allows MySQL to start up on system/terminal launch.
After you finish installing, double check that your server is running. If not, you can turn it on through that service.msc from run.

**Step 2: Finishing Up Installation**
Try running mysql in terminal. You might get an error like “command not found”. If so, in terminal, configure your computer’s $PATH so it recognizes mysql as an executable:
_$ export PATH=$PATH:/path/to/your/mysql/bin_

**Step 3: Creating MySQL Users**
NOTE: in this tutorial, we are altering the root user because it is assumed you do not have any other local users on your MySQL server. If you do, change the usernames accordingly
Now we are ready to use MySQL! Enter

_$ mysql -u root –p_

Log in using your root password. If this is your first time logging in, use the password that you saved in step 1. Now, if you want to change the root password to something of your own preference, in the MySQL shell, enter

_mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_new_password';_

Now, you have your root user set up and can log into it using your own password.
If you want to create your own user, enter

_mysql> CREATE USER 'your_new_username'@'localhost' IDENTIFIED BY 'new_password';_

_mysql> GRANT ALL PRIVILEGES ON * . * TO 'your_new_username'@'localhost';_

_mysql> FLUSH PRIVILEGES;_

the * . * allows the user to have all access to the databases and tables in the server. For more fine-toothed assignment of priviledges, check out the MySQL documentation.

**Step 4: Creating the Project Database**
In order to use MySQL with our project, we will need a Python 3 database connector library compatible with Django. So, we will install the database connector, mysqlclient.
_pip install mysqlclient_

Then, to create the database for your project:

_mysql> CREATE DATABASE your_project_name CHARACTER SET UTF8;_
_mysql> GRANT ALL PRIVILEGES ON your_project_name.* TO your_username@localhost;_
_mysql> FLUSH PRIVILEGES;_
_mysql> QUIT_

**Step 5: Changing Django App Settings**
Now, in your terminal, navigate to the root directory of your Django application.
Finally, in your settings.py file in your app, change the DATABASES section to the following:

_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_project_name',
        'USER': 'root',
        'PASSWORD': 'your_root_password',
        'HOST': 'your_host_address', 
        'PORT': 'your_port',
    }
}_

A reminder that your_project_name should be the same name as the database you created in MySQL in Step 2. your_password is the same password that you use to log into MySQL. The HOST and PORT values can be optional if you are simply hosting your webapp locally, but if you are running MySQL in a virtual server or a separate server then fill in your host address and port accordingly.

**Step 6: Make Migrations**
_$ python manage.py makemigrations
$ python manage.py migrate_
Once done we are now connected to our mysql database;
enter : _python manage.py runserver_

          
          


  

