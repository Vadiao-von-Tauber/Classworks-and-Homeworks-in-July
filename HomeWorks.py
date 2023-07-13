# HOMEWORK Container (early)

class regiment:
    def __init__(self):
        self.items = ["Private Gunkiss", "Sergeant Lustig", "Komissar Reuber"]

    def __contains__(self, item):
        return item in self.items

def main(first, second):
    bad_company = regiment()

    print("Sergeant Lustig" in bad_company)  # True
    print("Private Gunkiss" in bad_company)  # True
    print("Komissar Reuber" in bad_company)  # True
    print("Daemonhost Tcherubaehl" in bad_company)  # False

    if (("Sergeant Lustig" in bad_company) and ("Private Gunkiss" in bad_company) and ("Komissar Reuber" in bad_company)):
        print("Thank God the Emperor!")

    simple_container = [1, 2, 3]
    if (first in simple_container):
        print(first)
        print("This element placed in container")
    if not(second in simple_container):
        print(second)
        print("This element isn't placed in container")

# HOMEWORK Square 5.07.2023
# 1)  Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
# площадь квадрата и диагональ квадрата.


