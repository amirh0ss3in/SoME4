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
    # write it as "file name, class name" in a txt file in the media\videos\interactive_main\1080p60
    path = r"media/videos/interactive_main/1080p60/inputs.txt"

    # file 'class name'

    with open(path, "w", encoding="utf-8") as file:
        file.truncate(0)
        for class_name in classes:
            file.write(f"file '{class_name}.mp4'\n")
            print(f"file '{class_name}.mp4'")

    print(f"Class names extracted from {filepath} and written to {path}")
