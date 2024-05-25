"""
Модуль, в котором хранятся формы
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Users
from main.utility import (
    get_allergy,
    get_vitamins,
    get_LyfeStyleOptions,
    get_dish_type,
    get_place_of_dish,
)


class RegistrationForm(forms.Form):
    """
    Форма регистрации пользователя
    """

    username = forms.CharField(
        label="Логин",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Имя",
            }
        ),
    )
    password = forms.CharField(label="Пароль", required=True, widget=forms.PasswordInput())
    RepeatPassword = forms.CharField(label="Пароль", required=True, widget=forms.PasswordInput())
    Height = forms.IntegerField(
        required=True,
        label="Рост",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Рост",
            }
        ),
    )
    Weight = forms.IntegerField(
        required=True,
        label="Вес",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Вес",
            }
        ),
    )
    Age = forms.IntegerField(
        required=True,
        label="Возраст",
        widget=forms.TextInput(
            attrs={
                "style": "height:50px",
                "class": "form-control",
                "placeholder": "Возраст",
            }
        ),
    )
    Gender = forms.ChoiceField(required=True, label="Пол", choices={0: "Муж.", 1: "Жен."})
    IsBadHabits = forms.BooleanField(
        required=False,
        label="Есть ли у вас плохие привычки?",
    )
    Allergy = forms.MultipleChoiceField(
        required=False,
        label="Аллергия",
        choices=get_allergy(),
        widget=forms.CheckboxSelectMultiple(),
    )
    Vitamins = forms.MultipleChoiceField(
        required=False,
        label="Витамины",
        choices=get_vitamins(),
        widget=forms.CheckboxSelectMultiple(),
    )
    LifeStyle = forms.ChoiceField(
        label="Выберите ваш стиль жизни",
        required=True,
        choices=get_LyfeStyleOptions(),
    )


class LoginForm(forms.Form):
    """
    Форма для входа пользователя
    """

    username = forms.CharField(
        max_length=64,
        required=True,
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Логин",
            }
        ),
    )
    password = forms.CharField(
        max_length=64,
        required=True,
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Пароль",
            }
        ),
    )


class NewDishForm(forms.Form):
    """
    Форма для создания нового блюда
    """

    Title = forms.CharField(
        required=True,
        label="Название блюда",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Название блюда",
            }
        ),
    )
    Carbohydrates = forms.IntegerField(
        required=True,
        label="Углеводы",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Углеводы",
            }
        ),
    )
    Protein = forms.IntegerField(
        required=True,
        label="Белки",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Белки",
            }
        ),
    )
    Fats = forms.IntegerField(
        required=True,
        label="Жиры",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Жиры",
            }
        ),
    )
    Calories = forms.IntegerField(
        required=True,
        label="Калории",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Калории",
            }
        ),
    )
    Description = forms.CharField(
        required=True,
        label="Описание",
        max_length=1024,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Описание",
                "style": "height:100px",
            }
        ),
    )
    Recipe = forms.CharField(
        required=True,
        label="Рецепт",
        max_length=1024,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Рецепт",
                "style": "height:100px",
            }
        ),
    )
    RichOfVitamins = forms.MultipleChoiceField(
        required=True,
        label="Витамины",
        choices=get_vitamins(),
        widget=forms.CheckboxSelectMultiple(),
    )
    Allergy = forms.MultipleChoiceField(
        required=False,
        label="Аллергия",
        choices=get_allergy(),
        widget=forms.CheckboxSelectMultiple(),
    )
    TypeOfDish = forms.MultipleChoiceField(
        required=True,
        label="Тип блюда",
        choices=get_dish_type(),
        widget=forms.CheckboxSelectMultiple(),
    )
    PlaceOfDish = forms.MultipleChoiceField(
        required=True,
        label="Место блюда",
        choices=get_place_of_dish(),
        widget=forms.CheckboxSelectMultiple(),
    )


class ProfileChangeForm(forms.Form):
    """
    Форма смены данных пользователя
    """

    username = forms.CharField(
        required=False,
        label="",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Имя",
                "style": "height:40px",
            }
        ),
    )

    height = forms.CharField(
        required=False,
        label="",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Рост",
                "style": "height:40px",
            }
        ),
    )
    weight = forms.CharField(
        required=False,
        label="",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Вес",
                "style": "height:40px",
            }
        ),
    )
    age = forms.CharField(
        required=False,
        label="",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Возраст",
                "style": "height:40px",
            }
        ),
    )
    style = forms.ChoiceField(
        label="",
        required=False,
        choices=get_LyfeStyleOptions(),
    )
    gender = forms.ChoiceField(required=False, label="", choices={0: "Муж.", 1: "Жен."})


class PasswordChangeForm(forms.Form):
    """
    Форма смены пароля
    """

    old_password = forms.CharField(
        max_length=64,
        required=True,
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Пароль",
            }
        ),
    )
    new_password = forms.CharField(
        max_length=64,
        required=True,
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Новый пароль",
            }
        ),
    )
    repeat_new_password = forms.CharField(
        max_length=64,
        required=True,
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Повтор нового пароля",
            }
        ),
    )


class ChangeVitaminsForm(forms.Form):
    Vitamins = forms.MultipleChoiceField(
        label="Витамины",
        choices=get_vitamins(),
        widget=forms.CheckboxSelectMultiple(),
    )


class ChangeAllergyForm(forms.Form):
    Allergy = forms.MultipleChoiceField(
        label="Аллергия",
        choices=get_allergy(),
        widget=forms.CheckboxSelectMultiple(),
    )
