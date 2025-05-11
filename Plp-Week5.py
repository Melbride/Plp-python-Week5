
# Base Class – Superhero
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def show_profile(self):
        print(f" Superhero: {self.name}\n Power: {self.power}\n City: {self.city}")

    def move(self):
        print(f"{self.name} moves swiftly to save the day!")


#  Inherited Classes with Polymorphism

class FlyingHero(Superhero):
    def move(self):
        print(f"{self.name} takes off into the sky!")

class Speedster(Superhero):
    def move(self):
        print(f"{self.name} dashes through the city at lightning speed!")

class AquaHero(Superhero):
    def move(self):
        print(f"{self.name} swims through the waves to rescue sea creatures!")



# Create instances
hero1 = FlyingHero("SkyStorm", "Flight", "MetroSky")
hero2 = Speedster("FlashBeat", "Super Speed", "HyperTown")
hero3 = AquaHero("WaveGuard", "Water Control", "OceanSide")

# Show their profiles
hero1.show_profile()
hero2.show_profile()
hero3.show_profile()

print("\n--- Polymorphism in Action ---")
heroes = [hero1, hero2, hero3]
for hero in heroes:
    hero.move()

