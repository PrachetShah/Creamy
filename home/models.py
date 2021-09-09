from django.db import models

#Register your models in Admin

''' Create your models here.
After making models we make migrations , makemigrations = changes and store in a file
The migrate = apply pending changes created by makemigrations '''

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    text = models.TextField()
    date = models.DateTimeField()

    # This is used to show Name in Admin instead of ContactInfo(id) in database
    def __str__(self):
        return self.name