# Generated by Django 3.2 on 2023-02-24 19:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('value', models.FloatField()),
                ('from_date', models.DateField(default=django.utils.timezone.now)),
                ('to_date', models.DateField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='coupon/')),
            ],
        ),
    ]
