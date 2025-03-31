from minimax import minimax

def best_move(root, depth, algorithm='minimax'):
    best_value = float('-inf')
    best_node = None

    # Sāk ar max spēlētāju (dators)
    if algorithm == 'minimax':
        minimax(root, depth, True)
    elif algorithm == 'alphabeta':
        minimax(root, depth, True, float('-inf'), float('inf'))

    for child in root.children:
        if child.value > best_value:
            best_value = child.value
            best_node = child

    return best_node