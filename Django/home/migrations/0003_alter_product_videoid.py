# Generated by Django 5.0.4 on 2024-05-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_product_lesson_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='videoId',
            field=models.FileField(default=1, upload_to='videos/', verbose_name='Video'),
            preserve_default=False,
        ),
    ]
