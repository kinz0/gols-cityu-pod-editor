# Generated by Django 4.1.2 on 2022-10-28 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cityu_app', '0004_rename_image_images_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='imagesfile',
            new_name='imagefile',
        ),
    ]