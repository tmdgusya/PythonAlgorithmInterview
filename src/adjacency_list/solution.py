import unittest


def create_adjacency_list():

    graph = [[] for _ in range(3)]

    print(graph)

    graph[0].append((1,7))
    graph[0].append((2,5))

    graph[1].append((0,7))
    graph[2].append((0,5))


class TestClass(unittest.TestCase):

    def test_one(self):
        create_adjacency_list()