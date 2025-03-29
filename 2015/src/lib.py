def read_data(filename):
    """Read the entire file and return a list of lines."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()
