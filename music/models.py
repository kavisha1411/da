from django.db import models
from django.contrib import admin
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


STATUS_CHOICES = [
    ('u', 'Unverified'),
    ('v', 'Verified'),
]


class Artist(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20, null=True)
    artists = models.Manager()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artist'
        verbose_name = 'Artist'
        verbose_name_plural = 'Artist'


class Album(models.Model):
    name = models.CharField(max_length=30)
    number_songs = models.IntegerField(default=1)
    artist = models.ForeignKey(Artist, null=True, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",)

    def __str__(self):
        return self.name

    @admin.display(description='Album details')
    def details_album(self):
        return (f"{self.name} has {self.number_songs} songs and the artist is {self.artist}")
 
    class Meta:
        db_table = 'album'
        verbose_name = 'Album'
        verbose_name_plural = 'Album'


class Song(models.Model):
    name = models.CharField(max_length=30)
    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL, related_name='songs')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,related_name='songs')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Song, self).save(*args, **kwargs)
        print("Overriding save")

    class Meta:
        db_table = 'song'
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'
        order_with_respect_to = 'album'
        

@receiver(pre_save, sender=Song)
def pre_save_function(sender, **kwargs):
    print("PreSave")


def post_save_function(sender, **kwargs):
    print("PostSave")


post_save.connect(post_save_function)
