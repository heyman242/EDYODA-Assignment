# Generated by Django 4.2.2 on 2023-06-16 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MelodyShare', '0005_alter_privatemusicrecord_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatemusicrecord',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MelodyShare.newuser'),
        ),
    ]
