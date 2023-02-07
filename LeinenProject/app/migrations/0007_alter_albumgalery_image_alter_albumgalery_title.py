# Generated by Django 4.1.5 on 2023-02-06 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_album_galery_alter_album_front_albumgalery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumgalery',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='albumgalery',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galery', to='app.album'),
        ),
    ]