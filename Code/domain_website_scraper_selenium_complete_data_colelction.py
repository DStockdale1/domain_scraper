#import glassdoor_scraper_cloned as gs
import pandas as pd
import domain_website_scraper_house_sale_selenium_complete as domain_scraper
import time
import os
import os.path

os.chdir('C:/Users/Declan/.atom')

## northern beaches area
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_northern_beaches_sold_description_part_4.csv"):
    a = 1
else:
    print('northern_beaches')
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_northern_beaches_sold_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_northern_beaches_sold_description_part_1')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/northern-beaches-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_northern_beaches_sold_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_northern_beaches_sold_description_part_2')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/northern-beaches-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_northern_beaches_sold_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_northern_beaches_sold_description_part_3')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/northern-beaches-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_northern_beaches_sold_description_part_4.csv"):
        pass
    else:
        start = 751
        end  =  'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_northern_beaches_sold_description_part_4')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/northern-beaches-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

## Eastern Suburbs area
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_eastern_suburbs_sold_description_part_4.csv"):
    a = 1
else:
    print('eastern_suburbs')
    url = 'https://www.domain.com.au/sold-listings/eastern-suburbs-nsw/house/?excludepricewithheld=1&sort=solddate-desc'
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_eastern_suburbs_sold_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_eastern_suburbs_sold_description_part_1')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_eastern_suburbs_sold_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_eastern_suburbs_sold_description_part_2')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_eastern_suburbs_sold_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_eastern_suburbs_sold_description_part_3')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_eastern_suburbs_sold_description_part_4.csv"):
        pass
    else:
        start = 751
        end  =  'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_eastern_suburbs_sold_description_part_4')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

## Surry hills
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_surry_hills_area_sold_description_part_4.csv"):
    a = 1
    ##a = 1
else:
    print('surry_hills_area')
    url = 'https://www.domain.com.au/sold-listings/surry-hills-nsw-2010/house/?excludepricewithheld=1&sort=solddate-desc'
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_surry_hills_area_sold_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_surry_hills_area_sold_description_part_1')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_surry_hills_area_sold_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_surry_hills_area_sold_description_part_2')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_surry_hills_area_sold_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_surry_hills_area_sold_description_part_3')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_surry_hills_area_sold_description_part_4.csv"):
        pass
    else:
        start = 751
        end  =  'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_surry_hills_area_sold_description_part_4')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

## inner west
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_inner_west_area_sold_description_part_4.csv"):
    a = 1
    ##a = 1
else:
    print('inner_west_area')
    url = 'https://www.domain.com.au/sold-listings/inner-west-nsw/house/?excludepricewithheld=1&sort=solddate-desc'
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_inner_west_area_sold_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_inner_west_area_sold_description_part_1')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_inner_west_area_sold_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_inner_west_area_sold_description_part_2')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_inner_west_area_sold_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_inner_west_area_sold_description_part_3')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_inner_west_area_sold_description_part_4.csv"):
        pass
    else:
        start = 751
        end  =  'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_inner_west_area_sold_description_part_4')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

## parramatta area
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_parramatta_area_sold_description_part_4.csv"):
    a = 1
    ##a = 1
else:
    print('parramatta_area')
    url = 'https://www.domain.com.au/sold-listings/parramatta-nsw/house/?excludepricewithheld=1&sort=solddate-desc'
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_parramatta_area_sold_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_parramatta_area_sold_description_part_1')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_parramatta_area_sold_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_parramatta_area_sold_description_part_2')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_parramatta_area_sold_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_parramatta_area_sold_description_part_3')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_parramatta_area_sold_description_part_4.csv"):
        pass
    else:
        start = 751
        end  =  'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_parramatta_area_sold_description_part_4')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

## western sydney
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_western_sydney_area_sold_description_part_4.csv"):
    a = 1
    ##a = 1
