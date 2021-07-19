#sally.nguyen@oracle.com 7/16/21
import pandas as pd
import xml.etree.ElementTree as ET
import os
import re
import csv
pattern='^(\/[\w-]+)+\.|[\\.\w-]+\.(png|jpg|pdf|htm|html|mht|js)'
columns=['Path', 'prev_src']
df=pd.DataFrame(columns=columns)
catalog = ""
for root, dirs, files in os.walk(catalog, topdown=True):
    for f in files:
        webcat=os.path.join(root,f)
        if(not webcat.endswith('.atr')):
            with open(webcat, 'rb') as f:
                content=f.readlines()
                content=str(content)
            if(re.search(pattern,content)):
                matched=re.search(pattern,content)
                prev_path=matched.group(0)
                df=df.append({'Path':webcat,'prev_src':prev_path},ignore_index=True)
                #Pivot this:
                pivot=df.pivot_table(index=['prev_src'],values=['prev_src'], aggfunc=len,fill_value=0)']
                print(pivot)
                #df.to_csv('')

