
from bp_posts.views import CommentDAO


class TestCommentsDAO: #Тест на комментарии

    def test_foo(self):
        comment_dao_instance = CommentDAO("./bp_posts/test/comment_mock.json")
        return comment_dao_instance

        assert type(CommentDAO()._load_comments()) == list
        
        

