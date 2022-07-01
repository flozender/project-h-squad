import unittest
from peewee import *
from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email ='john@example.com',
                                         content='Hello world, I\'mJohn!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email ='jame@example.com',
                                         content='Hello world, I\'mJane!')
        assert second_post.id == 2
        assert first_post.name =='John Doe'
        assert second_post.name =='Jane Doe'
        assert first_post.email =='john@example.com'
        assert second_post.email =='jame@example.com'
        assert first_post.content =='Hello world, I\'mJohn!'
        assert second_post.content =='Hello world, I\'mJane!'
