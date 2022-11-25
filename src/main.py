from ursina import *
# añadir un jugador primera persona
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

textura_pasto = load_texture('assets/grass_block.png')
textura_piedra= load_texture('assets/stone_block.png')
textura_ladrrillo= load_texture('assets/brick_block.png')
textura_dirt= load_texture('assets/dirt_block.png')


class Voxel(Button):
    def __init__(self, position=(0, 0, 0,),texture=textura_pasto):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0, random.uniform(0.9,1)),
            height_color=color.lime,
            scale= 0.5
            )
    # Crear bloques y destruir bloques
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position = self.position)
            if key  == 'right mouse down':
                destroy(self)




for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()


app.run()
