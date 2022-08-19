# -? "BRUCE"
import math #line:9
import random #line:10
PLAYER_LIST_INDEX =0 #line:12
WEAPON_LIST_INDEX =1 #line:13
COLUMN_LIST_INDEX =2 #line:14
HAZARD_LIST_INDEX =3 #line:15
PLAYER_SIZE =21 #line:17
WEAPON_SIZE =11 #line:18
COLUMN_SIZE =40 #line:19
HAZARD_SIZE =61 #line:20
PLAYER_SIZE_HALF =(int )(PLAYER_SIZE /2 )#line:22
WEAPON_SIZE_HALF =(int )(WEAPON_SIZE /2 )#line:23
COLUMN_SIZE_HALF =(int )(COLUMN_SIZE /2 )#line:24
HAZARD_SIZE_HALF =(int )(HAZARD_SIZE /2 )#line:25
FIRST_QUAD =1 #line:27
SECOND_QUAD =2 #line:28
THIRD_QUAD =3 #line:29
FOURTH_QUAD =4 #line:30
RIGHT =5 #line:31
UP =6 #line:32
LEFT =7 #line:33
DOWN =8 #line:34
def abs (O00O0O0OOO0000O0O ):#line:36
    if O00O0O0OOO0000O0O <0 :#line:37
        O00O0O0OOO0000O0O *=-1 #line:38
    return O00O0O0OOO0000O0O #line:39
def calc_dist (O0OOOOOO0OOOO00O0 ,OO0O00O0O00O00O00 ):#line:41
    return abs (O0OOOOOO0OOOO00O0 -OO0O00O0O00O00O00 )#line:42
def clamp (O0O00O000OOOO0OO0 ,OO00O0O0000OOOO0O ,OOOOO0O000000OO00 ):#line:44
    if (O0O00O000OOOO0OO0 <OO00O0O0000OOOO0O ):#line:45
        return OO00O0O0000OOOO0O #line:46
    elif (O0O00O000OOOO0OO0 >OOOOO0O000000OO00 ):#line:47
        return OOOOO0O000000OO00 #line:48
    else :#line:49
        return O0O00O000OOOO0OO0 #line:50
def is_likely_same_obj (O0O0OO0O0O00000O0 ,O000O0OO0OOO00OOO ,O00OO0O00OOO0O000 ,OO0OOO0O00000O0O0 ):#line:52
    if O0O0OO0O0O00000O0 !=O00OO0O00OOO0O000 :#line:53
        return False #line:54
    O00OOOOOO000O0O0O =O0O0OO0O0O00000O0 #line:56
    if O00OOOOOO000O0O0O =="player":#line:58
        return True #line:59
    O0OOO0O000OOOO0O0 =calc_dist (O000O0OO0OOO00OOO ,OO0OOO0O00000O0O0 )#line:61
    if O00OOOOOO000O0O0O =="weapon":#line:63
        if (O0OOO0O000OOOO0O0 <=WEAPON_SIZE_HALF ):#line:64
            return True #line:65
    if O00OOOOOO000O0O0O =="hazard":#line:67
        if (O0OOO0O000OOOO0O0 <=HAZARD_SIZE_HALF ):#line:68
            return True #line:69
    if O00OOOOOO000O0O0O =="column":#line:71
        if (O0OOO0O000OOOO0O0 <=COLUMN_SIZE_HALF ):#line:72
            return True #line:73
def get_list_index (OO000O00O000O00OO ):#line:75
    if OO000O00O000O00OO =='player':#line:76
        O0OO000O0OOO00OO0 =PLAYER_LIST_INDEX #line:77
    elif OO000O00O000O00OO =='weapon':#line:78
        O0OO000O0OOO00OO0 =WEAPON_LIST_INDEX #line:79
    elif OO000O00O000O00OO =='column':#line:80
        O0OO000O0OOO00OO0 =COLUMN_LIST_INDEX #line:81
    elif OO000O00O000O00OO =='hazard':#line:82
        O0OO000O0OOO00OO0 =HAZARD_LIST_INDEX #line:83
    else :#line:84
        O0OO000O0OOO00OO0 =-1 #line:85
    return O0OO000O0OOO00OO0 #line:86
