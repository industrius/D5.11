# Generated by Django 3.1 on 2020-08-23 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_shelf', '0013_auto_20200822_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books_count',
        ),
        migrations.RemoveField(
            model_name='book',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='book',
            name='rented',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='books',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='books_count',
        ),
        migrations.AddField(
            model_name='book',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='rented_by_friend', to='books_shelf.Friend', verbose_name='Друг'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_publisher', to='books_shelf.publisher', verbose_name='Издатель'),
        ),
    ]
