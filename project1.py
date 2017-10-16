#Project 1: Time Management; Author: Jamie Nelson

def main():

    #Heading
    print("*** TIME MANAGEMENT ASSISTANT ***")

    #Initialize variables
    longestMin = 0
    longestDesc = ""
    totalMin = 0
    totalHours = 0
    totalDays = 0

    #Get start time and number of tasks
    taskNumber = int(input("Number of tasks: "))
    print("What time will you start (on a 24-hour clock)?")
    startHour = int(input("Hour: "))
    startMin = int(input("Minute: "))

    #For each task get the description and time in minutes
    for i in range(taskNumber):
        print("\nTASK ", i + 1)
        currentDesc = input("Task description: ")
        currentMin = int(input("How many minutes will this task take? "))
        
        #Add all the minutes to get a total at the end of the for loop
        totalMin = totalMin + currentMin
        
        #Check if the current task is the longest
        if currentMin > longestMin:
            longestMin = currentMin
            longestDesc = currentDesc

    #Find the average of all the tasks by dividing the total amount of minutes
    #by the amount of tasks
    averageMin = totalMin / taskNumber

    #Convert time to hours instead of minutes
    while totalMin >= 60:
        totalHours = totalHours + 1
        totalMin = totalMin - 60

    #Convert time to days instead of hours
    while totalHours >= 24:
        totalDays = totalDays + 1
        totalHours = totalHours - 24

    #Find the end time
    endHour = startHour + totalHours
    endMin = startMin + totalMin
    endDay = totalDays

    #Check if the minutes went over an hour
    if endMin >= 60:
        endHour = endHour + 1
        endMin = endMin - 60

    #Check if the hours went over a day
    if endHour >= 24:
        endDay = endDay + 1
        endHour = endHour - 24

    #Print the total time
    print("\nTOTAL TIME: ", totalDays, " day(s), ", totalHours, " hour(s), ", totalMin, " minute(s)")

    #Print the end time
    #Check if it is the same day
    if endDay == 0:
        print("END TIME: Today at ", endHour, ":", endMin)
    else:
        print("END TIME: In ", endDay, " day(s) at ", endHour, ":", endMin)

    #Print longest task
    print("LONGEST TASK: ", longestDesc, " (", longestMin, " minutes)")

    #Print average task time
    print("AVERAGE TASK LENGTH: ", round(averageMin, 1), " minutes")
        
main()    
                    

