"""
Модуль отображения страниц пользователя
"""

from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import (
    login as django_login,
    authenticate,
    logout as django_logout,
)
from main.forms import (
    RegistrationForm,
    LoginForm,
    NewDishForm,
    ProfileChangeForm,
    PasswordChangeForm,
    ChangeVitaminsForm,
    ChangeAllergyForm,
)
from main.models import Users, Dish, Diet
from main.ration_generator import generate_ration
from main.utility import (
    get_base_context,
    get_vitamins_string,
    get_allergy_string,
    get_valid_data_hwa,
    get_invalid_data_hwa,
    get_invalid_data_lp,
    get_filtered_data,
    get_vitamins_for_profile,
    get_allergy_from_profile,
    get_profile_context,
    get_vitamins,
)


def index_page(request: WSGIRequest) -> HttpResponse:
    """
    Главная страница, здесь можно сгенерировать своё блюдо!
    """
    context = get_base_context(request, "HalfATangarine", "HalfATangarine")
    if request.user.is_authenticated:
        context["name_of_user"] = request.user.username
    if request.method == "POST":
        generate_ration(request)
        return redirect("plan_of_day")
    return render(request, "pages/index.html", context)


def registration(request: WSGIRequest) -> HttpResponse:
    """
    Страница регистрации пользователя
    """
    print("Начало")
    context = get_base_context(
        request,
        "Регистрация",
        "Регистрация",
    )
    context["form"] = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        password = form.data["password"]
        repeatpassword = form.data["RepeatPassword"]
        if form.is_valid() and password == repeatpassword:
            username = form.data["username"]
            if Users.objects.filter(username=username).exists():
                messages.info(request, "Пользователь с вашим именем уже существует!!!!")
                return redirect("/")
            password = form.data["password"]
            height = form.data["Height"]
            weight = form.data["Weight"]
            gender = form.data["Gender"]
            age = form.data["Age"]
            if form.data.get("Vitamins") is None:
                vitamins_string = ""
            else:
                vitamins = form.cleaned_data.get("Vitamins")
                vitamins_string = get_vitamins_string(vitamins)
            isbadhabits = form.data.get("IsBadHabits")
            if form.data.get("Allergy") is None:
                allergy_string = ""
            else:
                allergy = form.cleaned_data.get("Allergy")
                allergy_string = get_allergy_string(allergy)
            lifestyle = form.data["LifeStyle"]
            if isbadhabits == "on":
                isbadhabits = 1
            else:
                isbadhabits = 0
            if get_valid_data_hwa(request, height, weight, age):
                user = Users(
                    username=username,
                    password=password,
                    Height=height,
                    Weight=weight,
                    Gender=gender,
                    Age=age,
                    Vitamins=vitamins_string,
                    IsBadHabits=isbadhabits,
                    Allergy=allergy_string,
                    LifeStyle=lifestyle,
                )
                user.set_password(user.password)
                user.save()
                diet = Diet(
                    BreakFast1=1,
                    BreakFast2=1,
                    BreakFast3=1,
                    Lunch1=1,
                    Lunch2=1,
                    Lunch3=1,
                    Dinner1=1,
                    Dinner2=1,
                    Dinner3=1,
                    BreakFast_id=1,
                    Dinner_id=1,
                    Lunch_id=1,
                    User_id=1,
                )
                diet.save()
                messages.success(request, "Вы успешно зарегестрировались!")
                auth_user = authenticate(request, username=username, password=password)
                if auth_user is not None:
                    django_login(request, user)
                    messages.success(request, f"Привет, {username.title()}, с возвращением!!")
                    return redirect("/")
            else:
                messages.info(request, get_invalid_data_hwa(height, weight, age))
            return redirect("/")
        else:
            messages.info(request, get_invalid_data_lp(password, repeatpassword))
            return redirect("/")
    return render(request, "pages/registration.html", context)


def login(request: WSGIRequest) -> HttpResponse:
    """
    Страница входа пользователя
    """
    context = get_base_context(request, "Login", "Login")
    context["form"] = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)
                messages.success(request, f"Привет, {username.title()}, с возвращением!!")
                return redirect("/")
            messages.info(request, "Некорректные данные в форме авторизации!")
            return redirect("login")
    return render(request, "pages/login.html", context)


