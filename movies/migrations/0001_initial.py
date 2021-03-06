# Generated by Django 3.1.2 on 2020-12-19 03:40

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('imdbID', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('posterURL', models.URLField(blank=True, max_length=2083, null=True)),
                ('bannerURL', models.URLField(blank=True, max_length=2083, null=True)),
                ('poster', models.ImageField(default='poster/poster.jpg', upload_to='poster')),
                ('banner', models.ImageField(default='banner/banner.jpg', upload_to='banner')),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE'), ('adventure', 'ADVENTURE'), ('animation', 'ANIMATION'), ('crime', 'CRIME'), ('documentary', 'DOCUMENTARY'), ('family', 'FAMILY'), ('fantasy', 'FANTASY'), ('horror', 'HORROR'), ('music', 'MUSIC'), ('scifi', 'SCI-FI'), ('thriller', 'THRILLER'), ('war', 'WAR')], max_length=100, null=True)),
                ('language', multiselectfield.db.fields.MultiSelectField(choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ar-dz', 'Algerian Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dsb', 'Lower Sorbian'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hsb', 'Upper Sorbian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('ig', 'Igbo'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kab', 'Kabyle'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('ky', 'Kyrgyz'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmål'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('tk', 'Turkmen'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')], max_length=100, null=True)),
                ('status', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('featured', 'FEATURED'), ('mostwatched', 'MOST WATCHED')], max_length=30, null=True)),
                ('tagline', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('trailer', models.URLField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(200)])),
                ('download', models.URLField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, max_length=283)),
                ('production', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('uploaded_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'ordering': ['-uploaded_on'],
            },
        ),
        migrations.CreateModel(
            name='StaticTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portion', multiselectfield.db.fields.MultiSelectField(choices=[('footer', 'FOOTER'), ('header', 'HEADER'), ('body', 'BODY')], max_length=30)),
                ('tag', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'StaticTag',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='WebTor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(blank=True, max_length=30, null=True)),
                ('source', models.CharField(max_length=2083)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_webtor', to='movies.movie')),
            ],
            options={
                'verbose_name': 'Webtor',
            },
        ),
        migrations.CreateModel(
            name='Torrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(blank=True, max_length=30, null=True)),
                ('link', models.URLField(max_length=2083)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_torrent', to='movies.movie')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Magnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(blank=True, max_length=30, null=True)),
                ('link', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_magnet', to='movies.movie')),
            ],
            options={
                'abstract': False,
            },
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
            name='DynamicTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portion', multiselectfield.db.fields.MultiSelectField(choices=[('footer', 'FOOTER'), ('header', 'HEADER'), ('body', 'BODY')], max_length=30)),
                ('tag', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_tag', to='movies.movie')),
            ],
            options={
                'verbose_name': 'DynamcTag',
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
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('commented_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_comment', to='movies.movie')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-commented_on'],
            },
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, unique=True)),
                ('imageURL', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(default='casts/casts.jpg', upload_to='casts')),
                ('movie', models.ManyToManyField(related_name='movie_cast', to='movies.Movie')),
            ],
        ),
    ]
