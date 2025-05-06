# kumu-connections-tric-dt.py
# This script reads in an xlsx file of stakeholder metadata and prepares a file for kumu mapping.

# # Set-up in terminal
# Adapted from [TTW local build step-by-step guide](https://the-turing-way.netlify.app/community-handbook/local-build.html?highlight=conda%20env) to use a conda environment
# 1. [install miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
# 2. `conda init`
# 3. `curl https://git.fmrib.ox.ac.uk/paulmc/grad_course_2019_python_intro/raw/master/env.yml` > kumu-env.yml
# 4. `conda env create -f kumu-env.yml`
# 5. `conda activate kumu_env`
# 6. in vs code, set python interpreter to kumu_env before running debugging (see [guide here](https://code.visualstudio.com/docs/python/environments#_using-the-create-environment-command))




# library of functions for checking, makeing, renaming files etc.
import os as os
import subprocess
# subprocess.run('source activate the-turing-way', shell=True)
# subprocess.run('pwd', shell=True)
# subprocess.run('pip install -r requirements.txt',shell=True)
# library for handelling data read in from the xlsx file
import pandas as pd
import numpy as np
import csv
from anonymizedf.anonymizedf import anonymize
import time
import json

# where all our data is
dataRoot = '/Users/cgouldvanpraag/Library/CloudStorage/OneDrive-TheAlanTuringInstitute/open-research-map/'

download_date = '20241018'
filename_prefix = 'stakeholder-list-open-research-map-MASTER-'
filename_extension = '.csv'

filename_read_orgs = filename_prefix+'orgs-'+download_date+filename_extension
filename_read_resources = filename_prefix+'resource-'+download_date+filename_extension
filename_read_people = filename_prefix+'people-'+download_date+filename_extension
# filename_read_interactions = filename_prefix+'interactions-'+download_date+filename_extension

timestr = time.strftime("-%Y%m%d-%H%M%S")

filename_write_internal = 'kumu-data-processed-open-research-map-MASTER-INTERNAL-'+download_date+timestr+'.xlsx'
path_write_internal = os.path.join(dataRoot,'kumu',filename_write_internal)

filename_write_public = 'kumu-data-processed-open-research-map-MASTER-PUBLIC-'+download_date+timestr+'.xlsx'
path_write_public = os.path.join(dataRoot,'kumu',filename_write_public)

dirname_datasource = 'google-sheet-downloads'

path_read_orgs = os.path.join(dataRoot,dirname_datasource,filename_read_orgs)
path_read_resources = os.path.join(dataRoot,dirname_datasource,filename_read_resources)
path_read_people = os.path.join(dataRoot,dirname_datasource,filename_read_people)

# path_read_interactions = os.path.join(dataRoot,filename_read_interactions) # Not working with interactions yet. Will need to incorporate this data into 'people' metadata


# csv file containing our index of scan IDs
# data_people = pd.read_excel(path_read,sheet_name='people')
data_people = pd.read_csv(path_read_people)
data_orgs = pd.read_csv(path_read_orgs)
data_resources = pd.read_csv(path_read_resources)
# data_interactions = pd.read_csv(path_read_interactions)

data_elements = pd.DataFrame()
data_connections = pd.DataFrame()

# print(data_people)
# print(data_orgs)
# print(data_resources)


# First column in each table is the entry name in sharepoint.
# Rename to "label" for kumu

data_people = data_people.rename(columns={'label-person': 'label'})
data_orgs = data_orgs.rename(columns={'label-org': 'label'})
data_resources = data_resources.rename(columns={'label-resource': 'label'})

# strip out the rows without anything in the label column
data_people = data_people[data_people['label'].notna() & (data_people['label'].str.strip() != '')]
data_orgs = data_orgs[data_orgs['label'].notna() & (data_orgs['label'].str.strip() != '')]
data_resources = data_resources[data_resources['label'].notna() & (data_resources['label'].str.strip() != '')]
                                                
# print(data_people)
# print(data_orgs)
# print(data_resources)

# Column names are different across the lists. Need to merge them together so all data types have the same metadata fields.
# You need to merge on all the common columns and use outer join (https://stackoverflow.com/questions/42940507/merging-dataframes-keeping-all-items-pandas)
# pd.merge(df1, df2, on = ['Name', 'Parent', 'Parent_Addr'], how = 'outer')
# find unique column headers over all dfs


