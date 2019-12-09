class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Parasite(Enemy):
    def __init__(self):
        self.name = "Parasite"
        self.hp = 10
        self.damage = 2


class ParasiteZ(Enemy):
    def __init__(self):
        self.name = "Parasite Zombie"
        self.hp = 30
        self.damage = 12


class Slime(Enemy):
    def __init__(self):
        self.name = "Slimy Blob"
        self.hp = 100
        self.damage = 10


class SJGolem(Enemy):
    def __init__(self):
        self.name = "Space Junk Golem"
        self.hp = 80
        self.damage = 35

class GhostMonkey(Enemy):
    def __init__(self):
        self.name = "Chimpanzee's Shadow"
        self.hp = 50
        self.damage = 17
