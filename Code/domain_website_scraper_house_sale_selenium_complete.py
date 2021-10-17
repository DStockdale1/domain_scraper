'''
trying selenium

need to fix bedroom >                                       done
fix batroomm not Showing                                    done
Parking spot is always 0 for some reason                    done
Fix bond having extra is additional info in post            done
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, SoupStrainer
from bs4 import BeautifulSoup, SoupStrainer
from selenium.webdriver.support.ui import WebDriverWait
import requests
import time
import re
import xlsxwriter
import os
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
import math
from selenium import webdriver
from time import gmtime
from time import strftime


def domain_scraper(domain_url,start, end):
    starttime = time.time()

    domain_url_final = str(domain_url)+'&page='
    url = domain_url_final+'1'#+str(page) # to find max houses
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, "html.parser")
    property_soup = str(soup.findAll("h1", {"data-testid":"summary"}))

    if 'Houses' in property_soup:
        num_of_properties = property_soup[property_soup.find("<strong>")+len("<strong>"):property_soup.find(" Houses")]
        print(num_of_properties, 'Houses')
        max_pages = math.ceil(int(num_of_properties)/20)
    elif 'Apartments' in property_soup:
        num_of_properties = property_soup[property_soup.find("<strong>")+len("<strong>"):property_soup.find(" Apartments")]
        max_pages = math.ceil(int(num_of_properties)/20)
        print(num_of_properties, " Apartments")

### edits taking place here
# if proprty url exists already
    try:
        if len(properties_url_list) > 0:
             # if already defined will work WHY DOESN"T IT WORK!!!!!!!!!!!!!
             print('list already exists')
        pass
    except:# list doesn't exists so create it
        print("list doesn't exists")
        properties_url_list = []

        for page in range(1,max_pages+1):
            url = domain_url_final+str(page)
            try:
                page = requests.get(url)
            except:
                print('no internet connection waiting 60s')
                time.sleep(60)
                try:
                    page = requests.get(url)
                    print('no internet connection waiting 60s')
                    time.sleep(60)
                except:
                    print('internet broke again')
                    break

            data = page.text
            soup = BeautifulSoup(data, "html.parser")
            property_soup = soup.findAll("link", {"itemprop":"url"})
            property_soup_str =str(property_soup).replace('<link href=',"")
            properties = property_soup_str.split('>')
            property = ([r.strip() for r in properties])

            for i in range(0,len(property)):
                property[i] = property[i].replace(' itemprop="url"/',"")
                property[i] = property[i].replace('[',"")
                property[i] = property[i].replace(']',"")
                property[i] = property[i].replace(", ","")
                property[i] = property[i].replace('"',"")

                if "New &amp" in property[i]:
                    continue

                if len(str(property[i])) == 0:
                    continue

                properties_url_list.append(property[i])

        print('number of property urls collected ', len(properties_url_list))
        print('time for collection of urls ', time.time()-starttime)

    #print(properties_url_list)
    '''
    properties_url_list = []

    if len(properties_url_list) == 0:
        print('list is empty collecting urls')

        properties_url_list = []

        for page in range(1,max_pages+1):
            url = domain_url_final+str(page)
            page = requests.get(url)
            data = page.text
            soup = BeautifulSoup(data, "html.parser")
            property_soup = soup.findAll("link", {"itemprop":"url"})
            property_soup_str =str(property_soup).replace('<link href=',"")
            properties = property_soup_str.split('>')
            property = ([r.strip() for r in properties])

            for i in range(0,len(property)):
                property[i] = property[i].replace(' itemprop="url"/',"")
                property[i] = property[i].replace('[',"")
                property[i] = property[i].replace(']',"")
                property[i] = property[i].replace(", ","")
                property[i] = property[i].replace('"',"")

                if "New &amp" in property[i]:
                    continue

                if len(str(property[i])) == 0:
                    continue

                properties_url_list.append(property[i])

        print('number of property urls collected ', len(properties_url_list))
        print('time for collection of urls ', time.time()-starttime)


    try: # should work if list is already collected
        properties_url_list[1]
        print('list already collected going straight to property info collection')
        pass
    except: # collect the list
          print('list is empty collecting urls')

          properties_url_list = []

          for page in range(1,max_pages+1):
              url = domain_url_final+str(page)
              page = requests.get(url)
              data = page.text
              soup = BeautifulSoup(data, "html.parser")
              property_soup = soup.findAll("link", {"itemprop":"url"})
              property_soup_str =str(property_soup).replace('<link href=',"")
              properties = property_soup_str.split('>')
              property = ([r.strip() for r in properties])

              for i in range(0,len(property)):
                  property[i] = property[i].replace(' itemprop="url"/',"")
                  property[i] = property[i].replace('[',"")
                  property[i] = property[i].replace(']',"")
                  property[i] = property[i].replace(", ","")
                  property[i] = property[i].replace('"',"")

                  if "New &amp" in property[i]:
                      continue

                  if len(str(property[i])) == 0:
                      continue

                  properties_url_list.append(property[i])

          print('number of property urls collected ', len(properties_url_list))
          print('time for collection of urls ', time.time()-starttime)
      #else:
         # print('properties_url_list already collected', len(properties_url_list) + ' already colleted')
         # pass
         '''

    property_information = []
    if  int(num_of_properties) > 1001:
        print('more than a 1000 properties, search limited to first 1000 due to limitation of domain website')
        num_of_properties = 1001

#############################################################################################################################
    start_time_property_analysis = time.time()
    print('number of properties', int(num_of_properties))

    if end =='max':
        end  = int(num_of_properties)-1
    i = 1
    for properties_url in range(start,end): #int(num_of_properties)-1
##
        if properties_url == math.floor((int(end)-int(start))*0.002):
            time_taken = time.time()-start_time_property_analysis
            time_to_finish = float(time_taken)/0.002
            print('2% completed in ', strftime("%H:%M:%S", gmtime(time_taken)))
            print('expected time to finish = ', strftime("%H:%M:%S", gmtime(time_to_finish)))

        #print('10% check ', math.floor((int(end)-int(start))*0.1))
        if properties_url == math.floor((int(end)-int(start))*0.1):
            time_taken = time.time()-start_time_property_analysis
            time_to_finish = float(time_taken)/0.1
            print('10% completed in ', time.time()-start_time_property_analysis)
            print('expected time to finish = ', int((time.time()-start_time_property_analysis))/0.1)

        #print('25% check ', math.floor((int(end)-int(start))*0.25))
        if properties_url == math.floor((int(end)-int(start))*0.25):
            time_taken = time.time()-start_time_property_analysis
            time_to_finish = float(time_taken)/0.25
            print('25% completed in ', time.time()-start_time_property_analysis)
            print('expected time to finish = ', int((time.time()-start_time_property_analysis))/0.25)

        if properties_url == math.floor((int(end)-int(start))*0.5):
            time_taken = time.time()-start_time_property_analysis
            time_to_finish = float(time_taken)/0.5
            print('50% completed in ', time.time()-start_time_property_analysis)
            print('expected time to finish = ', int((time.time()-start_time_property_analysis))/0.5)

        if properties_url == math.floor((int(end)-int(start))*0.75):
            time_taken = time.time()-start_time_property_analysis
            time_to_finish = float(time_taken)/0.75
            print('75% completed in ', time.time()-start_time_property_analysis)
            print('expected time to finish = ', int((time.time()-start_time_property_analysis))/0.75)

        if properties_url == math.floor((int(end)-int(start))*0.9):
            time_taken = time.time()-start_time_property_analysis
            time_to_finish = float(time_taken)/0.9
            print('90% completed in ', time.time()-start_time_property_analysis)
            print('expected time to finish = ', int((time.time()-start_time_property_analysis))/0.9)


        path_to_extension = "C:/Users/Declan/Desktop/1.30.2_4_ublock_origin_for_selenium"


        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument('load-extension=' + path_to_extension)
        driver = webdriver.Chrome(options=chrome_options, executable_path='C:/Users/Declan/Downloads/chromedriver_win32/chromedriver.exe')#''"C:/Users/Declan/Downloads/chromedriver_win32/chromedriver.exe")
        url = properties_url_list[properties_url]
        if str(url).startswith('https://www.domain.com.au/') == False:
            print("url isn't valid", url)
            continue
        else:
            a = 1

        if "New &amp" in url:
            continue

        try:
            driver.get(url)
        except:
            print('driver failed')
            time.sleep(60)
            try:
                print('trying driver again')
                driver.get(url)
            except:
                print('driver failed again')
                driver.quit()
                continue

        time.sleep(2.0)

        print('\n')

        try:
            driver.find_element_by_class_name('listing-details__description-button').click()
            #print('button 8th')
        except:
            a = 1
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[6]/div/div/div[4]/div[2]/button").click()
            #print('1st worked')
        except:
            a = 1

        try:
            driver.find_element_by_xpath('//*[@id="__domain_group/APP_ROOT"]/div[1]/div/div[5]/div/div/div[3]/div[2]/button').click()
            #print('2nd worked')
        except:
            a = 1

        try:
            driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[5]/div/div/div[4]/div[2]/button").click()
            #print('3rd worked')
        except:
            a = 1
        try:
            driver.find_element_by_xpath('//*[@id="property-features"]/button/span').click()
            #print('4th worked')
        except:
            a = 1

        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/button').click()
            #print('5th')
        except:
            a = 1

        try:
            driver.find_element_by_xpath('//*[@id="__domain_group/APP_ROOT"]/div[1]/div/div[5]/div/div/div[3]/div[2]/button').click()
            #print('6th')
        except:
            a = 1

        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/button').click()
            #print('7th')
        except:
            a = 1


        time.sleep(2.0)

        page_source = driver.page_source

        soup = BeautifulSoup(page_source,"html.parser")
        if "The requested URL was not found on the server" in str(soup):
            print('broken url')
            continue
        #print('looking for first time listed ', str(soup).encode('ascii', 'ignore').decode('ascii'))

        # looking first listed on domain_nav
        first_listed_test = str(soup).encode('ascii', 'ignore').decode('ascii')

        if 'First listed on' in first_listed_test:
            first_listed_test = first_listed_test[first_listed_test.find('First listed on ')+len('First listed on '):first_listed_test.find(', this house has')]
        else:
            first_listed_test = -1

        #####################
        #price
        #####################
        try:
            property_price_soup = str(soup.findAll("div", {"data-testid":"listing-details__summary-title"}))
            property_price_soup = property_price_soup.replace('[<div class="css-1texeil" data-testid="listing-details__summary-title">$',"")
            property_price = property_price_soup.replace('</div>]',"")
            property_price = property_price.replace('pw',"")
            property_price = property_price_soup.replace('$',"")
            property_price = property_price.replace('per week',"")
            property_price = property_price.replace('Per Week',"")
            property_price = property_price.replace('PER WEEK',"")
            property_price = property_price.replace('!!',"")
            property_price = property_price.replace('/',"")
            property_price = property_price.replace('From',"")
            property_price = property_price.replace('FROM',"")
            property_price = property_price.replace('weekly',"")
            property_price = property_price.replace('[<div class="css-1texeil" data-testid="listing-details__summary-title">',"")

            if 'auction' in str(property_price.lower()):
                property_price = '-1'
            if 'Auction' in str(property_price.lower()):
                property_price = '-1'

            property_price = property_price.lower()

            property_price = property_price.replace('contact agent',"")

            property_price = property_price.replace('auction - buyers guide on request',"")
            property_price = property_price.replace('auction',"")
            property_price = property_price.replace('auction',"")
            property_price = property_price.replace('on request',"")

            property_price = property_price.replace('<div>',"")
            property_price = property_price.replace('under offer',"")
            property_price = property_price.replace('<for sale >',"")
            property_price = property_price.replace('for sale.',"")
            property_price = property_price.replace('for sale',"")
            property_price = property_price.replace('price upon application',"")
            property_price = property_price.replace('buyers guide',"")
            property_price = property_price.replace("buyer's guide","")
            property_price = property_price.replace("buyer's guide","")
            property_price = property_price.replace(']',"")
            property_price = property_price.replace(' ',"")
            property_price = property_price.replace('=-buyersonrequest',"")
            property_price = property_price.replace(',',"") # removes commas should total alone

            property_price = property_price.replace('.00',"")
            property_price = property_price.replace('for sale.',"")
            property_price = property_price.replace('-',"")
            property_price = property_price.lower()
            property_price = property_price.replace('million',"")
            property_price = property_price.replace('guide',"")
            property_price = property_price.replace('m',"")
            property_price = property_price.replace('priceon',"")
            property_price = property_price.replace('sold',"")
            property_price = property_price.replace('price',"")
            property_price = property_price.replace('|',"")
            property_price = property_price.replace('withheld',"")
            property_price = property_price.replace('sold',"")

            if '.' in property_price:# and property_price.endswith('m'):
                property_price = property_price.replace('.',"")
                property_price = re.sub('\D', '', str(property_price))
                #property_price = property_price.replace('m',"")
                property_price = int(property_price)*1000000
                property_price = str(property_price)

            if len(str(property_price)) > 8:
                property_price = property_price[0:8] # this should get rid of the longer values is house price is over ten million

            if len(str(property_price)) == 0:
                property_price = '-1'

        except:
            property_price = '-1'


#######################################
        # looking for sold date
#######################################
        try:
            property_sold_date = str(soup.findAll("span", {"class":"css-h9g9i3"}))
            property_sold_date = property_sold_date.replace('<span class="css-h9g9i3" data-testid="listing-details__listing-tag">',"")
            property_sold_date = property_sold_date.replace('</span>',"")
            property_sold_date = property_sold_date.replace(']',"")
            property_sold_date = property_sold_date.replace('[',"")
            property_sold_date = property_sold_date.replace('Listing sold by advertiser ',"")
        except:
            property_sold_date = '-1'


        #####################
        # address
        ####################
        try:
            property_address_soup = str(soup.findAll("h1", {"class":"css-164r41r"}))
            property_address = property_address_soup.replace('[<h1 class="css-164r41r">',"").replace('</h1>]',"")
        except:
            property_address = '-1'
        ############################################
        ####bedrooms, bathrooms and parking spots ##
        ############################################
        try:
            property_rooms_soup_template =str(soup.findAll("span", {"data-testid":"property-features-text-container"}))
            property_rooms_soup = str(property_rooms_soup_template).encode('ascii','ignore')

            property_rooms_info = []

            property_rooms_soup_split = str(property_rooms_soup).split('data-testid="property-features-text-container">')

            try:
                bedrooms = property_rooms_soup_split[1][0:property_rooms_soup_split[1].find('<!-- -->')]
                if len(str(bedrooms)) == 0:
                    bedrooms = '0'
            except:
                bedrooms = '0'

            try:
                bathrooms = property_rooms_soup_split[2][0:property_rooms_soup_split[2].find('<!-- -->')]
                if len(str(bathrooms)) == 0:
                    bathrooms = '0'
            except:
                bathrooms = '0'

            try:
                parking_spots = property_rooms_soup_split[3][0:property_rooms_soup_split[3].find('<!-- -->')]
                if len(str(parking_spots)) == 0:
                    parking_spots = '0'
            except:
                parking_spots = '0'

            try:
                land_size = property_rooms_soup_split[4][0:property_rooms_soup_split[4].find('<!-- -->')]
                land_size = land_size.replace(',',"")
                land_size = land_size.replace('m',"")
                #print('try loop land size', land_size)
            except:
                land_size = '0'

            try:
                if int(land_size) <=25 and int(land_size) > 0:
                    #print('int')
                    land_size = '0'
            except:
                a = 1

            try:
                if float(land_size) <=25 and int(land_size) > 0:
                    #print('float')
                    land_size = '0'
            except:
                a = 1

            if '0ha' in str(land_size) or '1ha' in str(land_size) or '2ha' in str(land_size) or '3ha' in str(land_size) or '4ha' in str(land_size):
                #print('land size in hectares', land_size)
                land_size = str(land_size).replace('ha',"")
                try:
                    land_size = int(land_size)*10000
                except:
                    land_size = float(land_size)*10000

                # need to remove ha and find preiovus 6 digits
            if '5ha' in str(land_size) or '6ha' in str(land_size) or '7ha' in str(land_size) or '8ha' in str(land_size) or '9ha' in str(land_size):
                #print('land size in hectares', land_size)
                land_size = str(land_size).replace('ha',"")
                try:
                    land_size = int(land_size)*10000
                except:
                    land_size = float(land_size)*10000
                #land_size = int(land_size)*10000
        except:
            bedrooms = '-1'
            bathroms = '-1'
            parking_spots = '-1'
            land_size = '-1'

#############
### looking for property house type e.g. free standing, terrace ElementClickInterceptedException
#######################

        try:
            house_type = str(soup.findAll("span", {"class":"css-0"}))
            house_type = house_type.split('<span class="css-0">')
            suburb = house_type[4].replace('</span>,',"")
            house_type = house_type[5].replace('</span>,',"")

        except:
            suburb = '-1'
            house_type = '-1'
        #print('house_type', house_type)
        #print(house_type)
        #print('3rd', house_type[3])
        #print('4th', house_type[4])




    ######################################
    # looking for property description ###
    ######################################

        try:
            description_soup = soup.findAll("div", {"data-testid":"expander-wrapper"})
            description_soup = str(description_soup).encode('ascii','ignore')
            #print('description_soup 1' , description_soup)


            if 'Property type"' in str(description_soup):
                description_soup = str(description_soup)[str(description_soup).find('data-testid="listing-details__description-headline"')+len('data-testid="listing-details__description-headline"')-3:str(description_soup).find('Property type')]#-len('<p class="listing-details__description-property-type">Pr ')]
    # below is in it regardless, need to find out what terminates it
            elif '</p><div class="listing-details__description-key-features">' in str(description_soup):
                description_soup = str(description_soup)[str(description_soup).find('data-testid="listing-details__description-headline"')+len('data-testid="listing-details__description-headline"')-3:str(description_soup).find('</p><div class="listing-details__description-key-features">')]

            description_soup = str(description_soup).replace('</h4><p>'," ")
            description_soup = str(description_soup).replace('</p><p>'," ")
            description_soup = str(description_soup).replace('<br/>- '," ")
            description_soup = str(description_soup).replace('<br/>'," ")
            description_soup = str(description_soup).replace('br/>'," ")
            description_soup = str(description_soup).replace('</p><p class="listing-details__description-property-type">Pr'," ")
            description_soup = str(description_soup).replace('</p><p class="listing-details__description-property-type">'," ")
            description_soup = str(description_soup)[description_soup.find('>')+1::]

            if '</p>' in str(description_soup):
                #print('description_soup loop')
                #print(' find </p>position', str(description_soup).find('</p>'))
                #print('fucking test',  description_soup[::431])
                #description_soup = 'incomplete ' + str(description_soup)[0:str(description_soup).find('</p>')]
                description_soup = str(description_soup)[str(description_soup).rfind('>')+1::]
        except:
            description_soup = '-1'
###########
#works perfect if l click it manually
        #print('description_soup', description_soup)
        #print('description_soup final ', description_soup)


###############################
# checking to see if land size in description of not explicitly found earlier
#################################
        if land_size =='0':
            #print('searching desciption for land size')
            if 'm2 ' in description_soup:
                #print('m2 in desciption')
                description_soup_m2_search = description_soup[description_soup.find('m2 ')-10:description_soup.find('m2 ')]
                description_soup_m2_search = re.sub('\D', '', str(description_soup_m2_search))
                #print('description_soup_m2_search',description_soup_m2_search)
                land_size = description_soup_m2_search

            if 'sqm ' in description_soup:
                #print('sqm in desciption')
                description_soup_sqm_search = description_soup[description_soup.find('sqm ')-10:description_soup.find('sqm ')]
                description_soup_sqm_search = re.sub('\D', '', str(description_soup_sqm_search))
                #print('description_soup_sqm_search',description_soup_sqm_search)
                land_size = description_soup_sqm_search

            if 'acres ' in description_soup:
                #print('acres in desciption')
                description_soup_acres_search = description_soup[description_soup.find('acres ')-10:description_soup.find('acres ')]
                description_soup_acres_search = re.sub('\D', '', str(description_soup_acres_search))
                #print('description_soup_acres_search',description_soup_acres_search)
                try:
                    description_soup_acres_search = int(description_soup_acres_search)*4046.86
                    land_size = str(description_soup_acres_search)
                except:
                    ('find acres in description manually')
                    land_size = '0'
        #######################################
        #### Looking for Neighbour hood insights
        ##########################################
        insights= []

        try:
            neighbourhood_insights_soup = str(soup.findAll("div", {"class":"css-199ul8s"}))

            for neighbourhood_insights in range(1,5):
                #print('neighbourhood_insights_soup', neighbourhood_insights_soup)
                neighbourhood_insights_soup = neighbourhood_insights_soup[neighbourhood_insights_soup.find('min-width:')::]
                neighbourhood_insights_soup_append = neighbourhood_insights_soup[neighbourhood_insights_soup.find('>')+len('>'):neighbourhood_insights_soup.find('%</div>')]
                insights.append(neighbourhood_insights_soup_append) # works to this point
                neighbourhood_insights_soup = neighbourhood_insights_soup[neighbourhood_insights_soup.find('%</div>')::]

            ##########################
            # looking for long term residents
            ###########################

            long_term_residents = str(soup.findAll("div", {"data-testid":"text"}))
            long_term_residents = long_term_residents[long_term_residents.find('>')+1:long_term_residents.find('<!')]
            ##########################
            # looking for owner/renter
            ###########################
            owner_percent = str(soup.findAll("div", {"data-testid-hasleft":"has-left-colour"}))
            #print('owner_percent', owner_percent)
            owner_percent_value = owner_percent[owner_percent.find('style="width:')+len('style="width:'):owner_percent.find('%"></div>,')]

            #print('Owner percent', owner_percent_value)
            owner_percent_value = owner_percent_value.replace('%"></div>',"")
            owner_percent_value = owner_percent_value.replace('%',"")
            try:
                Renter_percent = 100-int(owner_percent_value)
            except:
                #print('manual')
                Renter_percent = '-1'
            #print('Renter percent', Renter_percent)

            family_percent = owner_percent[owner_percent.find('%"></div>,')+len('%"></div>,')::]
            family_percent_value = family_percent[family_percent.find('style="width:')+len('style="width:'):family_percent.find('%"></div>,')]
            #print('family_percent_value 1', family_percent_value)
            family_percent_value = family_percent_value.replace('%"></div>',"")

            try:
                single_percent_value = 100-int(family_percent_value)
            except:
                #print('manual')
                single_percent_value = '-1'
            #print('single_percent_value', single_percent_value)
            #print('single_percent_value', single_percent_value)

            ##################
            ## looking for demographics
            ###################
            population = str(soup.findAll("div", {"data-testid":"suburb-insights__data-point-value"}))
            average_age = population[population.rfind('suburb-insights__data-point-value">')+len('suburb-insights__data-point-value">')::].replace('</div>]',"")
            #print('Average age', average_age)
            population = population[0:population.rfind('data-testid="suburb-insights__data-point-value')]
            population = population[population.rfind('data-testid="suburb-insights__data-point-value')+len('data-testid="suburb-insights__data-point-value')+2:population.rfind('</div>,')]
            #print('Population', population)

            if len(average_age) == 0:
                average_age = '-1'
            if len(population) == 0:
                population = '-1'
        except:
            population = '-1'
            average_age = '-1'
            single_percent_value = '-1'
            family_percent_value = -1
            Renter_percent = '-1'
            owner_percent_value = '-1'
            long_term_residents = '-1'

        print(i, ' price', property_price, 'address', property_address, 'bedrooms', bedrooms, 'bathrooms', bathrooms, 'parking_spots', parking_spots, 'land_size', land_size)
        i = i+1
        property_information.append({'Url' : url,
                                    'Price' : property_price,
                                    'Selling date' : property_sold_date,
                                    'Address' : property_address,
                                    "Suburb" : suburb,
                                    'House Type' : house_type,
                                    'Bedrooms' : bedrooms,
                                    "Bathrooms" : bathrooms,
                                    "Parking spots" : parking_spots,
                                    "Land size" : land_size,
                                    "Description" : description_soup,
                                    "Under 20" : insights[0],
                                    "20 - 39" : insights[1],
                                    "40 - 59" : insights[2],
                                    "60+" : insights[3],
                                    "Long term residents" : long_term_residents,
                                    "Owner percent": owner_percent_value,
                                    "Renter percent" : Renter_percent,
                                    "Family percent" : family_percent_value,
                                    "Single percent" : single_percent_value,
                                    "Average age" : average_age,
                                    "First Listed" : first_listed_test,
                                    "Population" : population})



        driver.quit()


    return pd.DataFrame(property_information)
    #print(property_information)
