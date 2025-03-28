from minimax import minimax

def best_move(root, depth):
    best_value = float('-inf')
    best_node = None

    # Sāk ar max spēlētāju (dators)
    minimax(root, depth, True)

    for child in root.children:
        if child.value > best_value:
            best_value = child.value
            best_node = child

    return best_node