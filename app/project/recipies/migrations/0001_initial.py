# Generated by Django 2.1.5 on 2019-02-04 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('shelf_life', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='IngredientType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField()),
                ('photo', models.ImageField(upload_to='recipie_photos')),
                ('serves', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipieIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('unit', models.CharField(max_length=50)),
                ('adjective', models.CharField(max_length=100)),
                ('notes', models.CharField(max_length=240)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipies.Ingredient')),
                ('recipie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipies.Recipie')),
            ],
        ),
        migrations.CreateModel(
            name='RecipieStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('text', models.TextField()),
                ('recipie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipies.Recipie')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipies.IngredientType'),
        ),
    ]