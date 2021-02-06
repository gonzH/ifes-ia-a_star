import os

def load_map(filename):
    """[Transform a .TXT map into a 2D list]
    In order to use this function you should have folder "maps" in the root

    Args:
        filename ([string]): [Name of the map without its extension]

    Returns:
        [list]: [2D Map/Grid]
    """
    
    # Setting path
    current_path = os.path.dirname('.')
    maps_path = os.path.join(current_path, 'maps')
    
    # Map path
    filename = os.path.abspath(os.path.join(maps_path, filename + '.txt'))
    
    raw_map = []
    with open(filename, 'r') as reader:
        for line in reader:
            line_lst = line.split()
            raw_map.append([int(i) for i in line_lst])
    
    return raw_map
