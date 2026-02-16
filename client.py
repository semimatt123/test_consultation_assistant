import requests

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    response = requests.get(f"{BASE_URL}/")
    print("Status:", response.status_code)
    print("Data:", response.json())

def test_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    print("Status:", response.status_code)
    print("Data:", response.json())

if __name__ == "__main__":
    test_root()
    test_user(5)