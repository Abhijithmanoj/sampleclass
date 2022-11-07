class Line():
    def __init__(self,c1,c2):
        self.c1=c1
        self.c2=c2
        print("Coordinate 1\nX1={},Y1={}".format(c1[0],c1[1]))
        print("Coordinate 2\nX2={},Y2={}".format(c2[0], c2[1]))
    def distance(self):
        d = ((self.c2[0] - self.c1[0])**2 + (self.c2[1] - self.c1[1])**2)**0.5 #distance= sqrt((x2-x1)^2 + (y2-y1)^2))
        print(f"Distance: {d}")
    def slope(self):
        """s=y2-y1 / x2-x1"""
        s = (c2[1]-c1[1])/(c2[0]-c1[0])
        print("Slope: {}".format(s))
c1=(3,2)
c2=(8,10)
l=Line(c1,c2)
l.distance()
l.slope()