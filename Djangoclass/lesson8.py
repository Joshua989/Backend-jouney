'''
stactic files are files that are not dynamic and are not generated by the server.
examples are css, js, images, etc.
any external files that are not generated by the server are considered static files.
to add an external css file to your project, you need to create a folder called static in the app folder.
create a folder called css in the static folder.
it contains all the external  files.
go to the settings.py file and add the following code:
import os it get the operating system we are coding on
add the following code to the settings.py file:
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static')
)
in you html file add the following code:
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
the load static is used to load the static files
'''