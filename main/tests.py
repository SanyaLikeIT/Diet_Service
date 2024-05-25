"""
Модуль для тестов сайта
"""

from django.test import TestCase, Client
from main.models import Users


class BaseTests:
    def setUp(self):
        self.client = Client()

    def logining(self):
        login_info = {
            "username": "TestCaseUser101",
            "password": "TestCasePassword101",
            "Height": 123,
            "Weight": 123,
            "Gender": 0,
            "Age": 123,
            "IsBadHabits": "1",
            "LifeStyle": 0,
            "Allergy": "1",
            "Vitamins": "3",
        }
        Users.objects.create_user(**login_info)
        response = self.client.post("/login/", login_info, follow=True)
        self.assertTrue(response.context["user"].is_active)


class IndexPageTestCase(TestCase):
    """
    Тесты для главной страницы
    """

    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get("/")

    def test_correct_status_code(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_check_pagename(self) -> None:
        self.assertEqual("HalfATangarine", self.response.context["pagename"])

    def test_check_slidename(self) -> None:
        self.assertEqual("HalfATangarine", self.response.context["slidename"])

    def test_check_templates(self) -> None:
        self.assertTemplateUsed(self.response, "pages/index.html")


class RegistrationPageTestCase(TestCase):
    """
    Тесты для страницы регистрации
    """

    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get("/registration/")

    def test_check_correct_status_code(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_check_pagename(self):
        self.assertEqual("Регистрация", self.response.context["pagename"])

    def test_check_slidename(self):
        self.assertEqual("Регистрация", self.response.context["slidename"])

    def test_check_templates(self) -> None:
        self.assertTemplateUsed(self.response, "pages/registration.html")


class LoginTestCase(TestCase):
    """
    Тесты для страницы входа
    """

    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get("/login/")

    def test_check_correct_status_code(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_check_pagename(self):
        self.assertEqual("Login", self.response.context["pagename"])

    def test_check_slidename(self):
        self.assertEqual("Login", self.response.context["slidename"])

    def test_check_templates(self) -> None:
        self.assertTemplateUsed(self.response, "pages/login.html")


class NewDishPageTestCase(TestCase, BaseTests):
    """
    Тесты для страницы создания нового блюда
    """

    def setUp(self) -> None:
        super().setUp()
        super().logining()
        self.response = self.client.get("/new_dish/")

    def test_check_correct_status_code(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_check_pagename(self):
        self.assertEqual("Создание нового блюда", self.response.context["pagename"])

    def test_check_slidename(self):
        self.assertEqual("Создание нового блюда", self.response.context["slidename"])

    def test_check_templates(self) -> None:
        self.assertTemplateUsed(self.response, "pages/new_dish.html")


class DishPageTestCase(TestCase, BaseTests):
    """
    Тесты для страницы с блюдами
    """

    def setUp(self) -> None:
        super().setUp()
        super().logining()
        self.response = self.client.get("/dish/")

    def test_check_correct_status_code(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_check_pagename(self):
        self.assertEqual("", self.response.context["pagename"])

    def test_check_slidename(self):
        self.assertEqual("Блюда", self.response.context["slidename"])

    def test_check_templates(self) -> None:
        self.assertTemplateUsed(self.response, "pages/dish.html")


class PlanOfDayPageTestCase(TestCase, BaseTests):
    """
    Тесты для страницы с планом дня
    """

    def setUp(self) -> None:
        super().setUp()
        super().logining()
        self.response = self.client.get("/plan_of_day/")

    def test_check_correct_status_code(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_check_pagename(self):
        self.assertEqual("", self.response.context["pagename"])

    def test_check_slidename(self):
        self.assertEqual("План дня", self.response.context["slidename"])

    def test_check_templates(self) -> None:
        self.assertTemplateUsed(self.response, "pages/plan_of_day.html")


class RationPageTestCase(TestCase, BaseTests):
    """
    Тесты для страницы рациона питания
    """

    def setUp(self) -> None:
        super().setUp()
        super().logining()
        self.response = self.client.get("/ration/")

    def test_check_correct_status_code(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_check_pagename(self):
        self.assertEqual("", self.response.context["pagename"])

    def test_check_slidename(self):
        self.assertEqual("Рацион", self.response.context["slidename"])

    def test_check_templates(self) -> None:
        self.assertTemplateUsed(self.response, "pages/ration.html")


class DishListPageTestCase(TestCase, BaseTests):
    """
    Тесты для страницы со списком блюд
    """

    def setUp(self) -> None:
        super().setUp()
        super().logining()
        self.response = self.client.get("/dish_list/")

    def test_check_correct_status_code(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_check_pagename(self):
        self.assertEqual("", self.response.context["pagename"])

    def test_check_slidename(self):
        self.assertEqual("Список блюд", self.response.context["slidename"])

    def test_check_templates(self) -> None:
        self.assertTemplateUsed(self.response, "pages/dish_list.html")


class ProfilePageTestCase(TestCase, BaseTests):
    """
    Тесты для страницы профиля
    """

    def setUp(self) -> None:
        super().setUp()
        super().logining()
        self.response = self.client.get("/profile/")

    def test_check_correct_status_code(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_check_pagename(self):
        self.assertEqual("", self.response.context["pagename"])

    def test_check_slidename(self):
        self.assertEqual("Профиль", self.response.context["slidename"])

    def test_check_templates(self) -> None:
        self.assertTemplateUsed(self.response, "pages/profile.html")
