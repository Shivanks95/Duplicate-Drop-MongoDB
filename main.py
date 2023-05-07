import os
import sys
import subprocess

# set path to scripts
data_dump_path = os.path.join(os.getcwd(), 'data_dump.py')
drop_duplicates_path = os.path.join(os.getcwd(), 'drop_duplicates.py')

# run data dump script
subprocess.call([sys.executable, data_dump_path])

# run drop duplicates script
subprocess.call([sys.executable, drop_duplicates_path])