from minimax import minimax
from alfa_beta import alfa_beta

def best_move(root, depth, alpha, beta):
    best_value = float('-inf')
    best_node = None

    # Sāk ar max spēlētāju (dators)
    #minimax(root, depth, True)
    alfa_beta(root, depth, alpha, beta, True)
    for child in root.children:
        if child.value > best_value:
            best_value = child.value
            best_node = child

    return best_node