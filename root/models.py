from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='.')

class root (models.Model) :
    id_root = models.AutoField(primary_key=True)
    path = models.CharField(max_length=200)
 
