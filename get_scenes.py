import ast

def extract_class_names(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        source = file.read()

    tree = ast.parse(source, filename=filepath)
    class_names = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_names.append((node.lineno, node.name))

    # Sort by line number to preserve order of appearance
    class_names.sort(key=lambda x: x[0])
    return [name for _, name in class_names]

# Example usage
if __name__ == "__main__":
    filepath = "interactive_main.py"  # Replace with your target file
    classes = extract_class_names(filepath)
    print("Classes in order of appearance:")
    for cls in classes:
        print(cls)
