from pygraphs.main import Pygraph, Vertex
import unittest


class TestVertexFunctions(unittest.TestCase):

    def setUp(self):
        self.v1 = Vertex(100, 100)

    def test_vertex_center(self):
        x,y = self.v1.get_center()
        self.assertEqual(x, 100)
        self.assertEqual(y, 100)

    def test_vertex_print(self):
        self.assertEqual("Vertex(x=100, y=100)", str(self.v1))


class TestPygraphFunctions(unittest.TestCase):

    def setUp(self):
        self.p = Pygraph()
        self.p.create_vertex("a", 100, 100)
        self.p.create_vertex("b", 150, 150)

    def test_location(self):
        a = self.p.get_vertex("a")
        x, y = a.get_center()
        self.assertEqual(x, 100)
        self.assertEqual(y, 100)

    def test_connect(self):
        self.p.connect("a", "b")
        self.assertEqual([("a", "b")], self.p.get_edges())

    def test_collision(self):
        a = self.p.get_colliding_vertex(100, 100)
        b = self.p.get_colliding_vertex(50, 50)
        self.assertEqual(a, "a")
        self.assertEqual(b, None)

if __name__ == "__main__":
    unittest.main()