import re
import time

def getMonth(month):
    if month == "01":
        return "January"
    elif month == "02":
        return "February"
    elif month == "03":
        return "March"
    elif month == "04":
        return "April"
    elif month == "05":
        return "May"
    elif month == "06":
        return "June"
    elif month == "07":
        return "July"
    elif month == "08":
        return "August"
    elif month == "09":
        return "September"
    elif month == "10":
        return "October"
    elif month == "11":
        return "November"
    elif month == "12":
        return "December"

def timeConversion(input):

    concat = input[:2] + ":" + input[2:]
    t = time.strptime(concat, "%H:%M")
    convertedTime = time.strftime("%I:%M %p", t)

    return convertedTime


if __name__ == '__main__':
    date = input("Please enter the day you are looking for in the format mm/dd/yyyy\n")
    month, day, year = date.split('/')
    file = open("logs/[YTV] [" + year + "_" + month + "].log", "r", errors='replace')
    lines = file.readlines()

    output = []

    for line in lines:

        data = (re.split(r'\s{2,}', line))
        log_type = data[0]
        log_date = data[1]
        log_episode = data[2]

        if log_type == "PGRYTV":
            showtime_year = "20" + log_date[0:2]
            showtime_month = getMonth(log_date[2:4])
            showtime_day = log_date[4:6]

            showtime_time = log_date[6:8] + log_date[8:10]
            show_name = log_date[24:]
            show_episode = log_episode

            if (showtime_day == day):
                concatDate = showtime_month + " " + showtime_day + " " + showtime_year
                showtime_data = [concatDate, showtime_time, show_name, int(showtime_time), show_episode]
                output.append(showtime_data)

    length = len(output)

    for i in range(0, length):
        for j in range(0, length-i-1):
            if output[j][3] > output[j + 1][3]:
                temp = output[j]
                output[j] = output[j+1]
                output[j+1] = temp

    print("Schedule for " + showtime_month + " " + day + " " + showtime_year)

    for show in output:

        show[1] = str(show[1])
        show[1] = timeConversion((show[1]))
        txt = "{time: <20} {show: <60} {episode: <60}"
        print(txt.format(time = show[1], show = show[2], episode = show[4]))


    file.close()