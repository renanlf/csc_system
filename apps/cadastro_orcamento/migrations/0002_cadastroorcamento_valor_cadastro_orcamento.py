# Generated by Django 3.0.2 on 2020-02-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_orcamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastroorcamento',
            name='valor_cadastro_orcamento',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
