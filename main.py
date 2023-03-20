import arcade
import random
from dataclasses import dataclass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]


@dataclass
class Cercle:
    def __init__(self, r, x, y, c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.color = c

    def draw(self):
        # arcade.draw_circle_filled(center_x, center_y, rayon, color)
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []
        self.number_cercles = 20

    def setup(self):
        # remplir la liste avec 20 objets de type Cercle
        for _ in range(self.number_cercles):
            rayon = random.randint(10, 50)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercle = Cercle(rayon, center_x, center_y, color)

    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int, cercle):
        rayon = random.randint(10, 50)
        center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
        center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
        color = random.choice(COLORS)

        if x == (cercle.centre_x + cercle.rayon, SCREEN_WIDTH - cercle.rayon) and y == (self.centre_y + cercle.rayon, SCREEN_HEIGHT - cercle.rayon):

            if button == arcade.MOUSE_BUTTON_RIGHT:

                cercle = Cercle(rayon, center_x, center_y, color)
                self.liste_cercles.append(cercle)

    def on_draw(self):
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.draw()


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
