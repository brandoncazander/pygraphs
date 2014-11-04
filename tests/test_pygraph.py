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
        self.p.create_vertex("c", 150, 50)

    def test_location(self):
        a = self.p.get_vertex("a")
        x, y = a.get_center()
        self.assertEqual(x, 100)
        self.assertEqual(y, 100)

    def test_connect(self):
        self.p.connect("a", "b")
        self.assertEqual([("a", "b"), ("b", "a")], self.p.get_edges())

    def test_collides_center(self):
        a = self.p.get_colliding_vertex(100, 100)
        b = self.p.get_colliding_vertex(50, 50)
        self.assertEqual(a, "a")
        self.assertEqual(b, None)

    def test_collides_at_edge(self):
        c = self.p.get_colliding_vertex(108, 108)
        self.assertEqual(c, "a")

    def test_euclid_dist(self):
        self.assertEqual(0, self.p._euclid_dist(100, 200, 100, 200))
        self.assertEqual(35, self.p._euclid_dist(125, 125, 100, 100))

    def test_reconnect(self):
        self.p.connect("a", "b")
        self.p.connect("a", "b")
        self.assertEqual([("a", "b"), ("b", "a")], self.p.get_edges())

    def test_complete_graph_cycle(self):
        self.p.connect("a", "b")
        self.p.connect("a", "c")
        complete_graph = [
            ('a', ['b', 'c']),
            ('c', ['a', 'b']),
            ('b', ['a', 'c'])
        ]
        self.p.complete_graph()
        self.assertEqual(complete_graph, self.p.graph.items())

    def test_complete_graph_empty(self):
        complete_graph = [
            ('a', ['c', 'b']),
            ('c', ['a', 'b']),
            ('b', ['a', 'c'])
        ]
        self.p.complete_graph()
        self.assertEqual(complete_graph, self.p.graph.items())


if __name__ == "__main__":
    unittest.main()
