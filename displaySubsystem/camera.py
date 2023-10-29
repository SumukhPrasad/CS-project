import glm

import pygame as pg

FOV = 50  # deg
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSITIVITY = 0.1

class Camera:
     def __init__(self, ds, position=(0, 5, 4), yaw=-90, pitch=-30):
          self.ds = ds
          self.aspect_ratio = ds.WINDOW_SIZE[0] / ds.WINDOW_SIZE[1]
          self.position = glm.vec3(position)
          self.up = glm.vec3(0, 1, 0)
          self.right = glm.vec3(1, 0, 0)
          self.forward = glm.vec3(0, 0, -1)
          self.yaw = yaw
          self.pitch = pitch
          # view matrix
          self.m_view = self.get_view_matrix()
          # projection matrix
          self.m_proj = self.get_projection_matrix()

     def rotate(self):
          rel_x, rel_y = pg.mouse.get_rel()
          self.yaw += rel_x * SENSITIVITY
          self.pitch -= rel_y * SENSITIVITY
          self.pitch = max(-179, min(179, self.pitch))
          '''
               z
               |      forward
               |˙˙˙˙˙/.
               |    / .
               |   /  .
               |  /   .
               | /    .
               |/yaw  .
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ xy-plane (x)
              forward.x = cos(yaw)
              forward.z = sin(yaw)

               y
               |      forward
               |˙˙˙˙˙/.
               |    / .
               |   /  .
               |  /   .
               | /    .
               |/pitch.
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ xz-plane
              forward.x = cos(pitch)
              forward.y = sin(pitch)
              forward.z = cos(pitch)

              Resultants:
              forward.x = cos(yaw)cos(pitch)
              forward.y = sin(pitch)
              forward.z = sin(yaw)cos(pitch)
          '''

     def update_camera_vectors(self):
          yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

          self.forward.x = glm.cos(yaw) * glm.cos(pitch)
          self.forward.y = glm.sin(pitch)
          self.forward.z = glm.sin(yaw) * glm.cos(pitch)

          self.forward = glm.normalize(self.forward)
          self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
          self.up = glm.normalize(glm.cross(self.right, self.forward))

     def update(self):
          self.move()
          self.rotate()
          self.update_camera_vectors()
          self.m_view = self.get_view_matrix()

     def move(self):
          velocity = SPEED * self.ds.delta_time
          keys = pg.key.get_pressed()
          if keys[pg.K_w]:
               self.position += self.forward * velocity
          if keys[pg.K_a]:
               self.position -= self.right * velocity
          if keys[pg.K_s]:
               self.position -= self.forward * velocity
          if keys[pg.K_d]:
               self.position += self.right * velocity

          if keys[pg.K_r]:
               self.position += self.up * velocity
          if keys[pg.K_f]:
               self.position -= self.up * velocity

     def get_view_matrix(self):
          return glm.lookAt(self.position, self.position + self.forward, self.up)

     def get_projection_matrix(self):
          return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)