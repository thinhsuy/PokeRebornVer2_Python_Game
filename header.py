import pygame
from PIL import Image
import pyodbc
import os
import sys
import pygame_gui
import random
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-2T77F44\SQLEXPRESS;'
                      'Database=DB_PokeWar;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

notification = ""
SCREEN_HEIGHT, SCREEN_LENGTH = (600, 750)
STAB = pd.read_csv('scripts/STAB.csv', sep=',')
PATH = 'D:/Sequence/Compilers/Python/Projects/PokewarRework/'