def start ():#line:88
    return "defensive",{}#line:89
def get_circle_point (O00000000OO000O00 ,O00OOOOO00OO000O0 ):#line:91
    O0OO00O00OO0O000O =math .cos (math .radians (O00000000OO000O00 ))*O00OOOOO00OO000O0 #line:92
    OO0000000OOOO0OOO =math .sin (math .radians (O00000000OO000O00 ))*O00OOOOO00OO000O0 #line:93
    return (O0OO00O00OO0O000O ,OO0000000OOOO0OOO )#line:94
def circle_collision (OOO00OOOO0O000OO0 ,OO0OO0OOOOO00000O ,O00O00O00OOOOOO0O ,OO00O000O0O00O0OO ,OOOOO000O0OOO0OO0 ,OO0O0OO0OO00OOO0O ):#line:96
    return (OOO00OOOO0O000OO0 -OO00O000O0O00O0OO )**2 +(OO0OO0OOOOO00000O -OOOOO000O0OOO0OO0 )**2 <=(O00O00O00OOOOOO0O +OO0O0OO0OO00OOO0O )**2 #line:97
def is_path_to_player_clear (O00O0000O000O0000 ,O00OOO00OO0OOOO0O ,OO0OO00O000OO0OO0 ,OOOO0O0000O0O0O00 ,O00OOOOOO00OOO0OO ):#line:99
    OOOO00O0O0OO0OOO0 =True #line:101
    for O0000O0O00OO0O0O0 in OOOO0O0000O0O0O00 :#line:104
        if O0000O0O00OO0O0O0 .dist <=OO0OO00O000OO0OO0 :#line:105
            O0000O000O0OO0O00 ,OO0O0OO000OOO0O00 =get_circle_point (O0000O0O00OO0O0O0 .angle ,O0000O0O00OO0O0O0 .dist )#line:106
            if circle_collision (O00O0000O000O0000 ,O00OOO00OO0OOOO0O ,PLAYER_SIZE_HALF ,O0000O000O0OO0O00 ,OO0O0OO000OOO0O00 ,COLUMN_SIZE_HALF ):#line:107
                OOOO00O0O0OO0OOO0 =False #line:108
                break #line:109
    for OOO00OOO00O00O00O in O00OOOOOO00OOO0OO :#line:112
        if OOO00OOO00O00O00O .dist <=OO0OO00O000OO0OO0 :#line:113
            O00OOOO0OOOOOOOO0 ,O00O0000O0O00OO0O =get_circle_point (OOO00OOO00O00O00O .angle ,OOO00OOO00O00O00O .dist )#line:114
            if circle_collision (O00O0000O000O0000 ,O00OOO00OO0OOOO0O ,PLAYER_SIZE_HALF ,O00OOOO0OOOOOOOO0 ,O00O0000O0O00OO0O ,HAZARD_SIZE_HALF ):#line:115
                OOOO00O0O0OO0OOO0 =False #line:116
                break #line:117
    return OOOO00O0O0OO0OOO0 #line:119
def defensive ():#line:121
    O0O0O00O0OO0OO00O =percept ()#line:123
    OO0O0OOO00OO0O0OO =O0O0O00O0OO0OO00O [PLAYER_LIST_INDEX ]#line:124
    OO000OO0000OOO00O ,O0O0O000OO0OO0O0O =get_velocity_tuple ()#line:126
    if OO0O0OOO00OO0O0OO !=None and len (OO0O0OOO00OO0O0OO )!=0 :#line:128
        O000O0OOO000OOO0O =OO0O0OOO00OO0O0OO [0 ]#line:130
        O0OO00OO000OOOOOO ,O0OOO0000O00OO0O0 =get_circle_point (O000O0OOO000OOO0O .angle ,O000O0OOO000OOO0O .dist )#line:131
        OO00O0O00O000O0O0 =get_current_status ()#line:132
        if (O000O0OOO000OOO0O .dist <150 or OO00O0O00O000O0O0 <=50 ):#line:134
            if is_path_to_player_clear (O0OO00OO000OOOOOO ,O0OOO0000O00OO0O0 ,O000O0OOO000OOO0O .dist ,O0O0O00O0OO0OO00O [COLUMN_LIST_INDEX ],O0O0O00O0OO0OO00O [HAZARD_LIST_INDEX ]):#line:135
                OO0O000OOO0000000 =clamp (O0OO00OO000OOOOOO ,-1 ,1 )#line:136
                OOOO00OO0OO0OO00O =clamp (O0OOO0000O00OO0O0 ,-1 ,1 )#line:137
                return "defensive",{"ACLT_X":OO0O000OOO0000000 ,"ACLT_Y":OOOO00OO0OO0OO00O }#line:139
    OOOO0OOOOO0OO0OOO =-clamp (OO000OO0000OOO00O ,-1 ,1 )#line:141
    O0000OOOO0OO000OO =-clamp (O0O0O000OO0OO0O0O ,-1 ,1 )#line:142
    return "defensive",{"ACLT_X":OOOO0OOOOO0OO0OOO ,"ACLT_Y":O0000OOOO0OO000OO }#line:144
