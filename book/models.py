from django.db import models

class Book(models.Model):
    TIMELINE = (
        ('Актуален', 'Актуален'),
        ('Не актуален', 'Не актуален'),
    )
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    cost = models.CharField(max_length=10)
    create_date = models.DateTimeField(auto_now_add=True)
    video = models.URLField(null=True)
    timeline = models.CharField(max_length=100, choices=TIMELINE, default=TIMELINE[0], null=True)

    def __str__(self):
        return self.title
