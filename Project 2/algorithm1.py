#-----------------------------------------------------------------------------------------------
# Authors : Andres Perez, Andrew Gonzalez, Desire Hernandez, & Paul Le
# Due Date : March 17, 2024
# Section : CPSC 335-04
#-----------------------------------------------------------------------------------------------

#-------------------------- START OF ALGORITHM 1 FUNCTION --------------------------------------
def group_schedule( busy_schedule, working_period, duration_of_meeting ) :
  if not busy_schedule or not working_period:
    print( "Your lists are empty and cannot successfully create a group schedule for you.")
    return 0

  busy_schedule.sort()
  working_period.sort()

  schedule_in_mins = []
  available_times = []


  latest_start_time = max( working_period, key = lambda x: x[0] )[0]
  earliest_end_time = min( working_period, key = lambda x: x[1] )[1]

  busy_schedule = [item for item in busy_schedule if item[0] >= latest_start_time and item[1] <= earliest_end_time]
  print( busy_schedule )

  # After removing those time slots, if the list is empty return an empty list & tell user there are no available time slots
  if not busy_schedule:
    print("There are no available times to have a group meeting.")
    print( busy_schedule )
    return available_times

  if busy_schedule[0] == [latest_start_time, earliest_end_time]:
    print("There are no available times to have a group meeting.")
    print( busy_schedule )
    return available_times


  for i in range( 0, len(busy_schedule) ):
    hour1, mins1 = map( int, busy_schedule[i][0].split(':') )
    hour2, mins2 = map( int, busy_schedule[i][1].split(':') )
    schedule_in_mins.append( [hour1 * 60 + mins1, hour2 * 60 + mins2] )


  # I need to find the longest latest time in schedule_in_mins & subtract that from earliest end time
  latest_schedule_time = max( schedule_in_mins, key = lambda x: x[1] )[1]
  earliest_schedule_time = min( schedule_in_mins, key = lambda x: x[0] )[0]

  hour, mins = map( int, earliest_end_time.split(':') )
  earliest_time_mins = hour * 60 + mins

  hour, mins = map( int, latest_start_time.split(':') )
  latest_time_mins = hour * 60 + mins

  for i in range( 0, len(schedule_in_mins) ):
    end_current = ( schedule_in_mins[i][1] ) + 1
    print( end_current )

    if i < len(schedule_in_mins) - 1:
      start_next = schedule_in_mins[i + 1][0]
      print( start_next )

    if start_next - end_current >= duration_of_meeting:
      available_times.append( [ end_current - 1, start_next ] )

  if earliest_time_mins - latest_schedule_time >= duration_of_meeting:
    available_times.append( [latest_schedule_time, earliest_time_mins] )

  if earliest_schedule_time - latest_time_mins >= duration_of_meeting:
    available_times.append( [latest_time_mins, earliest_schedule_time] )

  for i in range( 0, len(available_times) ):
    hours1 = available_times[i][0] // 60
    minutes1 = available_times[i][0] % 60
    available_times[i][0] = f"{hours1:02d}:{minutes1:02d}"
    hours2 = available_times[i][1] // 60
    minutes2 = available_times[i][1] % 60
    available_times[i][1] = f"{hours2:02d}:{minutes2:02d}"

  available_times.sort()

  print( "Here are the available times to have the group meeting:\n" + str(available_times) )

  return available_times
