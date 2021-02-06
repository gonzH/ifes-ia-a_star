import input_loader
import a_star

def main():

    raw_start = input("Enter your starting coordinate: Example: 0,0 for X = 0 and Y = 0\n").split(',')
    start = (int(raw_start[0]), int(raw_start[1]))
    
    raw_goal = input("Enter your goal coordinate: Example: 9,8 for X = 9 and Y = 8\n").split(',')
    goal = (int(raw_goal[0]), int(raw_goal[1]))
    
    grid = input_loader.load_map(input("Enter map name: Example: mapa1\n"))
    
    
    # grid = input_loader.load_map('mapa1')
    # start = (0,0)
    # goal = (9, 8)
    cost = 1

    path = a_star.search(grid, start, goal, cost)
    
    print('\nTraveled path: \n', path[1])
    print('\nTraveled path (drawn):')
    [print(i) for i in path[0]]


if __name__ == '__main__':
    main()