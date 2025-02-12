# Exercice 1: Compte bancaire
class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.__solde = solde_initial

    def deposer(self, montant_depot):
        """Ici, on va déposer un montant au solde"""
        if montant_depot > 0:
            self.__solde += montant_depot
        else:
            print("Le montant à déposer doit être positif.")

    def retirer(self, montant_retire):
        if 0 <= montant_retire < self.__solde:
            self.__solde -= montant_retire
        elif montant_retire > self.__solde:
            print("Fonds insuffisants.")
        else:
            print("Le montant doit être positif")

    def afficher_solde(self):
        print(f"Solde actuel: {self.__solde}$")


# Exemple 2: Coordonnées de 2 points
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        """Ici, on retourne la coordonnée x"""
        return self.__x

    def get_y(self):
        """Ici, on retourne la coordonnée y"""
        return self.__y

    def distance_origine(self):
        return (self.__x ** 2 + self.__y ** 2) ** 0.5


# monPoint = Point(3,4)
# print(f"Les coordonnées de ce point sont: {monPoint.get_x()}, {monPoint.get_y()}")
# print(f"La distance de ce point par rapport à l'origine est : {monPoint.distance_origine()}")

# Exercice 3:

class Rectangle:
    def __init__(self, width, height):
        self.__width = abs(width)
        self.__height = abs(height)

    def get_surface(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)


monRectangle = Rectangle(3, 4)
print(monRectangle.get_surface())
print(monRectangle.get_perimeter())
