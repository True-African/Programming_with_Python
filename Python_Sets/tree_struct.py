# Create tree structure 
def create_node(name):
    return {"name": name, "children": []}

def add_child(parent_node, child_node):
    parent_node["children"].append(child_node)

def print_tree(node, level=0):
    print("\t" * level + node["name"])
    for child in node["children"]:
        print_tree(child, level + 1)

root = create_node("Pictures")
child1 = create_node("Downloads")
child2 = create_node("Screenshots")

add_child(root, child1)
add_child(root, child2)

sub_child1 = create_node("My saved pictures")
add_child(child1, sub_child1)

# Print tree
print_tree(root)