# Half a tangerine
## Что это?
**Half a tangerine** предлагает персонализированные рекомендации по питанию, учитывая индивидуальные потребности и предпочтения пользователя. Сайт помогает составить сбалансированное меню на день, учитывая не только калорийность, но и содержание белков, жиров, углеводов, витаминов, а также учитывая образ жизни. Благодаря Half a tangerine пользователь может получить информацию о питании и рецепты блюд, соответствующих его потребностям.
## Как установить
### Требования
Для установки и запуска, нужен [Python 3+](https://python.org) и [Git](https://git-scm.com/)
### Процесс установки
1. Клонировать репозиторий
```
git clone https://github.com/SanyaLikeIT/Diet_Service.git
```
2. Установить все нужные библиотеки
```
pip install -r requirements.txt
```
3. Сделать миграцию
```
python manage.py migrate
```
## Как запустить сервер
1. В терминале прописать команду для запуска локального сервера 
```
python manage.py runserver
```
2. Открыть локальный сайт [http://127.0.0.1:8000/](http://127.0.0.1:8000)
