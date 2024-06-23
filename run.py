#Day in a day code solution




# RULES NEEDED FOR MAX COLLEAGUES ON ONE SHIFT PATTERN!!!

# LOGIC

# Max opening hours is 07:00 until 21:00 (14 hours)

# Max shift is 7.5 hours

# Shifts should be 07:00 - 16:00 or 12:00 - 21:00 (Check this!!)

# A process shouldn't start until there is enough work to do for min one worker

# A process must go to a previous process to collect work when it is ready - this should dictate the time it starts and the number of workers to finish by 21:00

# Process flow - Load/Putaway -> Decant -> Processing






# Takes in the Weekly GM units forcast
def GM_Volumes():
    gm_vol = int(input("Please enter the weekly GM Forcast: \n"))
    return (gm_vol)


# Divides the Weekly GM forcast by number of days worked - set as 5 to start
def GM_Daily(gm_vol):
    gm_day = (gm_vol) //5
    print(gm_day)

# Maximum units per hour that can be completed by 1 worked and divides the total work by number of hours available to see how many worked needed in total each working 7.5 hours
# GM_Decant_Max_Units_Colleagues():

# Maximum units per hour that can be completed by 1 worked and divides the total work by number of hours available to see how many worked needed in total each working 7.5 hours
# GM_Prcss_Max_Units_Colleagues():

# Maximum units per hour that can be completed by 1 worked and divides the total work by number of hours available to see how many worked needed in total each working 7.5 hours
# GM_Putaway_Max_Units_Colleagues():






# Takes in the Weekly GM units forcast
# Beauty_Volumes():

# Divides the Weekly GM forcast by number of days worked - set as 5 to start
# Beauty_Daily():
# No decant function required as this follows a xdock process, in and straight out or putaway

# Maximum units per hour that can be completed by 1 worked and divides the total work by number of hours available to see how many worked needed in total each working 7.5 hours
# GM_Prcss_Max_Units_Colleagues():

# Maximum units per hour that can be completed by 1 worked and divides the total work by number of hours available to see how many worked needed in total each working 7.5 hours
# GM_Putaway_Max_Units_Colleagues():


def Main():
    
    GM_Volumes()
    GM_Daily()
    
Main()
    