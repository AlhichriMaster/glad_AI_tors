# -? "GYROS"
def start ():#line:4
    return "readjust_position",{"WEAPON":True }#line:5
def readjust_position ():#line:7
    if get_if_have_weapon ():#line:8
        return "move_to_center",{}#line:9
    OOOOOOO0000000OOO ,OO0OOO0000O0O000O =375 ,375 #line:10
    O00O0OO0OO00O00OO ,O0000O000OO000OO0 =get_position_tuple ()#line:11
    OOO00O00000OO000O =atan2 (OO0OOO0000O0O000O -O0000O000OO000OO0 ,OOOOOOO0000000OOO -O00O0OO0OO00O00OO )#line:12
    OOO0OO0OO0000OO00 =((OO0OOO0000O0O000O -O0000O000OO000OO0 )**2 +(OOOOOOO0000000OOO -O00O0OO0OO00O00OO )**2 )#line:13
    if OOO0OO0OO0000OO00 <225 **2 :#line:16
        O00OO00OOOOO00O00 =-cos (OOO00O00000OO000O )#line:17
        OO00O0O00O0O0O0O0 =-sin (OOO00O00000OO000O )#line:18
        return "readjust_position",{"ACLT_X":O00OO00OOOOO00O00 ,"ACLT_Y":OO00O0O00O0O0O0O0 }#line:19
    elif OOO0OO0OO0000OO00 >275 **2 :#line:21
        O00OO00OOOOO00O00 =cos (OOO00O00000OO000O )#line:22
        OO00O0O00O0O0O0O0 =sin (OOO00O00000OO000O )#line:23
        return "readjust_position",{"ACLT_X":O00OO00OOOOO00O00 ,"ACLT_Y":OO00O0O00O0O0O0O0 }#line:24
    else :#line:25
        return "slow_to_a_stop",{}#line:27
def slow_to_a_stop ():#line:29
    O0OOOOOOOO0000O00 ,O0O00O0OO0O0OO000 =get_velocity_tuple ()#line:31
    if O0OOOOOOOO0000O00 **2 +O0O00O0OO0O0OO000 **2 >2 :#line:33
        OO0O000O0O0000O00 =sqrt (O0OOOOOOOO0000O00 **2 +O0O00O0OO0O0OO000 **2 )#line:35
        return "slow_to_a_stop",{"ACLT_X":-O0OOOOOOOO0000O00 /OO0O000O0O0000O00 ,"ACLT_Y":-O0O00O0OO0O0OO000 /OO0O000O0O0000O00 }#line:36
    else :#line:37
        return "orbit_around_point",{}#line:39
def orbit_around_point ():#line:41
    O00O0000OO0OOOO0O ,OO00OOO0000O00OOO =375 ,375 #line:42
    (O0O00OO0OO0OO0OOO ,OOOOOO000000OOO00 )=get_position_tuple ()#line:43
    O0000000O00OO0O0O =atan2 (OO00OOO0000O00OOO -OOOOOO000000OOO00 ,O00O0000OO0OOOO0O -O0O00OO0OO0OO0OOO )#line:44
    OOOOOO0000OO0OO0O =((OO00OOO0000O00OOO -OOOOOO000000OOO00 )**2 +(O00O0000OO0OOOO0O -O0O00OO0OO0OO0OOO )**2 )#line:47
    if OOOOOO0000OO0OO0O <225 **2 or OOOOOO0000OO0OO0O >275 **2 :#line:48
        return "readjust_position",{}#line:49
    if get_if_have_weapon ():#line:51
        return "move_to_center",{}#line:52
    else :#line:53
        for OOOO0OOOOO0OOOO00 in range (360 ):#line:54
            (O0O0OO000000O000O ,O0OO000000OOO00O0 ,OO000OOOOOO000OOO )=get_the_radar_data (OOOO0OOOOO0OOOO00 )#line:55
            if O0O0OO000000O000O =="weapon"and not OO000OOOOOO000OOO and O0OO000000OOO00O0 <125 :#line:56
                return "move_to_weapon",{"WEAPON":True }#line:57
    O0OOO0OOO0O0O00OO =O00O0000OO0OOOO0O -400 *cos (O0000000O00OO0O0O +radians (9.7 ))#line:60
    O000OOOO00O0O000O =OO00OOO0000O00OOO -400 *sin (O0000000O00OO0O0O +radians (9.7 ))#line:61
    O000OOO0000OO0OO0 =atan2 (O000OOOO00O0O000O -OOOOOO000000OOO00 ,O0OOO0OOO0O0O00OO -O0O00OO0OO0OO0OOO )#line:62
    O000O0000O0O0OO00 =((degrees (O000OOO0000OO0OO0 )+90 ))%360 #line:63
    OOOOOO000000OOO0O =cos (radians (O000O0000O0O0OO00 ))#line:64
    O0O00O000OOO0OO00 =sin (radians (O000O0000O0O0OO00 ))#line:65
    OOO0O000O0O0O0000 ,O000OO000O0OO0O0O =0 ,0 #line:68
    OO0000OOOOOOOOOO0 =((O000O0000O0O0OO00 -get_throwing_angle ())+360 )%360 #line:69
    if OO0000OOOOOOOOOO0 >180 :#line:70
        O000OO000O0OO0O0O =1 #line:71
    else :#line:72
        OOO0O000O0O0O0000 =1 #line:73
    return "orbit_around_point",{"ACLT_X":OOOOOO000000OOO0O ,"ACLT_Y":O0O00O000OOO0OO00 ,"ROT_CC":OOO0O000O0O0O0000 ,"ROT_CW":O000OO000O0OO0O0O }#line:75
