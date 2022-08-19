# -> Ameel

# This agent, as demonstrated in the supplement video on cuLearn, contains exactly three states. The first state describes the behaviour while
# it is looking for a weapon (since, at the beginning of the match, the player will be unequipped). The agent will
# transition out of this state only if it gains possession of a weapon, so until it has a weapon it will scan all 360
# degrees around its current position (in one degree increments) and, whenever a weapon is detected, it place the angle
# at which that weapon was detected and the distance to that weapon in a list of possible weapons to pursue. If there
# is at least one candidate weapon, the list of possibilities is sorted by distance so that the ACLT_X and ACLT_Y keys
# of the return dictionary can be set to a unit vector corresponding to the direction of the nearest weapon. If there
# are no weapons visible to the player, the ACLT_X and ACLT_Y values are randomized with a probability of 0.1, which
# essentially means that the player starts to wander around, changing direction randomly about every 10 frames. Whether
# a weapon is currently visible or not, the WEAPON value in the dictionary is always set to True so that the agent will
# pick up a weapon whenever possible. The second state describes the behaviour while the agent is looking for a target
# (since the only way into this state is through the acquisition of a weapon). If again requires scanning at all angles
# from the current location and, if the opposing player is not detected, move randomly. But if, on the other hand, the
# opposing player is detected, the agent will move in the direction of that player until they arrive within a distance
# of 200 units. Only when the player is within 200 units does the agent move into the third and final behaviour state.
# The third state, only entered when the player has a weapon and is within 200 units of the opponent, entails scanning
# all 360 degrees (again) for the opposing player, and comparing the angle at which the opposing player is visible 
# against the current throwing angle of the player. Using either the cross product (as discussed in class) or a branch
# structure such as the one demonstrated below, the player can decide whether it is faster to rotate clockwise or
# counterclockwise (updating the return dictionary accordingly). When the throwing angle nearly matches the angle at
# which the opposing player was seen, the weapon is thrown (by setting the WEAPON key value in the return dictionary
# to false, and the machine returns to its first state and begins looking for another weapon.


# NOTE: This agent has been deliberately designed to be rudimentary and somewhat inferior - constantly checking all 
# 360 degrees around the player is inefficient and does incur a cost (i.e., the main program will give your program
# less frames for consideration as a result), and checking in 1 degree increments results in many possible blind spots.
# Additionally, the manner in which certain objectives are achieved (i.e., finding the nearest weapon, deciding whether
# to turn clockwise or counterclockwise, attempting to reduce velocity, etc.) are not accomplished in the best manner.

# You should treat this CLASS DEMO agent as a starting point that allows you to observe "HOW" glad_AI_tors is played.

import math

bbox = (50, 700)


def findMin(a,b):
    if a<b:
        c = a
    else:
        c = a
    return c

def bounding_box(list_tuples):
    min_x = 10000; min_y = min_x; max_x = 0; max_y = max_x
    for t in list_tuples:
        if t[0]<min_x: min_x = t[0]
        if t[1]<min_y: min_y = t[1]
        if t[0]>max_x: max_x = t[0]
        if t[1]>max_y: max_y = t[1]
    return (min_x, min_y, max_x, max_y)

def avg_of_list_tuples(list_tuples):
    sum1 = 0; sum2 = 0
    for t in list_tuples:
        sum1 = sum1+t[0]
        sum2 = sum2+t[0]
    return (  sum1/len(list_tuples) ,  sum2/len(list_tuples)  )

def comp_dist(a,b):
    return math.sqrt( (a[0]-b[0])**2  + (a[1]-b[1])**2  )

def comp_angle(a,b):
    hyp = a[1]-b[1]; base = a[0]-b[0]
    A = math.atan(hyp / base)
    if hyp>=0 and base<=0:
        angle = A+math.pi/2
    elif hyp<=0 and base<=0:
        angle = A-math.pi/2
    else: # angle is ok
        angle = A

    return angle


def best_accelerations(target_x ,target_y ):
	(x ,y )=get_position_tuple ()
	distanty =target_y - y 
	distantx =target_x - x 
	distance = sqrt (distantx **2 +distanty **2 )
	five_percent_of_dstancex =distantx /distance *min (5 ,distance /100 * 5 )
	five_percent_of_dstancey =distanty /distance *min (5 ,distance /100 * 5 )
	Vel_x ,Vel_y = get_velocity_tuple ()
	new_vel_or_acc_x =(five_percent_of_dstancex -Vel_x )*5
	new_vel_or_acc_y =(five_percent_of_dstancey -Vel_y )*5 
	return max (min (new_vel_or_acc_x*5 ,1 ),-1 ), max (min (new_vel_or_acc_y*5 ,1 ),-1 ), distance

screen_middle = (350,350)


# the "start" function is REQUIRED by glad_AI_tors and must return your desired initial state and an empty dictionary
def start():
    return "look_for_weapon", {}


