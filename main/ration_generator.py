"""
Модуль для генерации рациона питания для пользователя!
"""

import random
from django.core.handlers.wsgi import WSGIRequest
from main.models import Dish, Diet


def get_user_vitamins(request: WSGIRequest) -> list:
    """
    Возвращает список витамин пользователя
    """
    start_vitamin_string = request.user.Vitamins.split(" ")
    if start_vitamin_string[-1] == "":
        start_vitamin_string = start_vitamin_string[:-1]
    start_vitamin_string = list(map(int, start_vitamin_string))
    return start_vitamin_string


def get_normal_arr_of_vitamin_sort(request, arr):
    users_vitamins = get_user_vitamins(request)
    for i in range(len(arr)):
        s = get_normal_list_vitamins_of_dish(request, arr[i].RichVitamins)
        for j in range(len(s)):
            if s[j] in users_vitamins:
                arr.append(arr[i])
    return arr


def get_user_allergy(request: WSGIRequest) -> list:
    """
    Возвращает список витамин пользователя
    """
    start_vitamin_string = request.user.Allergy.split(" ")
    if start_vitamin_string[-1] == "":
        start_vitamin_string = start_vitamin_string[:-1]
    start_vitamin_string = list(map(int, start_vitamin_string))
    return start_vitamin_string


def get_normal_list_vitamins_of_dish(request: WSGIRequest, arr) -> list:
    arr = list(map(int, arr.split(",")))
    return arr


