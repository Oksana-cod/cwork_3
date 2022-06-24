import json
from json import JSONDecodeError

from bp_posts.dao.comment import Comment
from exceptions.data_excepoions import DataSourceError


class CommentDAO:   #менеджер абстракции

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

    def _load_comments(self):
        """Возвращает список экземпляров Comment"""
        comments_data = self._load_data()

        from bp_posts.dao.comment import Comment
        list_of_posts = [Comment(**comment_data) for comment_data in comments_data] #Распаковка не понятная
        comments = [Comment(**comment_data) for comment_data in comments_data]

        return list_of_posts

    def get_comments_by_post_pk(self, post_pk: int) -> list[Comment]:
        """Возвращает посты по pk"""
        comments: list[Comment] = self._load_comments()
        comments_match: list[Comment] = [c for c in comments if c.post_pk == post_pk]
        return comments_match


#cd = CommentDAO("../../data/comments.json")
#print(cd.get_comments_by_post_pk(2))



