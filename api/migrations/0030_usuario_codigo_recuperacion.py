# Generated by Django 4.0.4 on 2022-06-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_remove_infracciones_id_ejemplar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='codigo_recuperacion',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
    ]