def generate_ration(request: WSGIRequest) -> None:
    """
    Функция, которая генерирует пользователю меню!
    """
    if request.user.Gender == 0:  # man
        need_calories_for_user = (
            88.362
            + 13.397 * request.user.Weight
            + 4.799 * request.user.Height
            - 5.677 * request.user.Age
        )
    else:  # woman
        need_calories_for_user = (
            447.593
            + 9.247 * request.user.Weight
            + 3.098 * request.user.Height
            - 4.330 * request.user.Age
        )
    if request.user.LifeStyle == 0:
        need_calories_for_user *= 1.2
    elif request.user.LifeStyle == 1:
        need_calories_for_user *= 1.4
    else:
        need_calories_for_user *= 1.6
    need_calories_for_user = round(need_calories_for_user)
    protein = round(need_calories_for_user / 4)
    carbohydrate = round(need_calories_for_user / 2)
    fat = round(need_calories_for_user / 4)
    breakfast = round(need_calories_for_user * 0.3)
    lunch = round(need_calories_for_user * 0.4)
    dinner = round(need_calories_for_user * 0.3)
    all_dishes = Dish.objects.all()
    filter_dish_by_allergy = []
    allergy_string = get_user_allergy(request)
    for i in range(len(all_dishes)):
        al = all_dishes[i].Allergy
        if isinstance(al, str):
            al = list(map(int, al.split(", ")))
            flag_to_add = True
            for j in range(len(al)):
                if al[j] in allergy_string:
                    flag_to_add = False
            if flag_to_add:
                filter_dish_by_allergy.append(all_dishes[i])
        else:
            if al not in allergy_string:
                filter_dish_by_allergy.append(all_dishes[i])
    dishes_for_breakfast = []
    dishes_for_lunch = []
    dishes_for_dinner = []
    for i in range(len(filter_dish_by_allergy)):
        if filter_dish_by_allergy[i].TypeOfDish == 1:
            dishes_for_breakfast.append(filter_dish_by_allergy[i])
        elif filter_dish_by_allergy[i].TypeOfDish == 2:
            dishes_for_lunch.append(filter_dish_by_allergy[i])
        elif filter_dish_by_allergy[i].TypeOfDish == 3:
            dishes_for_dinner.append(filter_dish_by_allergy[i])
    dishes_for_breakfast_first_place = []
    dishes_for_breakfast_second_place = []
    dishes_for_breakfast_third_place = []
    dishes_for_lunch_first_place = []
    dishes_for_lunch_second_place = []
    dishes_for_lunch_third_place = []
    dishes_for_dinner_first_place = []
    dishes_for_dinner_second_place = []
    dishes_for_dinner_third_place = []
    for i in range(len(dishes_for_breakfast)):
        if dishes_for_breakfast[i].PlaceOfDish == 1:
            dishes_for_breakfast_first_place.append(dishes_for_breakfast[i])
        if dishes_for_breakfast[i].PlaceOfDish == 2:
            dishes_for_breakfast_second_place.append(dishes_for_breakfast[i])
        if dishes_for_breakfast[i].PlaceOfDish == 3:
            dishes_for_breakfast_third_place.append(dishes_for_breakfast[i])
    for i in range(len(dishes_for_lunch)):
        if dishes_for_lunch[i].PlaceOfDish == 1:
            dishes_for_lunch_first_place.append(dishes_for_lunch[i])
        if dishes_for_lunch[i].PlaceOfDish == 2:
            dishes_for_lunch_second_place.append(dishes_for_lunch[i])
        if dishes_for_lunch[i].PlaceOfDish == 3:
            dishes_for_lunch_third_place.append(dishes_for_lunch[i])
    for i in range(len(dishes_for_dinner)):
        if dishes_for_dinner[i].PlaceOfDish == 1:
            dishes_for_dinner_first_place.append(dishes_for_dinner[i])
        if dishes_for_dinner[i].PlaceOfDish == 2:
            dishes_for_dinner_second_place.append(dishes_for_dinner[i])
        if dishes_for_dinner[i].PlaceOfDish == 3:
            dishes_for_dinner_third_place.append(dishes_for_dinner[i])
    elite_dishes_for_breakfast_first_place = list(
        set(get_normal_arr_of_vitamin_sort(request, dishes_for_breakfast_first_place))
    )
    elite_dishes_for_breakfast_second_place = list(
        set(get_normal_arr_of_vitamin_sort(request, dishes_for_breakfast_second_place))
    )
    elite_dishes_for_breakfast_third_place = list(
        set(get_normal_arr_of_vitamin_sort(request, dishes_for_breakfast_third_place))
    )
    elite_dishes_for_lunch_first_place = list(
        set(get_normal_arr_of_vitamin_sort(request, dishes_for_lunch_first_place))
    )
    elite_dishes_for_lunch_second_place = list(
        set(get_normal_arr_of_vitamin_sort(request, dishes_for_lunch_second_place))
    )
    elite_dishes_for_lunch_third_place = list(
        set(get_normal_arr_of_vitamin_sort(request, dishes_for_lunch_third_place))
    )
    elite_dishes_for_dinner_first_place = list(
        set(get_normal_arr_of_vitamin_sort(request, dishes_for_dinner_first_place))
    )
    elite_dishes_for_dinner_second_place = list(
        set(get_normal_arr_of_vitamin_sort(request, dishes_for_dinner_second_place))
    )
    elite_dishes_for_dinner_third_place = list(
        set(get_normal_arr_of_vitamin_sort(request, dishes_for_dinner_third_place))
    )
    if len(elite_dishes_for_breakfast_first_place) == 0:
        elite_dishes_for_breakfast_first_place.append(
            dishes_for_breakfast_first_place[
                random.randint(0, len(dishes_for_breakfast_first_place) - 1)
            ]
        )
    if len(elite_dishes_for_breakfast_second_place) == 0:
        elite_dishes_for_breakfast_second_place.append(
            dishes_for_breakfast_second_place[
                random.randint(0, len(dishes_for_breakfast_second_place) - 1)
            ]
        )
    if len(elite_dishes_for_breakfast_third_place) == 0:
        elite_dishes_for_breakfast_third_place.append(
            dishes_for_breakfast_third_place[
                random.randint(0, len(dishes_for_breakfast_third_place) - 1)
            ]
        )
    if len(elite_dishes_for_lunch_first_place) == 0:
        elite_dishes_for_lunch_first_place.append(
            dishes_for_lunch_first_place[random.randint(0, len(dishes_for_lunch_first_place) - 1)]
        )
    if len(elite_dishes_for_lunch_second_place) == 0:
        elite_dishes_for_lunch_second_place.append(
            dishes_for_lunch_second_place[random.randint(0, len(dishes_for_lunch_second_place) - 1)]
        )
    if len(elite_dishes_for_lunch_third_place) == 0:
        elite_dishes_for_lunch_third_place.append(
            dishes_for_lunch_third_place[random.randint(0, len(dishes_for_lunch_third_place) - 1)]
        )
    if len(elite_dishes_for_dinner_first_place) == 0:
        elite_dishes_for_dinner_first_place.append(
            dishes_for_dinner_first_place[random.randint(0, len(dishes_for_dinner_first_place) - 1)]
        )
    if len(elite_dishes_for_dinner_second_place) == 0:
        elite_dishes_for_dinner_second_place.append(
            dishes_for_dinner_second_place[
                random.randint(0, len(dishes_for_dinner_second_place) - 1)
            ]
        )
    if len(elite_dishes_for_dinner_third_place) == 0:
        elite_dishes_for_dinner_third_place.append(
            dishes_for_dinner_third_place[random.randint(0, len(dishes_for_dinner_third_place) - 1)]
        )
    random.shuffle(elite_dishes_for_breakfast_first_place)
    random.shuffle(elite_dishes_for_breakfast_second_place)
    random.shuffle(elite_dishes_for_breakfast_third_place)
    random.shuffle(elite_dishes_for_lunch_first_place)
    random.shuffle(elite_dishes_for_lunch_second_place)
    random.shuffle(elite_dishes_for_lunch_third_place)
    random.shuffle(elite_dishes_for_dinner_first_place)
    random.shuffle(elite_dishes_for_dinner_second_place)
    random.shuffle(elite_dishes_for_dinner_third_place)
    diet = Diet.objects.get(id=request.user.id)
    diet.BreakFast1 = elite_dishes_for_breakfast_first_place[0].id
    diet.BreakFast2 = elite_dishes_for_breakfast_second_place[0].id
    diet.BreakFast3 = elite_dishes_for_breakfast_third_place[0].id
    diet.Lunch1 = elite_dishes_for_lunch_first_place[0].id
    diet.Lunch2 = elite_dishes_for_lunch_second_place[0].id
    diet.Lunch3 = elite_dishes_for_lunch_third_place[0].id
    diet.Dinner1 = elite_dishes_for_dinner_first_place[0].id
    diet.Dinner2 = elite_dishes_for_dinner_second_place[0].id
    diet.Dinner3 = elite_dishes_for_dinner_third_place[0].id
    diet.save()
