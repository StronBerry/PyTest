import requests

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email: str, password: str):
        """Получение API-ключа"""
        headers = {
            'email': email,
            'password': password,
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except Exception as e:
            result = res.text
        return status, result


    def get_pets(self, auth_key: str, filter: str = ""):
        """Получение списка питомцев"""
        headers = {"auth_key": auth_key}
        params = {"filter": filter}
        res = requests.get(self.base_url + 'api/pets', headers=headers, params=params)
        return res.status_code, res.json()

    def add_new_pet_simple(self, auth_key: str, name: str, animal_type: str, age: str):
        """Добавление нового питомца без фото."""
        data = {
            "name": name,
            "animal_type": animal_type,
            "age": age
        }
        headers = {"auth_key": auth_key}
        res = requests.post(self.base_url + "api/create_pet_simple", headers=headers, data=data)
        return res.status_code, res.json()


    def add_new_pet_with_photo(self, auth_key: str, name: str, animal_type: str, age: str, photo_path: str):
        """Добавление нового питомца с фото."""
        data = {
            "name": name,
            "animal_type": animal_type,
            "age": age
        }
        files = {
            'pet_photo': open(photo_path, 'rb')  # Открытие фото в бинарном режиме
        }
        headers = {"auth_key": auth_key}

        try:
            res = requests.post(self.base_url + "api/pets", headers=headers, data=data, files=files)
        finally:
            files['pet_photo'].close()  # Закрытие файла после использования

        return res.status_code, res.json()

    def add_pet_photo(self, auth_key: str, pet_id: str, photo_path: str):
        """Добавление фото питомца"""
        headers = {"auth_key": auth_key}
        files = {"pet_photo": open(photo_path, "rb")}
        res = requests.post(self.base_url + f'api/pets/set_photo/{pet_id}', headers=headers, files=files)
        return res.status_code, res.json()

    def delete_pet(self, auth_key: str, pet_id: str):
        """Удаление питомца"""
        headers = {"auth_key": auth_key}
        res = requests.delete(self.base_url + f'api/pets/{pet_id}', headers=headers)
        return res.status_code, res.text

    def update_pet(self, api_key, pet_id, name, animal_type, age):
        """Метод обновления данных питомца"""
        headers = {"auth_key": api_key}
        data = {
            "name": name,
            "animal_type": animal_type,
            "age": age
        }
        res = requests.put(f"{self.base_url}/api/pets/{pet_id}", headers=headers, data=data)
        return res.status_code, res.json()
