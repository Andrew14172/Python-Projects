# Floyd's Tortoise and Hare


class Tortoise:
    positions = tuple(i for i in range(6))

    def __init__(self, position, step):
        self.position = position if position >= 0 else 0
        self.step = step if step > 0 else 1

    def move(self):
        self.position = (self.position + self.step) % len(self.positions)


class Hare(Tortoise):
    def __init__(self, position, step):
        super().__init__(position, step)


tortoise = Tortoise(0, 2)
hare = Hare(0, 1)

tortoise.move()
hare.move()

while tortoise.position != hare.position:
    tortoise.move()
    hare.move()


print(f"Intersection: {tortoise.position}")
