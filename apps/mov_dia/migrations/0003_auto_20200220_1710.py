# Generated by Django 3.0.2 on 2020-02-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mov_dia', '0002_movdodia_valor_prov'),
    ]

    operations = [
        migrations.AddField(
            model_name='movdodia',
            name='ag_dep',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movdodia',
            name='banco_dep',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movdodia',
            name='codigo_de_barras',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movdodia',
            name='conta_dep',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