else:
    print('western_sydney_area')
    url = 'https://www.domain.com.au/sold-listings/western-sydney-nsw/house/?excludepricewithheld=1&sort=solddate-desc'
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_western_sydney_area_sold_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_western_sydney_area_sold_description_part_1')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_western_sydney_area_sold_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_western_sydney_area_sold_description_part_2')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_western_sydney_area_sold_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_western_sydney_area_sold_description_part_3')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_western_sydney_area_sold_description_part_4.csv"):
        pass
    else:
        start = 751
        end  =  'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_western_sydney_area_sold_description_part_4')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

## canterbury canterbry_bankstown_area
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_canterbry_bankstown_area_sold_description_part_4.csv"):
    a = 1
    ##a = 1
else:
    print('canterbry_bankstown_area')
    url = 'https://www.domain.com.au/sold-listings/canterbury-bankstown-nsw/house/?excludepricewithheld=1&sort=solddate-desc'
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_canterbry_bankstown_area_sold_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_canterbry_bankstown_area_sold_description_part_1')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_canterbry_bankstown_area_sold_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_canterbry_bankstown_area_sold_description_part_2')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_canterbry_bankstown_area_sold_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_canterbry_bankstown_area_sold_description_part_3')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_canterbry_bankstown_area_sold_description_part_4.csv"):
        pass
    else:
        start = 751
        end  =  'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_canterbry_bankstown_area_sold_description_part_4')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

## blue mountains
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_blue_mountains_area_sold_description_part_4.csv"):
    a = 1
    ##a = 1
else:
    print('blue_mountains_area')
    url = 'https://www.domain.com.au/sold-listings/blue-mountains-and-surrounds-nsw/house/?excludepricewithheld=1&sort=solddate-desc'
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_blue_mountains_area_sold_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_blue_mountains_area_sold_description_part_1')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_blue_mountains_area_sold_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_blue_mountains_area_sold_description_part_2')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_blue_mountains_area_sold_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_blue_mountains_area_sold_description_part_3')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_blue_mountains_area_sold_description_part_4.csv"):
        pass
    else:
        start = 751
        end  =  'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_blue_mountains_area_sold_description_part_4')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)
'''
## north shore upper
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_north_shore_upper_sold_description_part_4.csv"):
    a = 1
else:
    print('north_shore_upper')
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_north_shore_upper_sold_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_north_shore_upper_sold_description_part_1.csv')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/north-shore-upper-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_north_shore_upper_sold_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_north_shore_upper_sold_description_part_2.csv')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/north-shore-upper-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_north_shore_upper_sold_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_north_shore_upper_sold_description_part_3.csv')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/north-shore-upper-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_north_shore_upper_sold_description_part_4.csv"):
        pass
    else:
        start = 751
        end  = 'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_north_shore_upper_sold_description_part_4.csv')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/north-shore-upper-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)
'''
'''
## north shore lower
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_north_shore_lower_sold_description_part_4.csv"):
    a = 1
else:
    print('north_shore_lower')
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_north_shore_lower_sold_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_north_shore_lower_sold_description_part_1.csv')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/north-shore-lower-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_north_shore_lower_sold_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_north_shore_lower_sold_description_part_2.csv')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/north-shore-lower-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_north_shore_lower_sold_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_north_shore_lower_sold_description_part_3.csv')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/north-shore-lower-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_north_shore_lower_sold_description_part_4.csv"):
        pass
    else:
        start = 751
        end  = 'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_north_shore_lower_sold_description_part_4.csv')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/north-shore-lower-nsw/house/?excludepricewithheld=1&ssubs=0&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)
'''

if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_shoalhaven_area_description_part_4.csv"):
    a = 1
else:#$shoalhaven_area
    print('shoalhaven_area')
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_shoalhaven_area_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_shoalhaven_area_description_part_1')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/shoalhaven-nsw/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_shoalhaven_area_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_shoalhaven_area_description_part_2')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/shoalhaven-nsw/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_shoalhaven_area_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_shoalhaven_area_description_part_3')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/shoalhaven-nsw/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_shoalhaven_area_description_part_4.csv"):
        pass
    else:
        start = 751
        end  = 'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_shoalhaven_area_description_part_4')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/shoalhaven-nsw/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)


