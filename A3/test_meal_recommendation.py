from unittest.mock import Mock
from meal_recommendation import MealRecommendationService


def test_recommend_salad_when_weather_is_warm():
    weather_service = Mock()
    weather_service.get_weather.return_value = "warm"

    service = MealRecommendationService(weather_service)

    assert service.recommend_meal() == "Salat" 


def test_recommend_soup_when_weather_is_cold():
    weather_service = Mock()
    weather_service.get_weather.return_value = "cold"

    service = MealRecommendationService(weather_service)

    assert service.recommend_meal() == "Suppe"
