# Generated by Django 4.2.2 on 2023-06-15 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('id', models.CharField(max_length=5, unique=True)),
                ('email_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
