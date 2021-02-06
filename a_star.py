from node import Node

def search(grid, start, goal, cost):
    """[The A-Star algorithm]

    Args:
        grid ([list]): [A 2D list where the agent will act]
        start ([tuple]): [It is the initial coordinate (X,Y)]
        goal ([tuple]): [It is the coordinate (X,Y) to be reached]

    Returns:
        [list]: [Index 0 stores a drawn map and index 1 stores the traveled steps]
    """

    # Initial setup, start and goal node with f, g and h equals 0
    start_node = Node(None, start)
    goal_node = Node(None, goal)

    # A list to hold candidate nodes to be verified
    open_list = []
    open_list.append(start_node)
    
    # A list to hold candidates nodes already verified
    closed_list = []

    # Starting the search
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Add verified node to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Reach the goal
        if current_node == goal_node:
            # Initialize traveled path list
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
                
            # Reversed path
            path = path[::-1] 
            
            # Initialize drawn grid
            drawn_path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]    
            
            # Draw each step taken
            for i in range(len(path)-1):
                # movement check: UP (X descrese)
                if path[i][0] > path[i+1][0]:
                    drawn_path[path[i][0]][path[i][1]] = '^'
                
                # movement check: LEFT (X increase)
                elif path[i][1] > path[i+1][1]:
                    drawn_path[path[i][0]][path[i][1]] = '<'
                
                # movement check: DOWN (X increase)
                elif path[i][0] < path[i+1][0]:
                    drawn_path[path[i][0]][path[i][1]] = 'v'
               
                # movement check: RIGHT (Y increase)
                elif path[i][1] < path[i+1][1]:
                    drawn_path[path[i][0]][path[i][1]] = '>'
                
            # Draw goal coordinate
            drawn_path[goal[0]][goal[1]] = '*'
            
            # Return both drawn and coordinates path
            return [drawn_path, path]

        # Look for adjacent nodes
        adjacent_nodes = []
        for new_position in [(-1, 0), (0, -1), (1, 0), (0, 1)]: # Positions respectively UP LEFT DOWN RIGHT OR ^ < v >

            # Get the possible next node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] >= 0 and node_position[0] < len(grid) and node_position[1] >= 0 and node_position[1] < len(grid[0]):
                # Make sure walkable terrain
                if grid[node_position[0]][node_position[1]] == 0:
                    # Create candidate node
                    candidate_node = Node(current_node, node_position)
                    
                    # Append candidate node
                    adjacent_nodes.append(candidate_node)

        # Loop through adjacent nodes (candidates)
        for candidate in adjacent_nodes:
            
            # Select only available candidates
            if candidate not in closed_list:
                # Create the f, g, and h values, Manhattan method!
                candidate.h = abs(candidate.position[0] - goal_node.position[0]) + abs(candidate.position[1] - goal_node.position[1])
                candidate.g = current_node.g + cost
                candidate.f = candidate.g + candidate.h

                # Check if candidate is already in the open list
                if candidate in open_list:
                    # If this same candidate were already computed and has not the shortest path then we skip the open list append
                    for open_node in open_list:
                        if candidate.position == open_node.position and candidate.g > open_node.g:
                            continue
                
                # Add the candidate to the open list
                open_list.append(candidate)

                