# (https://stackoverflow.com/questions/59940311/retrieve-unique-column-names-over-multiple-dataframes-and-append-all-to-a-list)
alldf = [data_people, data_orgs, data_resources]
# alldf = [data_people, data_orgs]
desiredlist = []
for index, dataframe in enumerate(alldf):
    a = dataframe.columns.values.tolist()
    for column_name in a:
        if not column_name in desiredlist:
            desiredlist.append(column_name)

# combine data for "elements" tab
data_elements = pd.merge(data_people,data_orgs, on = 'label', how = 'outer')
data_elements = pd.merge(data_elements,data_resources, on = 'label', how = 'outer')


data_elements.columns = data_elements.columns.str.rstrip('_x')  # strip suffix at the right end only.
data_elements.columns = data_elements.columns.str.rstrip('_y')  # strip suffix at the right end only.

def sjoin(x): return ';'.join(x[x.notnull()].astype(str))
data_elements = data_elements.groupby(level=0, axis=1).apply(lambda x: x.apply(sjoin, axis=1))

# move 'label' to first column
# (https://stackoverflow.com/questions/25122099/move-column-by-name-to-front-of-table-in-pandas)
cols = list(data_elements)
# move the column to head of list using index, pop and insert
cols.insert(0, cols.pop(cols.index('label')))
# use ix to reorder
data_elements = data_elements.loc[:, cols]


# Kumu: If you want to store multiple values inside of one cell (for example, tags or keywords), 
# just separate each value with the pipe character |. 

data_elements['affiliation-label-org'] = data_elements['affiliation-label-org'].str.replace(',','|')
# data_elements['affiliations-turing'] = data_elements['affiliations-turing'].str.replace(',','|')
data_elements['contributor-resource'] = data_elements['contributor-resource'].str.replace(',','|')
data_elements['interaction-participant-all'] = data_elements['interaction-participant-all'].str.replace(',','|')
data_elements['interaction-participant-active'] = data_elements['interaction-participant-active'].str.replace(',','|')
data_elements['interaction-participant-presenter'] = data_elements['interaction-participant-presenter'].str.replace(',','|')
data_elements['interaction-participant-leadership'] = data_elements['interaction-participant-leadership'].str.replace(',','|')


# create a new column "type-what" as a copy of "type" for kumu filtering (kumu doesn't seemto like to work with "type" alone for colour etc. )
data_elements['type-what'] = data_elements.loc[:, 'type']

# # reorder columns so they are logical in kumu
# def swap_columns(df, col1, col2):
#     col_list = list(df.columns)
#     x, y = col_list.index(col1), col_list.index(col2)
#     col_list[y], col_list[x] = col_list[x], col_list[y]
#     df = df[col_list]
#     return df

# col_order = pd.Series(data_elements.columns)
# print(col_order)

# fix_cols = input("do you need to update the colomn order? (enter 0 or col number to by updated):")
# while int(fix_cols) > 0:
#     i = int(fix_cols)
#     # ask which column you want in position i
#     inputq = "what do you want in col" + str(i) + "? (type current index number):"
#     x = int(input(inputq))
#     # get the name of the col in position i
#     col_new = col_order.iloc[x]
#     # get the name of the column cirrently in position i
#     col_old = col_order.iloc[i]
#     # swap _old with _new
#     data_elements = swap_columns(data_elements, col_old, col_new)
#     col_order = pd.Series(data_elements.columns)
#     print(col_order)
#     fix_cols = input("do you need to update the colomn order? (enter 0 or col number to by updated):")


# drop the column 'ID' as kumu wan't to create that value itself.
# data_elements = data_elements.drop('ID', axis=1)

####################

# Now handel the connections!!!

data_people['affiliation-label-org'] = data_people['affiliation-label-org'].str.replace(',','|')
# data_people['affiliations-turing'] = data_people['affiliations-turing'].str.replace(',','|')
data_people['contributor-resource'] = data_people['contributor-resource'].str.replace(',','|') 

# print(data_people[['affiliation-label-org']].to_string(index=False)) 
# print(data_people[['affiliations-turing']].to_string(index=False)) 
# print(data_people[['contributor-resource']].to_string(index=False)) 
# print(data_people[['workstreams']].to_string(index=False)) 

# Kumu: If you put multiple elements in the "To" cell of a connection, separating each element with the pipe character |, 
# Kumu will draw a connection from the "From" element to each separate element in the "To" cell. (https://docs.kumu.io/guides/import/import)

