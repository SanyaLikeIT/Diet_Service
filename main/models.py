from django.db import models
from django.contrib.auth.models import AbstractUser


class Vitamins(models.Model):
    """
    Данный класс содержит информацию о разновидности витамина

    :param Title: Название витамина
    """

    Title = models.CharField(max_length=32)


class Dish(models.Model):
    """
    Данный класс содержит инфрмацию о блюдах и их характеристиках

    :param Title: Название блюда
    :param Carbohydrates: Содержание углеводов в блюде
    :param Protein: Содержание белков в блюде
    :param Fats: Содержание жиров в блюде
    :param Calories: Калорийность блюда
    :param Description: Описание блюда
    :param Recipe: Рецпет приготовления блюда
    :param RichVitamins: Данный параметр показывает витамины, содержащиеся в блюде
    """

    Title = models.CharField(max_length=64)
    Carbohydrates = models.IntegerField()
    Protein = models.IntegerField()
    Fats = models.IntegerField()
    Calories = models.IntegerField()
    Description = models.CharField(max_length=1024, default="Описание")
    Recipe = models.CharField(max_length=1024, default="Рецепт")
    RichVitamins = models.CharField(max_length=32, default=1)
    Allergy = models.CharField(max_length=32, default=1)
    TypeOfDish = models.IntegerField(default=1)
    RichOfVitamins = models.ManyToManyField(Vitamins)
    PlaceOfDish = models.IntegerField(default=1)


class Users(AbstractUser):
    Height = models.IntegerField(default=180)
    Weight = models.IntegerField(default=80)
    Gender = models.IntegerField(default=0)
    Age = models.IntegerField(default=20)
    IsBadHabits = models.IntegerField(default=0)
    Allergy = models.CharField(max_length=1024, default=1)
    Vitamins = models.CharField(max_length=1024, default=1)
    LackOfVitamins = models.ForeignKey(
        Dish,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    LifeStyle = models.IntegerField(default=1)


class Diet(models.Model):
    BreakFast = models.ForeignKey(
        Dish,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="BreakfastDish",
    )
    Lunch = models.ForeignKey(
        Dish,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="LunchDish",
    )
    Dinner = models.ForeignKey(
        Dish,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="DinnerDish",
    )
    User = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
    )
    BreakFast1 = models.IntegerField(default=1)
    BreakFast2 = models.IntegerField(default=1)
    BreakFast3 = models.IntegerField(default=1)
    Lunch1 = models.IntegerField(default=1)
    Lunch2 = models.IntegerField(default=1)
    Lunch3 = models.IntegerField(default=1)
    Dinner1 = models.IntegerField(default=1)
    Dinner2 = models.IntegerField(default=1)
    Dinner3 = models.IntegerField(default=1)
