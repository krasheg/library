# Generated by Django 4.1 on 2023-02-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_year_of_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_of_issue',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
