# Generated by Django 4.0.1 on 2022-01-23 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0003_alter_personalcomputer_mac_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                (
                    "telegram_user_id",
                    models.PositiveIntegerField(
                        verbose_name="ID пользователя telegram"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profiles",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Профиль",
                "verbose_name_plural": "Профили",
            },
        ),
        migrations.AddField(
            model_name="personalcomputer",
            name="allowed_profiles",
            field=models.ManyToManyField(
                related_name="personal_computers",
                to="api.Profile",
                verbose_name="Разрешённые проифили",
            ),
        ),
    ]