# Generated by Django 5.0.6 on 2024-05-25 15:04

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dish",
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
                ("Title", models.CharField(max_length=64)),
                ("Carbohydrates", models.IntegerField()),
                ("Protein", models.IntegerField()),
                ("Fats", models.IntegerField()),
                ("Calories", models.IntegerField()),
                ("Description", models.CharField(default="Описание", max_length=1024)),
                ("Recipe", models.CharField(default="Рецепт", max_length=1024)),
                ("RichVitamins", models.CharField(default=1, max_length=32)),
                ("Allergy", models.CharField(default=1, max_length=32)),
                ("TypeOfDish", models.IntegerField(default=1)),
                ("PlaceOfDish", models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="Vitamins",
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
                ("Title", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="Users",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("Height", models.IntegerField(default=180)),
                ("Weight", models.IntegerField(default=80)),
                ("Gender", models.IntegerField(default=0)),
                ("Age", models.IntegerField(default=20)),
                ("IsBadHabits", models.IntegerField(default=0)),
                ("Allergy", models.CharField(default=1, max_length=1024)),
                ("Vitamins", models.CharField(default=1, max_length=1024)),
                ("LifeStyle", models.IntegerField(default=1)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
                (
                    "LackOfVitamins",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.dish",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Diet",
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
                ("BreakFast1", models.IntegerField(default=1)),
                ("BreakFast2", models.IntegerField(default=1)),
                ("BreakFast3", models.IntegerField(default=1)),
                ("Lunch1", models.IntegerField(default=1)),
                ("Lunch2", models.IntegerField(default=1)),
                ("Lunch3", models.IntegerField(default=1)),
                ("Dinner1", models.IntegerField(default=1)),
                ("Dinner2", models.IntegerField(default=1)),
                ("Dinner3", models.IntegerField(default=1)),
                (
                    "User",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "BreakFast",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="BreakfastDish",
                        to="main.dish",
                    ),
                ),
                (
                    "Dinner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="DinnerDish",
                        to="main.dish",
                    ),
                ),
                (
                    "Lunch",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="LunchDish",
                        to="main.dish",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="dish",
            name="RichOfVitamins",
            field=models.ManyToManyField(to="main.vitamins"),
        ),
    ]