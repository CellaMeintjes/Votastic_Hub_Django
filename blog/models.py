from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    

    def __str__(self):
        return self.title