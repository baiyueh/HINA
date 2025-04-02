import pytest
import networkx as nx
import numpy as np
from hina.individual.diversity import diversity

def create_test_graph():
    B = nx.Graph()
    B = nx.Graph()
    B.add_nodes_from(['Alice', 'Bob', 'Charlie'], bipartite='student', group=['A', 'B', 'B'])
    B.add_nodes_from(['ask questions', 'answer questions', 'evaluating', 'monitoring'], bipartite='object', attr=['cognitive', 'cognitive', 'metacognitive', 'metacognitive'])
    B.add_weighted_edges_from([
        ('Alice', 'ask questions', 2),
        ('Alice', 'evaluating', 1),
        ('Bob', 'answer questions', 3),
        ('Charlie', 'monitoring', 1)
    ])
    return B


def test_diversity():
    B = create_test_graph()
    result = diversity(B)
    assert 'Alice' in result[0], "Diversity for Alice should be computed."
    

if __name__ == "__main__":
    pytest.main()
