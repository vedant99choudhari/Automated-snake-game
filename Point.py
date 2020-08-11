class Point:
    row  = 30              
    col = 30
    
    fruitx = None
    fruity = None
    def __init__(self):
        self.x =0
        self.y =0
        
    def __init__(self,x,y,check =True):
        if x>-1 and x<self.row and y>-1 and y<self.col :
            self.x = x
            self.y = y
        else:
            raise ValueError
            
        if x == Point.fruitx and  y ==Point.fruity and check:
            raise AssertionError

        
    
