#!/usr/bin/python
import urllib                                

def main():
    sock = urllib.urlopen("https://events.ccc.de/congress/2012/wiki/Assemblies")
    htmlSource = sock.read()
    sock.close()
    idx1=htmlSource.find("<tbody>")
    idx2=htmlSource.find("</tbody>",idx1)
    shortcode = htmlSource[idx1+20:idx2].strip()
    print "Content-type: text/html"
    print
    print shortcode

if __name__ == "__main__":
    main()