def go_to_screen_middle():
    global screen_middle 
    my_position = get_position_tuple()
    dist_to_center =   comp_dist( my_position   ,   screen_middle )  
    angle_to_center =  comp_angle( my_position   ,   screen_middle )  
    # print(dist_to_center)

    if dist_to_center>50:
        acc_x, acc_y, pos = best_accelerations( screen_middle[0]  , screen_middle[1]  )
        return "look_for_weapon", { "ACLT_X": acc_x, "ACLT_Y": acc_y  }
    else:
        return "look_for_weapon", {}



# the look_for_weapon function describes the behaviour when the agent is searching for (i.e., moving towards or wandering
# in search of) a weapon that it will use to against the opposing player
def look_for_weapon():
    have_weapon = get_if_have_weapon()
    see_weapon = False
    see_target = False

    # If I have a weapon, stop moving and look for target
    if have_weapon: 
            return "look_for_target", {"ACLT_X": 0, "ACLT_Y": 0}
        # return "go_to_screen_middle", {"WEAPON" : False, "ACLT_X": 0, "ACLT_Y": 0}
    # Else, scan for weapons
    else:
        # Find all possible weapons
        possible = []; 
        for angle in range(0, 360, 1):
            (type, distance, _) = get_the_radar_data(angle)
            
            if type == "weapon":
                possible.append( (distance, angle) )
                see_weapon = True
            if type == "player":
                tar_D = distance
                tar_A = angle
                see_target = True

        # Get your current angle and compare it to the desired angle
        if see_target:
            throw = get_throwing_angle()
            delta = ((tar_A-throw) + 360) % 360 

            if delta > 180:
                rot_cc = 0
                rot_cw = 1
            else:
                rot_cc = 1
                rot_cw = 0
        else:
            rot_cc = 0
            rot_cw = 0


        # If I see one, move toward it
        if see_weapon:
            possible.sort()
            distance, angle = possible[0]  
            if distance<50:
                # print('distance to weapon: ', distance)
                return "look_for_weapon", { "WEAPON" : True ,  "ACLT_X": (cos(radians(angle))), "ACLT_Y": (sin(radians(angle)))  }
            else:
                my_position = get_position_tuple()
                weapon_position = (my_position[0]+distance*cos(radians(angle)) , my_position[1]+distance*sin(radians(angle))   )
                acc_x, acc_y, pos = best_accelerations( weapon_position[0]  , weapon_position[1]  )
                return "look_for_weapon", { "WEAPON" : True , "ACLT_X": acc_x, "ACLT_Y": acc_y , \
                    "ROT_CC": rot_cc,  "ROT_CW": rot_cw }
                # angle_str = '000'+str(angle)
                # # angle_str = '0'+str(angle) if angle<10 else  str(angle)
                # # print(str(angle_str))  
                # return "go_to_weapon", {"WEAPON": True, "SAVE_A": angle_str[-4:-2] , "SAVE_B": angle_str[-2:]          }
        # Else, wander a bit
        else:
            
            if randint(1, 10) == 1:
                return "look_for_weapon", {"WEAPON" : True, "ACLT_X" : randint(-1, 1), "ACLT_Y" : randint(-1, 1), "ROT_CC": rot_cc,  "ROT_CW": rot_cw }
            else:
                return "look_for_weapon", {"WEAPON" : True,  "ROT_CC": rot_cc,  "ROT_CW": rot_cw }
		
    
    return "look_for_weapon", {}






# the look_for_target function describes the behaviour when the agent has acquired a weapon and is now searching for (i.e.,
# moving towards or wandering in search of) the opposing player	
def look_for_target():
    see_target = False
    in_range = False
    target = None
    max_distance = 300


    #check if we can shoot
    throw = get_throwing_angle()
    (type, distance, _) = get_the_radar_data(throw)
    if type=='player' and distance <max_distance :
        return "look_for_weapon", {"WEAPON": False}
    else:

        # Scan around for a player
        for angle in range(0, 360, 1):
            (type, distance, _) = get_the_radar_data(angle)
            
            if type == "player":
                tar_D = distance
                tar_A = angle
                see_target = True
                break

        # If I see a target
        if see_target:
            throw = get_throwing_angle()
            delta = ((tar_A-throw) + 360) % 360 
            # Check if the angle is within some threshold (near "360 degrees" or "0 degrees")
            angle_correct = (delta < 1) or (delta > 359)

            if delta > 180:
                rot_cc = 0
                rot_cw = 1
            else:
                rot_cc = 1
                rot_cw = 0

            my_position = get_position_tuple()
            target_position = (my_position[0]+distance*cos(radians(angle)) , my_position[1]+distance*sin(radians(angle))   )
            acc_x, acc_y, pos = best_accelerations( target_position[0]  , target_position[1]  )

            if angle_correct  and distance <max_distance:   
                # Recall: WEAPON: False means fire a weapon if we have one
                # return "look_for_weapon", {"WEAPON": False}
                return "look_for_weapon", {"WEAPON": False, "ACLT_X": acc_x, "ACLT_Y": acc_y , "ROT_CC": rot_cc,  "ROT_CW": rot_cw}
            else:
    
                return "look_for_target", {"WEAPON" : True , "ACLT_X": acc_x, "ACLT_Y": acc_y , "ROT_CC": rot_cc,  "ROT_CW": rot_cw }
                



        # If we don't see a target, just wander a bit
        else:
            if randint(1, 10) == 1:
                return "look_for_target", {"WEAPON" : True ,"ACLT_X" : randint(-1, 1), "ACLT_Y" : randint(-1, 1)}
            else:
                return "look_for_target", {"WEAPON" : True }

    return "look_for_target", {"WEAPON" : True }





