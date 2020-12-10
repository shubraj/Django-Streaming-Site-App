# Generated by Django 3.1.2 on 2020-12-10 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_webtor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='embed',
        ),
        migrations.CreateModel(
            name='Embed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(blank=True, max_length=30, null=True)),
                ('link', models.URLField(max_length=2083)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_embed', to='movies.movie')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(blank=True, max_length=30, null=True)),
                ('link', models.URLField(max_length=2083)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_download', to='movies.movie')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]