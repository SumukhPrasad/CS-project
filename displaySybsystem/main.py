import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



if not glfw.init():
    raise RuntimeError("Failed to initialize GLFW. Check if GLFW has been correctly installed. Exiting.")

class DisplaySubsystem:
    def __init__(self, w, h, title, runtimeFunc):
        self.window = glfw.create_window(w, h, title, None, None)
        if not self.window:
            glfw.terminate()
            raise RuntimeError("Failed to create GLFW window. Exiting.")
        
        glfw.window_hint(glfw.SAMPLES, 4)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.make_context_current(self.window)
        glViewport(0, 0, w, h)
        
        gluPerspective(45, 1, 0.1, 50.0)
        glTranslatef(0.0,0.0, -5)
        self.tick = 1
        while not glfw.window_should_close(self.window):
            try:
                runtimeFunc()
                self.glut_print(10, 10, f"frame {hex(self.tick)}", 0.0, 0.0, 0.0, 0.0)
                self.tick+=1
            except GLError as glex:
                print(f"GLError{glex.err}: {glex}")
            except:
                print("An error has occurred.")

            glfw.poll_events()
            glfw.swap_buffers(self.window)

    def glut_print( self, x,  y,  text, r,  g , b , a):
        glColor3fv((r, g, b))
        glPushMatrix();
        glWindowPos2f(x, y)
        for ch in text :
            glutBitmapCharacter( GLUT_BITMAP_9_BY_15, ctypes.c_int( ord(ch) ) )
        glPopMatrix();

