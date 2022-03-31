from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='.')

class youtube (models.Model) :
    id_ytb = models.AutoField(primary_key=True)
    id_song = models.IntegerField(blank=False,default=0)
    url = models.URLField(max_length=200)    


