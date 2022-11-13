from django.db import models


# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='photos/', blank=True, null=True)

    album = models.ForeignKey(
        'photos.Album',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Title:'{self.title}', URL:{self.image}, album:{self.album}"


class Album(models.Model):
    album_title = models.CharField(max_length=40)