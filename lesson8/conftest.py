import pytest
from api_client import YouGileAPI

@pytest.fixture
def api():
    return YouGileAPI()

@pytest.fixture
def project(api):
    data = {
        "title": "Тестовый проект для автотестов"
    }

    response = api.create_project(data)

    assert response.status_code in (200, 201), (
        f"Не удалось создать проект: {response.status_code}, "
        f"{response.text}"
    )

    project_id = response.json()["id"]

    return project_id
