import glfw
from OpenGL.GL import *
from OpenGL.GLU import *




if not glfw.init():
    raise RuntimeError("Failed to initialize GLFW. Check if GLFW has been correctly installed. Exiting.")

class DisplaySubsystem:
    def __init__(self, w, h, title, runtimeFunc):
        self.window = glfw.create_window(w, h, title, None, None)
        if not self.window:
            glfw.terminate()
            raise RuntimeError("Failed to create GLFW window. Exiting.")
        
        glfw.window_hint(glfw.SAMPLES, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.make_context_current(self.window)
        glViewport(0, 0, w, h)
        
        gluPerspective(45, 1, 0.1, 50.0)
        glTranslatef(0.0,0.0, -5)
        
        while not glfw.window_should_close(self.window):
            try:
                runtimeFunc()
            except GLError as glex:
                print(f"GLError{glex.err}: {glex}")

            glfw.poll_events()
            glfw.swap_buffers(self.window)