def logout(request: WSGIRequest) -> HttpResponse:
    """
    Выход пользователя
    """
    django_logout(request)
    messages.add_message(request, messages.INFO, "Вы успешно вышли из аккаунта")
    return redirect("/")


@login_required
def new_dish(request: WSGIRequest) -> HttpResponse:
    """
    Страница создания нового блюда
    """
    context = get_base_context(request, "Создание нового блюда", "Создание нового блюда")
    context["form"] = NewDishForm()
    if request.method == "POST":
        form = NewDishForm(request.POST)
        if form.is_valid():
            title = form.data["Title"]
            carbohydrates = form.data["Carbohydrates"]
            protein = form.data["Protein"]
            fats = form.data["Fats"]
            calories = form.data["Calories"]
            description = form.data["Description"]
            recipe = form.data["Recipe"]
            if form.data.get("RichOfVitamins") is None:
                richofvitamins = ""
            else:
                richofvitamins = form.cleaned_data.get("RichOfVitamins")
                richofvitamins = get_vitamins_string(richofvitamins)
            if form.data.get("Allergy") is None:
                allergy = ""
            else:
                allergy = form.cleaned_data.get("Allergy")
                allergy = get_allergy_string(allergy)
            typeofdish = form.data.get("TypeOfDish")
            place_of_dish = form.data.get("PlaceOfDish")
            richofvitamins = list(richofvitamins)
            if richofvitamins[-1] == " ":
                richofvitamins = richofvitamins[:-1]
            if " " in richofvitamins:
                for i in range(len(richofvitamins)):
                    if richofvitamins[i] == " ":
                        richofvitamins[i] = ", "
            richofvitamins = "".join(richofvitamins)
            allergy = list(allergy)
            if allergy[-1] == " ":
                allergy = allergy[:-1]
            if " " in allergy:
                for i in range(len(allergy)):
                    if allergy[i] == " ":
                        allergy[i] = ", "
            allergy = "".join(allergy)
            id_of_dish = len(Dish.objects.all()) + 1
            dish_save = Dish(
                id=id_of_dish,
                Title=title,
                Carbohydrates=carbohydrates,
                Protein=protein,
                Fats=fats,
                Calories=calories,
                Description=description,
                Recipe=recipe,
                Allergy=allergy,
                RichVitamins=richofvitamins,
                TypeOfDish=typeofdish,
                PlaceOfDish=place_of_dish,
            )
            dish_save.save()
            messages.success(request, "Блюдо создано!")
            return redirect("/")
        messages.info(request, "Произошла неизвестная ошибка!")
        return redirect("/")
    return render(request, "pages/new_dish.html", context)


@login_required
def dish(request: WSGIRequest) -> HttpResponse:
    """
    Страница блюда
    """
    context = get_base_context(request, "", "Блюда")

    return render(request, "pages/dish.html", context)


@login_required
def filtred_dish(request: WSGIRequest, filter_id: str) -> HttpResponse:
    """
    Страница отфильтрованных блюд,
    здесь можно посмотреть информацию по блюду,
    которое отфильтровал пользователь
    """
    context = get_base_context(request, "", "Отфильтрованные блюда")
    filtered_data = get_filtered_data(int(filter_id))
    context["filtered_data"] = filtered_data
    return render(request, "pages/filtered_dish.html", context)


@login_required
def plan_of_day(request: WSGIRequest) -> HttpResponse:
    """
    Страница плана дня, здесь можно посмотреть сгенерированное меню!
    """
    context = get_base_context(request, "", "План дня")
    context["breakfast_dishes1"] = Dish.objects.get(
        id=Diet.objects.get(id=request.user.id).BreakFast1
    )
    context["breakfast_dishes2"] = Dish.objects.get(
        id=Diet.objects.get(id=request.user.id).BreakFast2
    )
    context["breakfast_dishes3"] = Dish.objects.get(
        id=Diet.objects.get(id=request.user.id).BreakFast3
    )
    context["lunch_dishes1"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch1)
    context["lunch_dishes2"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch2)
    context["lunch_dishes3"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch3)
    context["dinner_dishes1"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner1)
    context["dinner_dishes2"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner2)
    context["dinner_dishes3"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner3)
    context["calories1"] = (
        Dish.objects.get(id=Diet.objects.get(id=request.user.id).BreakFast1).Calories
        + Dish.objects.get(id=Diet.objects.get(id=request.user.id).BreakFast2).Calories
        + Dish.objects.get(id=Diet.objects.get(id=request.user.id).BreakFast3).Calories
    )
    context["calories2"] = (
        Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch1).Calories
        + Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch2).Calories
        + Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch3).Calories
    )
    context["calories3"] = (
        Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner1).Calories
        + Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner2).Calories
        + Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner3).Calories
    )

    return render(request, "pages/plan_of_day.html", context)