# concatenate the affiliations and projects if not empty
# data_people['to'] = data_people[['affiliation-label-org', 'affiliations-turing', 'contributor-resource']].apply(lambda x: ','.join(x.dropna()), axis=1)
data_people['to'] = data_people[['affiliation-label-org', 'contributor-resource']].apply(lambda x: ','.join(x.dropna()), axis=1)
# data_people['to'] = data_people[['affiliation-label-org']].apply(lambda x: ','.join(x.dropna()), axis=1)

# replace ',' in 'to' with |
data_people['to'] = data_people['to'].str.replace(',[]','')
data_people['to'] = data_people['to'].str.replace(',','|')
# replace 'Alan Turing Institute|Turing-' with 'Turing-'
# This was to make Turing affiliated people connected to their programme only. Think it's better to keep the direct Turing affiliation, for discoverability.
# data_people['to'] = data_people['to'].str.replace('Alan Turing Institute|Turing-','Turing-')

# rename 'label' to 'from'
data_people = data_people.rename(columns={'label': 'from'})
# keep only 'from' and 'to'
data_people = data_people[['from', 'to']]
# add 'direction' column ("undriected")
data_people['direction'] = 'undirected'


# DO IT ALL AGAIN FOR CONNECTIONS FOR orgs AND PROJECTS

# 1. Merge affiliations
data_orgs['affiliation-label-org'] = data_orgs['affiliation-label-org'].str.replace(',','|')
data_resources['affiliation-label-org'] = data_resources['affiliation-label-org'].str.replace(',','|')

# 2. rename 'label' to 'from'
data_orgs = data_orgs.rename(columns={'label': 'from'})
data_resources = data_resources.rename(columns={'label': 'from'})

# 3. rename 'affiliation-label-org' to 'to'
data_orgs = data_orgs.rename(columns={'affiliation-label-org': 'to'})
data_resources = data_resources.rename(columns={'affiliation-label-org': 'to'})

# 4. keep only 'from' and 'to'
data_orgs = data_orgs[['from', 'to']]
data_resources = data_resources[['from', 'to']]

# 5. add 'undirected'
data_orgs['direction'] = 'undirected'
data_resources['direction'] = 'undirected'

# COMBINE ALL THE CONNECTIONS

frames = [data_people, data_orgs, data_resources]
# frames = [data_people, data_orgs]
data_connections = pd.concat(frames)
data_connections = data_connections.reset_index(drop=True)

# replace NaN in 'to' with '[]'
data_connections['to'] = data_connections['to'].fillna('[]')

#fix some column names
data_elements.rename(columns={'Created': 'created-date'}, inplace=True)
data_elements.rename(columns={'Created B': 'created-by'}, inplace=True)
data_elements.rename(columns={'Modified': 'modified-last-date'}, inplace=True)
data_elements.rename(columns={'Modified B': 'modified-last-by'}, inplace=True)
data_elements.rename(columns={'countr': 'country'}, inplace=True)

# fix the sizes
data_elements.loc[data_elements['type-what'] == 'person', 'size'] = 1
data_elements.loc[data_elements['type-what'] == 'research institute', 'size'] = 100
data_elements.loc[data_elements['type-what'] == 'university', 'size'] = 100
data_elements.loc[data_elements['type-what'] == 'public sector', 'size'] = 20
data_elements.loc[data_elements['type-what'] == 'private industry', 'size'] = 20
data_elements.loc[data_elements['type-what'] == 'non-profit', 'size'] = 20
data_elements.loc[data_elements['type-what'] == 'consortium', 'size'] = 35
data_elements.loc[data_elements['type-what'] == 'network', 'size'] = 35
# data_elements.loc[data_elements['type-what'] == 'Turing programme', 'size'] = 20
data_elements.loc[data_elements['type-what'] == 'project', 'size'] = 50





print('writing data to:' + path_write_internal)
with pd.ExcelWriter(path_write_internal) as writer:
    # use to_excel function and specify the sheet_name and index 
    # to store the dataframe in specified sheet
    data_elements.to_excel(writer, sheet_name="elements", index=False)
    data_connections.to_excel(writer, sheet_name="connections", index=False)
print('writing xlsx data for internal map - complete')    


####################
# Do anonymisation
####################

an = anonymize(data_elements)
an.fake_ids("label")

data_elements_anon = data_elements

data_elements_anon.rename(columns={'Fake_label': 'label-anon'}, inplace=True)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# if type-what not = "person" set consent-kumu to "consent-public"
data_elements_anon.loc[data_elements_anon['type-what'] != 'person', 'consent-kumu'] = 'consent-public'

