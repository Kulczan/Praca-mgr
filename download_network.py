import urllib.request
import shutil
import zipfile
from os import listdir, unlink
from os.path import isfile, join

url = 'http://nrvis.com/download/data/inf/inf-USAir97.zip'

temp_file = 'temp.zip'
temp_path = './tempdir'

try:
    unlink(join('.', temp_file))
       
    for ff in listdir(temp_path):
        pf = join(temp_path, ff)
        if isfile(pf):
            unlink(pf)
except:
    pass

with urllib.request.urlopen(url) as response, open(temp_file, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    
zip_ref = zipfile.ZipFile(temp_file, 'r')
zip_ref.extractall(temp_path)
zip_ref.close()

files = [f for f in listdir(temp_path) if isfile(join(temp_path, f))]

print(files)

for f in files:
    if not f.lower().endswith(('.htm','.html')):
        shutil.copyfile(join(temp_path, f), './net.wedges')

try:
    unlink(join('.', temp_file))
       
    for ff in listdir(temp_path):
        pf = join(temp_path, ff)
        if isfile(pf):
            unlink(pf)
except:
    pass