# the aim_at_target function descibes the behaviour when the player has a weapon and is close enough to the opposing player
# (i.e., withing 200 units of distance) to rotate the throwing angle towards the opponent and attempt a shot
def aim_at_target():
    see_target = False
    angle_correct = False
    delta = -1

    # Scan around for a player
    for angle in range(0, 360, 1):
        (type, distance, _) = get_the_radar_data(angle)
        
        if type == "player":
            see_target = True
            tar_D = distance
            tar_A = angle
            # Get your current angle and compare it to the desired angle
            throw = get_throwing_angle()
            delta = ((angle-throw) + 360) % 360 

            # Check if the angle is within some threshold (near "360 degrees" or "0 degrees")
            angle_correct = (delta < 1) or (delta > 359)
            break

    # From here on, we've definitely seen a target.
    #   If my attack angle is within a threshold, shoot!
    if angle_correct:   
        # Recall: WEAPON: False means fire a weapon if we have one
        # return "look_for_weapon", {"WEAPON": False}
        return "look_for_weapon", {"WEAPON": False}

    # Firstly, if I don't see a target, just swap back to searching
    if not see_target:
        return "look_for_target", {"WEAPON": True}
    #   Else, rotate canon toward it
    else:
        if delta > 180:
            rot_cc = 0
            rot_cw = 1
        else:
            rot_cc = 1
            rot_cw = 0

        my_position = get_position_tuple()
        target_position = (my_position[0]+distance*cos(radians(angle)) , my_position[1]+distance*sin(radians(angle))   )
        acc_x, acc_y, pos = best_accelerations( target_position[0]  , target_position[1]  )

        return "aim_at_target", {"WEAPON" : True , "ACLT_X": acc_x, "ACLT_Y": acc_y , "ROT_CC": rot_cc,  "ROT_CW": rot_cw }



    # We shouldn't ever get here...
    return "aim_at_target", {}



# the look_for_weapon function describes the behaviour when the agent is searching for (i.e., moving towards or wandering
# in search of) a weapon that it will use to against the opposing player
def find_objects():
    col_positions = []; haz_positions = []
    my_position = get_position_tuple()
    # Find all possible weapons
    for angle in range(0, 360, 1):
        (type, distance, _) = get_the_radar_data(angle)
        # "player",   "weapon",   "column",  or  "hazard"),  
        
        if type == "hazard":
            (p_x, p_y) = get_position_tuple()
            col_positions.append( (p_x+distance*cos(radians(angle)), p_y+distance*sin(radians(angle))) )
            # print('Foun hazard in (x,y)=' , p_x+distance*cos(radians(angle)), p_y+distance*sin(radians(angle))   )
            
        elif type == "column":
            (p_x, p_y) = get_position_tuple()
            haz_positions.append( (p_x+distance*cos(radians(angle)), p_y+distance*sin(radians(angle))) )
            # print('Foun column in (x,y)=' , p_x+distance*cos(radians(angle)), p_y+distance*sin(radians(angle))   )
            col_p = (   p_x+distance*cos(radians(angle)),   p_y+ distance*sin(radians(angle))   )
        else:
            # print('Other objects.')
            dummy = angle


    avg_columns = avg_of_list_tuples(col_positions)
    avg_hazards = avg_of_list_tuples(haz_positions) 
    bbox = bounding_box(col_positions) 
    # print('avg_columns: ', avg_columns )
    # print( 'avg_hazards: ', avg_hazards )
    # print( 'bbox: ', bbox )

    # global Target_poistion 
    # Target_poistion = (    int(avg_columns[0] )  ,  int(avg_columns[1] )   )
    acc_x, cc_y, pos = best_accelerations( (bbox[0]+bbox[2])/2 ,  (bbox[1]+bbox[3])/2  )
    # print( Target_poistion)
    bbox_int = (  int(bbox[0]) , int(bbox[1]) , int(bbox[2]) , int(bbox[3])  )
    return "find_objects", { "ACLT_X": acc_x, "ACLT_Y": cc_y, 'DEBUGS':  [ bbox_int   ]  }
