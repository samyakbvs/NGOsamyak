# Generated by Django 3.0.3 on 2020-04-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_auto_20200424_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='uid',
            field=models.CharField(default='qwerty', max_length=264),
            preserve_default=False,
        ),
    ]
