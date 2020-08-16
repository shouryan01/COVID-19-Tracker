import datetime
# yesterday's date
yesterday = world_confirmed.columns[-1]

def daily(n_top=10):
    # compute daily values for the n_top countries
    sets_grouped_daily = [df.sort_values(by=yesterday, ascending=False).iloc[:n_top, 2:].diff(axis=1).T 
                          for df in sets_grouped]
    
    return sets_grouped_daily

roll = 7

def rolling(n_since=100, roll=roll):

    # transform to rolling average
    dFs = daily()
    
    sets_grouped_daily_top_rolled = []
    for i in range (3): # Transform each dataset at a time
        dF = dFs[i] 
        top_countries = dF.columns
        # get the rolling mean
        dF = dF.rolling(roll).mean()
        # for each column in a DF, get rows >= n_since and reset index
        since = [pd.DataFrame( dF[i][dF[i] >= n_since].reset_index(drop=True) ) for i in top_countries]
        # concatenate the columns
        sets_grouped_daily_top_rolled.append(pd.concat(since, axis=1, join='outer'))

    return sets_grouped_daily_top_rolled