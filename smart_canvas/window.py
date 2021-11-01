import moderngl_window as mglw
from threading import Thread


# fyi :https://moderngl-window.readthedocs.io/en/latest/reference/context/windowconfig.html#moderngl_window.context.base.window.WindowConfig
class Window(mglw.WindowConfig):
    gl_version = (3, 3)
    title = "SmartCanvas"
    window_size = (1270, 720)
    aspect_ratio = 16 / 9
    resizable = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def run(cls):
        
        mglw.run_window_config(cls)

    #def key_event(self, key, action, modifiers):
    #    if action == self.wnd.keys.ACTION_PRESS:
    #        if key == self.wnd.keys.Q: