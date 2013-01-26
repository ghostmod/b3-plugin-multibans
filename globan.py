#
# Globan Plugin for BigBrotherBot(B3) (www.bigbrotherbot.net)
# Copyright (C) 2013 FaceHunter
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# Changelog:
#	0.1 game shows amount on join
#
#	TODO:
#		-find a way to add people on ban, but only on permban (or not :3)
#

import b3
import b3.plugin
import b3.events
import urllib

__version__ = '0.1'
__author__  = 'FaceHunter'

class GlobanPlugin(b3.plugin.Plugin):
	requiresConfigFile = False
	
	def onStartup(self):

		self._adminPlugin = self.console.getPlugin('admin')
		self.verbose("Starting globan plugin!")
 
		if not self._adminPlugin:
			# something is wrong, can't start without admin plugin
			self.error('Could not find admin plugin')
			return
			
		self.verbose('Registering events')
		self.registerEvent(b3.events.EVT_CLIENT_CONNECT)
		self.registerEvent(b3.events.EVT_CLIENT_BAN)
		self.debug('Started')
		
		self._adminPlugin.registerCommand(self, 'globantest', 1, self.globantest)
		
	def globantest(self,  data, client, cmd):
		self.console.saybig('Globan plugin is working!')
		
	def onEvent(self, event):
		if event.type == b3.events.EVT_CLIENT_CONNECT:
			self.lookup(event.client)
		if event.type == b3.events.EVT_CLIENT_BAN:
			
	def lookup(self, client):
		self.console.say('User: '+client.name+' has '+self.checkbans(client)+' bans!')
		
		
	def checkbans(self, client):
		guid = client.guid
		name = client.name
		checka = urllib.urlopen("http://localhost/globan/getinfo.php?name="+name+"&guid="+guid)
		stat = checka.read().strip()
		if stat == "None":
			return "no"
		else:
			return stat