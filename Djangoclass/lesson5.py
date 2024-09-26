#sending data to the template file
'''
static web pages are boring we need to send data to the template file
they do not carry any data
to send data to the template file we need to use the render function
example facebook we have the profile page the home page the about page the contact page
this are dynamic pages because they carry data that are different for different users



to send data to the template file we need to use the render function
go to the views.py file in the myApp folder
here we could create a varibale called name and assess it in the template file

name = 'john'
return render(request, 'index.html', {'name': name}) here we are sending the name variable to the template file

now go to the index.html file in the templates folder and add the following code
 updare the code to the following
 <p>hello {{name}}</p> here we are using the double curly braces to access the name variable

 sometime wen the date is coming from the database we need to use the following code
 in your views.py file in the myApp folder
 neme = user.name
    return render(request, 'index.html', {'name': name}) here we are sending the name variable to the template file
    context is a dictionary that is used to send data to the template file
    context = {
        'name': 'joh',
        'age': 20
        nationality: 'nigeria'
    }
    return render(request, 'index.html', context) here we are sending the context dictionary to the template file
    go ahead and update the index.html file in the templates folder to the following
'''