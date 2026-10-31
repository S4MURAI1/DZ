Папка lesson_07

Файлы:
- calculator_page.py — Page Object калькулятора
- login_page.py — Page Object авторизации SauceDemo
- inventory_page.py — Page Object каталога
- cart_page.py — Page Object корзины
- checkout_page.py — Page Object оформления заказа
- test_01_calculator.py — тест калькулятора (Chrome)
- test_02_shop.py — тест магазина (Firefox)

Установка зависимостей:
    python -m pip install selenium pytest

Запуск из папки lesson_07:
    python -m pytest test_01_calculator.py
    python -m pytest test_02_shop.py

Важно:
1. Для Chrome и Firefox браузеры должны быть установлены.
2. Selenium 4.6+ умеет автоматически подбирать драйвер через Selenium Manager.
3. Перед запуском test_02_shop.py замените Ivan, Ivanov и 12345 на свои данные.
4. Тест калькулятора ожидает появления результата 15 через явное ожидание;
   time.sleep() не используется.
