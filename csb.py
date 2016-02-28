import sys
import math
import numpy as np


def normalize(v):
    norm=np.linalg.norm(v)
    if norm==0: 
       return v
    return v/norm


def angle_between(v1, v2):
    v1_u = normalize(v1)
    v2_u = normalize(v2)
    angle = np.arccos(np.dot(v1_u, v2_u))
    if np.isnan(angle):
        if (v1_u == v2_u).all():
            return 0.0
        else:
            return np.pi
    return angle
    
def angle_between_ori(v1):
    #v1_u = normalize(v1)
    #angle = np.arccos(np.dot(v1_u, np.array([1,0])))
    
    
    angle = np.arccos(abs(v1[0])/np.linalg.norm(v1))
    
    #if np.isnan(angle):
    #    if (v1_u == v2_u).all():
     #       return 0.0
     #   else:
     #       return np.pi
     
    if v1[0] >= 0 and v1[1] >= 0:
        return angle
    elif v1[0] >= 0 and v1[1] < 0:
        return 2*np.pi - angle
    elif v1[0] < 0 and v1[1] >= 0:
        return np.pi - angle 
    elif v1[0] < 0 and v1[1] < 0:
        return angle + np.pi
    #v1_u = normalize(v1)
    #print(v1_u," ",v1_u[0]/v1_u[1], file=sys.stderr)
    #angle = np.arctan2(-v1[1],v1[0])

    #return angle

def eval_next_pos(cur_co,dest_co,v,power):
    
    v_target = dest_co-cur_co
    #norm_power = normalize(dest_co-cur_co)*power
    norm_power = v_target*power/np.linalg.norm(v_target)
    #print(norm_power, file=sys.stderr)
    next_co = cur_co + v + norm_power
    angle = np.round(np.degrees(angle_between_ori(v_target)))
    #print(np.round(np.degrees(angle_between_ori(dest_co - cur_co))), " " ,  dest_co - cur_co,file=sys.stderr)
    next_co = np.around(next_co)
    next_v = (v+norm_power)*0.85
    next_v = np.trunc(next_v)
    
    
    #print(np.degrees(angle_between_ori(dest_co - next_co)), file=sys.stderr)
    return next_co,next_v,angle
    


def find_parameter(myb):
    for point in range(150):
        for thrust in [10,40,90,150,200]:
            for dest in [checkpoints[0],checkpoints[0],checkpoints[0]]:
                a,b,c = eval_next_pos(myb["co"],dest,myb["speed"] ,thrust)

def coord_str(co):
    #print(co, file=sys.stderr)
    #return "100 100"
    return "{0} {1}".format(co[0],co[1])

checkpoints = {}
my_bots = {}
adv_bots = {}

bup = 0

laps = int(input())
checkpoint_count = int(input())
for i in range(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(j) for j in input().split()]
    checkpoints[i] = np.array([checkpoint_x,checkpoint_y])#(checkpoint_x, checkpoint_y)

    
# game loop
while True:
    for i in range(2):
        x, y, vx, vy, angle, ncp = [int(j) for j in input().split()]
        bot = {}
        bot["co"] = np.array([x,y]) #(x,y)
        bot["speed"] = np.array([vx,vy]) #(vx,vy)
        bot["angle"] = angle
        bot["ncp"] = ncp
        my_bots[i] = bot
    for i in range(2):
        x, y, vx, vy, angle, ncp = [int(j) for j in input().split()]
        bot = {}
        bot["co"] = np.array([x,y]) #(x,y)
        bot["speed"] = np.array([vx,vy]) #(vx,vy)
        bot["angle"] = angle
        bot["ncp"] = ncp
        adv_bots[i] = bot

        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    out = coord_str(checkpoints[my_bots[0]["ncp"]]) + " 100"
    bup = bup + 1
    if bup==5:    
       # out = coord_str(checkpoints[my_bots[0]["ncp"]]) + " SHIELD"
        bup = 0
    print(my_bots[0], file=sys.stderr)
    
    
    find_parameter(my_bots[0])
    
    aa,bb,angle = eval_next_pos(my_bots[0]["co"],
                            checkpoints[my_bots[0]["ncp"]],
                            my_bots[0]["speed"],
                            100)
                            
    if abs(angle-my_bots[0]["angle"]) >= 18:
        print("*INVALID* ",aa," ",bb, " ",angle, file=sys.stderr)
    else:
        print(aa," ",bb, " ",angle, file=sys.stderr)
    
    print(out)
    print(coord_str(checkpoints[0]) + " 100")
   # print(15000," ",cotmp[1]," ", 200)
    #print("8000 4500 100") 
#    print("8000 4500 100")


    
    

    




    
