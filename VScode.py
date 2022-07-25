#In the spirit of overcommunicating, there are a great deal of commentend code in this file. The reason for that varies but quite a bit of the files are in a non-ideal format. 
#The current sprint involves standing up each phase of the project and making sure that the code is in a good state. Then integrating in CI/CD as new pieces are improved.

#Importing the necessary packages for data science
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
from sklearn import linear_model
#from tensorflow import keras
from scipy import linalg, optimize
from matplotlib import pyplot as plt
#import xlwings as xw

#This makes sure that all columns are displayed 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)


#Assigning the data to a variable
Boss13 = pd.read_csv(r'C:\Users\Owner\Summit Data\summitmaster\BOSS Registration\2013studentReport.csv')
Boss14 = pd.read_csv(r'C:\Users\Owner\Summit Data\summitmaster\BOSS Registration\2014studentReport.csv')
Boss15 = pd.read_csv(r'C:\Users\Owner\Summit Data\summitmaster\BOSS Registration\2015studentReport.csv')
Boss16 = pd.read_csv(r'C:\Users\Owner\Summit Data\summitmaster\BOSS Registration\2016studentReport.csv')
Boss17 = pd.read_csv(r'C:\Users\Owner\Summit Data\summitmaster\BOSS Registration\2017studentReport.csv', encoding= 'unicode_escape')
Boss18 = pd.read_csv(r'C:\Users\Owner\Summit Data\summitmaster\BOSS Registration\2018studentReport.csv', encoding= 'unicode_escape')
Boss19 = pd.read_csv(r'C:\Users\Owner\Summit Data\summitmaster\BOSS Registration\2019studentReport.csv', encoding= 'unicode_escape')
Boss20 = pd.read_csv(r'C:\Users\Owner\Summit Data\summitmaster\BOSS Registration\2020studentReport.csv', encoding= 'unicode_escape')
Boss21 = pd.read_csv(r'C:\Users\Owner\Summit Data\summitmaster\BOSS Registration\2021studentReport.csv', encoding= 'unicode_escape')

#Bronto "CSV" was manually encoded on in an excel table improperly, will need to be corrected at the source level prior to import
#Bronto =  pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\Bronto Emails\BrontoContacts_FullAlumniList.csv')

#Jot
#All data from folder available but starting with the first two as they are the most relevant
Jot14 = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\2014 Adult Conference.xlsx')
Jot16AC = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\2016 Adult Conference.xlsx')
#Jot16SA = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\2016 Staff Applications.xlsx')
#Jot17SA = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\2017 Staff Applications.xlsx')
#Jot18SA = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\2018 Staff Applications.xlsx')
#Jot19SA = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\2019 Staff Applications.xlsx')
#Jot20SA = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\2020 Staff Applications.xlsx')
#Jot21SA = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\2021 Staff Applications.xlsx')
#JotACU = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\Alumni_Contact_Update2022-03-15_21_41_43.xlsx')
#JotJFC = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\JotFormContactUpdatesOct19.xlsx')
#JotRES22 = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\RE_SOURCE_Email_Sign_Up2022-03-15_21_42_20.xlsx')
#JotRES19 = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\RESOURCE Email Signups Oct19.xlsx')
#JotSTA = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\JotForm\SummitU Teachers and Administrators.xlsx')

AlumNM = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\Alumni Program\Alumni Network Master.xlsx')
AlumM = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\Alumni Program\AlumniMaster.xlsx')

NetIA = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\NetSuite\NS Institute Attendees (Semester Oxford).xlsx')
NetSC = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\NetSuite\NS Student Conference Attendees.xlsx')

WilCTD = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\Wilson Bennet List\CAMPAIGN_TO_DATE_May-12-2017_AllSegments_ProspectAllDataChanges (6).xlsx')
WilBC = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\Wilson Bennet List\WILSON_BENNET_CAMPAIGN_TO_DATE_May-12-2017_AllSegments_WrongNumbers (4).xls')

#UtX12 = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\UTX College Credit Students\UTX College Credit(2020-06-12) Internal Copy.xlsx')
#UtX13 = pd.read_excel(r'C:\Users\Owner\Summit Data\summitmaster\UTX College Credit Students\UTX_College_Credit2022-04-06_13_24_02.xlsx')



#Merging the dataframes
#Boss merge
BigBoss = [Boss13,Boss14,Boss15,Boss16,Boss17,Boss18,Boss19,Boss20,Boss21]
BigBoss1= pd.concat(BigBoss)

#print(BigBoss1)

#Jot merge

BigJot = [Jot14, Jot16AC]
BigJot1= Jot14[["First Name", "Last Name", "E-mail"]].merge(Jot16AC[["First Name", "Last Name", "E-mail"]], on= "E-mail", how = "left")
BigJot1.to_excel("Jotresults.xlsx", index = False)

#print(BigJot1)

#Alumni merge


BigAlum = [AlumM, AlumNM]
BigAlum1= AlumM[["FirstName", "LastName", "ProspectID"]].merge(AlumNM[["FirstName", "LastName", "ProspectID"]], on= "ProspectID", how = "left")
BigAlum1.to_excel("Alumresults.xlsx", index = False)

#print(BigAlum1)

#Netsuite merge *(Need to resolve issue where all parameters outside of email not showing up)

#BigNet = [NetIA, NetSC]
#BigNet1= AlumM[["Internal ID", "Email", "Address 1"]].merge(AlumNM[["Internal ID", "Email", "Address 1"]], on= "Email", how = "left")
#BigNet1.to_excel("Netresults.xlsx", index = False)

#print(BigNet1)


##Data Munging of merged data frames##

#Summary of BigBoss1
#print(BigBoss1.isnull().sum())


BigBoss1.drop_duplicates()
BigBoss1.fillna(0, inplace = True)
#print(BigBoss1.head())

#Summary of BigJot1
#print(BigJot1.isnull().sum())

BigJot1.drop_duplicates()
BigJot1.fillna(0, inplace = True)
#print(BigJot1.head())


#Summary of BigAlum1
#print(BigAlum1.isnull().sum())

BigAlum1.drop_duplicates()
BigAlum1.fillna(0, inplace = True)
#print(BigAlum1.head())


#Summary of BigNet1
#print(BigNet1.isnull().sum())

#BigNet1.drop_duplicates()
#BigNet1.fillna(0, inplace = True)
#print(BigNet1.head())

#Data Aggregation and Labeling

#BigAlum1.groupby(["FirstName", ""]).count()
BigBoss1.groupby(["firstname", "session year"])[["session","location"]].count()
#BigJot1.groupby(["First Name", "Last Name"]).count()

print(BigBoss1.groupby(["firstname", "session year"])[["session","location"]].count())

BigBoss1.to_excel(r'C:\Users\Owner\Summit Data\SummitMaster\BossforCRM.xlsx', index = False)
