# Generated by Django 2.2.12 on 2023-01-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jabar', '0004_auto_20230104_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kota',
            old_name='bentang_alam',
            new_name='pejabat',
        ),
        migrations.RemoveField(
            model_name='kota',
            name='koordinat',
        ),
        migrations.AddField(
            model_name='kota',
            name='wisata',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
