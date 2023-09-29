import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time


if not pygame.init():
    raise RuntimeError("Failed to initialize PyGame. Check if PyGame has been correctly installed. Exiting.")

class DisplaySubsystem:
    def __init__(self, w, h, title, runtimeFunc):
        run = True
        display = (w, h)
        pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

        glViewport(0, 0, w, h)
        
        gluPerspective(45, 1, 0.1, 50.0)
        glTranslatef(0.0,0.0, -5)
        self.tick = 1
        self._starttime = time.time()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            try:
                runtimeFunc()
                self.print_debug()
                self.print_grids()
                self.tick+=1
            except GLError as glex:
                print(f"GLError{glex.err}: {glex}")
            except Error as e:
                print("An error has occurred.", e)
                break

            pygame.display.flip()

    def glut_print( self, x,  y,  text, r,  g , b , a):
        glColor3fv((r, g, b))
        glPushMatrix();
        glWindowPos2f(x, y)
        for ch in text :
            glutBitmapCharacter( GLUT_BITMAP_9_BY_15, ctypes.c_int( ord(ch) ) )
        glPopMatrix();
    
    def print_grids(self):
        glLineWidth(1.0)  # Reset line width to default
        grid_spacing = 1.0  # Adjust this value to control grid density
        grid_size = 10.0  # Adjust this value to control grid size

        glColor3f(0.5, 0.5, 0.5)  # Gray color for the grid lines

        # Draw grids in the XY plane
        glBegin(GL_LINES)
        for i in range(int(-grid_size / grid_spacing), int(grid_size / grid_spacing) + 1):
            x = i * grid_spacing
            glVertex3f(x, -grid_size, 0.0)
            glVertex3f(x, grid_size, 0.0)

            y = i * grid_spacing
            glVertex3f(-grid_size, y, 0.0)
            glVertex3f(grid_size, y, 0.0)
        glEnd()

        # Draw grids in the XZ plane
        '''glBegin(GL_LINES)
        for i in range(int(-grid_size / grid_spacing), int(grid_size / grid_spacing) + 1):
            x = i * grid_spacing
            glVertex3f(x, 0.0, -grid_size)
            glVertex3f(x, 0.0, grid_size)

            z = i * grid_spacing
            glVertex3f(-grid_size, 0.0, z)
            glVertex3f(grid_size, 0.0, z)
        glEnd()

        # Draw grids in the YZ plane
        glBegin(GL_LINES)
        for i in range(int(-grid_size / grid_spacing), int(grid_size / grid_spacing) + 1):
            y = i * grid_spacing
            glVertex3f(0.0, y, -grid_size)
            glVertex3f(0.0, y, grid_size)

            z = i * grid_spacing
            glVertex3f(0.0, -grid_size, z)
            glVertex3f(0.0, grid_size, z)
        glEnd()'''

        glLineWidth(5.0)  # Set line width for the axes

        # X-axis (Red)
        glColor3f(1.0, 0.0, 0.0)  # Red color
        glBegin(GL_LINES)
        glVertex3f(grid_size, 0.0, 0.0)
        glVertex3f(-grid_size, 0.0, 0.0)
        glEnd()

        # Y-axis (Green)
        glColor3f(0.0, 1.0, 0.0)  # Green color
        glBegin(GL_LINES)
        glVertex3f(0.0, grid_size, 0.0)
        glVertex3f(0.0, -grid_size, 0.0)
        glEnd()

        # Z-axis (Blue)
        glColor3f(0.0, 0.0, 1.0)  # Blue color
        glBegin(GL_LINES)
        glVertex3f(0.0, 0.0, grid_size)
        glVertex3f(0.0, 0.0, -grid_size)
        glEnd()

    def print_debug(self):
        self.glut_print(10, 90, f"-- DEBUG --", 0.0, 0.0, 0.0, 0.0)
        self.glut_print(10, 70, f"{hex(self.tick)}", 0.0, 0.0, 0.0, 0.0)
        self.glut_print(10, 50, f"~{round((time.time() - self._starttime)/self.tick, 3)}s/frame", 0.0, 0.0, 0.0, 0.0)
        self.glut_print(10, 30, f"~{round(self.tick/(time.time() - self._starttime), 3)} FPS", 0.0, 0.0, 0.0, 0.0)
        self.glut_print(10, 10, f"Elapsed ~{round(time.time() - self._starttime, 3)}s", 0.0, 0.0, 0.0, 0.0)

