# Code written by Chooi Fei Ng
def add_time(start, duration, weekday = False):

  # split the actual time and the time of the day
  start_time = start.split()
  # obtain the start time and start minute by splitting using :
  start_temp = start_time[0].split(':')
  start_hour = int(start_temp[0])
  start_min = int(start_temp[1])
  #print(start_temp)
  # assign the time of the day
  daytime = start_time[1].strip()
  #print(daytime)
  # split the duration that is added to the start time using :
  duration_temp = duration.split(':')
  #print(duration_temp)
  duration_hour = int(duration_temp[0])
  duration_min = int(duration_temp[1])

  # add the duration minute to the start minute
  add_min = start_min + duration_min
  if (daytime == 'PM'):
    # if the start time is in the afternoon, add 12 hours to the start hours to convert it to 24 hour clock
    start_hour = start_hour + 12
  #print(add_min)
  if (add_min >= 60):
    # if the total minute is more than 60, we add an extra hour to the total hours and reduce the minutes by 60
    add_hour = start_hour + duration_hour + 1
    add_min = add_min - 60
    #print(add_hour)
    #print(add_min)
  else:
    # otherwise, just add the start hour to the duration hour
    add_hour = start_hour + duration_hour

  if (add_min <= 10):
    # if the minutes is less than 10, add a 0 in front of the total minutes and convert it to string
    str_min = '0' + str(add_min)
  else:
    # otherwise, just convert the total minutes into string
    str_min = str(add_min)

  # Initialise the number of days to zero
  days = 0
  if(add_hour > 24):
    # If the total hours calculated is greater than 24, decrease the hours by 24 hours as we increase the number of days
    while (add_hour > 24):
      add_hour = add_hour - 24
      days = days + 1

  #print(daytime)
  #print(add_hour)
  if(add_hour > 12):
    # If the number of hours is greater than 12, the final day time is AM if its 24 (meaning around midnight),
    # otherwise its PM.
    if (add_hour == 24):
      final_daytime = 'AM'
    else:
      final_daytime = 'PM'
    # The hours is reduced by 12 to reflect a 12 hour clock
    add_hour = add_hour - 12

  elif(add_hour == 12):
    # If it hits 12 noon, it changes to PM
    if (daytime == 'AM'):
      final_daytime = 'PM'
  else:
    # Otherwise, it is still in the morning
    final_daytime = 'AM'

  # The new time display that includes hour, min and daytime
  new_time = str(add_hour) + ':' + str_min + ' ' + final_daytime

  if (days == 1):
    if (final_daytime == 'AM' and add_hour == 12):
      # If its around 12 midnight
      days = days + 1  # number of days adds one

  if (weekday != False):
    # If a weekday is entered, change the weekday to lower case letter to be compared
    week = weekday.lower()
    if(week == 'monday'):
      # if its monday, the week number is 1
      week_num = 1
    elif(week == 'tuesday'):
      # if its tuesday, the week number is 2
      week_num = 2
    elif(week == 'wednesday'):
      # if its wednesday, the week number is 4
      week_num = 3
    elif (week == 'thursday'):
      # if its thursday, the week number is 4
      week_num = 4
    elif (week == 'friday'):
      # if its friday, the week number is 5
      week_num = 5
    elif (week == 'saturday'):
      # if its saturday, the week number is 6
      week_num = 6
    else:
      # else its sunday, the week number is 7
      week_num = 7

    # The number of days is added the the week day number
    week_num = week_num + days

    while (week_num > 7):
    # while the week number is greater than 7, reduce it by 7 until it is less than 7
      week_num = week_num - 7

    if (week_num == 1):
      # if the week number is 1, it is Monday
      dayweek = 'Monday'
    elif (week_num == 2):
      # if the week number is 2, it is Tuesday
      dayweek = 'Tuesday'
    elif (week_num == 3):
      # if the week number is 3, it is Wednesday
      dayweek = 'Wednesday'
    elif (week_num == 4):
      # if the week number is 4, it is Thursday
      dayweek = 'Thursday'
    elif (week_num == 5):
      # if the week number is 5, it is Friday
      dayweek = 'Friday'
    elif (week_num == 6):
      # if the week number is 6, it is Saturday
      dayweek = 'Saturday'
    else:
      # Otherwise, it is Sunday
      dayweek = 'Sunday'

    # Add the day of the week to the new time display
    new_time = new_time + ', ' + dayweek

  if (days == 1):
    # If the number of days is equal to one
    if(final_daytime == 'AM' and add_hour == 12):
      # If its around 12 midnight
      # Add the number of days later to the new time display
      new_time = new_time + ' (' + str(days) + ' days later)'
    else:
      # Otherwise, add next day to the new time display
      new_time = new_time + ' (next day)'

  elif(days > 1):
    # If the number of days is greater than 1, add the number of days later to the new time display
    new_time = new_time + ' (' + str(days) + ' days later)'

  # return the new time from the call function
  return new_time