@login_required
def ration(request: WSGIRequest, ration_id: str) -> HttpResponse:
    """
    Страница рациона питания,
    отображает информацию по завтраку/обуд/ужину,
    в зависимости от выбора пользователя!
    """
    context = get_base_context(request, "", "Рацион")
    if ration_id == "1":  # Завтрак
        context["CarboHydrates1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast1
        ).Carbohydrates
        context["Protein1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast1
        ).Protein
        context["Fats1"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).BreakFast1).Fats
        context["Calories1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast1
        ).Calories
        context["Title1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast1
        ).Title
        context["Description1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast1
        ).Description
        context["Recipe1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast1
        ).Recipe
        context["CarboHydrates2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast2
        ).Carbohydrates
        context["Protein2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast2
        ).Protein
        context["Fats2"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).BreakFast2).Fats
        context["Calories2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast2
        ).Calories
        context["Title2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast2
        ).Title
        context["Description2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast2
        ).Description
        context["Recipe2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast2
        ).Recipe
        context["CarboHydrates3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast3
        ).Carbohydrates
        context["Protein3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast3
        ).Protein
        context["Fats3"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).BreakFast3).Fats
        context["Calories3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast3
        ).Calories
        context["Title3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast3
        ).Title
        context["Description3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast3
        ).Description
        context["Recipe3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).BreakFast3
        ).Recipe
    elif ration_id == "2":  # Обед
        context["CarboHydrates1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch1
        ).Carbohydrates
        context["Protein1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch1
        ).Protein
        context["Fats1"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch1).Fats
        context["Calories1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch1
        ).Calories
        context["Title1"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch1).Title
        context["Description1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch1
        ).Description
        context["Recipe1"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch1).Recipe
        context["CarboHydrates2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch2
        ).Carbohydrates
        context["Protein2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch2
        ).Protein
        context["Fats2"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch2).Fats
        context["Calories2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch2
        ).Calories
        context["Title2"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch2).Title
        context["Description2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch2
        ).Description
        context["Recipe2"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch2).Recipe
        context["CarboHydrates3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch3
        ).Carbohydrates
        context["Protein3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch3
        ).Protein
        context["Fats3"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch3).Fats
        context["Calories3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch3
        ).Calories
        context["Title3"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch3).Title
        context["Description3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Lunch3
        ).Description
        context["Recipe3"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Lunch3).Recipe
    elif ration_id == "3":  # Ужин
        context["CarboHydrates1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner1
        ).Carbohydrates
        context["Protein1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner1
        ).Protein
        context["Fats1"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner1).Fats
        context["Calories1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner1
        ).Calories
        context["Title1"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner1).Title
        context["Description1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner1
        ).Description
        context["Recipe1"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner1
        ).Recipe
        context["CarboHydrates2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner2
        ).Carbohydrates
        context["Protein2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner2
        ).Protein
        context["Fats2"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner2).Fats
        context["Calories2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner2
        ).Calories
        context["Title2"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner2).Title
        context["Description2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner2
        ).Description
        context["Recipe2"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner2
        ).Recipe
        context["CarboHydrates3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner3
        ).Carbohydrates
        context["Protein3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner3
        ).Protein
        context["Fats3"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner3).Fats
        context["Calories3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner3
        ).Calories
        context["Title3"] = Dish.objects.get(id=Diet.objects.get(id=request.user.id).Dinner3).Title
        context["Description3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner3
        ).Description
        context["Recipe3"] = Dish.objects.get(
            id=Diet.objects.get(id=request.user.id).Dinner3
        ).Recipe
    return render(request, "pages/ration.html", context)


@login_required
def dish_list(request: WSGIRequest) -> HttpResponse:
    """
    Страница всех блюд, которые может съесть пользователь!
    """
    context = get_base_context(request, "", "Список блюд")
    dishes = Dish.objects.all()
    context["AllDishes"] = dishes
    return render(request, "pages/dish_list.html", context)


