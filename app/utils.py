from flask import Flask
class TestClientLogin():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, app: Flask, username: str, password: str):
        self.app = app
        self.username = username
        self.password = password
    def test_get_request(self, url: str, user_db, user_id: int):
        with self.app.app_context():
            user = user_db.query.get(user_id)
            with self.app.test_client(user) as client:
                print(client.get(url))

    def test_post_request(self, url: str, user_db, user_id: int, data: {}):
        with self.app.app_context():
            user = user_db.query.get(user_id)
            with self.app.test_client(user) as client:
                print(client.post(url, data=data))