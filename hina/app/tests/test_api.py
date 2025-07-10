import pytest
import json
import pandas as pd
from fastapi.testclient import TestClient

def test_upload_file(client, sample_csv):
    # Test file upload endpoint
    response = client.post(
        "/upload",
        files={"file": ("test.csv", sample_csv, "text/csv")}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "columns" in data
    assert "data" in data
    assert "upload_id" in data
    assert "timestamp" in data
    assert "filename" in data
    
    # Check columns names
    assert set(data["columns"]) >= {"student", "object1", "object2", "group", "attr"}, "Expected columns missing"

def test_build_hina_network_endpoint(client, sample_csv):
    # Test building HINA network endpoint
    # Upload the file
    upload_response = client.post(
        "/upload",
        files={"file": ("test.csv", sample_csv, "text/csv")}
    )
    upload_data = upload_response.json()
        
    # Build the network
    for layout in ["bipartite", "spring", "circular"]:
        response = client.post(
            "/build-hina-network",
            data={
                "data": upload_data["data"],
                "group_col": "group",
                "group": "Group 1",
                "student_col": "student",
                "object1_col": "object1",
                "object2_col": "",
                "attr_col": "attr",
                "pruning": "none",
                "alpha": 0.05,
                "fix_deg": "",
                "layout": layout
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "elements" in data
        assert "significant_edges" in data
        assert len(data["elements"]) > 0
    response = client.post(
        "/build-hina-network",
        data={
            "data": upload_data["data"],
            "group_col": "group",
            "group": "Group 1",
            "student_col": "student",
            "object1_col": "object1",
            "object2_col": "",
            "attr_col": "attr",
            "pruning": "none",
            "alpha": 0.05,
            "fix_deg": "",
            "layout": 'test'  # Invalid layout
        }
    )
    assert response.status_code == 200

def test_build_cluster_network_endpoint(client, sample_csv):
    # Test building clustered network endpoint
    # Upload the file
    upload_response = client.post(
        "/upload",
        files={"file": ("test.csv", sample_csv, "text/csv")}
    )
    upload_data = upload_response.json()
    
    # Build the clustered network
    for layout in ["bipartite", "spring", "circular", "test"]:
        response = client.post(
            "/build-cluster-network",
            data={
                "data": upload_data["data"],
                "group_col": "group",
                "student_col": "student",
                "object1_col": "object1",
                "object2_col": "",
                "attr_col": "attr",
                "pruning": "none",
                "alpha": 0.05,
                "fix_deg": "",
                "layout": layout,
                "number_cluster": "2"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "elements" in data
        assert "cluster_labels" in data
        assert "compression_ratio" in data
        assert "object_object_graphs" in data
        assert "significant_edges" in data

def test_build_object_network_endpoint(client, sample_csv):
    # Test building object network endpoint
    # Upload the file and create clustered network
    upload_response = client.post(
        "/upload",
        files={"file": ("test.csv", sample_csv, "text/csv")}
    )
    upload_data = upload_response.json()
    
    cluster_response = client.post(
        "/build-cluster-network",
        data={
            "data": upload_data["data"],
            "group_col": "group",
            "student_col": "student",
            "object1_col": "object1",
            "object2_col": "object2",  # Include object2 to create object-object graphs
            "attr_col": "attr",
            "pruning": "none",
            "alpha": 0.05,
            "fix_deg": "",
            "layout": "bipartite",
            "number_cluster": "2"
        }
    )
    
    cluster_data = cluster_response.json()
    
    # Skip test if no object_object_graphs were created
    if "object_object_graphs" not in cluster_data or not cluster_data["object_object_graphs"]:
        pytest.skip("No object-object graphs were created, skipping test")
    
    # Get first community ID
    community_id = list(cluster_data["object_object_graphs"].keys())[0]
    
    # Build the object network
    for layout in ["bipartite", "spring", "circular", "test"]:
        response = client.post(
            "/build-object-network",
            data={
                "data": json.dumps(cluster_data["object_object_graphs"]),
                "community_id": community_id,
                "object1_col": "object1",
                "object2_col": "object2",
                "layout": layout
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "elements" in data
        assert "community_id" in data

def test_quantity_diversity_endpoint(client, sample_csv):
    # Test quantity and diversity endpoint
    # Upload the file
    upload_response = client.post(
        "/upload",
        files={"file": ("test.csv", sample_csv, "text/csv")}
    )
    upload_data = upload_response.json()
    
    # Parse data from upload response
    data_list = upload_data["data"]
    if isinstance(data_list, str):
        data_list = json.loads(data_list)
    
    # Now get quantity and diversity
    response = client.post(
        "/quantity-diversity",
        data={
            "data": upload_data["data"],
            "student_col": "student",
            "object1_col": "object1",
            "object2_col": "object2",
            "attr_col": "attr",
            "group_col": "group"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "quantity" in data
    assert "normalized_quantity" in data
    assert "diversity" in data

    response = client.post(
        "/quantity-diversity",
        data={
            "data": upload_data["data"],
            "student_col": "student",
            "object1_col": "object1",
            "object2_col": "object2",
            "group_col": "group"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "quantity" in data
    assert "normalized_quantity" in data
    assert "diversity" in data

if __name__ == "__main__":
    pytest.main()