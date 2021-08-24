import zipfile
import shutil

f1 = open('fileone.txt' , 'w+')
f1.write('ONE FILE')
f1.close()

f2 = open('filetwo.txt', 'w+')
f2.write('TWO FILE')
f2.close

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')

