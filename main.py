
from tkinter import *

#import tkintermapview

root = Tk()
root.title("Mapbook_BS")
root.geometry("1024x768")


#RAMKI
ramka_lista_obiektow= Frame(root)
ramka_formularz= Frame(root)
ramka_szczegoly_obiektow= Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0)
ramka_mapa.grid(row=2, column=0)


#RAMKA LISTA OBIEKTÓW
label_lista_obiektow= Label(ramka_lista_obiektow,text="Lista obiektów: ")
label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow= Listbox(ramka_lista_obiektow)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly= Button(ramka_lista_obiektow, text="Pokaż Szczegóły")
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt= Button(ramka_lista_obiektow, text="Edytuj obiekt")
button_edytuj_obiekt.grid(row=2, column=1)
button_usun_obiekt= Button(ramka_lista_obiektow, text="Usuń obiekt")
button_usun_obiekt.grid(row=2, column=2)


#RAMKA FORMULARZ
label_formularz= Label(ramka_formularz, text="Formularz: ")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name= Label(ramka_formularz, text="Imię: ")
label_name.grid(row=1, column=0, sticky=W)
label_surname= Label(ramka_formularz, text="Nazwisko: ")
label_surname.grid(row=2, column=0, sticky=W)
label_post= Label(ramka_formularz, text="Liczba postów: ")
label_post.grid(row=3, column=0, sticky=W)
label_location= Label(ramka_formularz, text="Miejscowość: ")
label_location.grid(row=4, column=0, sticky=W)

entry_name= Entry(ramka_formularz)
entry_name.grid(row=1, column=1,)
entry_surname= Entry(ramka_formularz)
entry_surname.grid(row=2, column=1)
entry_post= Entry(ramka_formularz)
entry_post.grid(row=3, column=1)
entry_location= Entry(ramka_formularz)
entry_location.grid(row=4, column=1)

button_dodaj_obiekt= Button(ramka_formularz, text="Dodaj")
button_dodaj_obiekt.grid(row=5, column=1, columnspan=2)



#RAMKA SZCZEGÓŁY OBIEKTÓW
label_szczegoly_obiektu= Label(ramka_szczegoly_obiektow, text="Szczegóły użytkownika: ")
label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)

label_name_szczegoly_obiektu= Label(ramka_szczegoly_obiektow, text="Imię: ")
label_name_szczegoly_obiektu.grid(row=1, column=0)

label_name_szczegoly_obiektu_wartosc= Label(ramka_szczegoly_obiektow, text="....")
label_name_szczegoly_obiektu_wartosc.grid(row=1, column=1)

label_surname_szczegoly_obiektu= Label(ramka_szczegoly_obiektow, text="Nazwisko: ")
label_surname_szczegoly_obiektu.grid(row=1, column=2)

label_surname_szczegoly_obiektu_wartosc= Label(ramka_szczegoly_obiektow, text="....")
label_surname_szczegoly_obiektu_wartosc.grid(row=1, column=3)


label_posts_szczegoly_obiektu= Label(ramka_szczegoly_obiektow, text="Postów: ")
label_posts_szczegoly_obiektu.grid(row=1, column=4)

label_posts_szczegoly_obiektu_wartosc= Label(ramka_szczegoly_obiektow, text="....")
label_posts_szczegoly_obiektu_wartosc.grid(row=1, column=5)

label_location_szczegoly_obiektu= Label(ramka_szczegoly_obiektow, text="Miejscowość: ")
label_location_szczegoly_obiektu.grid(row=1, column=6)

label_location_szczegoly_obiektu_wartosc= Label(ramka_szczegoly_obiektow, text="....")
label_location_szczegoly_obiektu_wartosc.grid(row=1, column=7)

#RAMKA MAPA
# map_vidget= tkintermapview.TkinterMapView(ramka_mapa, width=1024, height=400)
# map_vidget.set_position(52.23, 21)
# map_vidget.set_zoom(5)
# map_vidget.grid(row=0, column=0, columnspan=8)



root.mainloop()



def get_map(users_data: list) -> None:
    mapa = folium.Map(location=[52.3, 21.00], zoom_start=6)
    for user in users_data:
        folium.Marker(
            location=get_coordinates(city_name=user["location"]),
            popup=f'{user["name"]}<br/>{user["location"]}<br/>{user["posts"]}<br/>'
                  f'<img src="{user["picture"]}" alt="{user["picture"]}"/>',
        ).add_to(mapa)

    mapa.save("mapa.html")


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

    def add_user():
        imie = entry_name.get
        nazwisko = entry_surname.get
        posty = entry_post.get()
        miejscowosc = entry_location.get()



    users.append(User(name = imie , surname = nazwisko, location = miejscowosc, posts = posty))


    Obiekt_1 = User(name="Tomek", surname="Johny", location="Warszawa", posts=100)



















