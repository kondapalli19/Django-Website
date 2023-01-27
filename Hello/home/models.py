from django.db import models


# Make migrations = means to create changes and store in a file
# migrate = Apply the pending changes created by makemigrations

# Create your models here.  
class Contact(models.Model):
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.email