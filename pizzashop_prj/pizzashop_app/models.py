from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pizzeria(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Pizzeria')
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    # have problem with displaying images on django
    # trows error that Pillow is not installed, while it's installed globally --ver 6.0.0
    # tryed to downgrade to ver. 4.0 and 5.4 not working
    # pip install --user pillow
    # installs in ~/.local/bin/python3.7/ and still not working
    # logo = models.ImageField('Pizzeria logo', upload_to='pizzeria_logo/', blank=False)

    def __str__(self):
        return self.name
