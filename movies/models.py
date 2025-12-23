from django.db import models

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True, verbose_name="ID на TMDB")
    title = models.CharField(max_length=255, verbose_name="Title")
    original_title = models.CharField(max_lenght=255, verbose_name="Original title")

    digital_release_date = models.DateField(null=True, blank=True, verbose_name="Date release ")

    poster_path = models.CharField(max_leght=255, null=True, blank=True)
    overview = models.TextField(verbose_name="Description", blank=True)
    genres = models.JSONField(default=list, verbose_name="genres")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.digital_release_date})"

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "films"
        ordering = {'-digital_release_data'}
