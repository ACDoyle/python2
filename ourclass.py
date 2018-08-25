class OurClass(object):
  def __init__(self, a):
    self.OurAtrr = a

  @property
  def OurAtrr(self):
    return self.__OurAtrr

  @OurAtrr.setter
  def OurAtrr(self, val):
    if val < 0:
      self.__OurAtrr = 0
    elif val > 10:
      self.__OurAtrr = 10
    else:
      self.__OurAtrr = val

if __name__ == "__main__":
  x = OurClass(-100)
  print(x.OurAtrr)
  x = OurClass(3)
  print(x.OurAtrr)
  x = OurClass(100)
  print(x.OurAtrr)
  x = OurClass(8.9)
  print(x.OurAtrr)
