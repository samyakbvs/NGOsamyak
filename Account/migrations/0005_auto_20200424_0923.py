# Generated by Django 3.0.3 on 2020-04-24 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Account', '0004_auto_20200423_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='Donation_Type',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='NGO',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='NGO_Address',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='User_Address',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='User_Phone',
        ),
        migrations.RemoveField(
            model_name='monetarycollection',
            name='NGO',
        ),
        migrations.RemoveField(
            model_name='monetarycollection',
            name='NGO_Address',
        ),
        migrations.RemoveField(
            model_name='monetarycollection',
            name='User_Address',
        ),
        migrations.RemoveField(
            model_name='monetarycollection',
            name='User_Phone',
        ),
        migrations.AddField(
            model_name='collection',
            name='ngo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Account.Site'),
        ),
        migrations.AddField(
            model_name='monetarycollection',
            name='ngo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Account.Site'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CreateHistory',
        ),
    ]