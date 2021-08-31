class SpaceAge:
    def __init__(self, seconds):
        self.__earth_years = seconds / 60 / 60 / 24 / 365.25

    def on_earth(self):
        return self._age(1)

    def on_mercury(self):
        return self._age(0.2408467)

    def on_venus(self):
        return self._age(0.61519726)

    def on_mars(self):
        return self._age(1.8808158)

    def on_jupiter(self):
        return self._age(11.862615)

    def on_saturn(self):
        return self._age(29.447498)

    def on_uranus(self):
        return self._age(84.016846)

    def on_neptune(self):
        return self._age(164.79132)

    def _age(self, orbital_period):
        return round(self.__earth_years / orbital_period, 2)

    
