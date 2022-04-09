import pyglet

w, h = 500, 500

screen = pyglet.canvas.get_display().get_screens()[0]
window = pyglet.window.Window(screen=screen, width=w, height=h,
                              caption="Example")

window.set_location((screen.width - w)//2, (screen.height - h)//2)
pyglet.gl.glClearColor(0.8, 0.8, 0.8, 1.0)
batch = pyglet.graphics.Batch()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == 1:
        label = pyglet.text.Label(f'X = {x}, Y = {y}', x=x, y=y,
                                  batch=batch, color=(0, 0, 0, 255))

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()