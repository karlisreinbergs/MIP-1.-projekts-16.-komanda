def minimax(node, depth, maximizing_player):
    state = node.state

    if state.tuksa_virkne() or depth == 0:
        node.value = state.h_vertiba
        return state.h_vertiba
    state.generate_children()

    if maximizing_player:
        max_eval = float('-inf')
        for child_state in state.children:
            child_node = node.add_child(child_state)
            eval = minimax(child_node, depth - 1, False)
            max_eval = max(max_eval, eval)
        node.value = max_eval
        return max_eval
    
    else:
        min_eval = float('inf')
        for child_state in state.children:
            child_node = node.add_child(child_state)
            eval = minimax(child_node, depth - 1, True)
            min_eval = min(min_eval, eval)
        node.value = min_eval
        return min_eval
