from django.db import models

class genre (models.Model) :
    id_genre = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=100, null=False)
    
    def __str__(self) :
        return self.genre 