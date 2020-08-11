from external import A_star 
from Point import Point
from snake import snake


row = Point.row
col = Point.col
brick = 30
is_update = True
ratio = 0.9
offset = brick/2
read = True
num = 0
path =[]  

player =snake()


def setup():
    #size((row+2)*brick, (col+2)*brick)
    
    
    global row,col,brick
    
    
    size( row*brick ,col*brick)
    noStroke()
    rectMode(CENTER)

    update_fruit()  


    


def draw():
    update()
    #print "the path is",path
    # for node in path:
    #     node.printn()

    
    
    


def draw_brick(node,color=-1):
    draw_brick(node.i,node.j,node,color)


def draw_brick(x,y,color=-1):
    if color==1:
        fill(255,0,0)
    elif color == 2:
        fill(0,255,0)
    elif color == 3:
        fill(0,0,255)
    else :
        fill(255,204)
        
    rect(offset+(brick*x),offset+(brick*y),brick*ratio,brick*ratio)
    fill(255,204)

def update_fruit():
    global row,col,path,player,is_update
    if is_update:
        Point.fruity = int(random(col))    
        Point.fruitx= int(random(row)) 
        
        body = player.get_body()
        
        for block in body:
            if block.x==Point.fruitx and block.y==Point.fruity:
                update_fruit()
                return
        
        test = A_star(player.get_body(),Point(Point.fruitx,Point.fruity,False))
        path = test.find()   
        if path== None:
            print "YOU LOSE"
            path =[]
            is_update =False
            #print_path()
    
def update():
    global is_update,body
    if is_update:
        background(51)
        fill(255, 204)
        body = player.get_body()
        if len(body) == 0:
            return
        draw_brick(Point.fruitx,Point.fruity)  # draw fruit
        
        for block in body:                    #draw body 
            draw_brick(block.x,block.y,1)
        
        draw_brick(body[0].x,body[0].y,2)
        
        
        text(str(len(body)),offset+(brick*(row-2)),offset+(brick))
    else :
        background(51)
        text("Score " + str(len(body)), row*brick/2, col*brick/2, brick+5, brick+5)    

def keyPressed():
    global read,player,path
    if key == '8':
        read = player.move_up()
    elif key == '6':
        read = player.move_right()
    elif key == '2':
        read = player.move_down()
    elif key == '4':
        read = player.move_left()
    elif key == ' ':
         if len(path)>0:
            x  = path.pop()
            read = player.abs_move(x.i,x.j)
    else:
        print key
        read =False
    
    if read:
        update_fruit()
    
