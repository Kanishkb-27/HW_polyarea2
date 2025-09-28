class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area of the rectangle is:",self.l*self.b)
class parallelogram:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area of the parallelogram is:",self.l*self.b)
rctngl=rectangle(6,8)
prlgrm=parallelogram(9,3)
for shape in (rctngl,prlgrm):
    shape.area()