# Generated by Django 2.2.4 on 2021-05-24 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0004_auto_20210524_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auts', to='books_app.Book'),
        ),
    ]
