# Generated by Django 3.0.2 on 2020-02-03 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20200203_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nome_usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
