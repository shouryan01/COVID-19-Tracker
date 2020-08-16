import pandas as pd;

# Load Data
WORLD_CONFIRMED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
WORLD_DEATHS_URL    = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
WORLD_RECOVERED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

world_confirmed     = pd.read_csv(WORLD_CONFIRMED_URL)
world_deaths        = pd.read_csv(WORLD_DEATHS_URL)
world_recovered     = pd.read_csv(WORLD_RECOVERED_URL)

sets = [world_confirmed, world_deaths, world_recovered]

# Rename Country/Region and Province/State, and replace NaN's for '' 
for i in range(3):
    sets[i].rename(columns={'Country/Region':'Country', 'Province/State':'State'}, inplace=True)
    sets[i][['State']] = sets[i][['State']].fillna('')
    sets[i].fillna(0, inplace=True)
   
# Group States and sum
sets_grouped = []
cases = ['confirmed cases', 'deaths', 'recovered cases']
for i in range(3):
    sets_grouped.append(sets[i].groupby('Country').sum())