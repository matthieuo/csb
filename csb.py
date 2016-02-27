import sys
import math


def coord_str(co):
    #print(co, file=sys.stderr)
    #return "100 100"
    return "{0} {1}".format(co[0],co[1])

checkpoints = {}
my_bot = {}
adv_bot = {}

laps = int(input())
checkpoint_count = int(input())
for i in range(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(j) for j in input().split()]
    checkpoints[i] = (checkpoint_x, checkpoint_y)

    
# game loop
while True:
    for i in range(2):
        x, y, vx, vy, angle, ncp = [int(j) for j in input().split()]
        my_bot["co"] = (x,y)
        my_bot["speed"] = (vx,vy)
        my_bot["angle"] = angle
        my_bot["ncp"] = ncp 
    for i in range(2):
        x, y, vx, vy, angle, ncp = [int(j) for j in input().split()]
        adv_bot["co"] = (x,y)
        adv_bot["speed"] = (vx,vy)
        adv_bot["angle"] = angle
        adv_bot["ncp"] = ncp 

        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
        
    
    print(my_bot["ncp"], " ",adv_bot["ncp"], file=sys.stderr)
    
    out = coord_str(checkpoints[my_bot["ncp"]]) + " 100"
    print(out)
    print(out)
    #print("8000 4500 100") 
#    print("8000 4500 100")


    
