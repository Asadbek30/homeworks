hours = int(input('Enter hours: '))
minutes = int(input('Enter minutes: '))
delta = float(input('Enter delta: '))
if 0 <= hours <= 24: 
    if 0 <= minutes <= 60:
        if delta <= delta // 1:
            hours = (hours + delta) % 24
            hours = '0' + str(int(hours)) if hours < 10 else hours
            minutes = '0' + str(minutes) if minutes < 10 else minutes
            print(str(hours) + ':' + str(minutes))
    if delta > delta // 1 and minutes >= 0:
        newhours = (hours + delta // 1) % 24
        newminutes = (minutes + ((delta - (delta // 1)) * 60)) 
        newhours = newhours + 1 if newminutes >= 60 else int(newhours) 
        newminutes = (minutes + ((delta - (delta // 1)) * 60)) % 60
        newminutes = (newminutes - ((newminutes % 1) + 1))
        newhours = '0' + str(int(newhours)) if int(newhours) < 10 else int(newhours)
        newminutes = '0' + str(int(newminutes)) if int(newminutes) < 10 else int(newminutes)
        print(str(newhours) + ':' + str(newminutes))











    

