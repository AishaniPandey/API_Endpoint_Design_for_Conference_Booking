import json
from app.main import app

def test_add_conference():
    with app.test_client() as client:
        response = client.post(
            '/api/v1/conferences',
            data=json.dumps({
                "name": "Test Conference",
                "location": "Test Location",
                "topics": ["Topic1", "Topic2"],
                "start_time": "2024-08-03T09:00:00Z",
                "end_time": "2024-08-03T21:00:00Z",
                "available_slots": 100
            }),
            content_type='application/json'
        )
        assert response.status_code == 201
        assert response.json["name"] == "Test Conference"
