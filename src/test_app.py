from io import BytesIO

from fastapi.testclient import TestClient
from fastapi import status

from main import app

headers = {"authorization": "Bearer ###"}


def post_corrupted() -> int:
    with TestClient(app) as client:
        response = client.post(
            "/api/v1/memes",
            data={
                "text": "corrupted",
            },
            files={"file": ("corrupted.png", BytesIO(b"0000"))},
            headers={**headers, "Content-Type": "multipart/form-data; boundary=kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A" },
        )
        data = response.json()
        print(data)
        return data["id"]


id_1, id_2 = post_corrupted(), post_corrupted()


def test_index():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == status.HTTP_404_NOT_FOUND


def test_docs():
    with TestClient(app) as client:
        response = client.get("/docs")
        assert response.status_code == status.HTTP_200_OK


def test_memes_list():
    with TestClient(app) as client:
        response = client.get("/api/v1/memes?per_page=10&page=1")
        assert response.status_code == status.HTTP_200_OK


def test_memes_create():
    with TestClient(app) as client:
        response = client.post(
            "/api/v1/memes",
            json={},
            headers=headers,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_memes_detail():
    with TestClient(app) as client:
        response = client.get(f"/api/v1/memes/{id_1}")
        assert response.status_code == status.HTTP_200_OK


def test_memes_update():
    with TestClient(app) as client:
        response = client.put(
            f"/api/v1/memes/{id_1}",
            json={
                "text": "six",
                "picture": "http://0.0.0.0:8000/media/1719146287.9597971-photo_5453989681847983651_y.jpg",
                "id": 1,
            },
            headers=headers,
        )
        assert response.status_code == status.HTTP_202_ACCEPTED


def test_memes_delete():
    with TestClient(app) as client:
        response = client.delete(f"/api/v1/memes/{id_2}", headers=headers)
        assert response.status_code == status.HTTP_204_NO_CONTENT


def test_unauthorized():
    with TestClient(app) as client:
        response = client.delete(f"/api/v1/memes/{id_2}")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
