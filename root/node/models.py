from django.db import models

# Create your models here.
class Mode(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=50)
    class Meta:
        db_table = "mode"