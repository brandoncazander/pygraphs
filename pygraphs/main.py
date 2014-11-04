from collections import defaultdict
from Tkinter import *
import math

class Pygraph:

    def __init__(self, width=500, height=250, w=14, y=14):
        self.master = Tk()
        self.canvas = Canvas(self.master, width=width, height=height)
        self.canvas.pack()
        self.vertices = {}
        self.graph = defaultdict(list)
        self.name_index = 0
        self.w = w
        self.y = y
        self.dw = self.w / 2
        self.dy = self.y / 2

    def create_vertex(self, name, x, y):
        self.vertices[name] = Vertex(x,
                                     y)
        self.canvas.create_oval(x - self.dw,
                                y - self.dy,
                                x + self.dw,
                                y + self.dy,
                                fill="red")

    def run(self):
        self.canvas.bind("<Button-1>", self.click_callback)
        self.canvas.bind("<ButtonRelease-1>", self.unclick_callback)
        mainloop()

    def get_vertices(self):
        return self.vertices.items()

    def get_vertex(self, name):
        return self.vertices[name]

    def connect(self, v1, v2):
        self.graph[v1].append(v2)
        c1 = self.get_vertex(v1).get_center()
        c2 = self.get_vertex(v2).get_center()
        self.canvas.create_line(c1, c2, fill="red")

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                edges.append((vertex, neighbour))
        return edges

    def click_callback(self, event):
        self.mouse_start_x = event.x
        self.mouse_start_y = event.y

    def get_colliding_vertex(self, x, y):
        for name, vertex in self.get_vertices():
            x_2, y_2 = vertex.get_center()
            if math.sqrt((x-x_2)**2 + (y-y_2)**2) < self.dw:
                return name
        return None

    def unclick_callback(self, event):
        if (abs(self.mouse_start_x - event.x) > 14
            or abs(self.mouse_start_y - event.y) > 14):
            # dragging
            print("dragged from ({}, {}) to ({}, {})".format(self.mouse_start_x,
                                                             self.mouse_start_y,
                                                             event.x,
                                                             event.y))
            start = self.get_colliding_vertex(self.mouse_start_x, self.mouse_start_y)
            end = self.get_colliding_vertex(event.x, event.y)
            if (start and end):
                self.connect(start, end)
        else:
            # no drag, select or create vertex
            name = "v{}".format(++self.name_index)
            self.create_vertex(name, event.x, event.y)


class Vertex:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_center(self):
        return (self.x, self.y)

    def __str__(self):
        return "Vertex(x={}, y={})".format(self.x, self.y)

    def __getitem__(self):
        return self

if __name__ == "__main__":
    c = Pygraph()
    c.create_vertex("a", 100, 100)
    c.create_vertex("b", 150, 150)
    c.create_vertex("c", 150, 50)
    c.connect("a", "b")
    c.connect("a", "c")
    c.run()
