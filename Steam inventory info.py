import requests
app_id= 730
def get_inventory_items(steam_id, context_id=2):
    """
    Получает список предметов из инвентаря Steam по SteamID64.
    """
    url = f'http://steamcommunity.com/inventory/{steam_id}/{app_id}/{context_id}'
    try:
        response = requests.get(url).json()
        if 'descriptions' in response:
            return response['assets'], response['descriptions']
        else:
            print(f"Ошибка при получении предметов: {response.get('message', 'Неизвестная ошибка')}")
            return None
    except requests.RequestException as e:
        print(f"Ошибка HTTP запроса: {e}")
        return None

def main():
    steam_id = input("Введите SteamID64 профиля Steam: ")
    assets, descriptions = get_inventory_items(steam_id)
    if assets:
        print("Предметы инвентаря:")
        for asset in assets:
            classid = asset['classid']
            for description in descriptions:
                if description['classid'] == classid:
                    print(f"Name: {description['name']}")
                    print(f"Type: {description['type']}")
                    print(f"Marketable: {'Yes' if description['marketable'] else 'No'}")
                    print('---')
    else:
        print("Не удалось получить предметы инвентаря.")

if __name__ == '__main__':
    main()