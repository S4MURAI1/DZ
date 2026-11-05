def test_create_project_positive(api):
    data = {
        "title": "Позитивный тест создания проекта"
    }

    response = api.create_project(data)

    assert response.status_code in (200, 201)
    assert "id" in response.json()

def test_create_project_negative(api):
    data = {}

    response = api.create_project(data)

    assert response.status_code >= 400

def test_update_project_positive(api, project):
    data = {
        "title": "Обновленный тестовый проект"
    }

    response = api.update_project(project, data)

    assert response.status_code == 200

def test_update_project_negative(api):
    data = {
        "title": "Несуществующий проект"
    }

    response = api.update_project(
        "00000000-0000-0000-0000-000000000000",
        data
    )

    assert response.status_code >= 400

def test_get_project_positive(api, project):
    response = api.get_project(project)

    assert response.status_code == 200
    assert response.json()["id"] == project

def test_get_project_negative(api):
    response = api.get_project(
        "00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code >= 400
