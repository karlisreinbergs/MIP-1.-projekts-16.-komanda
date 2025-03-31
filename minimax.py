def minimax(node, depth, maximizing_player, alpha=float('-inf'), beta=float('inf')):
    state = node.state

    if state.tuksa_virkne() or depth == 0:
        node.value = state.h_vertiba
        return state.h_vertiba
    state.generate_children()

    if maximizing_player:
        max_eval = float('-inf')
        for child_state in state.children:
            child_node = node.add_child(child_state)
            eval = minimax(child_node, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        node.value = max_eval
        return max_eval
    
    else:
        min_eval = float('inf')
        for child_state in state.children:
            child_node = node.add_child(child_state)
            eval = minimax(child_node, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        node.value = min_eval
        return min_eval