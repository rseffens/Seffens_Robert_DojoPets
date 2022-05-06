import parent


pet1 = parent.Pet("Boomer", "German Shepard", energy=70)
ninja1 = parent.Ninja("Robert", "Seffens", pet1)



# print(pet1.name)
# print(pet1.type)
# print(pet1.health)
# print(pet1.energy)


ninja1.walk().feed().bathe().info()