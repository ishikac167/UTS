# Generated by Django 4.0.4 on 2022-06-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0003_account_address_account_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=30, null=True, verbose_name='Email'),
        ),
    ]
