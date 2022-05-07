from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    text = models.TextField()
    image = ImageField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
