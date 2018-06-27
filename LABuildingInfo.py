# need pip install selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# read csv file
f = open('APN.csv')
lines = f.readlines()
f.close()

# need chromedriver.exe installed in C:
chrome = webdriver.Chrome('/Users/rover/Downloads/chromedriver')

chrome.get("http://zimas.lacity.org/")

donot_btn = chrome.find_element_by_xpath('//*[@id="chekbox"]')
donot_btn.click()

accept_btn = chrome.find_element_by_xpath('//*[@id="btn"]')
accept_btn.click()

for line in lines[1:]:

    apn_value = line.split(',')[0].strip()

    time.sleep(1)

    APN_btn = chrome.find_element_by_xpath('//*[@id="tdSearchBodyAPN"]/a')
    APN_btn.click()

    # lat_value = line.split(',')[0].strip()
    # long_value = line.split(',')[1].strip()

    # housenumber_value = line.split(',')[2].strip()
    # streetname_value = line.split(',')[3].strip()

    try:
        # wait for permit information to show up
        exist = WebDriverWait(chrome, 1).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="txtAPN"]'))
        )

        apn_box = chrome.find_element_by_xpath('//*[@id="txtAPN"]')
        apn_box.send_keys(apn_value)

        submit_btn = chrome.find_element_by_xpath('//*[@id="btnSearchGo"]')
        submit_btn.click()

        # wait for information to show up
        exist = WebDriverWait(chrome, 1).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="divTab1"]/table/tbody/tr[1]/td[2]'))
        )


        num_rows = len(chrome.find_elements_by_xpath('//*[@id="divTab1"]/table/tbody/tr'))        
        for i in range(1, num_rows):
            
            if 'Lot/Parcel Area (Calculated) ' in chrome.find_element_by_xpath('//*[@id="divTab1"]/table/tbody/tr[%d]/td[1]'%i).text:
                LotArea = chrome.find_element_by_xpath('//*[@id="divTab1"]/table/tbody/tr[%d]/td[2]'%i)

                f = open('lotarea.csv', 'a')
                f.write('%s,%s\n'%(apn_value, LotArea.text))
                f.close()
                print ('%s,%s\n'%(apn_value, LotArea.text))
                break
        Address_btn = chrome.find_element_by_xpath('//*[@id="divDataTabs"]/table/tbody/tr[1]/td/a')
        Address_btn.click()


        Jurisdictional_btn = chrome.find_element_by_xpath('//*[@id="divDataTabs"]/table/tbody/tr[3]/td/a')
        Jurisdictional_btn.click()
        num_rows = len(chrome.find_elements_by_xpath('//*[@id="divTab2"]/table/tbody/tr'))  

        for i in range(1, num_rows):

            if 'Census Tract # ' in chrome.find_element_by_xpath('//*[@id="divTab2"]/table/tbody/tr[%d]/td[1]'%i).text:
                CensusTract_field = chrome.find_element_by_xpath('//*[@id="divTab2"]/table/tbody/tr[%d]/td[2]'%i)

                f = open('censustract.csv', 'a')
                f.write('%s,%s\n'%(apn_value, CensusTract_field.text))
                f.close()
                print ('%s,%s\n'%(apn_value, CensusTract_field.text))
                break
        Jurisdictional_btn.click()


        Planning_btn = chrome.find_element_by_xpath('//*[@id="divDataTabs"]/table/tbody/tr[5]/td/a')
        Planning_btn.click()
        num_rows = len(chrome.find_elements_by_xpath('//*[@id="divTab3"]/table/tbody/tr'))

        for i in range(1,num_rows):

            if 'General Plan Land Use' in chrome.find_element_by_xpath('//*[@id="divTab3"]/table/tbody/tr[%d]/td[1]'%i).text:
                LandUse = chrome.find_element_by_xpath('//*[@id="divTab3"]/table/tbody/tr[%d]/td[2]'%i)

                f = open('landuse.csv', 'a')
                f.write('%s,%s\n'%(apn_value, LandUse.text))
                f.close()
                print ('%s,%s\n'%(apn_value, LandUse.text))
                break
        Planning_btn.click()

 

        assessor_btn = chrome.find_element_by_xpath('//*[@id="divDataTabs"]/table/tbody/tr[7]/td/a')
        assessor_btn.click()

        num_rows = len(chrome.find_elements_by_xpath('//*[@id="divTab4"]/table/tbody/tr'))

        for i in range(1, num_rows):

            if 'Year Built' in chrome.find_element_by_xpath('//*[@id="divTab4"]/table/tbody/tr[%d]/td[1]'%i).text:
                yearbuilt_field = chrome.find_element_by_xpath('//*[@id="divTab4"]/table/tbody/tr[%d]/td[2]'%i)

                f = open('yearbuilt.csv', 'a')
                f.write('%s,%s\n'%(apn_value, yearbuilt_field.text))
                f.close()
                print ('%s,%s\n'%(apn_value, yearbuilt_field.text))
                break

        for i in range(1, num_rows):
            
            if 'Assessed Land Val. ' in chrome.find_element_by_xpath('//*[@id="divTab4"]/table/tbody/tr[%d]/td[1]'%i).text:
                AssessedLandVal = chrome.find_element_by_xpath('//*[@id="divTab4"]/table/tbody/tr[%d]/td[2]'%i)

                f = open('landvalue.csv', 'a')
                f.write('%s,%s\n'%(apn_value, AssessedLandVal.text))
                f.close()
                print ('%s,%s\n'%(apn_value, AssessedLandVal.text))
                break

        for i in range(1,num_rows):
                
            if 'Assessed Improvement Val.' in chrome.find_element_by_xpath('//*[@id="divTab4"]/table/tbody/tr[%d]/td[1]'%i).text:
                AssessedImprovementVal = chrome.find_element_by_xpath('//*[@id="divTab4"]/table/tbody/tr[%d]/td[2]'%i)

                f = open('improvementvalue.csv', 'a')
                f.write('%s,%s\n'%(apn_value, AssessedImprovementVal.text))
                f.close()
                print ('%s,%s\n'%(apn_value, AssessedImprovementVal.text))
                break



    except:
        # raise
        f = open('yearbuilt.csv', 'a')
        f.write('%s,%s\n'%(apn_value, 'Time Out'))
        f.close()
        print ('%s,%s\n'%(apn_value, 'Time Out'))

    chrome.get("http://zimas.lacity.org/")


# //*[@id="divTab4"]/table/tbody/tr[30]/td[1]
# //*[@id="divTab4"]/table/tbody/tr[30]/td[2]



# chrome.close()

