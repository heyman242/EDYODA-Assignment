# Generated by Django 4.2.2 on 2023-06-18 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MelodyShare', '0007_alter_protectedmusicrecord_email_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='protectedmusicrecord',
            old_name='email_id',
            new_name='email_ids',
        ),
    ]
