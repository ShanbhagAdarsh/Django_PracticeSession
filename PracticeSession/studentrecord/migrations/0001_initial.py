# Generated by Django 4.0.3 on 2022-03-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studrecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(max_length=10)),
                ('fname', models.CharField(max_length=10)),
                ('mname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('mobno', models.IntegerField()),
                ('emailid', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]