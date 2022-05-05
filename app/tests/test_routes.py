#Create a test to check GET /planets returns 200 and an empty array.

def test_get_all_planets_with_no_records(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

'''
Create test fixtures and unit tests for the following test cases:

GET /planets/1 returns a response body that matches our fixture  DONE
GET /planets/1 with no data in test database (no fixture) returns a 404  DONE
GET /planets with valid test data (fixtures) returns a 200 with an array including appropriate test data
POST /planets with a JSON request body returns a 201
'''
def test_get_one_planet_that_matches_our_fixture(client, two_saved_planets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == {
        "title": "Mercury",
        "description": "Best planet, grey",
        "moons": False
    }

# def test_get_one_planet_with_no_records(client):
#     #Act
#     response = client.get("/planets/1")
#     response_body = response.get_json()

#     #Assert
#     assert response.status_code == 404
#     assert response_body == {}

# def test_get_all_planets_matching_our_fixture(client):
#     #Act
#     response = client.get("/planets")
#     response_body = response.get_json()

#     #Assert
#     assert response.status_code == 200
#     assert response_body == [
#         {
#         "description": "Grey, closest to the sun, smallest planet",
#         "id": 1,
#         "moons": false,
#         "title": "Mercury"
#         },
#         {
#         "description": "Brown and grey, hottest planet",
#         "id": 2,
#         "moons": false,
#         "title": "Venus"
#         },
#         {
#         "description": "Blue, brown green and white, water world, 1 moon",
#         "id": 3,
#         "moons": true,
#         "title": "Earth"
#         },
#         {
#         "description": "Red, brown and tan, 2 moons",
#         "id": 4,
#         "moons": true,
#         "title": "Mars"
#         },
#         {
#         "description": "Brown, orange and tan, with white cloud stripes, largest planet, 79 moons",
#         "id": 5,
#         "moons": true,
#         "title": "Jupiter"
#         },
#         {
#         "description": "Golden, brown, and blue-grey, large and distinct ring system, 82 moons",
#         "id": 6,
#         "moons": true,
#         "title": "Saturn"
#         },
#         {
#         "description": "Blue-green, holds the record for the coldest temperature ever measured in the solar system, 27 moons",
#         "id": 7,
#         "moons": true,
#         "title": "Uranus"
#         },
#         {
#         "description": "Blue, on average the coldest planet, 14 moons",
#         "id": 8,
#         "moons": true,
#         "title": "Neptune"
#         }
#     ]

# def test_post_first_planet(client):
#     response = client.post("/planets", json={
#             "title": "Mercury",
#             "description": "NICE PLANET!!!!!",
#             "moons": false})
#     response_body = response.get_json()
#     assert response.statuscode == 201
#     assert response_body == "Planet Mercury has been successfully created!"
