from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Model representing a blog post.

    Fields:
        id (AutoField): Primary key for the post.
        title (CharField): Title of the blog post (max length: 140 characters).
        body (TextField): Content of the blog post.
        date (DateTimeField): Date and time of the blog post.
        header_image (ImageField): Image associated with the blog post (optional).

    Methods:
        __str__(): String representation of the Post object.
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    

    def __str__(self):
        """
        String representation of the Post object.
        """
        return self.title
    