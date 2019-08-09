# Auction_Project_Web
A simple auction website using Django and MySQL.

This repository stores the code for Principle of Database System final project.

To run the code, please fill your used database name, your MYSQL name and password in the setting.py, cd to Auction/Project_web/app directory, then use following commands in your termianl:



Run server:

python manage.py runserver 0.0.0.0:8000



Renew the database and table:

python manage.py makemigrations Index

python manage.py migrate

Then starting development server at the homepage http://127.0.0.1:8000/static/template/index.html. 