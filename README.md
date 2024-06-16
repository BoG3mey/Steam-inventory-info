# Steam inventory info
Это простая программа для получения списка предметов из инвентаря Steam по SteamID64. По умолчанию используется игра CS2 (app_id=730), но вы можете изменить app_id на другую игру.

Программа создана без Steam API Key

# Функции
Запрос инвентаря: Получает список предметов из инвентаря Steam по SteamID64
Отображение предметов: Показывает информацию о каждом предмете (название, тип, возможность продажи на рынке)
## Использование
1. Установите необходимые библиотеки (pip install requests)
2. При запуске введите SteamID64 профиля Steam
3. Если вы хотите изменить игру, замените значение переменной app_id в коде программы (по умолчанию установлено app_id=730 для CS2)

# Пример

Предметы инвентаря:
Name: AK-47 | Redline
Type: Rifle
Marketable: Yes

Name: Desert Eagle | Blaze
Type: Pistol
Marketable: No


This project is created by [abik](https://github.com/BoG3mey).
