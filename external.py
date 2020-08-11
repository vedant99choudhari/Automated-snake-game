from Point import Point
class node:

    def __init__(self, i, j, g=-1, parent=None):
        self.i = i
        self.j = j
        self.parent = parent
        self.g_score = g
        self.f_score = -1

    def printn(self):
        print "i th: ", self.i, " j th:", self.j, " f_score:", self.f_score

    def __eq__(self, object):
        return isinstance(object, node) and self.i == object.i and self.j == object.j

    def e_distance(self, other):
        return ((self.i - other.j) ** 2 + (self.j - other.j) ** 2) ** 0.5

    def distance(self, object):
        return self.e_distance(object)

    def calculate(self, object):
        self.f_score = self.g_score + self.distance(object)

    def get_neighbour(self):
        x = self.i
        y = self.j
        g = self.g_score + 1
        neighbour = []
        neighbour.append(node(x + 1, y, g, self))
        neighbour.append(node(x - 1, y, g, self))
        neighbour.append(node(x, y + 1, g, self))
        neighbour.append(node(x, y - 1, g, self))

        return neighbour

    def get_path(self):
        path = []
        path.append(self)
        if (not self.parent == 0) and not(self.parent == None):
            path.append(self.parent)
            temp = self.parent.get_path()
            if not temp == None:
                path.extend(temp)

        return path


def get_f_score(object):
    return object.f_score


def print_list(nodes):
    print "start"
    for node in nodes:
        print node.printn()
    print "end"
    
def print_bodies(points):
    print "start"
    for point_1 in points:
        print point_1.x ,point_1.y
    print"end"

class A_star:

    def __init__(self, body, target):
        self.body = body
        self.target = node(target.x, target.y)

    def is_valid(self, node):
        if node.i > -1 and node.i < Point.row and node.j > -1 and node.j < Point.col:
            for scale_part in self.body:
                if node.i==scale_part.x and node.j==scale_part.y:
                    return False
            return True

        return False
    
    def get_unique(self,data):
        unique = []
        for item in data:
            if item not in unique:
                unique.append(item)
        
        return unique
    
    def draw_rect(self,x,y,color=-1):
        block = 30
        ratio =0.9
        offset = block/2
        if color==1:
            fill(255,0,0)
        elif color == 2:
            fill(0,255,0)
        elif color == 3:
            fill(0,0,255)
        else :
            fill(255,204)

        rect(offset+(block*x),offset+(block*y),block*ratio,block*ratio)
        fill(255,204)

    def find(self):
        open_list = []
        closed_list = []

        start = self.body[0]

        # inserting the initial node
        open_list.append(node(start.x, start.y, 0))
        open_list[0].calculate(self.target)

        while len(open_list) > 0:
            current = min(open_list, key=get_f_score)
            index = open_list.index(current)

            if current == self.target:
                path = current.get_path()
                # for block in path:
                #     self.draw_rect(block.i,block.j,3)
                path = self. get_unique(path)
                return path

            open_list.remove(current)

            if not current in closed_list:
                # print "adding element to closed list:", current.printn()
                closed_list.append(current)

            neighbour = current.get_neighbour()

            for location in neighbour:
                if not self.is_valid(location):
                    # print "invalid"
                    continue
                # print "valid neighbour" , location.printn()
                if location in closed_list:
                    # print "the element is in closed list:", location.printn()
                    continue

                if location in open_list:
                    # print "the element is in open list:",location.printn() ,
                    # "at location:",open_list.index(location)
                    in_list_index = open_list.index(location)
                    in_list = open_list[in_list_index]

                    if in_list.g_score < location.g_score:
                        open_list.remove(in_list)
                        open_list.append(location)
                else:
                    # print "adding elemt to open_list" , location.printn()
                    location.calculate(self.target)
                    open_list.append(location)

        print "no solution"
