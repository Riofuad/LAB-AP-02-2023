from TP9_1_H071231007 import Warrior, Assassin, Support

assassin = Assassin("ninja", 80)
warrior = Warrior("bambang", position = 10)
support = Support("udin",position=30)
# sebelum
print("health (before)", warrior.get_health())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.get_health())
print("-"*10)
# sebelum
print("warrior (health)", warrior.get_health())
print("support (speed) : ",support.get_speed())
print("-"*10)
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.get_health())
print("support (speed): ",support.get_speed())

print(warrior.get_speed())
print (warrior.get_position())
warrior.movement("RLRRRLR")
print(warrior.get_position())
