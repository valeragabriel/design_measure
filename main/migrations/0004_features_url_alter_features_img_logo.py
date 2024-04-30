# Generated by Django 5.0.4 on 2024-04-28 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='url',
            field=models.URLField(default='bodyMeasure.html'),
        ),
        migrations.AlterField(
            model_name='features',
            name='img_logo',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]