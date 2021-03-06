# Generated by Django 2.1.7 on 2019-02-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('alert', '0001_initial'), ('alert', '0002_advisory'), ('alert', '0003_auto_20190221_1657')]

    initial = True

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailforms', '0003_capitalizeverbose'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('enddate', models.DateField()),
            ],
        ),
    ]
