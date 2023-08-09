class TestRoutes:
    def test_personal_route(self, client):
        response = client.get("/api/personal/")
        assert response.status_code == 200

        json_data = response.get_json()
        assert isinstance(json_data, dict)
        assert "name" in json_data
        assert "email" in json_data
        assert "phone" in json_data

    def test_experience_route(self, client):
        response = client.get("/api/experience/")
        assert response.status_code == 200

        json_data = response.get_json()
        assert isinstance(json_data, list)

        first_experience = json_data[0]
        assert "company" in first_experience
        assert "position" in first_experience
        assert "years" in first_experience

    def test_education_route(self, client):
        response = client.get("/api/education/")
        assert response.status_code == 200

        json_data = response.get_json()
        assert isinstance(json_data, list)

        first_education = json_data[0]
        assert "institution" in first_education
        assert "degree" in first_education
        assert "years" in first_education

    def test_bad_route(self, client):
        response = client.get("/api/non_existent_route/")
        assert response.status_code == 404
