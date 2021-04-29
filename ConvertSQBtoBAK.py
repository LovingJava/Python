import os
from os import path

import datetime
import glob
import shutil

today = datetime.date.today()
today = str(today)
nohyphen_today = today.replace('-','')
revised_today = "LOG_us_bcan_multi_replica_" + nohyphen_today 

src = "C:\\Users\\Justin Dolt\\Test1"
dst = "C:\\Users\\Justin Dolt\\Today"
password = "Pcc+ihcmi=$uccess"

src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dst)   

for f in glob.glob('*.SQB'):
    os.system( f'start SQBConverter "{f}" "{dst}/{f[:-4]}.bak" {password}' )