# if type-what == "person" and consent-kumu == []; consent-kumu = "consent-none"
data_elements_anon.loc[(data_elements_anon['type-what'] == 'person') & (data_elements_anon['consent-kumu'] == ''), 'consent-kumu'] = 'consent-none'

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# # Select the specified columns and assign them to a new DataFrame
elements_consent_lookup = data_elements_anon[['label', 'consent-kumu', 'label-anon','type-what']].copy()


data_connections_anon = data_connections[['from', 'to', 'direction']].copy()
data_connections_anon['label-public'] = np.nan


df1 = data_connections_anon
df2 = elements_consent_lookup


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# # Loop through df1 and find matching values in df2
for index, row in df1.iterrows():
    print(index)
    print(df1.iloc[index]) #df1.at[index, 'label-public']
    if index == 835:
        print(df1.iloc[835])
    id_value = row['from']
    matching_row = df2[df2['label'] == id_value]
    if not matching_row.empty:
        if matching_row['consent-kumu'].values[0] == 'consent-none':
            print("Matching value in df2 for id", id_value, ":", "Consent is none")
            # Add the 'Fake-label' value to df1
            df1.at[index, 'label-public'] = matching_row['label-anon'].values[0]
        elif matching_row['consent-kumu'].values[0] == 'consent-public':
            print("Matching value in df2 for id", id_value, ":", "Consent is public")
            df1.at[index, 'label-public'] = matching_row['label'].values[0]
        elif matching_row['consent-kumu'].values[0] == 'consent-pseudonymised':
            print("Matching value in df2 for id", id_value, ":", "Consent is pseudonymised")
            df1.at[index, 'label-public'] = matching_row['label-anon'].values[0]
        else:
            print("Matching value in df2 for id", id_value, ":", "Consent is: ",matching_row['consent-kumu'].values[0])
    else:
        print("No matching value found in df2 for id", id_value)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

data_connections_anon = df1

# redact identifable information from data_elements_anon where no consent
columns_identifiable = ['email', 'github', 'position', 'pronouns', 'url']
data_elements_anon.loc[data_elements['consent-kumu'] == 'consent-none', columns_identifiable] = np.nan

# delete opinion columns for everyone %**
# columns_opinions = ['how-to-engage','influence-over-programme','interaction-participant-active','interaction-participant-all','interaction-participant-leadership','interaction-participant-presenter','interactions-count','interest-in-programme','moe-level','notes']
columns_opinions = ['how-to-engage','influence-over-programme','interaction-participant-active','interaction-participant-all','interaction-participant-leadership','interaction-participant-presenter','interest-in-programme','moe-level','notes']
data_elements_anon = data_elements_anon.drop(columns_opinions,axis=1)

# get rid of boring columns %**
columns_boring = ['created-date', 'created-by', 'modified-last-date', 'modified-last-by', 'url']
data_elements_anon = data_elements_anon.drop(columns_boring,axis=1)



# replace labels with label_anon where consent == none
data_elements_anon.loc[data_elements_anon['consent-kumu'] == 'consent-public', 'label-anon'] = data_elements_anon['label']

# rename
data_elements_anon.rename(columns={'label-anon': 'label-public'}, inplace=True)

# delete the old "label" and "from", replace with the anonymised values
data_elements_anon = data_elements_anon.drop('label',axis=1)
data_elements_anon.rename(columns={'label-public': 'label'}, inplace=True)

data_connections_anon = data_connections_anon.drop('from',axis=1)
data_connections_anon.rename(columns={'label-public': 'from'}, inplace=True)

# and move the new ones to the first column (for kumu)
cols = list(data_elements_anon.columns)
cols.insert(0, cols.pop(cols.index('label')))
data_elements_anon = data_elements_anon[cols]

cols = list(data_connections_anon.columns)
cols.insert(0, cols.pop(cols.index('from')))
data_connections_anon = data_connections_anon[cols]

# write out
print('writing anonymised data to:' + path_write_public)
with pd.ExcelWriter(path_write_public) as writer:
    # use to_excel function and specify the sheet_name and index 
    # to store the dataframe in specified sheet
    data_elements_anon.to_excel(writer, sheet_name="elements", index=False)
    data_connections_anon.to_excel(writer, sheet_name="connections", index=False)
print('writing xlsx data for public map - complete')


# #################



# # %%%%%%%%%%%%%%%%%%%%%%%%%%%



