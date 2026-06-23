class MealRecommendationService:

    def __init__(self, weather_service):
        self.weather_service = weather_service

    def recommend_meal(self):
        weather = self.weather_service.get_weather()

        if weather == "warm":
            return "Salat"

        return "Suppe"
