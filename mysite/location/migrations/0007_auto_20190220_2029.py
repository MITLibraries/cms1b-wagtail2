# Generated by Django 2.1.7 on 2019-02-20 20:29

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20190220_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'academic fields',
            },
        ),
        migrations.AddField(
            model_name='locationpage',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=42.35922, max_digits=9, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='locationpage',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=-71.089354, max_digits=9, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='locationpage',
            name='telephone',
            field=models.CharField(max_length=12, verbose_name='Telephone'),
        ),
        migrations.AddField(
            model_name='locationpage',
            name='academics',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='location.AcademicField'),
        ),
    ]
