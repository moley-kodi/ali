# -*- coding: utf-8 -*-

"""
Copyright (C) 2015

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
"""

import urllib, urllib2, sys, re, os, unicodedata
import xbmc, xbmcgui, xbmcplugin, xbmcaddon, base64

plugin_handle = int(sys.argv[1])
mysettings = xbmcaddon.Addon(id = 'plugin.video.ccloudtv')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')

fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
iconpath = xbmc.translatePath(os.path.join(home, 'resources/icons/'))
icon = xbmc.translatePath(os.path.join(home, 'resources/icons/icon.png'))
searchicon = xbmc.translatePath(os.path.join(home, 'search.png'))
newsicon = xbmc.translatePath(os.path.join(home, 'news.png'))
entertainmenticon = xbmc.translatePath(os.path.join(home, 'entertainment.png'))
announcementsicon = xbmc.translatePath(os.path.join(home, 'announcements.png'))
newsicon = xbmc.translatePath(os.path.join(home, 'news.png'))
allchannelsicon = xbmc.translatePath(os.path.join(home, 'allchannels.png'))
newsicon = xbmc.translatePath(os.path.join(home, 'news.png'))
top10icon = xbmc.translatePath(os.path.join(home, 'top10.png'))
documentaryicon = xbmc.translatePath(os.path.join(home, 'documentaries.png'))
sportsicon = xbmc.translatePath(os.path.join(home, 'sports.png'))
familyicon = xbmc.translatePath(os.path.join(home, 'family.png'))
moviesicon = xbmc.translatePath(os.path.join(home, 'movies.png'))
musicicon = xbmc.translatePath(os.path.join(home, 'news.png'))
ondemandicon = xbmc.translatePath(os.path.join(home, 'ondemand.png'))
twentyfoursevenicon = xbmc.translatePath(os.path.join(home, 'twentyfourseven.png'))
radioicon = xbmc.translatePath(os.path.join(home, 'radio.png'))
englishicon = xbmc.translatePath(os.path.join(home, 'english.png'))


xml_regex = '<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>'
m3u_thumb_regex = 'tvg-logo=[\'"](.*?)[\'"]'
m3u_regex = '#(.+?),(.+)\s*(.+)\s*'
yt = 'http://www.youtube.com'
m3u = 'WVVoU01HTkViM1pNTTBKb1l6TlNiRmx0YkhWTWJVNTJZbE01ZVZsWVkzVmpSMmgzVURKck9WUlViRWxTYXpWNVZGUmpQUT09'.decode('base64')
text = 'http://pastebin.com/raw.php?i=Zr0Hgrbw'

					
def read_file(file):
    try:
        f = open(file, 'r')
        content = f.read()
        f.close()
        return content
    except:
        pass
		
###Thanks to Spoyser for the code below###
def showText(heading, text, waitForClose=False):
    id = 10147

    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)

    win = xbmcgui.Window(id)

    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            retry = 0
        except:
            retry -= 1

    if waitForClose:
        while xbmc.getCondVisibility('Window.IsVisible(%d)' % id) == 1:
            xbmc.sleep(50)

