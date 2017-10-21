class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class bandit(Enemy):
    def __init__(self):
        super().__init__(name = "Bandit", hp = 30, damage = 15)

class wolf(Enemy):
    def __init__(self):
        super().__init__(name = "Wolf", hp = 15, damage = 10)
