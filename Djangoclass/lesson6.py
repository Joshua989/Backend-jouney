'''
word counter project
craete a form in your vs code
that accept data from the user
now the action in the form should direct to the path that your word s would be submitted to
here we craeted a new path called counter
in our url.py file in the myApp folder
heres how the code should look like
path('counter/', views.counter, name='counter')
now in our views.py file in the myApp folder
we need to craete a new function called counter
here is how the code should look like
def counter(request):
    word = request.GET['text'] here we are getting the word from the form passing it to the word variable
    the nmame of the textare as is it in the get should be text
    amount_of_words = len(text.split()) here we are splitting the word and counting the number of words
    
    return render(request, 'counter.html', {amout : amount_of_words}) here we are sending the amount_of_words variable to the counter.html file

    create a new file in the templates folder called counter.html
    add the following code to the counter.html file
    <!DOCTYPE html>
    <html>
    <head>
        <title>counter</title>
    </head>
    <body>
        <h1>the amount of words in the text is {{amount}}</h1>
    </body>
    </html>
    now it should work
    now if you notice all your words are in the url how do you prevent this
    when we use post method to submit we would need to make use of the csrf_token
    why because the post method is more secure than the get method
    the full meaning of csrf is cross site request forgery and it helps to prevent hackers from submitting data to your form
    to use cfrf_token we need to do the following
    {% csrf_token %} add this code to the form in the counter.html file
'''