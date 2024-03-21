import random
from tabulate import tabulate
import time

def main():
    def dimension1(moves):
        count = 0
        for run in range(0,100):
            x = 0
            for move in range(0, moves):
                move = random.choice([-1,1])
                x += move
                if x == 0:
                    count += 1
                    break
        return count       
            
        
    def dimension2(moves):
        count = 0
        for run in range(0,100):
            x = 0
            y = 0
            for move in range(0, moves):
                move = random.choice([(-1,0),(1,0),(0,-1),(0,1)])
                x += move[0]
                y += move[1]
                if x == 0 and y == 0:
                    count += 1
                    break
        return count  
 
    def dimension3(moves):
        count = 0
        for run in range(0,100):
            x = 0
            y = 0
            z = 0
            for move in range(0, moves):
                move = random.choice([(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)])
                x += move[0]
                y += move[1]
                z += move[2]
                if x == 0 and y == 0 and z == 0:
                    count += 1
                    break
        return count  
    

    moves_list = [20, 200, 2000, 20000, 200000, 2000000]
    count_row_headers = [["1D"],["2D"],["3D"]]
    time_row_headers = [["1D"],["2D"],["3D"]]
    table_headers = ["Number of steps: ","20","200","2000","20000","200000","2000000"]

    for moves in moves_list:
        starttime = time.time()
        count_1d = dimension1(moves)
        timeforloop = time.time() - starttime
        count_row_headers[0].append(count_1d)
        time_row_headers[0].append(timeforloop)
        
        
        starttime = time.time()
        count_2d = dimension2(moves)
        timeforloop = time.time() - starttime
        count_row_headers[1].append(count_2d)
        time_row_headers[1].append(timeforloop)

        
        starttime = time.time()
        count_3d = dimension3(moves)
        timeforloop = time.time() - starttime
        count_row_headers[2].append(count_3d)
        time_row_headers[2].append(timeforloop)
    
    count_table = tabulate(count_row_headers, table_headers, tablefmt = "grid")
    time_table = tabulate(time_row_headers, table_headers, tablefmt = "grid")
    
    print("Percentages of time particle returned to origin: ")
    print(count_table)
    print()
    print("Run time (seconds): ")
    print(time_table)
    
main()