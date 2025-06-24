hina.individual
++++++++++++

Tutorial
========

The `individual` module provides functions for computing node-level measures related to the participation of individuals in learning processes. The module focuses on analyzing the quantity and diversity of interactions based on the connections between individuals and tasks. This module provides  node-level measures for understanding individual participation patterns.

.. list-table:: Functions

Currently, the module contains the following Python files:

- `quantity.py`: Provides functions to calculate the quantity of individual interactions with tasks.
- `diversity.py`: Provides functions to calculate the diversity of individual interactions based on task distributions.

.. list-table:: Functions
   :header-rows: 1

   * - Function
     - Description
   * - `quantity(B, attr=None, group=None, return_type='all') <#quantity>`_
     - Computes various quantities and normalized quantities for student nodes in a bipartite graph.
   * - `diversity(B, attr=None) <#diversity>`_
     - Computes the diversity value of individual nodes in a bipartite graph based on a specified attribute or the object nodeset.

Reference
---------

.. _quantity:

.. raw:: html

   <div id="quantity" class="function-header">
       <span class="class-name">function</span> <span class="function-name">quantity(B, attr=None, group=None, return_type='all')</span> 
       <a href="../Code/quantity_diversity.html#quantity" class="source-link">[source]</a>
   </div>

**Description**:
Computes various quantities and normalized quantities for student nodes in a bipartite graph, gauging the quantity of individual involvement in the studied objects.

**Parameters**:

.. raw:: html

   <div class="parameter-block">
       (B, attr=None, group=None, return_type='all')
   </div>

   <ul class="parameter-list">
       <li><span class="param-name">B</span>: A bipartite graph with weighted edges. Nodes are expected to have attributes if <code>attr</code> or <code>group</code> is provided.</li>
       <li><span class="param-name">attr</span>: The name of the object node attribute used to categorize the connected object nodes. If provided, the function calculates quantity by category. Default is <code>None</code>.</li>
       <li><span class="param-name">group</span>: The name of the student node attribute used to group nodes. If provided, the function calculates normalized quantity by group. Default is <code>None</code>.</li>
       <li><span class="param-name">return_type</span>: Specifies the type of results to return. Options are:
		<ul>
            <li><code>'all'</code>: Returns all computed quantities (default).</li>
            <li><code>'quantity'</code>: Returns only the raw quantity for each node.</li>
            <li><code>'quantity_by_category'</code>: Returns only the quantity partitioned by category.</li>
            <li><code>'normalized_quantity'</code>: Returns only the normalized quantity for each node.</li>
            <li><code>'normalized_quantity_by_group'</code>: Returns only the normalized quantity by group.</li>
		</ul>
   </ul>

**Returns**:
  - **dict**: A dictionary containing the computed quantities based on the `return_type` parameter. Possible keys include:

    - ``'quantity'``: A dictionary mapping each node to its total edge weight.
    - ``'normalized_quantity'``: A dictionary mapping each node to its normalized edge weight.
    - ``'quantity_by_category'``: A dictionary mapping (node, category) tuples to their total edge weight.
    - ``'normalized_quantity_by_group'``: A dictionary mapping each node to its normalized edge weight within its group.

  - **dataframe**: A dataframe containing the diversity value of each student node.


.. _diversity:

.. raw:: html

   <div id="diversity" class="function-header">
       <span class="class-name">function</span> <span class="function-name">diversity(B, attr=None)</span> 
       <a href="../Code/quantity_diversity.html#diversity" class="source-link">[source]</a>
   </div>

**Description**:
Computes the diversity value of individual nodes in a bipartite graph based on a specified attribute or the object nodeset.

**Parameters**:

.. raw:: html

   <div class="parameter-block">
       (B, attr=None)
   </div>

   <ul class="parameter-list">
       <li><span class="param-name">B</span>: A bipartite graph. Nodes are expected to have a 'bipartite' attribute indicating their partition.</li>
       <li><span class="param-name">attr</span>: The column name of the attribute related to the studied objects. If provided, diversity is calculated based on the categories of the specified attribute. Default is <code>None</code>.</li>
   </ul>

**Returns**:
  - **dict**: A dictionary where keys are nodes and values are their diversity values, indicating how evenly their connections are distributed across different categories.
  - **dataframe**: A dataframe containing the diversity value of each student node.

Demo
====

Example Code
------------

This example demonstrates how to use the `quantity` and `diversity` functions to compute node-level measures.

**Step 1: Import necessary libraries**

.. code-block:: python

    import pandas as pd
    from hina.individual import quantity, diversity
    from hina.construction import get_bipartite

**Step 2: Define the dataset**

A dataset containing student-task interactions:

.. code-block:: python

    df = pd.DataFrame({
         'student': ['Alice', 'Bob', 'Alice', 'Charlie'],
         'object1': ['ask questions', 'answer questions', 'evaluating', 'monitoring'],
         'object2': ['tilt head', 'shake head', 'nod head', 'nod head'],
         'group': ['A', 'B', 'A', 'B'],
         'attr': ['cognitive', 'cognitive', 'metacognitive', 'metacognitive']
     })

**Step 3: Construct the bipartite network representation**

We create a bipartite network representation of the interactions between students and objects in the 'object1' category, adding the additional attribute 'attr' storing object codes.

.. code-block:: python

    B = get_bipartite(df,student_col='student', object_col='object1', attr_col='attr', group_col='group')

**Step 4a: Compute quantity measures**

We calculate the quantity of interactions for each student relative to the object.

.. code-block:: python

    quantities = quantity(B, attr='attr', group='group', return_type='all')
    print("Quantities for bipartite network:\n", quantities[0])

**Step 4b: Compute diversity measures**

We calculate the diversity of interactions for each student relative to the object.

.. code-block:: python

	diversities = diversity(B, attr='attr')
	print("Diversities for Tripartite network:\n", diversities[0])

Example Output
--------------

.. code-block:: console

	Quantities for bipartite network:
	{'quantity': {'Alice': 2, 'Bob': 1, 'Charlie': 1}, 
	'normalized_quantity': {'Alice': 0.5, 'Bob': 0.25, 'Charlie': 0.25}, 
	'quantity_by_category': defaultdict(<class 'float'>, {('Alice', 'cognitive'): 1.0, ('Alice', 'metacognitive'): 1.0, ('Bob', 'cognitive'): 1.0, ('Charlie', 'metacognitive'): 1.0}), 
	'normalized_quantity_by_group': {'Alice': 1.0, 'Bob': 0.5, 'Charlie': 0.5}}

	Diversities for Tripartite network:
	{'Alice': 1.0, 'Bob': -0.0, 'Charlie': -0.0}

Paper Source
============

If you use this function in your work, please cite:

Feng, S., Gibson, D., & Gasevic, D. (2025). Analyzing students' emerging roles based on quantity and heterogeneity of individual contributions in small group online collaborative learning using bipartite network analysis. Journal of Learning Analytics, 12(1), 253–270.
