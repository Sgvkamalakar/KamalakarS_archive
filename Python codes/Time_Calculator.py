def add_time(start, duration, dayOfWeek = None):
      
  new_time = ""
  s = start.split(" ")
  st = s[0].split(":")
  meridian = s[1]
  sh = int(st[0])
  sm = int(st[1])
  
  if meridian == "PM" :
    sh = sh + 12
  sm = sm + (60 * sh)

  dtime = duration.split(":")
  dhour = int(dtime[0])
  dmin = int(dtime[1])
  dmin = dmin + (60 * dhour)

  minutes = sm + dmin

  fmin = minutes % 60
  hours = int(minutes / 60)
  if len(str(fmin)) == 1:
    new_time = "0" + str(fmin)
  elif len(str(fmin)) == 2:
    new_time = str(fmin)

  hour = hours % 24
  days = int(hours / 24)


  fhour = hour % 12
  if int(hour / 12) == 0:
    fmeridian = 'AM'
    if fhour == 0:
      fhour = 12
  else:
    fmeridian = 'PM'
    if fhour == 0:
      fhour = 12
  new_time = str(fhour) + ':' + new_time + ' ' + fmeridian 

  if not dayOfWeek == None:
    daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pos = 0
    while True:
      if dayOfWeek.lower() == daysOfWeek[pos].lower():
        break
      pos= pos + 1
    newDayOfWeek = daysOfWeek[((pos + (days % 7)) % 7)]
    new_time = new_time + ", " + newDayOfWeek

  if days == 1:
    new_time = new_time + " (next day)"
  elif days > 1:
    days = str(days)
    new_time = new_time + " (" + days + " days later)"

  print(new_time)

if __name__=="__main__":
    add_time("3:00 PM", "3:10")
    add_time("11:30 AM", "2:32", "Monday")
    add_time("11:43 AM", "00:20")
    add_time("10:10 PM", "3:30")
    add_time("11:43 PM", "24:20", "tueSday")
    add_time("6:30 PM", "205:12")
