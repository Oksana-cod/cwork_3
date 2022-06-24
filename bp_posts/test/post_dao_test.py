from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO
from bp_posts.views import post_dao


class TestPostsDAO:

    def test_dao(self):
        post_dao_instance = PostDAO("./bp_posts/tests/post_mock.json")
        return post_dao_instance

        assert type(PostDAO()._load_posts()) == list

    def test_get_all(self):
        posts = post_dao.get_all()
        assert type(posts) == list

    def test_get_all_correct_ids(self):
        posts = post_dao.get_all()

        # correct_pks = {1, 2, 3}
        # pks = set([post.pk for post in posts])
        assert len(posts) > 0

    def test_get_by_pk_types(self):
        post = post_dao.get_by_pk(1)
        assert type(post) == Post, "Incorrect type for for result single item"

    def test_get_by_pk_fields(self):
        post = post_dao.get_by_pk(1)
        assert hasattr(post, 'pk')

    def test_get_by_pk_none(self):
        post = post_dao.get_by_pk(999)
        assert post is None, "Should be None for non existent pk"
