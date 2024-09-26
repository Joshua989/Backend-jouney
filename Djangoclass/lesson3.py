#django app
#django app is a web application that is created using the django framework it is a subsetof a perticular app
#example in istagram we have the profile app the post app the comment app the like app the follow app all this are django apps
#to craete an app use the following command python manage.py startapp name_of_app
'''
the structure of a django app
admin.py file is used to configure the admin page of the app it help control your app from the admin page 
it is also used to reagister database models
apps.py file is used to configure the app it is used to configure the app name and the app label
it is also used to configure the app ready method
it is also used to configure the app verbose name
models.py file is used to configure the database models of the app it is used to configure the database models of the app
dealing with the database in Django is very easy because Django comes with a built-in database called SQLite so we dont need to write a single line of sql
tests.py file is used to configure the test of the app it is used to configure the test of the app
views.py file is used to configure the views of the app it is used to configure the views of the app


url configuration
url configuration is the process of configuring the urls of the app
craete a urls.py file in the app folder
import the following
from django.urls import path
from . import views thsi is used to import the views of the app

urlpatterns = [ 
    path('', views.index, name='index') root url  index is a function in the views.py file that is used to render the home page
    path('about/', views.view, name='name') about url
]


now go to your views.py file and create a function that would render the home page

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

to run the server use the following command
python manage.py runserver

now running this would take you to djangio default page
to make our veiw.index the default page we need to go to the urls.py file in the myproject folder and change the path to the following
first import the following
from django.urls import include
from django.urls import path
from . import views
 add path('', include('myApp.urls')) to the urlpatterns list

'''