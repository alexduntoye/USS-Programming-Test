import os
import pandas as pd


def cv_data(rootdir):
    extension = '.csv'
    dates_of_interest = {}  # a dictionary that we will be using in future

    for subdir, dirs, files in os.walk(rootdir):
        key = subdir[-9:]
        dates_of_interest.setdefault(key, [])
        for file in files:
            if file.endswith(extension):
                dates_of_interest[key].append(file)
                for key in dates_of_interest:
                    fund_df = pd.DataFrame()
                    for filename in dates_of_interest[key]:
                        fund_df = fund_df.append(pd.read_csv(rootdir + '/' + key + '/' +
                                                             filename))  # iterate over every filename for specific key in dictionary and appending it to fund_df
                        fund_df['Valuation Date'] = filename[17:25]
                        fund_df = fund_df[['Valuation Date', 'Fund', 'Allocation']]
                fund_df.to_csv("combined_csv.csv", index=False, mode='a')
    # The next section is to sort and clean the data
    filtered_df = pd.read_csv('combined_csv.csv').drop_duplicates(keep="first")
    filtered_df.drop(index=filtered_df.index[-1], axis=0, inplace=True)
    filtered_df.sort_values(by=['Valuation Date', 'Fund'], inplace=True)
    os.remove('combined_csv.csv')
    filtered_df.to_csv("combined_csv.csv", index=False, header=True, mode='a') # The user can rename the resulting csv file


# Enter the root directory here, i.e. '/..../Fund Allocations'
cv_data(
    '/Users/alexduntoye/Library/Mobile Documents/com~apple~CloudDocs/CV-Interviews and Cover Letter/USS/Latest Exercise/Problem 1/Fund Allocations')
