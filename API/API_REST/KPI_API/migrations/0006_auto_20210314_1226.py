# Generated by Django 3.1.7 on 2021-03-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KPI_API', '0005_auto_20210314_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsondataset',
            name='enveloppe_prev_en_meu',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='jsondataset',
            name='longitude',
            field=models.DecimalField(decimal_places=15, default=0, max_digits=17),
        ),
        migrations.AlterField(
            model_name='jsondataset',
            name='montant_des_ap_votes_en_meu',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='jsondataset',
            name='nombre_de_lots',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
