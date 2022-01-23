from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="пользователь",
        related_name="profiles",
        on_delete=models.CASCADE,
    )
    telegram_user_id = models.PositiveIntegerField(
        verbose_name="ID пользователя telegram"
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self) -> str:
        return f"{self.user} {self.telegram_user_id}"


class PersonalComputer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название пк")
    mac_address = models.CharField(max_length=17, verbose_name="Мак адрес")
    allowed_profiles = models.ManyToManyField(
        Profile,
        related_name="personal_computers",
        verbose_name="Разрешённые проифили",
    )

    class Meta:
        verbose_name = "Компьютер"
        verbose_name_plural = "Компьютеры"

    def __str__(self) -> str:
        return self.name
