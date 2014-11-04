from collections import defaultdict
from Tkinter import *
import math

VERTEX_MODE = 0
DRAG_MODE = 1
EDGE_MODE = 2

class Pygraph(object):

    def __init__(self, width=500, height=250, diam=25):
        self.master = Tk()
        self.make_toolbar()
        self.canvas = Canvas(self.master, width=width, height=height)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.vertices = {}
        self.graph = defaultdict(list)
        self.name_index = 0
        self.w = diam
        self.y = diam
        self.dw = self.w / 2
        self.dy = self.y / 2

    """
    Buttons
    """
    def make_toolbar(self):
        self.toolbar = Frame(self.master)
        self.b_vertex = Button(self.toolbar, text="Add Vertices", command=self.button_vertex)
        self.b_drag = Button(self.toolbar, text="Drag", command=self.button_drag)
        self.b_edge = Button(self.toolbar, text="Add Edges", command=self.button_edge)
        self.b_complete = Button(self.toolbar, text="Complete Graph", command=self.button_complete)
        self.b_vertex.pack()
        self.b_drag.pack()
        self.b_edge.pack()
        self.b_complete.pack()
        self.toolbar.pack()
        self.button_vertex()

    def button_vertex(self):
        self.mode = VERTEX_MODE

    def button_drag(self):
        self.mode = DRAG_MODE

    def button_edge(self):
        self.mode = EDGE_MODE

    def button_complete(self):
        self.complete_graph()

    """
    Getter/setter functions
    """
    def get_vertices(self):
        return self.vertices.items()

    def get_vertex(self, name):
        return self.vertices[name]

    """
    Canvas functions
    """
    def create_vertex(self, name, x, y):
        self.vertices[name] = Vertex(x,
                                     y)
        self.canvas.create_oval(x - self.dw,
                                y - self.dy,
                                x + self.dw,
                                y + self.dy,
                                fill="red",
                                tags="vertex")
        self.canvas.create_text(x, y, text=name, tags="label")
        self.reorder()

    def reorder(self):
        self.canvas.tag_raise("vertex")
        self.canvas.tag_raise("label")

    def connect(self, v1, v2):
        if v2 not in self.graph[v1] and v1 not in self.graph[v2]:
            self.graph[v1].append(v2)
            c1 = self.get_vertex(v1).get_center()
            c2 = self.get_vertex(v2).get_center()
            self.canvas.create_line(c1, c2, fill="red", tags="edge")

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                edges.append((vertex, neighbour))
        return edges

    def get_colliding_vertex(self, x, y):
        for name, vertex in self.get_vertices():
            x_2, y_2 = vertex.get_center()
            if self._euclid_dist(x, y, x_2, y_2) <= self.w / 2:
                return name
        return None

    def run(self):
        self.canvas.bind("<Button-1>", self.click_callback)
        self.canvas.bind("<ButtonRelease-1>", self.unclick_callback)
        mainloop()

    """
    Helper functions
    """
    def _euclid_dist(self, x_1, y_1, x_2, y_2):
        return int(math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2))

    """
    Mouse callbacks
    """
    def click_callback(self, event):
        self.mouse_start_x = event.x
        self.mouse_start_y = event.y

    def unclick_callback(self, event):
        if self.mode is EDGE_MODE:
            if (abs(self.mouse_start_x - event.x) > self.w
                or abs(self.mouse_start_y - event.y) > self.w):
                # dragging
                start = self.get_colliding_vertex(self.mouse_start_x,
                                                  self.mouse_start_y)
                end = self.get_colliding_vertex(event.x, event.y)
                if (start and end):
                    self.connect(start, end)
        elif self.mode is DRAG_MODE:
            pass
        elif self.mode is VERTEX_MODE:
            # Create a new vertex
            name = "v{}".format(self.name_index)
            self.name_index += 1
            self.create_vertex(name, event.x, event.y)

    """
    Graph functions
    """
    def complete_graph(self):
        pass

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
