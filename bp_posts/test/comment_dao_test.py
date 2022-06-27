from bp_posts.dao.comment import Comment
from bp_posts.views import CommentDAO


class TestCommentsDAO:  # Тест на комментарии

    def test_foo(self):
        comment_dao_instance = CommentDAO("./bp_posts/test/comment_mock.json")
        comments = comment_dao_instance._load_comments()
        assert type(comments) == list
        assert len(comments) > 0
        assert type(comments[0]) == Comment
        
        

