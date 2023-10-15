# Generated by Django 4.2.6 on 2023-10-15 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rename_created_date_book_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='timeline',
            field=models.CharField(choices=[('Актуален', 'Актуален'), ('50 на 50', '50 на 50'), ('Стрем', 'Стрем')], default=('Актуален', 'Актуален'), max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='video',
            field=models.URLField(null=True),
        ),
    ]
