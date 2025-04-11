import pytest
import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
import matplotlib.pyplot as plt
from hina.construction import get_bipartite
from hina.mesoscale import hina_communities
from hina.visualization import plot_hina, plot_bipartite_clusters

def create_test_graph():
    # Create a test graph from DataFrame using get_bipartite 
    df = pd.DataFrame({
        'student': ['Alice', 'Bob', 'Alice', 'Charlie'],
        'object1': ['ask questions', 'answer questions', 'evaluating', 'monitoring'],
        'object2': ['tilt head', 'shake head', 'nod head', 'nod head'],
        'group': ['A', 'B', 'A', 'B'],
        'attr': ['cognitive', 'cognitive', 'metacognitive', 'metacognitive']
    })
    
    B = get_bipartite(
        df,
        student_col='student', 
        object_col='object1', 
        attr_col='attr', 
        group_col='group'
    )
    return B

def test_plot_hina_basic():
    # Test basic functionality of plot_hina
    B = create_test_graph()
    
    # Test with default parameters
    plt.figure()  # Create a new figure
    result = plot_hina(B)
    plt.close() 

def test_plot_hina_with_layout():
    # Test plot_hina with different layout options
    B = create_test_graph()
    
    # Test with bipartite layout
    plt.figure()
    plot_hina(B, layout='bipartite')
    plt.close()
    
    # Test with spring layout
    plt.figure()
    plot_hina(B, layout='spring')
    plt.close()
    
    # Test with circular layout
    plt.figure()
    plot_hina(B, layout='circular')
    plt.close()

def test_plot_hina_with_group_filtering():
    # Test plot_hina with group filtering
    B = create_test_graph()
    
    # Test for all groups (no filtering)
    plt.figure()
    plot_hina(B, layout='bipartite', group_name=['group', None])
    plt.close()
    
    # Test for specific group
    plt.figure()
    plot_hina(B, layout='bipartite', group_name=['group', 'A'])
    plt.close()

def test_plot_hina_with_pruning():
    # Test plot_hina with pruning parameters
    B = create_test_graph()
    
    # Test with custom pruning parameters
    plt.figure()
    pruning_kwargs = {'fix_deg': 'None', 'alpha': 0.05}
    plot_hina(B, pruning_kwargs=pruning_kwargs)
    plt.close()

def test_plot_hina_with_networkx_kwargs():
    # Test plot_hina with custom NetworkX parameters
    B = create_test_graph()
    
    plt.figure()
    networkx_kwargs = {'width': 2.0, 'alpha': 0.7, 'edge_color': 'blue'}
    plot_hina(B, NetworkX_kwargs=networkx_kwargs)
    plt.close()

def test_plot_bipartite_clusters_auto():
    # Test plot_bipartite_clusters with automatic community detection
    B = create_test_graph()
    
    # Test with automatic community detection
    plt.figure()
    plot_bipartite_clusters(B)
    plt.close()


if __name__ == "__main__":
    pytest.main()