#---------------------------- END OF ALGORITHM 1 FUNCTION --------------------------------------
# group_schedule( [ ['07:00', '08:30'], ['12:00', '13:00'], ['16:00', '18:00'],
#                             ['09:00', '10:30'], ['12:20', '13:30'], ['14:00', '15:00'],
#                             ['16:00', '17:00'] ], [ ['09:00', '19:00'], ['09:00', '18:30'] ],
#                             30 )
#group_schedule( [ ['07:00', '08:30'], ['12:00', '13:00'], ['16:00', '18:00'],
#                  ['09:00', '10:30'], ['12:20', '13:30'], ['14:00', '15:00'],
#                  ['16:00', '17:00'] ], [ ['09:00', '19:00'], ['15:00', '16:30'] ],
#                  30 )
# group_schedule( [ ['07:00', '08:30'], ['12:00', '13:00'], ['16:00', '18:00'],
#                   ['09:00', '10:30'], ['12:20', '13:30'], ['14:00', '15:00'],
#                   ['16:00', '17:00'] ], [ ['09:00', '19:00'], ['00:00', '10:30'] ],
#                   30 )
# group_schedule( [ ['07:00', '08:30'], ['12:00', '13:00'], ['16:00', '18:00'],
#                   ['09:00', '10:30'], ['12:20', '13:30'], ['14:00', '15:00'],
#                   ['16:00', '17:00'] ], [ ['09:00', '19:00'], ['09:00', '16:30'] ],
#                   30 )
# ----------------------- START OF INTERACTIVE CODE (CHOICE #1) --------------------------------
def main():
  # Create two lists to hold user's inputs for booked slots & daily activities
  busy_schedule = []
  daily_act = []
  # Creating two lists to check each individuals times
  check_schedule = []
  check_daily_act = []

  # Ask user for the number of times(slots) in their schedule
  n = int( input( "Enter number of times in your schedule : " ) )

  # Loop n times to gather the user's information for each slot
  for i in range( 0, n ):
    print( "\nSlot " + str( i + 1 ) + ":" )
    while True:
      # Asking user for the start time for Slot i + 1
      start_time = input("Enter start time (HH:MM): ")
      # Asking user for the end time for Slot i + 1
      end_time = input("Enter end time (HH:MM): ")
      # Converting the user's inputs into 24hr military format (HH:MM), just in case the user did not
      hours, minutes = map( int, start_time.split(':') )
      start_time = f"{hours:02d}:{minutes:02d}"

      if hours < 0 or hours > 24:
        print( "Invalid Input: The start time hour cannot be less than 0 or greater than 24." )
        return -1
      if minutes < 0 or minutes > 60:
        print( "Invalid Input: The start time minutes cannot be less than 0 or greater than 60. ")
        return -1

      hours, minutes = map( int, end_time.split(':') )
      end_time = f"{hours:02d}:{minutes:02d}"

      if hours < 0 or hours > 24:
        print( "Invalid Input: The end time hour cannot be less than 0 or greater than 24." )
        return -1

      if start_time > end_time:
        print( "Invalid Input: The start time cannot be greater than the end time." )
        return -1
      break;

    # Creating a list of Slot i + 1 start & end times, then adding it into a list
    busy_schedule.append( [start_time, end_time] )
    # Also adding it into another list to validate
    check_schedule.append( [start_time, end_time] )
    print( check_schedule )
  # Ask user to enter their daily working periods (earliest, latest)
  print( "\nPlease enter the times you are available for meetings daily." )
  while True:
    # Asking user for the start time
    start_time = input("Enter start time (HH:MM): ")
    # Asking user for the end time
    end_time = input("Enter end time (HH:MM): ")
    # Converting the user's inputs into 24hr military format (HH:MM), just in case the user did not
    hours, minutes = map( int, start_time.split(':') )
    start_time = f"{hours:02d}:{minutes:02d}"

    if hours < 0 or hours > 24:
      print( "Invalid Input: The start time hour cannot be less than 0 or greater than 24." )
      return -1
    if minutes < 0 or minutes > 60:
      print( "Invalid Input: The start time minutes cannot be less than 0 or greater than 60. ")
      return -1

    hours, minutes = map( int, end_time.split(':') )
    end_time = f"{hours:02d}:{minutes:02d}"

    if hours < 0 or hours > 24:
      print( "Invalid Input: The end time hour cannot be less than 0 or greater than 24." )
      return -1
    if minutes < 0 or minutes > 60:
      print( "Invalid Input: The end time minutes cannot be less than 0 or greater than 60. ")
      return -1

    if start_time > end_time:
        print( "Invalid Input: The start time cannot be greater than the end time." )
        return 0
    break;
  # Creating a list of the daily working periods earliest & latest times, then adding it into a list
  daily_act.append( [start_time, end_time] )
  # Also adding it into another list to validate
  check_daily_act.append( [start_time, end_time] )

  for i in range( 0, len(check_schedule) ):
    if check_schedule[i][0] < check_daily_act[0][0]:
      print( "Invalid Input: The start time of your working period cannot start after your planned meeting." )
      print( "Start time of your working period: " + str(check_daily_act[0][0]) +"\nStart time of your first meeting: " + str(check_schedule[i][0]) )
      return -1
    elif check_schedule[i][1] > check_daily_act[0][1]:
      print( "Invalid Input: The end time of your working period cannot end before your planned meeting." )
      print( "End time of your working period: " + str(check_daily_act[0][1]) +"\nEnd time of your meeting: " + str(check_schedule[i][1]) )
      return -1
  check_schedule.clear()
  check_daily_act.clear()
  print( check_schedule )

  # Asking user for the number of group members they want to include
  num_of_members = int( input( "\nEnter number of group members : " ) )
  # Loop num_of_members times to gather each group members information
  for i in range( 0, num_of_members ):
    print( "\nGroup Member # " + str( i + 1 ) + ":" )
    # Ask for the number of times(slots) in the current group member's schedule
    n = int( input( "Enter number of times in their schedule : " ) )
    # Loop n times to gather the current group member's information for each slot
    for i in range( 0, n ):
      print( "\nSlot " + str( i + 1 ) + ":" )

      while True:
        # Asking user for the start time for Slot i + 1
        start_time = input("Enter start time (HH:MM): ")
        # Asking user for the end time for Slot i + 1
        end_time = input("Enter end time (HH:MM): ")
        # Converting the user's inputs into 24hr military format (HH:MM), just in case the user did not
        hours, minutes = map( int, start_time.split(':') )
        start_time = f"{hours:02d}:{minutes:02d}"

        if hours < 0 or hours > 24:
          print( "Invalid Input: The start time hour cannot be less than 0 or greater than 24." )
          return -1
        if minutes < 0 or minutes > 60:
          print( "Invalid Input: The start time minutes cannot be less than 0 or greater than 60. ")
          return -1

        hours, minutes = map( int, end_time.split(':') )
        end_time = f"{hours:02d}:{minutes:02d}"

        if hours < 0 or hours > 24:
          print( "Invalid Input: The end time hour cannot be less than 0 or greater than 24." )
          return -1
        if minutes < 0 or minutes > 60:
          print( "Invalid Input: The end time minutes cannot be less than 0 or greater than 60. ")
          return -1

        if start_time > end_time:
          print( "Invalid Input: The start time cannot be greater than the end time." )
          return 0
        break;
      # Creating a list of Slot i + 1 start & end times, then adding it into a list that combines all schedules
      busy_schedule.append( [start_time, end_time] )
      # Also adding it into another list to validate
      check_schedule.append( [start_time, end_time] )
    # Ask user to enter the current group member's daily working periods (earliest, latest)
    print( "\nPlease enter the times they are available for meetings daily." )

    while True:
      # Asking user for the start time
      start_time = input("Enter start time (HH:MM): ")
      # Asking user for the end time
      end_time = input("Enter end time (HH:MM): ")
      # Converting the user's inputs into 24hr military format (HH:MM), just in case the user did not
      hours, minutes = map( int, start_time.split(':') )
      start_time = f"{hours:02d}:{minutes:02d}"

      if hours < 0 or hours > 24:
        print( "Invalid Input: The start time hour cannot be less than 0 or greater than 24." )
        return -1
      if minutes < 0 or minutes > 60:
        print( "Invalid Input: The start time minutes cannot be less than 0 or greater than 60. ")
        return -1

      hours, minutes = map( int, end_time.split(':') )
      end_time = f"{hours:02d}:{minutes:02d}"

      if hours < 0 or hours > 24:
        print( "Invalid Input: The end time hour cannot be less than 0 or greater than 24." )
        return -1
      if minutes < 0 or minutes > 60:
        print( "Invalid Input: The end time minutes cannot be less than 0 or greater than 60. ")
        return -1

      if start_time > end_time:
        print( "Invalid Input: The start time cannot be greater than the end time." )
        return 0
      break;
    # Creating a list of the daily working periods earliest & latest times, then adding it into a list that combines all daily periods
    daily_act.append( [start_time, end_time] )
    # Also adding it into another list to validate
    check_daily_act.append( [start_time, end_time] )

    for i in range( 0, len(check_schedule) ):
      print( check_schedule[i][0] )
      print( check_daily_act[0][0] )
      if check_schedule[i][0] < check_daily_act[0][0]:
        print( "Invalid Input: The start time of their working period cannot start after their planned meeting." )
        print( "Start time of their working period: " + str(check_daily_act[0][0]) +"\nStart time of their meeting: " + str(check_schedule[i][0]) )
        return -1
      elif check_schedule[i][1] > check_daily_act[0][1]:
        print( "Invalid Input: The end time of their working period cannot end before their planned meeting." )
        print( "End time of their working period: " + str(check_daily_act[0][1]) +"\nEnd time of their meeting: " + str(check_schedule[i][1]) )
        return -1

    check_schedule.clear()
    check_daily_act.clear()
  # Asking user for the minimum duration time in minutes(integer)
  duration_of_meeting = int( input( "\nEnter the minimum duration of the meeting you want to schedule (in minutes): " ) )
  # Sorting both lists
  busy_schedule.sort()
  daily_act.sort()

  group_schedule( busy_schedule, daily_act, duration_of_meeting )
# ----------------------- END OF INTERACTIVE CODE (CHOICE #1) ----------------------------------

if __name__ == "__main__":
  main()

# ----------------------- START OF PREDETERMINED INPUTS (CHOICE #2) ----------------------------
# Call function with predetermined inputs below :
# Example :group_schedule( [ ['07:00', '08:30'], ['12:00', '13:00'], ['16:00', '18:00'],
#                            ['09:00', '10:30'], ['12:20', '13:30'], ['14:00', '15:00'],
#                            ['16:00', '17:00'] ], [ ['09:00', '19:00'], ['09:00', '18:30'] ],
#                            30 )

# ----------------------- END OF PREDETERMINED INPUTS (CHOICE #2) ------------------------------
'''

'''