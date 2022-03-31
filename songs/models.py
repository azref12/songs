from django.db import models
from django.db.models.deletion import CASCADE
from artist.models import artist
from category.models import category
from genre.models import genre
from root.models import root
from youtube.models import youtube
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='.')

class song (models.Model) :
    id_songs = models.AutoField(primary_key=True)
    code_song = models.IntegerField(blank=False, default=0)
    title_song = models.CharField(max_length=100, null=False)
    alias1 = models.CharField(max_length=100, null=False)
    alias2 = models.CharField(max_length=100, null=False)
    alias3 = models.CharField(max_length=100, null=False)
    paths = models.CharField(max_length=200)
    xvoc = models.IntegerField(blank=False, default=0)
    voc = models.IntegerField(blank=False, default=0)
    vol=models.IntegerField(blank=False, default=0)
    Foto = models.FileField(upload_to='media/songs', storage=fs, null=True)
    id_ytb = models.ForeignKey(youtube, related_name='ytb', on_delete=models.CASCADE)
    id_artist = models.ForeignKey(artist, related_name='artists', on_delete=models.CASCADE)
    id_category = models.ForeignKey(category, related_name='categories', on_delete=models.CASCADE)
    id_genre = models.ForeignKey(genre, related_name='genres', on_delete=models.CASCADE)
    id_root = models.ForeignKey(root,  related_name='roots',on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.title_song, self.alias1, self.alias2, self.alias3

