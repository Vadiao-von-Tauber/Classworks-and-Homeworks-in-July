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