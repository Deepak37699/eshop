from django.db.models import models
class Category(models.Model):
    name = models.CharField(max_length=50)
