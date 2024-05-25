from main.models import Users, Dish, Diet


def calories(Users) -> None:
    if Users.Gender == 0:  # man
        calorie = 88.362 + 13.397 * Users.Weight + 4.799 * Users.Height - 5.677 * Users.Age
    else:  # woman
        calorie = 447.593 + 9.247 * Users.Weight + 3.098 * Users.Height - 4.330 * Users.Age

    if Users.LifeStyle == 0:
        calorie *= 1.2
    elif Users.LifeStyle == 1:
        calorie *= 1.4
    else:  # LifeStyle == 2
        calorie *= 1.6

    # курение надо бы добавить

    protein = calorie / 4
    carbohydrate = calorie / 2
    fat = calorie / 4

    breakfast = calorie * 0.3
    lunch = calorie * 0.4
    dinner = calorie * 0.3

    n = Dish.objects.all().count()
    breakfast_diff = []
    lunch_diff = []
    dinner_diff = []

    # витамины тоже надо бы добавить

    for i in range(n):
        dishes = Dish.objects.get(id=n)
        delta = (
            abs(dishes.Calories - breakfast)
            + abs(dishes.Protein - protein)
            + abs(dishes.Carbohydrates - carbohydrate)
            + abs(dishes.Fats - fat)
        )
        breakfast_diff[i] = delta
    b = Dish.objects(id=breakfast_diff.index(min(lunch_diff)))

    for i in range(n):
        dishes = Dish.objects.get(id=n)
        delta = (
            abs(dishes.Calories - lunch)
            + abs(dishes.Protein - protein)
            + abs(dishes.Carbohydrates - carbohydrate)
            + abs(dishes.Fats - fat)
        )
        lunch_diff[i] = delta
    l = Dish.objects(id=lunch_diff.index(min(lunch_diff)))

    for i in range(n):
        dishes = Dish.objects.get(id=n)
        delta = (
            abs(dishes.Calories - dinner)
            + abs(dishes.Protein - protein)
            + abs(dishes.Carbohydrates - carbohydrate)
            + abs(dishes.Fats - fat)
        )
        dinner_diff[i] = delta
    d = Dish.objects(id=dinner_diff.index(min(dinner_diff)))

    if Diet.objects.filter(User=Users).exists():
        diet = Dish.objects.get(User=Users)
        diet.BreakFast = b
        diet.Lunch = l
        diet.Dinner = d
        diet.save()

    else:
        diet = Diet(BreakFast=b, Lunch=l, Dinner=d, User=Users)
        diet.save()
