from urllib import response
import pytest
import requests
import os
from dotenv import load_dotenv
from pprint import pprint
import unittest


dotenv_path = 'config_MY.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class TestYandexDiskAPI(unittest.TestCase):
    API_URL = "https://cloud-api.yandex.net/v1/disk/resources"
    TOKEN = os.getenv("YA_token")
    HEADERS = {"Authorization": f"OAuth {TOKEN}"}

    def folder_name(self):
        return "test_folder"

    def test_create_folder_success(self):
        """Тест успешного создания папки"""
        self.params = {"path": f"/{folder_name}"}
        self.response = requests.put(self.API_URL, headers=self.HEADERS, params=self.params)
                # Проверяем код ответа
        self.assertEqual(response.status_code, 201)
        
        # Проверяем, что папка действительно создалась
        check_response = requests.get(self.API_URL, headers=self.HEADERS, params=self.params)
        self.assertEqual(check_response.status_code, 200)
    def test_create_folder_already_exists(self, folder_name, requests=None):
        """Тест попытки создания уже существующей папки"""
        params = {"path": f"/{folder_name}"}
        response = requests.put(self.API_URL, headers=self.HEADERS, params=self.params)
        # Должны получить 409 Conflict, если папка уже существует
        self.assertEqual(response.status_code, 409)
        self.assertIn("уже существует", response.json()["description"])
    def test_create_folder_unauthorized(self, folder_name):
        """Тест попытки создания папки без авторизации"""
        params = {"path": f"/{folder_name}_unauth"}
        response = requests.put(self.API_URL, headers={"Authorization": "OAuth invalid_token"}, params=params)

        # Должны получить 401 Unauthorized
        self.assertEqual(response.status_code, 401)
        self.assertIn("Не авторизован", response.json()["description"])

    def test_create_folder_invalid_path(self):
        """Тест попытки создания папки с недопустимым именем"""
        invalid_names = ["", "  ", "invalid/name"]
        
        for name in invalid_names:
            params = {"path": f"/{name}"}
            response = requests.put(self.API_URL, headers=self.HEADERS, params=self.params)
            
            # Должны получить 400 Bad Request
            self.assertEqual(response.status_code, 400)

    def cleanup(self, folder_name):
        """функция для удаления тестовой папки после всех тестов"""

        params = {"path": f"/{folder_name}", "permanently": "true"}
        requests.delete(self.API_URL, headers=self.HEADERS, params=self.params)


if __name__ == '__main__':
    unittest.main()