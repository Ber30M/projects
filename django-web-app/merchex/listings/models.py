'''
POUR AJOUTER UNE INSTANCE A LA CLASSE
____________________________________


In [18]: listing = Listing()

In [19]: listing.title = 'Beethoven - Moonlight Sonata - original manuscript EX 
    ...: TREMELY RARE'

In [20]: listing.save()

In [21]: listing
Out[21]: <Listing: Listing object (3)>    
'''
from pyexpat import model
from django.db import models

class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    
class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
    
