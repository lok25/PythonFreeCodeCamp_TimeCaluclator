

def getNextDay(day):
    
    if day=='Monday':
        return 'Tuesday'
    elif day=='Tuesday':
        return 'Wednesday'
    elif day=='Wednesday':
        return 'Thursday'
    elif day=='Thursday':
        return 'Friday'
    elif day=='Friday':
        return 'Saturday'
    elif day=='Saturday':
        return 'Sunday'
    elif day=='Sunday':
        return 'Monday'
   
   
        
     
     


def splitTime(t):
     a=[]
     if "AM" in t or "PM" in t:
          x=t.split()
          a=x[0].split(':')
          return a
     else:
          return t.split(':')
     
   


def getNoOfDays(t):
  i = 0
  while t >24 :  
        i += 1
        t=t-24
  
  return i

    




def add_time(clockformatTime,duration,day=None):

    am=0
    pm=0
    #is Am Pm

        #check am or pm
    if "AM" in clockformatTime:
         am=1
    else:
         pm=1

   

    cft=splitTime(clockformatTime)
    dur=splitTime(duration)

    cft_hour=int(cft[0])
    cft_min=int(cft[1])

    dur_hour=int(dur[0])
    dur_min=int(dur[1])

    resAmPm=""    
   
 
    
    resHour=int(cft[0])+ int(dur[0])


    if(pm==1 ):
        resAmPm='PM'
    else:
        resAmPm='AM'


    while resHour>12:    

        if(day!=""):
            day=getNextDay(day)            
            resAmPm='AM'
        else:
            resAmPm='PM'

        resHour=resHour-12


    resMin=int(cft[1])+int(dur[1])

    if(resMin>60):
        resHour=resHour+1
        resMin=resMin-60
        if(resHour>12):
            resAmPm='Pm'
            resHour=resHour-12



    if(resMin<10):
        strResMin="0"+str(resMin)
    else:
        strResMin=str(resMin)
        

             #number of days 
    resNumOfDays=0
    if(dur_hour>24):
        resNumOfDays=(int)(dur_hour/24)+1

    


    if(resNumOfDays>1): strresNumOfDays="("+str(resNumOfDays)+" days later)"
    elif(resNumOfDays==1):strresNumOfDays="("+"next day"+")"
    else:strresNumOfDays=""


    if day !=None  and strresNumOfDays=="":
        strresNumOfDays=day



     
    print(str(resHour)+":"+strResMin+" "+resAmPm+" "+strresNumOfDays)

add_time("11:43 PM", "24:20","Tuesday")
add_time("6:30 PM", "205:12","")
add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")
















    
    