## ryde area
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_ryde_surrounding_suburbs_description_part_4.csv"):
    a = 1
else:#$ryde_surrounding_suburbs
    print('ryde_surrounding')
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_ryde_surrounding_suburbs_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_ryde_surrounding_suburbs_description_part_1')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/ryde-nsw-2112/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_ryde_surrounding_suburbs_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_ryde_surrounding_suburbs_description_part_2')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/ryde-nsw-2112/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_ryde_surrounding_suburbs_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_ryde_surrounding_suburbs_description_part_3')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/ryde-nsw-2112/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_ryde_surrounding_suburbs_description_part_4.csv"):
        pass
    else:
        start = 751
        end  = 'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_ryde_surrounding_suburbs_description_part_4')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/ryde-nsw-2112/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

## sutherland area
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_sutherland_area_description_part_4.csv"):
    a = 1
else:
    print('sutherland_area')
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_sutherland_area_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_sutherland_area_description_part_1')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/sutherland-nsw/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_sutherland_area_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_sutherland_area_description_part_2')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/sutherland-nsw/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_sutherland_area_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_sutherland_area_description_part_3')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/sutherland-nsw/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_sutherland_area_description_part_4.csv"):
        pass
    else:
        start = 751
        end  = 'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_sutherland_area_description_part_4')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/sutherland-nsw/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

##  Strathfield
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_strathfield_area_area_sold_description_part_4.csv"):
    a = 1
    ##a = 1
else:
    print('strathfield_area_area')
    url = 'https://www.domain.com.au/sold-listings/strathfield-nsw-2135/house/?excludepricewithheld=1&sort=solddate-desc'
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_strathfield_area_area_sold_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_strathfield_area_area_sold_description_part_1')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_strathfield_area_area_sold_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_strathfield_area_area_sold_description_part_2')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_strathfield_area_area_sold_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_strathfield_area_area_sold_description_part_3')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_strathfield_area_area_sold_description_part_4.csv"):
        pass
    else:
        start = 751
        end  =  'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_strathfield_area_area_sold_description_part_4')
        df = domain_scraper.domain_scraper(url, start, end)
        df.to_csv(file_name + '.csv', index = False)

## nowra area
if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_nowra_surrounding_suburbs_description_part_4.csv"):
    a = 1
else:#$nowra_surrounding_suburbs
    print('ryde_surrounding')
    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_nowra_surrounding_suburbs_description_part_1.csv"):
        pass
    else:
        start = 0
        end  = 250
        file_name = ('domain_house_13_10_nowra_surrounding_suburbs_description_part_1')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/nowra-nsw-2541/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_nowra_surrounding_suburbs_description_part_2.csv"):
        pass
    else:
        start = 251
        end  = 500
        file_name = ('domain_house_13_10_nowra_surrounding_suburbs_description_part_2')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/nowra-nsw-2541/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_nowra_surrounding_suburbs_description_part_3.csv"):
        pass
    else:
        start = 501
        end  = 750
        file_name = ('domain_house_13_10_nowra_surrounding_suburbs_description_part_3')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/nowra-nsw-2541/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)

    if os.path.exists("C:/Users/Declan/.atom/domain_house_13_10_nowra_surrounding_suburbs_description_part_4.csv"):
        pass
    else:
        start = 751
        end  = 'max'#int(num_of_properties)-1
        file_name = ('domain_house_13_10_nowra_surrounding_suburbs_description_part_4')
        df = domain_scraper.domain_scraper('https://www.domain.com.au/sold-listings/nowra-nsw-2541/house/?excludepricewithheld=1&sort=solddate-desc', start, end)
        df.to_csv(file_name + '.csv', index = False)
