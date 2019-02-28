# Generated by Django 2.1.7 on 2019-02-28 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('css', models.URLField(blank=True, help_text='theme css')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'theme',
            },
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='facebook',
            field=models.URLField(blank=True, help_text='Facebook page URL'),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='instagram',
            field=models.CharField(blank=True, help_text='Instagram username, without the @', max_length=255),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='twitter',
            field=models.CharField(blank=True, help_text='Your twitter handle without the @', max_length=255),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='youtube',
            field=models.URLField(blank=True, help_text='Your YouTube channel or user account URL'),
        ),
    ]
