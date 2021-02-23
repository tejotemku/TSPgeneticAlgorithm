class City:
    def __init__(self, index, x, y, debug=False):
        self.Debug = debug
        self.x = x
        self.y = y
        self.index = index
        self.neighbours = {}
        if self.Debug:
            print("created: " + str(index) + ", x: " + str(x) + ", y: " + str(y))

    def add_neighbour(self, index, distance):
        if self.Debug:
            print("City : " + str(self.index) + ", connected to city : " + str(index) + ", distance : " + str(distance))
        self.neighbours.update({index: distance})

    def get_neighbour(self, index):
        return self.neighbours.get(index)
