from django.db import models

from django.urls import reverse
# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length =200)
    author = models.ForeignKey(
        'auth.user',
        on_delete = models.CASCADE
    )
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self): 

        return reverse('postdetial', args=[str(self.id)])