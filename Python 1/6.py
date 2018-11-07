import os

for root, dirs, files in os.walk("..", topdown = False):
	print(dirs)
	print(files)