@login_required
def profile(request: WSGIRequest) -> HttpResponse:
    """
    Страница профиля пользователя
    """
    context = get_profile_context(request)
    context["vitamins"] = get_vitamins_for_profile(request)
    context["allergies"] = get_allergy_from_profile(request)
    context["change_profile_form"] = ProfileChangeForm()
    context["change_password_form"] = PasswordChangeForm()
    context["change_vitamins_form"] = ChangeVitaminsForm()
    context["change_allergy_form"] = ChangeAllergyForm()
    if request.method == "POST" and "ChangeProfile" in request.POST:
        form = ProfileChangeForm(request.POST)
        if form.is_valid():
            username = form.data.get("username")
            height = form.data.get("height")
            weight = form.data.get("weight")
            gender = form.data.get("gender")
            style = form.data.get("style")
            age = form.data.get("age")
            if username != "":
                request.user.username = username
            if height != "":
                request.user.Height = height
            if weight != "":
                request.user.Weight = weight
            if gender != request.user.Gender:
                request.user.Gender = gender
            if age != "":
                request.user.Age = age
            if style != request.user.LifeStyle:
                request.user.LifeStyle = style
            if username != "":
                if len(username) > 50:
                    messages.info(
                        request,
                        "Вы ввели слишком длинное имя",
                    )
                    return redirect("profile")
            if weight != "":
                if int(weight) > 800 or int(weight) < 10:
                    messages.info(
                        request,
                        "Вы ввели некорректный возраст",
                    )
                    return redirect("profile_change")
            if height != "":
                if int(height) > 333 or int(height) < 50:
                    messages.info(
                        request,
                        "Вы ввели некорректный возраст",
                    )
                    return redirect("profile")
            if age != "":
                if int(age) > 200 or int(age) < 0:
                    messages.info(
                        request,
                        "Вы ввели некорректный возраст",
                    )
                    return redirect("profile")
            request.user.save()
            return redirect("profile")
    elif request.method == "POST" and "ChangePassword" in request.POST:
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            old_password = form.data.get("old_password")
            new_password = form.data.get("new_password")
            repeat_new_password = form.data.get("repeat_new_password")
            if new_password == repeat_new_password and check_password(
                old_password, request.user.password
            ):
                if len(new_password) < 4 and new_password != "":
                    messages.info(
                        request,
                        "Слишком короткий пароль (минимум 4 символа)",
                    )
                else:
                    request.user.set_password(new_password)
                    request.user.save()
            else:
                return redirect("profile")
    elif request.method == "POST" and "ChangeVitamins" in request.POST:
        form = ChangeVitaminsForm(request.POST)
        if form.is_valid():
            vitamins = form.cleaned_data.get("Vitamins")
            vitamins_string = get_vitamins_string(vitamins)
            request.user.Vitamins = vitamins_string
            request.user.save()
            return redirect("profile")
    elif request.method == "POST" and "ChangeAllergy" in request.POST:
        form = ChangeAllergyForm(request.POST)
        if form.is_valid():
            allergy = form.cleaned_data.get("Allergy")
            allergy_string = get_allergy_string(allergy)
            request.user.Allergy = allergy_string
            request.user.save()
            return redirect("profile")
    return render(request, "pages/profile.html", context)


def current_dish(request: WSGIRequest, dish_id: int) -> HttpResponse:
    """
    Страница для конкретного блюда
    """
    context = get_base_context(request, "", "Блюдо")
    dishes = Dish.objects.filter(id=dish_id)
    context["dish_title"] = dishes[0].Title
    context["dish_description"] = dishes[0].Description
    context["carbohydrates"] = dishes[0].Carbohydrates
    context["protein"] = dishes[0].Protein
    context["fats"] = dishes[0].Fats
    context["calories"] = dishes[0].Calories
    context["recipe"] = dishes[0].Recipe
    vitamins_dict = get_vitamins()
    vitamins_list = []
    for i in range(1, 14):
        if str(i) in dishes[0].RichVitamins:
            vitamins_list.append(vitamins_dict[i])
    send_vitamins = ""
    for i in range(len(vitamins_list)):
        send_vitamins += " " + str(vitamins_list[i])
    context["vitamin"] = send_vitamins
    return render(request, "pages/current_dish.html", context)
