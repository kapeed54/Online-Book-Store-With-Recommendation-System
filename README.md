# Online-Book-Store-With-Recommendation-System
This project deals with developing an e-commerce website for Online Book Sale. It provides the user with a catalog of different books available for purchase in the store. In order to facilitate online purchase a shopping cart is provided to the user. The users are recommended on the basis of previous users rating.

Things to do before running this projects:
1. Download all the requirements raised by this project
2. MySQl database is used in this project but you can use the default Sqlite database . If you want yo use MYSQL follow these steps
  DOWNLOADING AND SETTING up MySQL
  ( You can skip this step if you already have MySQL set up on your computer.)
      STEP 1: First, we will download and set up MySQL using . Make sure to save the    
              temporary 
              root password they give you! Once MySQL is installed, we will set up a  
              launch 
              daemon that allows MySQL to start up on system/terminal launch.
              After you finish installing, double check that your server is running. If               not, you 
              can turn it on through that service.msc from run.
      
      Try running mysql in terminal. You might get an error like “command not found”. If       so, in terminal, configure your computer’s $PATH so it recognizes mysql as an     
      exectutable:

  a. In order to use MySQL with our project, we will need a Python 3 database connector      library compatible with Django. So, we will install the database connector,    
     mysqlclient.
     pip install mysqlclient
  b. We can now build our DATABASES settings in our settings.py as follow.
      Verify that the server is running by checking MYSQL in services. (Press window key  
      and search services)
      i. Log in MYSQL.
         open terminal and type mysql -u -p
     ii. Once logged in Create a database for your project
          mysql > CREATE DATABASE bookstore;
          mysql > SHOW DATABASES; (TO verify that the database is created)
      We have successfully created database for our project. 
     
    iii. Adding MYSQL Database Connection to our application:inside settings.py of  bookstore app
          DATABASES = {
              'default': {
                  'ENGINE': 'django.db.backends.mysql',
                  'NAME': 'bookstore',
                  'USER': 'root', 
                  'PASSWORD': 'DATABASE_PASSWORD',
                  'HOST': '',
                  'PORT': '',
              }
          }

          To check it is working we will simply make migrations and migrate
          python manage.py makemigrations
          python manage.py migrate
          Once done we are now connected to our mysql database;
          enter : python manage.py runserver

      iv. Create a admin by typing the following command in ternminal:
          python manage.py createsuperuser
          

          
          


  

