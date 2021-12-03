from tkinter import messagebox,colorchooser
import turtle,time
####DO NOT DELETE!!!!!!!!!!!!!####
####SCREEN CONFIGURATION####
rscreen = turtle.Screen()
xtrarndr = turtle.Turtle()
####SETTINGS####
MANAGED = False #if the browser is managed
MANAGED_BY = 'ENTER_HERE' #who/what orginizatoin the browser is managed by
BLOCKED_SITES = ['SITE_HERE','SITE_HERE'] #sites that are bolcked. Feel free to add more sites

COMMANDLINE_ENABLED = True #If the user can use the CommandLine
####MAIN [CODE]####
while True :
 rscreen.title('PyBrowser Renderer')
 url = rscreen.textinput('PyBrowser V.10','Open URL [URLL for URL List]:')
