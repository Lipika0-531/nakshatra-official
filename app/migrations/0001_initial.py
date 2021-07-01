# Generated by Django 3.2.4 on 2021-06-30 10:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=18, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('author', models.CharField(max_length=18)),
                ('description', models.CharField(max_length=200)),
                ('image_URl', models.ImageField(upload_to='images/')),
                ('publised_on', models.DateTimeField(editable=False)),
                ('price', models.PositiveIntegerField(default=0)),
                ('likes', models.PositiveIntegerField(default=0, null=True)),
                ('avg_ratings', models.IntegerField(default=5, null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('rating_count', models.PositiveIntegerField(default=0, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('body', models.TextField(max_length=4000, null=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.products')),
            ],
        ),
    ]
