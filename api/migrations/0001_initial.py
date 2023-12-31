# Generated by Django 4.2.7 on 2023-11-16 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('CEO', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT')], max_length=10)),
                ('about', models.TextField()),
                ('base', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
