class mul_node:
  def __init__(self):
    self.x,self.y=None,None
    self.z=None

  def forward(self,x,y):
    self.x,self.y=x,y
    self.z=self.x*self.y
    return self.z

  def backward(self,dz):
    return dz*self.y,dz*self.x

class minus_node:
  def __init__(self):
    self.x,self.y=None,None
    self.z=None

  def forward(self,x,y):
    self.x,self.y=x,y
    self.z=self.x-self.y
    return self.z

  def backward(self,dz):
    return dz,-dz

class square_node:
  def __init__(self):
    self.x,self.z=None,None

  def forward(self,x):
    self.x=x
    self.z=self.x**2
    return self.z

  def backward(self,dz):
    return 2*self.x*dz
