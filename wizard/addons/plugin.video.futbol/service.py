import urllib2 , xbmc , xbmcaddon , os
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.futbol'
Oo0Ooo = xbmcaddon . Addon ( id = OO0o )
if 85 - 85: OOO0O0O0ooooo % IIii1I . II1 - O00ooooo00
I1IiiI = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
I11i11Ii = os . path . join ( I1IiiI , "futbol" )
if 65 - 65: i1iIi11iIIi1I
if os . path . exists ( I1IiiI ) == False :
 os . makedirs ( I1IiiI )
 if 78 - 78: i11ii11iIi11i . oOoO0oo0OOOo + IiiI / Iii1ii1II11i
try :
 iI111iI = urllib2 . Request ( 'http://www.webs4you.es/Futbol/samples/music/Deporte2014.html#_home' )
 IiII = urllib2 . urlopen ( iI111iI )
 iI1Ii11111iIi = IiII . read ( )
 IiII . close ( )
 i1i1II = open ( I11i11Ii , mode = 'w' )
 i1i1II . write ( iI1Ii11111iIi )
except : pass
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
