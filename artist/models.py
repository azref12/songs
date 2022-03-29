from django.db import models
from django.core.files.storage import FileSystemStorage
from django.db.models.deletion import CASCADE

fs = FileSystemStorage(location='.')

class artist (models.Model) :
    id_artist = models.AutoField(primary_key=True)
    code_artist = models.IntegerField(blank=False,default=0)
    artist_name = models.CharField(max_length=100, null=False)
    aliasname1 = models.CharField(max_length=100, null=False)
    aliasname2 = models.CharField(max_length=100, null=False)
    aliasname3 = models.CharField(max_length=100, null=False)
    foto_artist = models.ImageField(upload_to='media/artist', storage=fs, null=True)
    
    def __srt__(self) :
        return self.artist_name, self.aliasname1, self.aliasname2, self.aliasname3
