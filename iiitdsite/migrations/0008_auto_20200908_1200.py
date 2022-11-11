# Generated by Django 3.0.8 on 2020-09-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdsite', '0007_auto_20200908_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='SenateMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_hindi', models.CharField(max_length=100)),
                ('name_kannada', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=300)),
                ('position_hindi', models.CharField(max_length=300)),
                ('position_kannada', models.CharField(max_length=300)),
                ('image_link', models.CharField(max_length=300)),
            ],
        ),
        migrations.RenameModel(
            old_name='Senate',
            new_name='SenateChairperson',
        ),
    ]