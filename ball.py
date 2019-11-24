class Ball:
  def __init__(self, radius, color, weight):
    self.radius = radius
    self.color = color
    self.weight = weight

class Football:
  """A standard, regulation NFL ball"""
  def __init__(self, radius, color, pressure):
    self.radius = radius
    self.color = color
    self.pressure = pressure

  def inflate(self, psiChange):
    self.pressure = self.pressure + psiChange

  def deflate(self, psiChange):
    self.pressure = self.pressure - psiChange

class PatriotsBall(Football):
  # Tom Brady approved
  def inflate(self, psiChange):
    self.pressure = self.pressure - psiChange
