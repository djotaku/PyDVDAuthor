import os, sys, curses

"""Calls dvdauthorxml from dvdauthor.py to provide the information necessary to create the XML file."""

from dvdauthor import dvdauthorxml

__program_name__ = "Pydvdauthor_ncurses"
__author__ = "Eric Mesa"
__version__ = "v0.1.6"
__license__ = "GNU GPL v3"
__copyright__ = "(c)2008 Eric Mesa"
__email__ = "ericsbinaryworld at gmail dot com"

def get_param(prompt_string, pos):
    """This asks the user for a string and then returns to the program"""
    #screen.clear()
    #screen.border(0)
    screen.addstr(pos,2,prompt_string)
    screen.refresh()
    input = screen.getstr(pos+5,10,60)
    return input

def execute_cmd(cmd_string):
    """Executes a command"""
    system("clear")
    a = system(cmd_string)
    print ""
    if a == 0:
        print "Command executed correctly"
    else:
        print "Command terminated with error"
    raw_input("Press Enter")
    print ""

screen = curses.initscr()

screen.clear()
screen.border(0)
screen.addstr(2,2,"Welcome to " + __author__ + "'s " + __program_name__)
screen.addstr(3,2,"Version " + __version__)
screen.addstr(4,2,__license__)
screen.addstr(5,2, __copyright__)
screen.refresh()

#may want to change this - getch is get character
#screen.getch()

pathtodvd = get_param("Please enter the path where you want the DVD files created.  This must be a full path (eg /home/user_name/spamalot)", 6)

pathtovideo = get_param("Please enter the path and filename where the video can be found.  At this time, this must be an MPEG-2 DVD compliant video (eg /home/user/spamspamspam.mpg)", 14)

chapters = get_param( "Please enter the times where you want a chapter to be created.  \n Enter this in the format of \n hour:minute:seconds.  \n If you don't want any chapters then at least enter 0. \n Separate all chapters with a comma. (eg 0, 14:30, 19:34)", 22)

#do the part where they can change it - but that may not be necessary with the type of gui I want
#this will come later

screen.addstr(29,2, "Generating the XML file!")

screen.refresh()
screen.getch()
chapters2 = chapters.split(",")

dvdauthorxml(pathtodvd,pathtovideo,chapters2)

#screen.addstr(2,3, "Now look for the file named dvdauthor.xml.  It should be in this path, then type dvdauthor -x dvdauthor.xml")

curses.endwin()
