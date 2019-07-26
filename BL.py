import pandas as pd
import numpy as np

df = pd.read_csv("190725_singlebiinput.csv", encoding='latin-1')

old_names = ['RecipientId SAP','Device Model','Implanted Ear','DeviceSerial', 'First Given Name','Last Name','Professional: First Name','Professional: Last Name','Professional: Phone']
new_names = ['id','Model','ImplEar','SerNo','FNme','LNme','ProFNme','ProLNme','ProPh']

df.rename(columns=dict(zip(old_names, new_names)), inplace=True)

df.replace({'300-M079':'CI-1601-04', '300-M049':'CI-1600-04', '300-M089':'CI-1601-05','7095316-62V':'CI-1500-04', '7095316-64J':'CI-1400-01','300-M075':'CI-1600-05'}, inplace=True)
df.replace({'7095316-49H':'CI-1400-02H', '7095316-60J':'CI-1500-01', '300-M081':'CI-1600-04','300-M078':'CI-1600-05','7095316-80V':'CI-1500-04','7095316-72V':'CI-1500-04'}, inplace=True)
df.replace({'300-M077':'CI-1600-05', '300-M092':'CI-1601-04', '300-M091':'CI-1601-05'}, inplace=True)
df.replace({'7095316-48J':'CI-1400-01', '300-M072':'CI-1600-05'}, inplace=True)

df = df.replace(np.nan, '', regex=True)

df_L = df[df.ImplEar == 'Left'].drop('ImplEar', axis=1)
df_R = df[df.ImplEar == 'Right'].drop('ImplEar', axis=1)

df_RT = pd.merge(df_L.iloc[:, 0:3], df_R.iloc[:, 0:8], on = 'id', suffixes=['L', 'R'], how='right') ### Right
df_RR = df_RT[['id', 'ModelL', 'SerNoL', 'FNme', 'LNme','ProFNme','ProLNme', 'ProPh', 'ModelR','SerNoR']]  ## Right

df_LL = pd.merge(df_L.iloc[:, 0:8], df_R.iloc[:, 0:3], on = 'id', suffixes=['L', 'R'], how='left') ### Left
df_IN = pd.merge(df_L.iloc[:, 0:8], df_R.iloc[:, 0:3], on = 'id', suffixes=['L', 'R'], how='inner') ### Inner

pieces = (df_RR, df_LL, df_IN)

#df_final = pd.concat(pieces, ignore_index = True)
df_final = pd.concat(pieces, ignore_index=True, sort =False)
df_final1 = df_final.replace(np.nan, '', regex=True)
df_final2 = df_final1.drop_duplicates()

pd.options.display.float_format = '{:.0f}'.format

df_final2
#print(df_RT)

df_final2.to_csv("190725_singlebioutput.csv")