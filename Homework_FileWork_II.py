# Upload Homework_FileWork

import Homework_FileWork

list_ships = ['I. starship Cruor Vult.txt',
              'II. battleship Alexei Stukov',
              'III. cargoship Black Jenna',
              'IV. tugboat Jurgen',
              'V. space yacht Externus Exterminatus']
print(list_ships)
len(list_ships)
print('\n \n \n immaterium \n      is a \n          dangerous')
print()

#
#
#
# next steps nomework
# peeped at Alex BeaveRG :)


class Ships:
    def __init__(self, title: str, captain : str, experience: int, awards: int) -> None:
        self.id_ship = self.__hash__()
        self.title = title
        self.captain = captain
        self.experience = experience
        self.awards = awards
        self.places = []

    def add_place(self, place) -> None:
        self.places.append(place.name)

    def print_information(self) -> None:
        print(f'Ship ID: {self.id_ship}')
        print(f'Title: {self.title}')
        print(f'Captain: {self.captain}')
        print(f'Experience: {self.experience}')
        print(f'Awards: {self.awards}')
        print('Places:')
        for place in self.places:
            print(f'\t{place}')

class ShipCompany:
    pass

class Shipyard(ShipCompany):
    def __init__(self, name):
        self.name = name
        self.ship = []

    def add_ship(self, ship: Ships):
        if self.name not in ship.places:
            self.ships.append(ship)
            ship.add_place(self)
        else:
            print(f"""Ship "{ship.title}" has not accepted by Officio Munitorum to "{self.name}" """)

class ShipBase(ShipCompany):
    def __init__(self, name: str) -> None:
        self.name = name
        self.ships = []

    def add_ship(self, ship: Ships) -> None:
        if self.name not in ship.places:
            self.ships.append(ship)
            ship.add_place(self)
        else:
            print(f"""Ship "{ship.title}" has not accepted by Officio Munitorum to "{self.name}" """)


class Order:

    def __init__(self) -> None:
        self.id = str(self.__hash__())[-10:]
        self.ships = {}
        self.statuses = ['refectio',
                         'in progressus',
                         'navis acceptatio',
                         'paratus ire',
                         'in immaterium',
                         'destruatur']
        self.status = self.statuses[0]
        self.places = []

    def add_ship(self, ship: Ships, expirience=3) -> None:
        if ship.title in self.ships:
            self.ships[ship.title] += expirience
        else:
            self.ships[ship.title] = expirience
        for place in ship.places:
            if place not in self.places:
                if len(self.places) == 0:
                    self.places.append(place)
                elif 'Gate' in self.places[0] and 'Gate' in place:
                    self.places.append(place)
                elif 'Ramp' in self.places[0] and 'Ramp' in place:
                    self.places.append(place)

    def status_moderati(self):
        if self.statuses.index(self.status) < 6:
            self.status = self.statuses[self.statuses.index(self.status) + 2]

    def informatio(self) -> None:
        print(f'\nOrder ID: {self.id}')
        print(f'Status: {self.status}')
        print('Ships:')
        for ship, expirience in self.ships.items():
            print(f'\t{ship}: {expirience}')
        print('Places:')
        for place in self.places:
            print(f'\t{place}')

class Nauta: # Traveler (lat.)
    def __init__(self, race: str, name: str, surname: str, sex: str, age: int, planets: dict, vox_code: str) -> None:
        self.race = race
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        self.planets = planets
        self.vox_code = vox_code
        self.orders = {}

    def add_order(self, order: Order) -> None:
        self.orders[order.id] = order.status

    def informatio(self) -> None:
        print(f'Race: {self.race}')
        print(f'Name: {self.name}')
        print(f'Surname: {self.surname}')
        print(f'Sex: {self.sex}')
        print(f'Age: {self.age}')
        print('Planets:')
        for planet_type, planet in self.planets.items():
            print(f'\t{planet_type}: {planet}')
        print(f'Vox Code: {self.vox_code}')
        print('Orders:')
        for order_id, status in self.orders.items():
            print(f'\t{order_id}: {status}')