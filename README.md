"# Doctor-Appointment" 

About this project:
This project is simple doctor patient appointment scheduler project. This contains api as well web application.
Main feature is that it avoid clashing ie it allows only one patient to get scheduled at particular time slot.
View screenshot of api here https://drive.google.com/file/d/1v6Dw9qS5jXX3SXyHSJGqZRL9QcEQaROG/view?usp=sharing

How to run this project:
1) Install django
2)Install django restful api
3)Make migration using command 
 python manage.py makemigrations
 python manage.py migrate
4)Then run server:
python manage.py runserver
5)Visit http://127.0.0.1:8000
6)Visit http://127.0.0.1:8000/doctorr/ for doctor API and http://127.0.0.1:8000/appointmentt/ for appointment api
