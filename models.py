class Country:
    def __init__(self, name: str, capital: str, population: int, area: float):
        self.name = name  # the name of the country
        self.capital = capital  # the name of the capital city
        self.population = population  # the population of the country in millions
        self.area = area  # the area of the country in square kilometers

    def __str__(self):
        return f"{self.name}"

    def get_density(self):
        # returns the population density of the country in people per square kilometer
        return self.population * 1000000 / self.area
