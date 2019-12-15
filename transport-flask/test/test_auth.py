import unittest
from client import Client

"""
    使用requests.post()时, json={key:value}
"""

# 测试app的登录, 注册, 登出
class AppAuthTestCase(unittest.TestCase):

    # 固件
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        self.client = None

    # 在未登录时请求数据会被禁止
    def test_request_nologin(self):
        res = self.client.get("/driver")
        self.assertTrue(res.status_code == 403)
        self.assertTrue(res.json().get("state") == "error")
        self.assertTrue(res.json().get("data") == {})
    
    def test_error_login(self):
        data = {"phone": "一定不会登录上!", "password": "cxk"}
        res = self.client.post("/login", data=data)
        self.assertTrue(res.status_code == 200)
        self.assertTrue(res.json().get("state") == "error")
    
    def test_right_login(self):
        data = {"phone": "test", "password": "123"}
        res = self.client.post("/login", data=data)
        self.assertTrue(res.status_code == 200)
        self.assertTrue(res.json().get("state") == "success")
        
    def test_error_register(self):
        data = {"phone": "test", "password": "123", "username": "test", "role": "1"}
        res = self.client.post("/register", data=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get("state"), "error")
    
    def test_logout(self):
        data = {"phone": "test", "password": "123"}
        res = self.client.post("/login", data=data)
        self.assertTrue(res.status_code == 200)
        self.assertTrue(res.json().get("state") == "success")

        res = self.client.post("/logout")
        self.assertTrue(res.status_code == 200)
        self.assertTrue(res.json().get("state") == "success")


if __name__ == "__main__":
    unittest.main()
