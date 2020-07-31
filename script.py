# -*- coding: utf-8 -*-
import webbrowser
import time
import pyautogui as gui
import pandas as pd


def covid_status(name):
    
    c = int(confirmed[name])
    r = int(recovered[name])
    d = int(dead[name])
    c = str(c)
    date = '30-July-2020'
    r = str(r)
    d = str(d)
    if name == 'TT':
        name = 'India'
    else:
        name = state_dict.get(name)
    
    msg = "Here is the COVID-19 status of " + name + " on " + date + "  %0aCONFIRMED :  " + c + "%0aRECOVERED :  " + r + "%0aDECEASED    :  " + d +"%0a%0aNOTE: This message was sent by COVID-19 Tracking bot made by St0mp"
    return msg

data = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
date_wise = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise_daily.csv')
state_data = data[['State',"Confirmed",'Recovered',"Deaths",'Active','Last_Updated_Time']]
#state_data = state_data[state_data['State']!='Total']
confirmed = date_wise[date_wise['Status']=='Confirmed']
confirmed = confirmed[confirmed['Date']=='30-Jul-20'] 
recovered = date_wise[date_wise['Status']=='Recovered']
recovered = recovered[recovered['Date']=='30-Jul-20']
dead = date_wise[date_wise['Status']=='Deceased']
dead = dead[dead['Date']=='30-Jul-20']

state_list = ['Total','Andhra Pradesh',"Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala",'Ladakh',"Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli and Daman and Diu","Laakshadweep","Delhi","Puducherry" ]
state_dict = {'TT':'Total','AP':'Andhra Pradesh','AN':'Arunachal Pradesh','AS':'Assam','BR':'Bihar','CT':'Chhattisgarh','GA':'Goa','GJ':'Gujarat','HR':'Haryana','HP':'Himachal Pradesh','JK':'Jammu and Kashmir','JH':'Jharkhand','KA':'Karnataka','KL':'Kerala','LA':'Ladakh','MP':'Madhya Pradesh','MH':'Maharashtra','MN':'Manipur','ML':'Meghalaya','MZ':'Mizoram','NL':'Nagaland','OR':'Odisha','PB':'Punjab','RJ':'Rajasthan','SK':'Sikkim','TN':'Tamil Nadu','TG':'Telangana','TR':'Tripura','UP':'Uttar Pradesh','UT':'Uttarakhand','WT':'West Bengal','AR':'Andaman and Nicobar Islands','CH':'Chandigarh','DN':'Dadra and Nagar Haveli and Daman and Diu','LD':'Lakshadweep','DL':'Delhi','PY':'Puducherry'}
state_code = ['TT','AP','AN','AS','BR','CT','GA','GJ','HR','HP','JK','JH','KA','KL','LA','MP','MH','MN','ML','MZ','NL','OR','PB','RJ','SK','TN','TG','TR','UP','UT','WT','AR','CH','DN','LD','DL','PY']

for i in range (len(state_list)):
    print(state_list[i] + "("+ state_code[i]+ ")")
print()
state = str(input('Please Enter the code of the state: '))


interval = 2
position = 1000,400
position2 = 1000,500
numbers={919876543210}


message= covid_status(state)


for i in numbers:
    url = 'https://wa.me/{}?text={}'.format(i, message)
    webbrowser.open(url)
    time.sleep(3)
    gui.click(position)
    time.sleep(3)
    gui.click(position2)
    time.sleep(10)
    gui.press('enter')
    time.sleep(2)
    gui.hotkey('ctrl','w')
    gui.click(position)
    time.sleep(interval)
