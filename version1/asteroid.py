import pyglet as pg

game_window = pg.window.Window(800, 800)


player_image = pg.resource.image("player.png")
bullet_image = pg.resource.media("bullet.png")
asteroid_image = pg.resource.media("asteroid.png")


def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)

score_label = pg.text.Label(text="Score: 0", x=10, y=460)


@game_window.event
def on_draw():
    game_window.clear()

    score_label.draw()


if __name__ == '__main__':
    pg.app.run()
