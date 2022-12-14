# Generated by Django 4.1.3 on 2022-12-12 04:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                ("description", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="portfolioapp/images/")),
                ("url", models.URLField(blank=True)),
            ],
        ),
    ]
