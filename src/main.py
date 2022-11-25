from ursina import *
# añadir un jugador primera persona
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
#Texturas
textura_pasto = load_texture('assets/grass_block.png')
textura_piedra = load_texture('assets/stone_block.png')
textura_ladrrillo = load_texture('assets/brick_block.png')
textura_tierra = load_texture('assets/dirt_block.png')
textureCielo= load_texture('assets/skybox.png')
textura_arma= load_texture('assets/arm_texture.png')
sonido = Audio('assets/punch_sound',loop = False, autoplay= False )
lock_presionado = 1


def update():
    global block_presionado
    if held_keys['left mouse'] or held_keys['right mouse']:
        mano.active()
    else:
        mano.passive()
    if held_keys['1']:
        block_presionado = 1
    if held_keys['2']:
        block_presionado = 2
    if held_keys['3']:
        block_presionado = 3
    if held_keys['4']:
        block_presionado = 4


class Voxel(Button):
    def __init__(self, position=(0, 0, 0,), texture=textura_pasto):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            height_color=color.lime,
            scale=0.5
        )
    def input(self, key):
        if self.hovered:           
            if key == 'left mouse down':
                sonido.play()
                if block_presionado == 1:voxel =Voxel(position=self.position+ mouse.normal,texture=textura_pasto)
                if block_presionado == 2:voxel =Voxel(position=self.position+ mouse.normal,texture=textura_piedra)
                if block_presionado == 3:voxel =Voxel(position=self.position+ mouse.normal,texture=textura_ladrillo)
                if block_presionado == 1:voxel =Voxel(position=self.position+ mouse.normal,texture=textura_tierra) 

                
            
            if key == 'right mouse down':
                sonido.play()
                destroy(self)



class Cielo (Entity):
    def __init__(self):
        super().__init__(
            parent= scene,
            model= 'sphere',
            texture= textureCielo,
            scale=150,
            double_sided=True,
        )


class Mano (Entity):
    def __init__(self):
        super().__init__(
            parent= camera.ui,
            model='assets/arm',
            texture=textura_arma,
            scale=0.2,
            rotation=Vec3(150,-10,0),
            position = Vec2(-0.4,-0.6)
            
            )
    def active(self):
        self.position= Vec2(0.3,-0.6)
    def passive(self):
          self.rotation = Vec3(150,-10,0)

   


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
cielo=Cielo()
mano=Mano()
app.run()
