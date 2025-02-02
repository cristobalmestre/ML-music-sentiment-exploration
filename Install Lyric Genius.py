import subprocess
import sys

# Run the pip install command
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'lyricsgenius'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'rauth'])