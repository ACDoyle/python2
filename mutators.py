class P:
  def __init__(self,x):
    self.set_x(x)
 
  def get_x(self):
    return self.__x

  def set_x(self, x):
    if x < 0:
      self.__x = 0
    elif x > 100:
    	self.__x = 100
    else:
    	self.__x = x