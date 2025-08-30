import sys
import requests

LOCAL_HOST = "http://127.0.0.1"

def connect_nodes(n: int):
    # Build node URLs: 5001, 5002, ..., 500N
    nodes = [f"{LOCAL_HOST}:{5000 + i}" for i in range(1, n + 1)]

    # for each node, register all others
    for i, node in enumerate(nodes, start=1):
        for target in nodes:
            if node == target:
                continue  ### ignore adding its own port to itself
            try:
                url = f"{node}/nodes/add_nodes"
                payload = {"nodes": [target]}
                r = requests.post(url, json=payload, timeout=5)
                print(f"{target} -> {node}: {r.json()}")
            except Exception as e:
                print(f"Failed {target} -> {node}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python connect_nodes.py <number_of_nodes>")
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 2:
        print("Must have at least 2 nodes")
        sys.exit(1)

    connect_nodes(n)