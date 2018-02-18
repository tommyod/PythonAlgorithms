#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Undirected graphs.
"""

import collections
import heapq

try:
    from algorithms.unionfind import UnionFind
except ModuleNotFoundError:
    from ..algorithms.unionfind import UnionFind

PRINTING = False


def pprint(*args, **kwargs):
    """
    Printing which can be turned off or on globally. For debugging and
    learning.
    """
    if PRINTING:
        print(*args, **kwargs)


class UndirectedGraph(object):
    """
    """
    
    def __init__(self, edges, weights=None):
        """Initialize a new undirected graph lists of edges and weights.

        The undirected graph is represented using a dictionary.

        Parameters
        ----------
        edges : sequence
            An sequence of tuples representing vertices joined by an edge, i.e.
            [(2, 3), (2, 4), (1, 2)].
            
        weights : sequence
            Weights corresponding to each edge in `list_of_edges`, i.e.
            [2, 1, 3].
        
            
        Examples
        --------
        >>> edges = [(2, 3), (2, 4), (1, 2)]
        >>> weights = [2, 1, 3]
        >>> g = UndirectedGraph(edges, weights)
        
        >>> edges = [('a', 'b'), ('a', 'c'), ('a', 'd')]
        >>> g2 = UndirectedGraph(edges)
        
        >>> edges = [('a', 'b'), ('a', 'd'), ('a', 'c'), ('a', 'd')]
        >>> g3 = UndirectedGraph(edges)
        >>> g2 == g3
        True

        """
        
        # Initialize a default dictionary representing the edges and weights
        self._edges = collections.defaultdict(set)
        self._weights = collections.defaultdict(lambda: None)
        
        # Depending on whether or not weights were passed, create itertors
        if weights:
            if not len(edges) == len(weights):
                err_msg = 'Number of edges must equal number of weights.'
                raise ValueError(err_msg)
            edge_iterator = zip(edges, weights)
        else:
            edge_iterator = iter(edges)
        
        # Add every edge to the default dictionary
        for item in edge_iterator:
            
            # Unpack the weight if weights were passed
            if weights:
                (a, b), weight = item
            else:
                (a, b) = item
            
            # No self-joined vertices are allowed
            if a == b:
                continue
            
            self._edges[a].add(b)
            self._edges[b].add(a)
            
            # Use a frozenset, since edge (a,b) has the same weight as (b, a)
            if weights:
                self._weights[frozenset((a, b))] = weight
                
    def weight(self, edge):
        """
        Returns the weight of an edge.
        """
        
        return self._weights[frozenset(edge)]
                
    def edges(self, and_weights=False):
        """Yield the edges in the graph, and alternatively the weights too.
        
        Parameters
        ----------
        and_weights : bool
            Yield tuples with ((u, v), weight) if `True`.
            
        Yields
        ------
        tuple: (edge, weight) = ((u, v), weight)
            
        Examples
        --------
        >>> weights = list(range(3))
        >>> g = UndirectedGraph([(0, 1), (1, 2), (2, 3)])
        >>> for edge in g.edges():
        ...    print(edge)
        (0, 1)
        (1, 2)
        (2, 3)
        
        >>> g = UndirectedGraph([(0, 1), (1, 2), (2, 3)], weights)
        >>> for edge, weight in g.edges(and_weights=True):
        ...    print(edge, '->',  weight)
        (0, 1) -> 0
        (1, 2) -> 1
        (2, 3) -> 2
        """

        # Keep track of yielded so as not to yield (1, 2) AND (2, 1), since
        # they are the same edge using this graph representation
        yielded = set()
        
        # Iterate over the vertices in the graph
        for vertex, neighbors in self._edges.items():
            for neighbor in neighbors:
                
                # Use a frozen set to keep track of tuples without caring
                # about the order of the elements
                to_yield = frozenset((vertex, neighbor))
                
                # Seen it before, so do not yield it again
                if to_yield in yielded:
                    continue
                # Never seen before, add it
                else:
                    yielded.add(to_yield)

                # Yield edge and weights if the user requested it
                if and_weights:
                    yield (vertex, neighbor), self._weights[to_yield]
                else:
                    yield (vertex, neighbor)
                
    def __eq__(self, other):
        """Test if two undirected graphs are equal.
        
        Two graphs are equal iff they share the same
        dictionary representation.
        
        Returns
        ------
        bool: True if the graphs are equal.
            
        Examples
        --------
        >>> # Permuting the edges does not change equality
        >>> g = UndirectedGraph([(0, 1), (1, 2), (2, 3)])
        >>> h = UndirectedGraph([(1, 2), (2, 3), (0, 1)])
        >>> g == h
        True
        
        >>> # Repetition of the same edge is removed, so these are equal
        >>> g = UndirectedGraph([(0, 1), (1, 2), (2, 3)])
        >>> h = UndirectedGraph([(0, 1), (0, 1), (1, 2), (2, 3)])
        >>> g == h
        True
        
        # Permuting the order of the verticies does not change equality
        >>> g = UndirectedGraph([(0, 1), (1, 2)])
        >>> h = UndirectedGraph([(0, 1), (2, 1)])
        >>> g == h
        True
        """
        if isinstance(other, type(self)):
            same_edges = self._edges == other._edges
            same_weights = self._weights == other._weights
            return same_edges and same_weights
        else:
            return False
                
    def copy(self):
        """
        Return a copy of the graph.
            
        Examples
        --------
        >>> g = UndirectedGraph([(0, 1), (1, 2), (2, 3)])
        >>> g2 = g.copy()
        >>> g == g2
        True
        
        >>> g = UndirectedGraph([(0, 1), (1, 2)], [1, 4])
        >>> g2 = g.copy()
        >>> g == g2
        True
        """
        edges, weights = [], []
        
        # Here's a microoptimization
        edges_append = edges.append
        weights_append = weights.append
        
        for edge, weight in self.edges(and_weights=True):
            edges_append(edge)
            weights_append(weight)
            
        return type(self)(edges, weights)
         
    def __repr__(self):
        """
        Representation for printing.
        
        Examples
        --------
        >>> g = UndirectedGraph([(0, 1), (1, 2), (2, 3)])
        >>> g
        0 : {1}
        1 : {0, 2}
        2 : {1, 3}
        3 : {2}
        
        >>> # If the graph has weights, they will be printed too
        >>> weights = [5, 2, 3]
        >>> g = UndirectedGraph([(0, 1), (1, 2), (2, 3)], weights)
        >>> g
        0 : {1} [5]
        1 : {0, 2} [5, 2]
        2 : {1, 3} [2, 3]
        3 : {2} [3]
        """
        has_weights = any(True for k in self._weights.keys())
        
        ret = ''
        for key, value in sorted(self._edges.items()):
            ret += ' : '.join([repr(key), repr(value)])
                    
            if has_weights:
                fs = frozenset
                ret += ' ' + repr([self._weights[fs((key, v))] for v in value])
            ret += '\n'
            
        return ret.strip()
    
    def neighbors(self, vertex, and_weights=False):
        """
        Yield the neighbors of a vertex.
        
        Parameters
        ----------
        and_weights : bool
            Yield tuples with (neighbor, weight) if `True`.
            
        Examples
        --------
        >>> g = UndirectedGraph([(0, 1), (1, 2), (2, 3)])
        >>> set(g.neighbors(1)) == {0, 2}
        True
        
        >>> g = UndirectedGraph([(1, 2), (1, 3), (2, 3), (3, 4)],
        ...                        [11, 13, 14, 12])
        >>> set(g.neighbors(1, True)) == set([(2, 11), (3, 13)])
        True
        """
        if and_weights:
            for neighbor in self._edges[vertex]:
                yield neighbor, self._weights[frozenset((vertex, neighbor))]
        else:
            yield from iter(self._edges[vertex])

    def remove(self, vertex):
        """
        Remove a vertex from the graph (and all edges connected to it).
            
        Examples
        --------
        >>> g = UndirectedGraph([(0, 1), (1, 2), (2, 3)])
        >>> g.remove(0) 
        >>> g == UndirectedGraph([(1, 2), (2, 3)])
        True
        """
        
        try:
            # Attempt to delete the vertex-key if it's in the dictionary.
            del self._edges[vertex]
            
        except KeyError:
            # Silently ignore errors where the vertex is not in the dictionary
            # TODO: Reconsider this behaviour?
            pass
        
        finally:
            # Attempt to delete the vertex of the values in the edge dictionary
            for v, neighbors in self._edges.items():
                if vertex in neighbors:
                    neighbors.remove(vertex)
                    
    def minimum_spanning_tree(self, start_vertex):
        """
        Implementation of Prim's algorithm for minimum spanning trees.
        
        Examples
        --------
        >>> # This example is from page 140 in Halim
        >>> edges = [(0, 1), (1, 2), (0, 2), (2, 3), (0, 3), (0, 4), (3, 4)]
        >>> weights = [4, 2, 4, 8, 6, 6, 9]
        >>> g = UndirectedGraph(edges, weights)
        >>> mst = g.minimum_spanning_tree(0)
        >>> mst == UndirectedGraph([(1, 0), (1, 2), (0, 3), (0, 4)], 
        ...                         weights=[4, 2, 6, 6])
        True
        
        >>> # This example is from Wikipedia
        >>> edges = [('A', 'B'), ('A', 'D'), ('D', 'B'), ('D', 'E'), 
        ...         ('B', 'E'), ('B', 'C'), ('C', 'E'), ('F', 'E'), ('C', 'F')]
        >>> weights = [1, 3, 5, 1, 1, 6, 5, 4, 2]
        >>> g = UndirectedGraph(edges, weights)
        >>> mst = g.minimum_spanning_tree('A')
        >>> mst == UndirectedGraph([('E', 'D'), ('B', 'A'), ('E', 'F'), ('F', 
        ...         'C'), ('E', 'B')], weights=[1, 1, 4, 2, 1])
        True
        """

        # Initialize sets of seen variables to far in the algorithm
        taken_edges = set()
        taken_vertices = set([start_vertex])
        all_vertices = set(self._edges.keys())
        
        # Create a list from the neighbors, heapify to turn into a queue
        neighbors_iterator = ((w, (start_vertex, v)) for (v, w) in 
                              self.neighbors(start_vertex, and_weights=True))
        queue = list(neighbors_iterator)
        heapq.heapify(queue)
        
        # While not every single vertex is taken
        while not (taken_vertices == all_vertices):

            # Pop the minimum edge (u, v) from the priority queue
            weight, (u, v) = heapq.heappop(queue)

            # If v is already taken, we have a cycle and continue
            if v in taken_vertices:
                continue
            
            # If v is not already taken, add the edge and vertex to the sets
            taken_vertices.add(v)
            taken_edges.add((frozenset((u, v)), weight))
            
            # Get edges going out to neighbors of v, i.e. every (v, u)
            for (u, w) in self.neighbors(v, and_weights=True):

                # If u is taken the edge is not interesting, since it would
                # add a cycle. If it's not taken, add to the queue
                # This if-statement speeds up computations from 5 to 4.5s
                if u not in taken_vertices:
                    heapq.heappush(queue, (w, (v, u)))
                    
        # The minimum spanning tree is found. Extract information and create
        # a new graph from it.
        mst_edges = [(u, v) for ((u, v), weight) in taken_edges]
        mst_weights = [weight for ((u, v), weight) in taken_edges]
        
        return type(self)(mst_edges, mst_weights)
        
    def _search(self, start_vertex, kind='BFS'):
        """
        General search algorithm.
        TODO
        """
        
        if kind == 'BFS':
            pop_name = 'pop'
            append_name = 'appendleft'
        if kind == 'DFS':
            pop_name = 'pop'
            append_name = 'append'
        
        # Initialize set of visited vertices and a queue
        visited = set()
        queue = collections.deque([start_vertex])
        
        # While the queue is not empty
        while queue:
            
            # Get the vertex, abandon it if it has been seen before
            vertex = getattr(queue, pop_name)()
            if vertex in visited:
                continue
            visited.add(vertex)
            yield vertex
            
            # Go through neighbors, add unseen to the queue
            for neighbor in self.neighbors(vertex):
                if neighbor not in visited:
                    getattr(queue, append_name)(neighbor)
    
    def BFS(self, start_vertex):
        """
        BFS, i.e. first in - last out.
        TODO
        """
        yield from self._search(start_vertex, kind='BFS')
            
    def DFS(self, start_vertex):
        """
        DFS, i.e. first in - first out.
        TODO
        """
        yield from self._search(start_vertex, kind='DFS')
        
    def vertices(self):
        """
        Yield the vertices in the graph.
        
        Examples
        --------
        >>> g = UndirectedGraph([(0, 1), (1, 2), (2, 3)])
        >>> set(g.vertices()) == {0, 1, 2, 3}
        True
        """
        
        yielded = set()
        
        # Iterate over every tuple of edges, e.g. ..., (1, 2), (4, 3), ...
        for vertices in self.edges():
            # Iterate over every vertex in the tuple, e.g. ..., 1, 2, 4, 3, ...
            for vertex in vertices:
                # Yield if it has not been yielded already
                if vertex not in yielded:
                    yield vertex
        
    def is_connected(self):
        """
        The graph is connected if every vertex is found using BFS or DFS.
            
        Examples
        --------
        >>> g = UndirectedGraph([(0, 1), (1, 2), (2, 3)])
        >>> g.remove(0) 
        >>> g == UndirectedGraph([(1, 2), (2, 3)])
        True
        """
        
        # All the vertices in the graph
        vertices = set(self.vertices())
        
        # Take a random vertex to start the search from
        vertex_search_start = self._edges.keys()[0]
        vertices_found = set(self.DFS(vertex_search_start))
        
        return vertices == vertices_found
    
    def kruskal(self):
        """
        Implementation of Prim's algorithm for minimum spanning trees.
        
        Examples
        --------
        >>> # This example is from page 140 in Halim
        >>> edges = [(0, 1), (1, 2), (0, 2), (2, 3), (0, 3), (0, 4), (3, 4)]
        >>> weights = [4, 2, 4, 8, 6, 6, 9]
        >>> g = UndirectedGraph(edges, weights)
        >>> mst = g.kruskal()
        >>> mst == UndirectedGraph([(1, 0), (1, 2), (0, 3), (0, 4)], 
        ...                         weights=[4, 2, 6, 6])
        True
        
        >>> # This example is from Wikipedia
        >>> edges = [('A', 'B'), ('A', 'D'), ('D', 'B'), ('D', 'E'), 
        ...         ('B', 'E'), ('B', 'C'), ('C', 'E'), ('F', 'E'), ('C', 'F')]
        >>> weights = [1, 3, 5, 1, 1, 6, 5, 4, 2]
        >>> g = UndirectedGraph(edges, weights)
        >>> mst = g.kruskal()
        >>> mst == UndirectedGraph([('E', 'D'), ('B', 'A'), ('E', 'F'), ('F', 
        ...         'C'), ('E', 'B')], weights=[1, 1, 4, 2, 1])
        True
        
        >>> edges = [(1, 2), (3, 4), (1, 3), (2, 4)]
        >>> weights = [1, 2, 8, 10]
        >>> g = UndirectedGraph(edges, weights)
        >>> mst = g.kruskal()
        >>> mst == UndirectedGraph([(1, 2), (3, 4), (1, 3)], 
        ...                           weights=[1, 2, 8])
        True
        """
        
        # Initiablize counters, used to terminate the while loop
        num_taken_edges = 0
        num_vertices = len(self._edges.keys())

        # Initialize sets of seen variables to far in the algorithm
        taken_edges = set()
        unionfind_vertices = UnionFind(list(self._edges.keys()))
        
        queue = list((w, e) for (e, w) in self.edges(and_weights=True))
        heapq.heapify(queue)
        
        while not (num_taken_edges == num_vertices - 1):
            
            # Pop off 
            weight, (u, v) = heapq.heappop(queue)
            
            # If both are in the taken set, a cycle would've been created
            if unionfind_vertices.in_same_set(u, v):
                continue
            unionfind_vertices.union(u, v)
            
            # Add the edge
            taken_edges.add((weight, (u, v)))
            num_taken_edges += 1

        # The while-loop is finished, extract information
        taken_edges = list(taken_edges)
        mst_weights = [w for (w, e) in taken_edges]
        mst_edges = [e for (w, e) in taken_edges]
        return type(self)(mst_edges, mst_weights)
        
    
if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])


if __name__ == "__main__":
    pass
    """
    %load_ext line_profiler
    %lprun -f slow_functions.main slow_functions.main()
    """
    
    # This example is from page 140 in Halim
    edges = [(1, 2), (3, 4), (1, 3), (2, 4)]
    weights = [1, 2, 8, 10]
    g = UndirectedGraph(edges, weights)
    mst = g.kruskal()
    print(mst)
    assert mst == UndirectedGraph([(1, 2), (3, 4), (1, 3)], 
                                  weights=[1, 2, 8])

    