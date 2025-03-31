from minimax import minimax
from alfa_beta import alfa_beta

def best_move(root, depth, alpha, beta, algorithm="minimax"):
    best_value = float('-inf')
    best_node = None

    if algorithm == "minimax":
        # Run minimax algorithm
        minimax(root, depth, True)
    else:
        # Run alpha-beta algorithm
        alfa_beta(root, depth, alpha, beta, True)

    # Find the best child node
    for child in root.children:
        if child.value > best_value:
            best_value = child.value
            best_node = child

    return best_node