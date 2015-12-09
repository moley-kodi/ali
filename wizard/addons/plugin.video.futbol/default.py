import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os


ADDON = xbmcaddon.Addon(id='plugin.video.futbol')

datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
futbol=os.path.join(datapath, "futbol")

if os.path.exists(futbol)==False:
    if os.path.exists(datapath) == False:
            os.makedirs(datapath)
    try:
        req = urllib2.Request('http://www.webs4you.es/Futbol/samples/music/Deporte2014.html#_home')
        req.add_header('User-Agent', '/Apple iPhone')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        f = open(world, mode='w')
        f.write(link)
        f.close()
    except:pass


def CATEGORIES():
    link=open(futbol).read()
    match=re.compile('<a href="(.+?)".+?style="vertical-align: top;" >(.+?)/a></li>').findall(link)
    for m3u8 , NAME in  match:
        
        if 'COLOR=black' in NAME:
           name=re.compile('COLOR=black>(.+?)</FONT>').findall(NAME)[0]
        else:
           name=NAME.replace('<','')
           
        addLink(name.title(),m3u8,'')
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)    
 
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    
    
    

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param


def addLink(name,url,iconimage):
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)

        
 
        
def setView(content, viewType):
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':#<<<----see here if auto-view is enabled(true) 
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )#<<<-----then get the view type
                      
               
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
   
        
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
