import json
from bp_posts.dao.post import Post
from json import JSONDecodeError
from exceptions.data_excepoions import DataSourceError
from pprint import pprint as pp


class PostDAO:  # Менеджер постов
    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """Считывает и Загружает данные json"""
        try:
            with open(self.path, "r", encoding='utf-8') as file:
                posts_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f"Не удается получить данные из {self.path}")

        return posts_data

    def _load_posts(self):
        """Возвращает список экземпляров Post"""
        posts_data = self._load_data()

        list_of_posts = [Post(**post_data) for post_data in posts_data]  # Распаковка не понятная

        return list_of_posts

    def get_all(self):
        """:return class Post"""
        posts = self._load_posts()
        return posts

    def get_by_pk(self, pk):
        """Получает пост по рк"""
        if type(pk) != int:
            raise TypeError("pk не число")

        posts = self._load_posts()

        for post in posts:
            if post.pk == pk:
                return post
        else:
            return None  # "нет такого ID"

    def search_in_content(self, substring):
        """Поиск постов по substring (подстрока) """

        if type(substring) != str:
            raise TypeError("ошибка ввода")

        substring = str(substring).lower()
        posts = self._load_posts()
        matching_post = [post for post in posts if substring in post.content]
        return matching_post

    def get_by_poster(self, user_name):
        """Поиско поста по автору"""

        if type(user_name) != str:
            raise TypeError("ошибка ввода")

        user_name = str(user_name).lower()
        posts = self._load_posts()
        matching_post = [post for post in posts if post.poster_name == user_name]
        return matching_post

# pd = PostDAO("../../data/posts.json")
# pp(pd.get_by_pk())
