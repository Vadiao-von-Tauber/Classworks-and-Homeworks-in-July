# Homework classes
# Starships theme

class Starships_Info:

    @staticmethod
    def star_port_order():

        with open('I. starship Cruor Vult.txt', 'r') as f:

            for line in f:
                print(line.strip())

            for line in f:
                print(line.strip())

            while True:
                line = f.readline()
                if not line:
                    break
                print(line.strip())

        with open('II. battleship Alexei Stukov.txt', 'r') as ff:
            for line in ff:
                print(line.strip())

            for line in ff:
                print(line.strip())

            while True:
                line = ff.readline()
                if not line:
                    break
                print(line.strip())

            with open('III. cargoship Black Jenna.txt', 'r') as fff:
                for line in fff:
                    print(line.strip())

                for line in fff:
                    print(line.strip())

                while True:
                    line = fff.readline()
                    if not line:
                        break
                    print(line.strip())
            #f.close()


Starships_Info.star_port_order()

# .txt docs:
#
# I. starship Cruor Vult.txt'
# name ship: "Crvor Vult"
# codename: "carmine"
# space displacement: 800000 brt
# number of guns: 104
# hold volume: 380000 brt
# home port: "Koronus Prime", 18004458900501
# status: 'in immaterium'.



# ___

# II. battleship Alexei Stukov.txt
# name ship: "Alexei Stukov"
# codename: "mare sancti"
# space displacement: 500000 brt
# number of guns: 384
# hold volume: 135000 brt
# home port: "Mar Sara", 204600451-000DTR02
# status: 'loading ammunition'


# ___

# III. cargoship Black Jenna.txt
# name ship: "Black Jenna"
# codename: "obsidian moon"
# space displacement: 2000000 brt
# number of guns: 32
# hold volume: 1800000 brt
# home port: "Serendipity", 365444200006
# status: 'in immaterium'.


# ___

