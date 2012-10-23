import os, sys

def dvdauthorxml(pathtodvd, pathtovideo, chapters):
    """This will take in 3 parameters:
    The path where the DVD will be created, the path to the video which will make up the DVD, and the times where chapters should be created.
    This is meant to be the backend which creates the dvdauthor.xml file.
    It is up to the programmer to design a frontend for user interaction.

    pathtodvd and pathtovideo should be strings and chapters should be a list

    This currently creates a DVD without a menu, it just begins playing the
    movie and the user can skip around the chapters."""

    __author__ = "Eric Mesa"
    __version__ = "v0.1.6"
    __license__ = "GNU GPL v3.0"
    __copyright__ = "(c) 2008 Eric Mesa"
    __email__ = "ericsbinaryworld at gmail dot com"

    outputfile = open('/home/emesa/bin/python/dvdauthor.xml', 'w')
    outputfile.write('<dvdauthor dest="' + pathtodvd + '"> \
\n<vmgm /> \
\n<titleset> \
\n<titles> \
\n<pgc> \
\n<vob file="' + pathtovideo  + '" chapters="' + ", ".join(chapters)  +  '"/> \
\n</pgc> \
\n</titles> \
\n</titleset> \
\n</dvdauthor>')
    outputfile.close()

    
#Testing Suite with the if name trick

if __name__ == "__main__":
    print "It worked!"
    x = 'pathtofile'
    y = 'pathtodvd'
    z = ['0', '14:37',]
    dvdauthorxml(y,x,z)
