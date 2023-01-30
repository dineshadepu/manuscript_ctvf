import glob
import shutil

# root_dir needs a trailing slash (i.e. /root/dir/)
root_dir = "./"
for file_type in ['**/*.pdf', '**/*.png', '**/*.svg']:
    for filename in glob.iglob(root_dir + file_type, recursive=True):
        filename_dash = filename.replace("/", "_")
        filename_dash = filename_dash.replace("0.", "0_")
        print(filename_dash[2:])
        shutil.copy(filename, filename_dash[2:])
