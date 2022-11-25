from ursina  import *  

#Class

class Cubo (Entity):
    def __init__(self):
        super().__init__(
        model='cube',
        color= color.white,
        
        )

#Movimiento
def update():
    if held_keys ['a']:
        cuadrado.x -= 2 * time.dt  

#Estamos importado Ursin
app = Ursina()

cuadrado  = Entity(model='quad',color = color.red,scale=(1,4),position=(5,4))


app.run()