"""
Модуль для вспомогательных функций!
"""

from django.core.handlers.wsgi import WSGIRequest

from main.models import Dish


def get_LyfeStyleOptions() -> dict:
    OPTIONS = {
        0: "Подвижный образ жизни",
        1: "Сидячий образ жизни",
        2: "Что-то среднее",
    }
    return OPTIONS


def get_dish_type() -> dict:
    Allergy = {
        1: "Завтрак",
        2: "Обед",
        3: "Ужин",
    }
    return Allergy


def get_place_of_dish() -> dict:
    place_of_dish = {
        1: "Первое",
        2: "Второе",
        3: "Напиток",
    }
    return place_of_dish


def get_allergy_string(allergy) -> str:
    """
    Получаем строку из аллергий(в числах), для удобной записи в БД
    """
    allergy_string = ""
    for i in allergy:
        allergy_string += i + " "
    return allergy_string


def get_vitamins_string(vitamins) -> str:
    """
    Получаем строку из витаминов(в числах), для удобной записи в БД
    """
    vitamins_string = ""
    for i in vitamins:
        vitamins_string += i + " "
    return vitamins_string


def get_vitamins() -> dict:
    """
    Получаем все витамины по числам
    """
    vitamins = {
        1: "A",
        2: "B1",
        3: "B2",
        4: "B3",
        5: "B5",
        6: "B6",
        7: "B7",
        8: "B9",
        9: "B12",
        10: "C",
        11: "D",
        12: "E",
        13: "K",
    }
    return vitamins


def get_allergy() -> dict:
    """
    Поулчаем все аллергии по числам
    """
    allergy = {
        1: "Молоко",
        2: "Яйца",
        3: "Орехи",
        4: "Рыба",
        5: "Соя",
        6: "Пшеница",
        7: "Цитрусовые",
        8: "Шоколад",
        9: "Колбасные изделия",
    }
    return allergy


def get_base_context(request, pagename, slidename) -> dict:
    """
    Возвращает имя страницы и заголовок страницы
    """
    return {
        "pagename": pagename,
        "slidename": slidename,
        "user": request.user,
    }


def get_vitamins_for_profile(request: WSGIRequest) -> list:
    """
    Возвращает витамины пользователя для их вывода в профиле
    """
    vitamins_from_user = list(map(int, (request.user.Vitamins).split()))
    all_vitamins = get_vitamins()
    vitamins = []
    for i in range(len(vitamins_from_user)):
        vitamins.append(all_vitamins[vitamins_from_user[i - 1]])
    return vitamins


def get_allergy_from_profile(request: WSGIRequest) -> list:
    """
    Возвращает аллергию пользователя для её вывода в профиле
    """
    allergy_from_user = list(map(int, (request.user.Allergy).split()))
    all_allergy = get_allergy()
    allergy = []
    for i in range(len(allergy_from_user)):
        allergy.append(all_allergy[allergy_from_user[i - 1]])
    return allergy


def get_filtered_data(filter_id: int) -> list:
    """
    Возвращает отсортированные по фильтрам блюда
    """
    list_of_all_filters: list = []
    # Фильтры по завтраку/обеду/ужину
    list_of_all_filters.append(Dish.objects.filter(TypeOfDish=1))
    list_of_all_filters.append(Dish.objects.filter(TypeOfDish=2))
    list_of_all_filters.append(Dish.objects.filter(TypeOfDish=3))
    # Фильтры по калориям
    list_of_all_filters.append(Dish.objects.filter(Calories__gte=50, Calories__lt=100))
    list_of_all_filters.append(Dish.objects.filter(Calories__gte=100, Calories__lt=200))
    list_of_all_filters.append(Dish.objects.filter(Calories__gte=200, Calories__lt=300))
    list_of_all_filters.append(Dish.objects.filter(Calories__gte=300, Calories__lt=400))
    list_of_all_filters.append(Dish.objects.filter(Calories__gte=400, Calories__lt=500))
    list_of_all_filters.append(Dish.objects.filter(Calories__gte=500, Calories__lt=600))
    list_of_all_filters.append(Dish.objects.filter(Calories__gte=600, Calories__lt=750))
    list_of_all_filters.append(Dish.objects.filter(Calories__gte=750, Calories__lt=1000))
    # Фильтры по витаминам
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="1")
    )  # фильтр по витамину A
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="2")
    )  # фильтр по витамину B1
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="3")
    )  # фильтр по витамину B2
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="4")
    )  # фильтр по витамину B3
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="5")
    )  # фильтр по витамину B5
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="6")
    )  # фильтр по витамину B6
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="7")
    )  # фильтр по витамину B7
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="8")
    )  # фильтр по витамину B9
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="9")
    )  # фильтр по витамину B12
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="10")
    )  # фильтр по витамину C
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="11")
    )  # фильтр по витамину D
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="12")
    )  # фильтр по витамину E
    list_of_all_filters.append(
        Dish.objects.filter(RichVitamins__contains="13")
    )  # фильтр по витамину K
    return list_of_all_filters[filter_id - 1]


def get_profile_context(request: WSGIRequest) -> dict:
    """
    возвращает контекст для профиля
    """
    context = get_base_context(request, "", "Профиль")
    context["username"] = request.user.username
    context["age"] = request.user.Age
    style = request.user.LifeStyle
    gender = request.user.Gender
    if style == 0:
        style = "Подвижный образ жизни"
    elif style == 1:
        style = "Сидячий образ жизни"
    else:
        style = '"Что-то среднее"'
    if gender == 0:
        gender = "муж."
    else:
        gender = "жен."
    context["style"] = style
    context["gender"] = gender
    context["weight"] = request.user.Weight
    context["height"] = request.user.Height
    return context


def get_valid_data_hwa(request: WSGIRequest, height: str, weight: str, age: str) -> bool:
    """
    Проверяет корректность роста, веса и возраста
    """
    true_counter = 0
    if int(height) >= 75 and int(height) <= 280:
        true_counter += 1
    if int(age) >= 0 and int(age) <= 200:
        true_counter += 1
    if int(weight) >= 10 and int(weight) <= 500:
        true_counter += 1
    if true_counter == 3:
        return True
    return False


def get_invalid_data_hwa(height: str, weight: str, age: str) -> str:
    """
    Если получились не корректные вес, рост или возраст, возвращает сообщение с уточнением проблемы
    """
    if int(height) < 75 or int(height) > 280:
        return "Пожалуйста введите корректный рост"
    if int(weight) < 10 or int(weight) > 500:
        return "Пожалуйста введите корректный вес"
    if int(age) < 0 and int(age) > 200:
        return "Пожалуйста введите корректный возраст"


def get_invalid_data_lp(password: str, repeatpassword: str) -> str:
    """
    Возвращает сообщение, если не корректный пароль или имя пользователя!
    """
    message = "Пожалуйста, придумайте более длинный пароль"
    if password != repeatpassword:
        message = "Вы ввели разные пароли"
    else:
        message = "Ваш логин занят, введите другой, пожалуйста"
    return message