def make_request(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason

			
def main():
	add_dir('[COLOR royalblue][B]***Latest Announcements***[/B][/COLOR]', yt, 3, announcementsicon, fanart)
	add_dir('[COLOR red][B]Search[/B][/COLOR]', 'searchlink', 99, searchicon, fanart)
	if len(List) > 0:	
		add_dir('[COLOR yellow][B]All Channels[/B][/COLOR]', yt, 2, allchannelsicon, fanart)
		#showText('[COLOR yellow]Message From cCloud[/COLOR]', '')
	if (len(List) < 1 ):		
		mysettings.openSettings()
		xbmc.executebuiltin("Container.Refresh")
	add_dir('[COLOR royalblue][B]Top 10[/B][/COLOR]', 'top10', 51, top10icon, fanart)
	add_dir('[COLOR royalblue][B]Sports[/B][/COLOR]', 'sports', 52, sportsicon, fanart)
	add_dir('[COLOR royalblue][B]News[/B][/COLOR]', 'news', 53, newsicon, fanart)
	add_dir('[COLOR royalblue][B]Documentary[/B][/COLOR]', 'documentary', 54, documentaryicon, fanart)
	add_dir('[COLOR royalblue][B]Entertainment[/B][/COLOR]', 'entertainment', 55, entertainmenticon, fanart)
	add_dir('[COLOR royalblue][B]Family[/B][/COLOR]', 'family', 56, familyicon, fanart)
	add_dir('[COLOR royalblue][B]Movies[/B][/COLOR]', 'movie', 57, moviesicon, fanart)
	add_dir('[COLOR royalblue][B]Music[/B][/COLOR]', 'music', 58, musicicon, fanart)
	add_dir('[COLOR royalblue][B]On Demand[/B][/COLOR]', 'ondemand', 59, ondemandicon, fanart)
	add_dir('[COLOR royalblue][B]24/7 Channels[/B][/COLOR]', '24', 60, twentyfoursevenicon, fanart)
	add_dir('[COLOR royalblue][B]Radio[/B][/COLOR]', 'radio', 61, radioicon, fanart)
	add_dir('[COLOR royalblue][B]English[/B][/COLOR]', 'english', 62, englishicon, fanart)

		
def removeAccents(s):
	return ''.join((c for c in unicodedata.normalize('NFD', s.decode('utf-8')) if unicodedata.category(c) != 'Mn'))
		
def search(): 	
	try:
		keyb = xbmc.Keyboard('', 'Enter Channel Name')
		keyb.doModal()
		if (keyb.isConfirmed()):
			searchText = urllib.quote_plus(keyb.getText()).replace('+', ' ')
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass

def sports(): 	
	try:
		searchText = 'sports'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
	

def top10(): 	
	try:
		searchText = 'top10'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
	
def news(): 	
	try:
		searchText = 'news'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
	
	
def documentary(): 	
	try:
		searchText = 'document'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
	
	
def entertainment(): 	
	try:
		searchText = 'entertainment'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
	
	
def family(): 	
	try:
		searchText = 'family'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass

		
	
def movie(): 	
	try:
		searchText = 'movie'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
	


def music(): 	
	try:
		searchText = 'music'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
	


def ondemand(): 	
	try:
		searchText = 'ondemand'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
	
	
def twentyfour7(): 	
	try:
		searchText = '24/7'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
	

	
def radio(): 	
	try:
		searchText = 'radio'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
	

	
def english(): 	
	try:
		searchText = 'english'
		if len(List) > 0:		
			content = make_request(List)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
	
	
		
def text_online():		
	content = make_request(text)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass

	
def m3u_online():		
	content = make_request(List)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
		
def m3u_playlist(name, url, thumb):	
	name = re.sub('\s+', ' ', name).strip()			
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')			
			add_dir(name, url, '', thumb, thumb)			
		else:	
			add_dir(name, url, '', icon, fanart)
	else:
		if 'youtube.com/watch?v=' in url:
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % (url.split('=')[-1])
		elif 'dailymotion.com/video/' in url:
			url = url.split('/')[-1].split('_')[0]
			url = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url=%s' % url	
		else:			
			url = url
		if 'tvg-logo' in thumb:				
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			add_link(name, url, 1, thumb, thumb)			
		else:				
			add_link(name, url, 1, icon, fanart)	

def play_video(url):
	media_url = url
	item = xbmcgui.ListItem(name, path = media_url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return

def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param
	
List = 'YUhSMGNEb3ZMM1JwYm5rdVkyTXZTMjlrYVE9PQ=='.decode('base64') .decode('base64')
def add_dir(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok		
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

def add_link(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)	
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)  
		
params = get_params()
url = None
name = None
mode = None
iconimage = None

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass  

print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)
print "iconimage: " + str(iconimage)		

if mode == None or url == None or len(url) < 1:
	main()

elif mode == 1:
	play_video(url)

elif mode == 2:
	m3u_online()
	
elif mode == 3:
	text_online()
	
	
elif mode == 51:
	top10()
		
elif mode == 52:
	sports()
	
elif mode == 53:
	news()
	
elif mode == 54:
	documentary()
	
elif mode == 55:
	entertainment()
	
elif mode == 56:
	family()
	
elif mode == 57:
	movie()
	
elif mode == 58:
	music()
	
elif mode == 59:
	ondemand()
	
elif mode == 60:
	twentyfour7()
	
elif mode == 61:
	radio()
	
elif mode == 62:
	english()

elif mode == 99:
	search()
	
xbmcplugin.endOfDirectory(plugin_handle)