from ursina import *

app = Ursina()

player = Entity(
    madel = 'cube',
    color = color.orange,
    texture = 'white_cube',
    position = (0,0,0)
)

ground = Entity(
    model = 'plane',
    scale = (10,1,10),
    color = color.green,
    collider = 'box'
)
def update():
    player.x += held_keys['d'] * time.dt * 3
    player.x -= held_keys['a'] * time.dt * 3
    player.y += held_keys['w'] * time.dt * 3
    player.y -= held_keys['s'] * time.dt * 3

app.run()