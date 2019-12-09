class BossEnemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class TrashMan(BossEnemy):
    def __init__(self):
        self.name = "Trash Grinder"
        self.hp = 200
        self.damage = 10
##edited enemy class to be unique boss enemy for bosstile-Nick
