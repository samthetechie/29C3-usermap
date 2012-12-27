#!/usr/bin/python
'''
__author__ = "Samuel Carlisle"
__copyright__ = "Copyright 2012"
__credits__ = ["samthetechie,izrail,andy,nobody"]
__license__ = "GPL Affero"
__version__ = "3"
__maintainer__ = "Samuel Carlisle"
__email__ = "samuelcarlisle@gmail.com"
__status__ = "Development"
                                                       ____
           ___                                      .-~. /_"-._        _______________________________
          `-._~-.                                  / /_ "~o\  :Y      /We made 29C3-usermap so that   \
              \  \                                / : \~x.  ` ')      |people could find their way    |
               ]  Y                              /  |  Y< ~-.__j      |and get to the talks they want |
              /   !                        _.--~T : l  l<  /.-~      < to. We hope you like it :)     |
             /   /                 ____.--~ .   ` l /~\ \<|Y          \_______________________________/
            /   /             .-~~"        /| .    ',-~\ \L|
           /   /             /     .^   \ Y~Y \.^>/l_   "--'
          /   Y           .-"(  .  l__  j_j l_/ /~_.-~    .
         Y    l          /    \  )    ~~~." / `/"~ / \.__/l_
         |     \     _.-"      ~-{__     l  :  l._Z~-.___.--~
         |      ~---~           /   ~~"---\_  ' __[>
         l  .                _.^   ___     _>-y~
          \  \     .      .-~   .-~   ~>--"  /
           \  ~---"            /     ./  _.-'
            "-.,_____.,_  _.--~\     _.-~
                        ~~     (   _}  
                                `. ~(
                                  )  \
                                 /,`--'~\--'
This file is part of 29C3-usermap.

29C3-usermap is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

29C3-usermap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Affero Public License
along with 29C3-usermap.  If not, see <http://www.gnu.org/licenses/>.
'''
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
