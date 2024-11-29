import requests
from typing import Tuple, Dict, Union


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email: str, password: str) -> Tuple[int, Union[Dict, str]]:
        """Получение API-ключа."""
        if not email or not password:
            return 400, {"error": "Email и пароль обязательны"}

        headers = {'email': email, 'password': password}
        try:
            res = requests.get(self.base_url + 'api/key', headers=headers)
            res.raise_for_status()
            return res.status_code, res.json()
        except requests.exceptions.RequestException as e:
            return 500, {"error": f"Ошибка запроса: {str(e)}", "response": res.text}

    def get_pets(self, auth_key: str, filter: str = "") -> Tuple[int, Union[Dict, str]]:
        """Получение списка питомцев."""
        headers = {"auth_key": auth_key}
        params = {"filter": filter}
        try:
            res = requests.get(self.base_url + 'api/pets', headers=headers, params=params)
            res.raise_for_status()
            return res.status_code, res.json()
        except requests.exceptions.RequestException as e:
            return 500, {"error": f"Ошибка запроса: {str(e)}", "response": res.text}

    def add_new_pet_simple(self, auth_key: str, name: str, animal_type: str, age: str) -> Tuple[int, Union[Dict, str]]:
        """Добавление нового питомца без фото."""
        if not all([name, animal_type, age]):
            return 400, {"error": "Все поля (name, animal_type, age) обязательны"}

        headers = {"auth_key": auth_key}
        data = {"name": name, "animal_type": animal_type, "age": age}

        try:
            res = requests.post(self.base_url + "api/create_pet_simple", headers=headers, data=data)
            res.raise_for_status()
            return res.status_code, res.json()
        except requests.exceptions.RequestException as e:
            return 500, {"error": f"Ошибка запроса: {str(e)}", "response": res.text}

    def add_new_pet_with_photo(self, auth_key: str, name: str, animal_type: str, age: str, photo_path: str) -> Tuple[
        int, Union[Dict, str]]:
        """Добавление нового питомца с фото."""
        if not all([name, animal_type, age, photo_path]):
            return 400, {"error": "Все поля (name, animal_type, age, photo_path) обязательны"}

        headers = {"auth_key": auth_key}
        data = {"name": name, "animal_type": animal_type, "age": age}

        try:
            with open(photo_path, 'rb') as pet_photo:
                files = {'pet_photo': pet_photo}
                res = requests.post(self.base_url + "api/pets", headers=headers, data=data, files=files)
                res.raise_for_status()
                return res.status_code, res.json()
        except FileNotFoundError:
            return 400, {"error": "Файл фото не найден"}
        except requests.exceptions.RequestException as e:
            return 500, {"error": f"Ошибка запроса: {str(e)}"}

    def add_pet_photo(self, auth_key: str, pet_id: str, photo_path: str) -> Tuple[int, Union[Dict, str]]:
        """Добавление фото питомца."""
        headers = {"auth_key": auth_key}
        try:
            with open(photo_path, 'rb') as pet_photo:
                files = {"pet_photo": pet_photo}
                res = requests.post(self.base_url + f'api/pets/set_photo/{pet_id}', headers=headers, files=files)
                res.raise_for_status()
                return res.status_code, res.json()
        except FileNotFoundError:
            return 400, {"error": "Файл фото не найден"}
        except requests.exceptions.RequestException as e:
            return 500, {"error": f"Ошибка запроса: {str(e)}"}

    def delete_pet(self, auth_key: str, pet_id: str) -> Tuple[int, Union[Dict, str]]:
        """Удаление питомца."""
        headers = {"auth_key": auth_key}
        try:
            res = requests.delete(self.base_url + f'api/pets/{pet_id}', headers=headers)
            res.raise_for_status()
            return res.status_code, {"message": "Питомец удалён успешно"}
        except requests.exceptions.RequestException as e:
            return 500, {"error": f"Ошибка запроса: {str(e)}", "response": res.text}
