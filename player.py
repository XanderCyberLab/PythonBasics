class GameCharacter:

    speed = 1.0 
    
    def __init__(self, name, health, x_pos):
        self.name = name
        self.health = health
        self.x_pos = x_pos

    def move(self, amount):
        self.x_pos += amount

    def damage_taken(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0

    def check_if_dead(self):
        self.health <= 0
        return self.health <= 0
    
    def change_speed(to_speed):
        GameCharacter.speed = to_speed
    
    
class PlayerCharacter(GameCharacter):   
    
    def __init__(self, name, health, x_pos, num_lives):
        super().__init__(name, health, x_pos)
        self.max_health = health
        self.num_lives = num_lives
        
        
    def damage_taken(self, amount):
        self.health -= amount
        if self.health <= 0 and self.num_lives != 0:
            self.num_lives -= 1
            self.health = self.max_health
    
    def check_if_dead(self):
        return self.health <= 0 and self.num_lives <= 0
    
    def cure(self, amount):
        self.health += amount
        
pc = PlayerCharacter('Wishmaster', 100, 1, 3)
npc = GameCharacter('Wolf', 100, 3)

print(pc.speed)
print(npc.speed)

#pc.change_speed(4)
#npc.change_speed(6)

GameCharacter.change_speed(2)

print(pc.speed)
print(npc.speed)

# pc.damage_taken(50)
# npc.damage_taken(80)

# print(pc.health)
# print(npc.health)

# pc.cure(10)
# npc.damage_taken(20)

# print(pc.health)
# print(npc.health)

# print(pc.check_if_dead())
# print(npc.check_if_dead())

# pc.damage_taken(100)

# print(pc.health)
# print(pc.num_lives)
# print(pc.check_if_dead())

# pc.damage_taken(100)

# print(pc.health)
# print(pc.num_lives)
# print(pc.check_if_dead())

# pc.damage_taken(100)

# print(pc.health)
# print(pc.num_lives)
# print(pc.check_if_dead())

# pc.damage_taken(100)

# print(pc.health)
# print(pc.num_lives)
# print(pc.check_if_dead())




        
            
        