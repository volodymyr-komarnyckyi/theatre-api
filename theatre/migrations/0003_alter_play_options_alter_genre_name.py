# Generated by Django 4.2.4 on 2023-08-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("theatre", "0002_reservation_ticket"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="play",
            options={"ordering": ["title"]},
        ),
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]