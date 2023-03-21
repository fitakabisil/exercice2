import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# la liste de couleur
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]


class Cercle:
    def __init__(self, r, x, y, c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.color = c

    def draw(self):
        # arcade.draw_circle_filled(center_x, center_y, rayon, color)
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


# la class qui configure le jeu
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")  # appel les variables de la class Window
        self.liste_cercles = []  # initialisation de la liste de cercles

    def setup(self):
        # remplir la liste avec 20 objets de type Cercle
        for _ in range(20):
            rayon = random.randint(10, 50)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercle = Cercle(rayon, center_x, center_y, color)
            self.liste_cercles.append(cercle)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

        for cercle in self.liste_cercles:  # quand le mouse press est activé dans un cercle,
            if cercle.centre_x + cercle.rayon > x > cercle.centre_x - cercle.rayon and cercle.centre_y - cercle.rayon < y < cercle.centre_y + cercle.rayon:

                if button == arcade.MOUSE_BUTTON_LEFT:  # enlève un cercle quand le bouton M1 est appuié
                    self.liste_cercles.remove(cercle)

                if button == arcade.MOUSE_BUTTON_RIGHT:  # change la couleur du cercle quand le bouton M2 est appuié
                    cercle.color = random.choice(COLORS)

    def on_draw(self):  # dessine les cercles
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.draw()


def main():  # ouvre la fenêtre
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