def move_to_weapon ():#line:77
    OO0OOO0OOOOOO00O0 ,OOO000O0O000O0O0O =-1 ,-1 #line:78
    for O0O0000OO00O000O0 in range (360 ):#line:79
        (O00000OOOO0000O0O ,O00OO0O00OO0OO0O0 ,O00OOO00OO00000OO )=get_the_radar_data (O0O0000OO00O000O0 )#line:80
        if O00000OOOO0000O0O =="weapon"and not O00OOO00OO00000OO and O00OO0O00OO0OO0O0 <125 :#line:81
            OOO000O0O000O0O0O =O00OO0O00OO0OO0O0 #line:82
            OO0OOO0OOOOOO00O0 =O0O0000OO00O000O0 #line:83
            break #line:84
    if OOO000O0O000O0O0O ==-1 or OO0OOO0OOOOOO00O0 ==-1 :#line:86
        return "readjust_position",{}#line:87
    if get_if_have_weapon ():#line:89
        return "move_to_center",{}#line:90
    O0O000OOO0OOO0OO0 =cos (radians (OO0OOO0OOOOOO00O0 ))#line:92
    OOO0OOOO0OOOO0OO0 =sin (radians (OO0OOO0OOOOOO00O0 ))#line:93
    (O0OOO00OO0OO0OO00 ,O00O000OOO00OO0OO )=get_velocity_tuple ()#line:94
    O0OOOOO0OO00OOOO0 =atan2 (OOO0OOOO0OOOO0OO0 -0.25 *O00O000OOO00OO0OO ,O0O000OOO0OOO0OO0 -0.25 *O0OOO00OO0OO0OO00 )#line:95
    return "move_to_weapon",{"ACLT_X":cos (O0OOOOO0OO00OOOO0 ),"ACLT_Y":sin (O0OOOOO0OO00OOOO0 )}#line:97
def move_to_center ():#line:99
    OO00OOO0O000O0000 ,O0OO0000O0OO0O0O0 =375 ,375 #line:100
    (OO0O000000O000000 ,OO0OOOOOO0OO0O0OO )=get_position_tuple ()#line:101
    OOO00000O0O0OOO0O =atan2 (O0OO0000O0OO0O0O0 -OO0OOOOOO0OO0O0OO ,OO00OOO0O000O0000 -OO0O000000O000000 )#line:102
    OO00OO0O0000OOOOO =((O0OO0000O0OO0O0O0 -OO0OOOOOO0OO0O0OO )**2 +(OO00OOO0O000O0000 -OO0O000000O000000 )**2 )#line:103
    OOOOOO00OOOOO00OO ,O0O000O0OOOO00O0O =0 ,0 #line:104
    if OO00OO0O0000OOOOO >200 :#line:105
        if not get_if_have_weapon ():#line:106
            return "readjust_position",{}#line:107
        OO0O00OOO0O0O00O0 =-1 #line:109
        for O0000000OO000O0O0 in range (360 ):#line:110
            (OOO0OOO0OOOO00OO0 ,O0O0O0O0OOOO0O000 ,_OOO000OOO000O0000 )=get_the_radar_data (O0000000OO000O0O0 )#line:111
            if OOO0OOO0OOOO00OO0 =="player":#line:112
                OO0O00OOO0O0O00O0 =O0000000OO000O0O0 #line:113
                break #line:114
        OO0O0000O0000OOO0 =True #line:116
        O0O00OOO0O000OOOO ,O00000000OO0000O0 =0 ,0 #line:117
        if OO0O00OOO0O0O00O0 !=-1 :#line:118
            OO000OOO0O00OO0OO =((OO0O00OOO0O0O00O0 -get_throwing_angle ())+360 )%360 #line:120
            if OO000OOO0O00OO0OO <1 or OO000OOO0O00OO0OO >359 :#line:121
                OO0O0000O0000OOO0 =False #line:122
            if OO000OOO0O00OO0OO >180 :#line:123
                O00000000OO0000O0 =1 #line:124
            else :#line:125
                O0O00OOO0O000OOOO =1 #line:126
        OOOOOO00OOOOO00OO =cos (OOO00000O0O0OOO0O )#line:128
        O0O000O0OOOO00O0O =sin (OOO00000O0O0OOO0O )#line:129
        return "move_to_center",{"ACLT_X":OOOOOO00OOOOO00OO ,"ACLT_Y":O0O000O0OOOO00O0O ,"ROT_CC":O0O00OOO0O000OOOO ,"ROT_CW":O00000000OO0000O0 ,"WEAPON":OO0O0000O0000OOO0 }#line:131
    else :#line:132
        return "readjust_position",{"WEAPON":False }#line:133
    return "move_to_center",{}#line:135
