# Generated by Django 3.0.2 on 2020-04-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arogyasetu', '0004_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('mobile', models.IntegerField(null=True)),
            ],
        ),
    ]
