# Generated by Django 4.1 on 2023-02-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='plated_end_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
