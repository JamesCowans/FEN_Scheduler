#Day in a day code solution




# RULES NEEDED FOR MAX COLLEAGUES ON ONE SHIFT PATTERN!!!

# LOGIC

# Max opening hours is 07:00 until 21:00 (14 hours)

# Max shift is 7.5 hours

# Shifts should be 07:00 - 16:00 or 12:00 - 21:00 (Check this!!)

# A process shouldn't start until there is enough work to do for min one worker

# A process must go to a previous process to collect work when it is ready - this should dictate the time it starts and the number of workers to finish by 21:00

# Process flow - Load/Putaway -> Decant -> Processing

# Needs to include the volume the dock can process per hour - minimum manning of 3?






# Takes in the Weekly GM units forcast
def GM_Volumes():
    gm_vol = int(input("Please enter the weekly GM Forcast: \n"))
    return (gm_vol)
total_volumes_gm = GM_Volumes()




# Divides the Weekly GM forcast by number of days worked - set as 5 to start
def GM_Daily():
    gm_day = (total_volumes_gm) /5
    return (gm_day)
daily_volumes_gm = GM_Daily()
# print(daily_volumes_gm)




# Maximum units per hour that can be completed by 1 worked and divides the total work by number of hours available to see how many worked needed in total each working 7.5 hours - 782 per shift?
def GM_Decant_Max_Units_Colleagues():
    gm_max = (daily_volumes_gm) //782 # This is the decant KPI per shift, by dividing the overall amount of work by the maximum achievable we see the total colleagues required
    return (gm_max)
max_gm_vol = GM_Decant_Max_Units_Colleagues() # This is the maximum number of colleagues required to complete decant work in a day
print(max_gm_vol)




# Maximum units per hour that can be completed by 1 worked and divides the total work by number of hours available to see how many worked needed in total each working 7.5 hours
# GM_Prcss_Max_Units_Colleagues():


# Maximum units per hour that can be completed by 1 worked and divides the total work by number of hours available to see how many worked needed in total each working 7.5 hours
def GM_Putaway_Max_Units_Colleagues():
    putaway_work = (daily_volumes_gm) * 0.30 # percentage of work that is likely to be putaway
    return(putaway_work)
total_putaway_work = GM_Putaway_Max_Units_Colleagues()
# print(total_putaway_work)
    






# Takes in the Weekly HB units forcast
def HB_Volumes():
    hb_vol = int(input("Please enter the weekly Beauty Forcast: \n"))
    return (hb_vol)
total_volumes_hb = HB_Volumes()



# Divides the Weekly HB forcast by number of days worked - set as 5 to start
def HB_Daily():
    hb_day = (total_volumes_hb) /5
    return (hb_day)
daily_volumes_hb = HB_Daily()
# print(daily_volumes_hb)

# No decant function required as this follows a xdock process, in and straight out or putaway



# Maximum units per hour that can be completed by 1 worked and divides the total work by number of hours available to see how many worked needed in total each working 7.5 hours
def HB_Prcss_Max_Units_Colleagues():
    units_per_hb_colleague = (daily_volumes_hb) / 384 # This is the units per colleague per hour 384 per hour
    max_hb_colleagues = (units_per_hb_colleague) // 7.5 # Come back to this, the calculation is incorrect - dividing by 384 shows the number of hours needed to complete,  
    if max_hb_colleagues == 0:
        
       max_hb_colleagues = max_hb_colleagues +1 # This sets minimum staffing levels to one if there is not enough work to carry out

         
    return(max_hb_colleagues) #if this is then divided by 7.5 (max shift length) this will then give th enumber of colleagues needed 
hb_col_total =HB_Prcss_Max_Units_Colleagues()
# print(hb_col_total)



# Maximum units per hour that can be completed by 1 worked and divides the total work by number of hours available to see how many worked needed in total each working 7.5 hours
def HB_Putaway_Max_Units_Colleagues():
    putaway_work_hb = (daily_volumes_hb) * 0.30 # percentage of work that is likely to be putaway
    return(putaway_work_hb)

total_putaway_work_hb = HB_Putaway_Max_Units_Colleagues()
# print(total_putaway_work_hb)




