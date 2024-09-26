"""
having our own external html file and helping django to lacate and render it
in your root directory create a folder called templates
we need to tell django to look for the templates folder
oper the settings.py file in the myproject folder
go to the templates section and add the following
'DIRS': [BASE_DIR, 'templates'], should be what you would do
go into your templates folder and create a file called index.html
add the following code to the index.html file
<!DOCTYPE html>
<html>
<head>
    <title>index</title>    
</head>
<body>
    <h1>hello world</h1>    
</body>
</html>

now go to your views.py file in the myApp folder and change the code to the following
from django.shortcuts import render
from django.http import HttpResponse
now write a function that would render the index.html file
def index(request):
    return render(request, 'index.html')
"""