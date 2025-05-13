


class User:
    def __init__(self, name, surname, location, posts):
        self.name = name
        self.surname = surname
        self.location = location
        self.posts = posts
        self.coordinates = self.get_coordinates()

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        address_url: str = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(address_url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude: float = float(response_html.select(".longitude")[1].text.replace(",", "."))
        # print(longitude)
        latitude: float = float(response_html.select(".latitude")[1].text.replace(",", "."))
        # print(latitude)
        return [latitude, longitude]



Obiekt_1 = User(name= "Tomek", surname = "Johny", location = "Warszawa", posts = 100)


print(Obiekt_1.name)
print(Obiekt_1.surname)
print(Obiekt_1.location)
print(Obiekt_1.posts)
print(Obiekt_1.coordinates)





