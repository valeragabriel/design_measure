# Generated by Django 5.0.4 on 2024-04-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_delete_footer_delete_header_delete_home_delete_we_do'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('img_logo', models.ImageField(upload_to='features/')),
            ],
        ),
    ]
