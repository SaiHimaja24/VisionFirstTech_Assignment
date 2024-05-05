import random
import json

def generate_nodes(email):
    random.seed(email)
    num_nodes = random.randint(4, 8)  # Number of nodes can vary between 4 to 8
    nodes = []
    for i in range(num_nodes):
        node_name = chr(65 + i // 26) + chr(65 + i % 26)  # Generate node names as uppercase alphabets
        nodes.append(node_name)
    return nodes

def generate_edges(nodes):
    random.seed(sum(ord(c[0]) for c in nodes))  # Seed depends on sum of ASCII values of first character of node names
    num_edges = random.randint(5, min(15, len(nodes)*(len(nodes)-1)//2))  # Number of edges can vary between 5 to n*(n-1)/2
    edges = []
    while len(edges) < num_edges:
        from_node = random.choice(nodes)
        to_node = random.choice(nodes)
        if from_node != to_node:
            cost = round(random.uniform(1, 5), 2)  # Random cost between 1 to 5
            edge = {"from": from_node, "to": to_node, "cost": cost}
            if edge not in edges:  # Avoid duplicate edges
                edges.append(edge)
    return edges

def generate_data(email):
    nodes = generate_nodes(email)
    edges = generate_edges(nodes)
    return {"Nodes": nodes, "Edges": edges}

def main():
    email = input("Enter student's email ID: ")
    data = generate_data(email)
    with open('assignment2_data.json', 'w') as file:
        json.dump(data, file)
    print("Data saved to assignment2_data.json")

if __name__ == "__main__":
    main()
