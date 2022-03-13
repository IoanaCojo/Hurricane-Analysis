class Hurricane:

    # names of hurricanes
    names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

    # months of hurricanes
    months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

    # years of hurricanes
    years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

    # maximum sustained winds (mph) of hurricanes
    max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

    # areas affected by each hurricane
    areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

    # damages (USD($)) of hurricanes
    damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

    # deaths for each hurricane
    deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

    # write your update damages function here:
    def update_damage(damages):
        new = []
        for case in damages:
            if case != 'Damages not recorded':
                if case[-1] == 'M':
                    new.append(float(case[:-1])*1000000)
                else:
                    new.append(float(case[:-1])*1000000000)
            else:
                new.append('Damages not recorded')
        return new
    new_damages = update_damage(damages)
    #print(new_damages)

    # print(len(names))
    # print(len(months))
    # print(len(years))
    # print(len(max_sustained_winds))
    # print(len(areas_affected))
    # print(len(new_damages))
    # print(len(deaths))
    # write your construct hurricane dictionary function here:
    hurricanes={}
    for i in range(len(names)):
        #print(i)
        #print(new_damages[i])
        hurricanes[names[i]] = {'Name':names[i],'Month':months[i],'Year':years[i],'Max sustained wind':max_sustained_winds[i], 'Areas Affected':areas_affected[i], 'Damage':new_damages[i], 'Deaths':deaths[i]}

    print(hurricanes)

    # write your construct hurricane by year dictionary function here:

    hurricaneByYear = {}
    for key, val in hurricanes.items():
        current_year = hurricanes[key]['Year']
        current_cane = hurricanes[key]
        #print(current_cane)
        #print(current_year)
        if current_year in hurricaneByYear:
            hurricaneByYear[current_year] =hurricaneByYear[current_year], current_cane
            print(current_cane)
        else:
            hurricaneByYear[current_year]=current_cane
    print(hurricaneByYear)


    # write your count affected areas function here:
    #times = 0
    danger_zone={}
    # for key in hurricanes.keys():
    #     upto = len(hurricanes[key]['Areas Affected'])
    #     for i in range(upto):
    #         city= hurricanes[key]['Areas Affected']
    #         if hurricanes[key]['Areas Affected'][i] in danger_zone == False:
    #             danger_zone[city]= 1
    #         else:
    #             danger_zone[city] += 1
    # print(danger_zone)

    for area in hurricanes.values():
        for city in area["Areas Affected"]:
            if city not in danger_zone:
                danger_zone[city] = 1
            else:
                danger_zone[city] = danger_zone[city] + 1
    print("My result: {}".format(danger_zone))

    # write your find most affected area function here:
    most_affected =''
    danger_val=0
    for key, val in danger_zone.items():
        if val > danger_val:
            danger_val = val
            most_affected = key
    print('the most affected area is {} - {} times'.format(most_affected, danger_val))


    # write your greatest number of deaths function here:
    max_deaths=0
    hurricane =''
    for hur, deaths in hurricanes.items():
        if deaths['Deaths']>max_deaths:
            max_deaths = deaths['Deaths']
            hurricane = hur
    print('The most distructive hurricane was {}, killing {} people'.format(hurricane, max_deaths))

    # write your catgeorize by mortality function here:
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    mortality_rate={}
    for hur, death in hurricanes.items():
        for rate, val in mortality_scale.items():
            if death['Deaths']< val:
                if rate in mortality_rate:
                    mortality_rate[rate].append(hur)
                else:
                    mortality_rate[rate] = [hur]
                #print(' Hurricane {} has a rating of {} on the mortality scale'.format(hur, rate))
                break
   # print(mortality_rate)


    # write your greatest damage function here:
    def gratest_damage(hurricanes):
        cost = 0
        na = 'a'
        for val in hurricanes.values():
            if val['Damage'] != 'Damages not recorded':
                if val['Damage'] > cost:
                    cost = val['Damage']
                    na = val['Name']
        return cost, na
    print(hurricanes)
    cost, hurr = gratest_damage(hurricanes)
    print('{} was the costliest hurricane - {}'.format(hurr, cost))

    # write your catgeorize by damage function here:
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}

    damage_rate={}
    for hur, damage in hurricanes.items():
        for rate, val in damage_scale.items():
            if (damage['Damage'] != 'Damages not recorded') and (damage['Damage']< val):
                if rate in damage_rate:
                    damage_rate[rate].append(hur)
                else:
                    damage_rate[rate] = [hur]
                break
    print(damage_rate)
