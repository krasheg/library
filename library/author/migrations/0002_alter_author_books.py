# Generated by Django 4.1 on 2023-02-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0003_book_date_of_issue"),
        ("author", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="books",
            field=models.ManyToManyField(
                default=None, null=True, related_name="authors", to="book.book"
            ),
        ),
    ]
