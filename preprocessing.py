def remove_empty_prefix(text):
    lines = text.split("\n")
    spaces = min([len(line) - len(line.lstrip()) for line in lines])
    return "\n".join([line[spaces:] for line in lines])


def load_text_blocks(file):
    with open(file, 'r') as f:
        text = f.read()
        blocks = text.split("\n\n")
        blocks = list(map(remove_empty_prefix, blocks))
        return blocks


if __name__ == '__main__':
    blocks = load_text_blocks("input.txt")
    
