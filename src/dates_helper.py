import datetime

def get_dates_in_interval(initiateDate:str, endingDate:str) -> list:
        
    if initiateDate is None or endingDate is None: # if initial date is none -> end
        return 

    start = datetime.datetime.strptime(initiateDate, "%m/%d/%Y") # format variable and assigned to start
    end = datetime.datetime.strptime(endingDate, "%m/%d/%Y") # format variable and assigned to start

    if end < start: # if end day if greater than start -> end
        return 

    # we create the range of the dates
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start + datetime.timedelta(1)).days)]
    # Parsed the date to string
    parsed_date = [date.strftime("%-m/%d/%Y") for date in date_generated]

    return parsed_date # return the list of dates