class PerceptData :#line:146
    def __init__ (O0O0000OO0O0O0000 ,OOOOO000000OOOO0O ,O00O0O0OOOO0O000O ,O00OO00O00O000000 ,O0OOO000OO0O0OOO0 ):#line:147
        O0O0000OO0O0O0000 .type =OOOOO000000OOOO0O #line:148
        O0O0000OO0O0O0000 .angle =O00O0O0OOOO0O000O #line:149
        O0O0000OO0O0O0000 .dist =O00OO00O00O000000 #line:150
        O0O0000OO0O0O0000 .info =O0OOO000OO0O0OOO0 #line:151
    def __eq__ (OO0000OO0O0OOOO0O ,OO0OOO0OO00O0OOO0 ):#line:153
        if not isinstance (OO0OOO0OO00O0OOO0 ,PerceptData ):#line:154
            return NotImplemented #line:155
        return OO0000OO0O0OOOO0O .type ==OO0OOO0OO00O0OOO0 .type and OO0000OO0O0OOOO0O .angle ==OO0OOO0OO00O0OOO0 .angle and OO0000OO0O0OOOO0O .dist ==OO0OOO0OO00O0OOO0 .dist and OO0000OO0O0OOOO0O .info ==OO0OOO0OO00O0OOO0 .info #line:156
    def __str__ (O00OO0O0O00OO0OO0 ):#line:158
        return O00OO0O0O00OO0OO0 .type #line:159
def percept ():#line:161
    O0O00OOOOOO00O000 =[[],[],[],[]]#line:163
    O0OOOOO0OOO00O0O0 =""#line:165
    O0OOO000OOOOOO00O =0 #line:166
    for O00O0O000O0OOOO00 in range (0 ,360 ):#line:169
        O0OO00O0O000O000O ,O0OOO000OO000O00O ,O0O0000000OOOOOOO =get_the_radar_data (O00O0O000O0OOOO00 )#line:171
        OOOO0000000OOOOOO =PerceptData (O0OO00O0O000O000O ,O00O0O000O0OOOO00 ,O0OOO000OO000O00O ,O0O0000000OOOOOOO )#line:172
        OO00000O0O0O00000 =get_list_index (OOOO0000000OOOOOO .type )#line:173
        if OO00000O0O0O00000 !=-1 :#line:175
            if not is_likely_same_obj (OOOO0000000OOOOOO .type ,OOOO0000000OOOOOO .dist ,O0OOOOO0OOO00O0O0 ,O0OOO000OOOOOO00O ):#line:176
                O0O00OOOOOO00O000 [OO00000O0O0O00000 ].append (OOOO0000000OOOOOO )#line:177
            elif OOOO0000000OOOOOO .type ==O0OOOOO0OOO00O0O0 :#line:178
                if O0OOO000OO000O00O <O0O00OOOOOO00O000 [OO00000O0O0O00000 ][-1 ].dist :#line:179
                    O0O00OOOOOO00O000 [OO00000O0O0O00000 ][-1 ].dist =O0OOO000OO000O00O #line:180
        O0OOOOO0OOO00O0O0 =OOOO0000000OOOOOO .type #line:182
        O0OOO000OOOOOO00O =OOOO0000000OOOOOO .dist #line:183
    return O0O00OOOOOO00O000 #line:185
