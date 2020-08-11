import Point as dummy
class snake:
    def __init__(self):
        self.body = []
        
        
        self.body.append(dummy.Point(0,0))
        
    def get_body(self):
        return self.body
    
    def append_body(self,a):
        self.body.append(a)
    
    def move_up(self):
        print "up"
        return self.move_to(0,-1)
        
    def move_down(self):
        print "down"
        return self.move_to(0,1)
        
    def move_left(self):
        print "left"
        return self.move_to(-1,0)
        
    def move_right(self):
        print "right"
        return self.move_to(1,0)
    
    def abs_move(self,x,y):
        try:
            head = self.body[0]
            temp=self.body.pop()
            #print x ,' ',y , " head " , head.x ,' ',head.y 
            if head.x == x and head.y == y:
                self.body.append(temp)
                print "no change"
                return False
            self.check(x,y)
            self.body.insert(0,dummy.Point(x,y))
            return False
        except AssertionError:
            print "ate fruit"
            self.body.insert(0,dummy.Point(x,y,False))
            self.body.append(temp)
            return True
        except ValueError:
            print "value error"
            self.body.append(temp)
        except Exception ,error:
            print str(error)
                
    def move_to(self,x,y):
        try:
            head = self.body[0]
            temp=self.body.pop()
            self.check(head.x+x,head.y+y)
            self.body.insert(0,dummy.Point(head.x+x,head.y+y))
            return False
        except AssertionError:
            print "ate fruit"
            self.body.insert(0,dummy.Point(head.x+x,head.y+y,False))
            self.body.append(temp)
            return True
        except ValueError:
            print "value error"
            self.body.append(temp)
        except Exception ,error:
             print str(error)
    
    
    def check(self,X,Y):
        for block in self.body:
            if block.x == X and block.y == Y:
                print "in body"

            
            
            
        
