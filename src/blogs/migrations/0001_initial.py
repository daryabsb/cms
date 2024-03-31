# Generated by Django 5.0.3 on 2024-03-31 11:34

import ckeditor_uploader.fields
import django.db.models.deletion
import mptt.fields
import src.core.modules
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
                ('comment', models.BooleanField(default=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('Published', 'Published'), ('Draft', 'Draft'), ('Pending', 'Pending')], default='Published', max_length=255)),
                ('visibility', models.CharField(choices=[('Pu', 'Public'), ('PP', 'Password Protected'), ('Pr', 'Private')], default='Pu', max_length=255)),
                ('publish_on', models.DateField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('feature_image', models.ImageField(default='default/default.jpg', max_length=500, upload_to=src.core.modules.upload_image_file_path)),
                ('video_url', models.URLField(blank=True, help_text='YouTube Embed URL', null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'order_with_respect_to': 'publish_on',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('blog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blogs.blogs')),
                ('meta_keywords', models.CharField(blank=True, max_length=500, null=True)),
                ('meta_descriptions', models.TextField(blank=True, null=True)),
                ('blog_url', models.URLField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Seo',
                'verbose_name_plural': 'Seos',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blogs.categories')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='blogs',
            name='categories',
            field=mptt.fields.TreeManyToManyField(blank=True, to='blogs.categories'),
        ),
        migrations.CreateModel(
            name='Metas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('value', models.TextField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.blogs')),
            ],
            options={
                'verbose_name': 'Meta',
                'verbose_name_plural': 'Metas',
            },
        ),
        migrations.AddField(
            model_name='blogs',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blogs.tags'),
        ),
    ]
