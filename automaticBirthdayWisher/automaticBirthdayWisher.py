import pandas
import datetime
import smtplib
# google no longer support this
# Enter you id and password of gamil
gmailid =""
gmailpss = ""
# NOTE: turn on less secure option for gmail otherwise google will block the login

def sendmail(to, sub, message):
    try:
        
        # s = smtplib.SMTP('smtp.gmail.com', 587)     # enter smtp and port number for gmail
        # s.starttls()        # start server
        # s.login(gmailid, gmailpss)      # login to gmail
        # s.sendmail(gmailid, to, f"Subject: {sub}\n\n{message}")     # send mail
        # s.quit()        # close the connection
        # print("Mail sent")
        print(f"Mail to: {to}\nSubject: {sub}\n{message}")
    except:
        print("Mail not send")
date = datetime.datetime.now().strftime("%d-%m")        # takes only date and month
year = datetime.datetime.now().strftime("%Y")           # takes only current year
# print(date)

data = pandas.read_excel("Python\\Mini Projects\\automaticBirthdayWisher\\Birthday LIst.xlsx")  # read excel file
# print(data)
updateexcel = []    # to update the excel file when someone has been wished
for index, items in data.iterrows():        # interate excel data row by row
    bd = items['Birthday'].strftime("%d-%m")        # fetch date and month of birthday from excel data
    
    if(date == bd and year not in str(items['Year'])):      # check if someone has already been wished
        sendmail(items['Mail'], "Happy Birthday", items['Message'])
        updateexcel.append(index)
if updateexcel:     # if list will be empty it will return false
    for i in updateexcel:
        yr = data.loc[i, 'Year']    # fetch the record of given cell
        data.loc[i, 'Year'] = str(yr) + ', ' + str(year)        # update the record with current year
        
    data.to_excel("Python\\Mini Projects\\automaticBirthdayWisher\\Birthday LIst.xlsx", index = False)     # update changes to the excel file
                                                                            # index = Flase prevents wirting index everytime in excel file