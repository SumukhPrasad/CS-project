import glm

class Light:
     def __init__(self, position=(3,3,-3), color=(1,1,1)):
          self.position = glm.vec3(position)
          self.color = glm.vec3(color)
          
          # LIGHTING -- ambient + diffuse + specular
          self.intensities = {
               "ambient": 0.1*self.color,
               "diffuse": 0.8*self.color,
               "specular": 1.0*self.color
          }