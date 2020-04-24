# Generated by Django 3.0.3 on 2020-04-23 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20200423_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createhistory',
            name='NGO_image',
        ),
        migrations.RemoveField(
            model_name='createhistory',
            name='NGO_name',
        ),
        migrations.AddField(
            model_name='createhistory',
            name='ngo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Account.Site'),
        ),
    ]
