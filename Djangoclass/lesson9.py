'''
model in django

this is a class that is used to create a table in the database
it is a subclass of the django.db.models.Model class
THEY ARE USED TO CONFIGIRE THE DATABASE
MODEL VEEW TEMPLATE
THSI IS THE MVT ARCHITECTURE
THE MODEL IS THE DATABASE
THE VIEW IS THE LOGIC
THE TEMPLATE IS THE USER INTERFACE
WE USE CLASSES TO CREATE MODELS

GO INTO YOUR MODELS.PY FILE AND CREATE A CLASS
EXAPLE:
  class feature:
        name = models.CharField(max_length=100)
        description = models.TextField()
        price = models.FloatField()
        image = models.ImageField(upload_to='images/')
        
        def __str__(self):
            return self.name
'''