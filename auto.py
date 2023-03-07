#!/usr/bin/env python3
import os
import shutil

source_dir = '/Users/solomon/Downloads'
img_dest_dir = '/Users/solomon/Downloads/Images'
pdf_dest_dir = '/Users/solomon/Downloads/PDF'
vid_dest_dir = '/Users/solomon/Downloads/Videos'
zips_dest_dir = '/Users/solomon/Downloads/Zips'
iso_dest_dir = '/Users/solomon/Downloads/Other/Iso'
text_dest_dir = '/Users/solomon/Downloads/Text File'

    
with os.scandir(source_dir) as entries:
    for entry in entries:
         FileName = entry.name.lower()
         if FileName.endswith('.jpg') or FileName.endswith('.jpeg') or FileName.endswith('.png'):
            if(os.path.isfile(img_dest_dir+'/'+FileName)):
               continue
            else:
               shutil.move(source_dir+'/'+FileName,img_dest_dir)
         elif FileName.endswith('.mp4') or FileName.endswith('.mov'):
             if(os.path.isfile(vid_dest_dir+'/'+FileName)):
                  continue
             else:
                shutil.move(source_dir+'/'+FileName,vid_dest_dir)
         elif FileName.endswith('.pdf'):
             if(os.path.isfile(pdf_dest_dir+'/'+FileName)):
                continue
             else:
                shutil.move(source_dir+'/'+FileName,pdf_dest_dir) 
         elif FileName.endswith('.zip'):
             if(os.path.isfile(zips_dest_dir+'/'+FileName)):
                continue
             else:
                shutil.move(source_dir+'/'+FileName,zips_dest_dir)
         elif FileName.endswith('.iso'):
             if(os.path.isfile(iso_dest_dir+'/'+FileName)):
               continue
             else:
                shutil.move(source_dir+'/'+FileName,iso_dest_dir)
         elif FileName.endswith('.txt'):
            if(os.path.isfile(text_dest_dir+'/'+FileName)):
               continue 
            else:
                shutil.move(source_dir+'/'+FileName,text_dest_dir)
               

         

