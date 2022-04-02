import sys
import configparser
from pathlib import Path

from PIL import Image
import numpy as np

target_filepath = Path(sys.argv[1])
img = Image.open(target_filepath).convert('RGBA')  # make sure image is RGBA
background = Image.new('RGBA', (2000,1000), (0,0,0,0))

configParser = configparser.RawConfigParser()   
configFilePath = 'config.txt'
configParser.read(configFilePath)

x = int(configParser.get('positions', 'x'))
y = int(configParser.get('positions', 'y'))

background.paste(img, (x, y), img)

background.save(f'!place_{target_filepath.name}')
