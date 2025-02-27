import pytest
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from hina.visualization.network_visualization import plot_HINA, plot_bipartite_clusters

@pytest.fixture
def sample_data():
    data = {
        'student id': ['s1', 's2', 's3', 's4'],
        'task': ['t1', 't2', 't1', 't2'],
        'group': ['A', 'A', 'B', 'B']
    }
    return pd.DataFrame(data)

def test_plot_HINA(sample_data):
    try:
        plot_HINA(sample_data, attribute_1='student id', attribute_2='task', group='A', layout='spring')
    except Exception as e:
        pytest.fail(f"plot_HINA raised an exception: {e}")

def test_plot_HINA_invalid_layout(sample_data):
    with pytest.raises(ValueError):
        plot_HINA(sample_data, attribute_1='student id', attribute_2='task', layout='invalid')

def test_plot_bipartite_clusters():
    G = [('s1', 't1', 1), ('s2', 't2', 2), ('s3', 't1', 3), ('s4', 't2', 4)]
    community_labels = {'s1': 0, 's2': 1, 's3': 0, 's4': 1}
    try:
        plot_bipartite_clusters(G, community_labels)
    except Exception as e:
        pytest.fail(f"plot_bipartite_clusters raised an exception: {e}")

if __name__ == "__main__":
    pytest.main()
