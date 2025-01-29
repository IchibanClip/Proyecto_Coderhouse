# Generated by Django 5.1.4 on 2025-01-23 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusicstore', '0008_listadeseados_delete_oferta'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrarusuario',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='registrarusuario',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registrarusuario',
            name='fecha_de_cumpleanios',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registrarusuario',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
