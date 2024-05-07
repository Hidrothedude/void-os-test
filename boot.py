import subprocess
import os

file_path = 'User/Setup_Done.txt'

if os.path.exists(file_path):
    subprocess.run(["python", "Login.py"])
else:
   subprocess.run(["python", "Setup.py"])