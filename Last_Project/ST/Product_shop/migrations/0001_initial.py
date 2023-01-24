# Generated by Django 4.1.3 on 2023-01-12 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='Product_shop/static/icons')),
                ('base64', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Product_shop.category')),
                ('icon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Product_shop.icon')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Product_shop.icon'),
        ),
    ]
