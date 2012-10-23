import sys

"""Calls dvdauthorxml from dvdauthor.py to provide the information necessary to create the XML file."""

__program_name__ = "Pydvdauthor"
__author__ = "Eric Mesa"
__version__ = "v0.1.6"
__license__ = "GNU GPL v3"
__copyright__ = "(c)2008 Eric Mesa"
__email__ = "ericsbinaryworld at gmail dot com"

from dvdauthor import dvdauthorxml

print "Welcome to " + __author__ + "'s" + __program_name__
print "Version " + __version__
print __license__ + "\n"  + __copyright__

loop_me = True

#Begin the inquisition - no one EVER expects the inquisition!

print "Please enter the path where you want the DVD files created.  This must be a full path (eg /home/user_name/spamalot)"
pathtodvd = raw_input()

print "Please enter the path and filename where the video can be found.  At this time, this must be an MPEG-2 DVD compliant video (eg /home/user/spamspamspam.mpg)"
pathtovideo = raw_input()

print "Please enter the times where you want a chapter to be created.  \n Enter this in the format of \n hour:minute:seconds.  \n If you don't want any chapters then at least enter 0. \n Separate all chapters with a comma. (eg 0, 14:30, 19:34)"
chapters = raw_input()

#Hit them with a fish, I mean, with what they have given us so far

print "Here is what you have so far:"
print pathtodvd + "\n" + pathtovideo + "\n" + chapters + "\n"

#Ask if it's correct

print "\n\nIs this correct? (y or n)"
q1 = raw_input()

#A, currently, very untidy little bugger which only allows them to correct one mistake

if q1 == 'y':
    print "Excellent!  We will continue!"
    loop_me = False

while loop_me == True:
    print "Which was wrong?  Your choices are (dvd, file, chapters)"
    q2 = raw_input()

    if q2 == 'dvd':
        print "Enter the path where you want the dvd created"
        pathtodvd = raw_input()
    elif q2 == 'file':
        print "Enter the path where the file is:"
        pathtovideo = raw_input()
    elif q2 == 'chapters':
        print "Re-enter the chapters."
        chapters = raw_input()
    else:
        print "Please give a valid reponse!"

    print "Here is what you have now entered:"
    print "Here is what you have so far:"
    print pathtodvd + "\n" + pathtovideo + "\n" + chapters + "\n"
    
    print "Is everything correct now? (y or n)"
    q3 = raw_input()
    if q3 == 'y':
        loop_me = False
    

print "\nGenerating the XML file!"

chapters2 = chapters.split(",")

dvdauthorxml(pathtodvd, pathtovideo, chapters2)

print "Now look for the file named dvdauthor.xml.  It should be in this path, then type dvdauthor -x dvdauthor.xml"

#Yippie!
