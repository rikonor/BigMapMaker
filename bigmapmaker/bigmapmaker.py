import subprocess

# get all map segments
subprocess.call(["phantomjs","mapmaker.js"])

# stitch segments into large map
subprocess.call(["python","mapstitch.py"])

# lay a grid on the map
subprocess.call(["python","gridlayer.py", "images/mapFull.jpeg"])

# apply text to fullmap and to keymaps
subprocess.call(["python","applytext.py"])
