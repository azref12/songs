from django.db import models

class category (models.Model) :
    id_category = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, null=False)
    
    def __str__(self) :
        return self.category_name

