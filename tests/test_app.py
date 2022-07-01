import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Portfolio Template</title>" in html
        assert '<meta charset="utf-8" />' in html
        assert '<html lang="en">' in html
        assert '<!DOCTYPE html>' in html
        

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        response = self.client.post("/api/timeline_post", data={
            "name": "John" ,"email": "john@example.com",
            "content": "hi my name is john"})
        assert response.status_code == 200
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1

    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "hi my name is john"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html
        
        response = self.client.post("/api/timeline_post", data={
            "name": "John" ,
            "content": "hi my name is john"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

        response = self.client.post("/api/timeline_post", data={
            "name": "John" ,"email": "john@example.com",
            })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html
    


































