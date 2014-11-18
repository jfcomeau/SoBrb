#!/usr/bin/env python
# -*- coding: utf-8 -*-

import soco, pickle
from soco import SoCo

ROOT = '~/Documents/scripts/SoBrb/'

muted_zones = []


def isMutedZones():
	global muted_zones
	
	input = open(ROOT + 'data.pkl', 'rb')
	muted_zones = pickle.load(input)
	input.close()

	if not muted_zones:
		return False

	return True


def isPlaying(zone):
	state = zone.get_current_transport_info().get(u'current_transport_state')
	if state == 'PLAYING':
		return True

	return False


def isUriToMute(zone, muted_zone):
	uri = zone.get_current_track_info().get(u'uri')
	if muted_zone['uri_signature'] in uri:
		return True

	return False


def isStillMuted(zone, muted_zone):
	if zone.volume == muted_zone['muted_vol']:
		return True

	return False


def resetFile():
	muted_zones = []
	output = open(ROOT + 'data.pkl', 'wb')
	pickle.dump(muted_zones, output)
	output.close()

	return


def main():
	# Are there any muted zones?
	if isMutedZones():
		for muted_zone in muted_zones:
			zone = SoCo(muted_zone['ip'])
			# Make sure the zone have not been stopped meanwhile...
			if isPlaying(zone):
				# Make sure the zone is still playing radio...
				if isUriToMute(zone, muted_zone):
					# Make sure volume have not been changed meanwhile...
					if isStillMuted(zone, muted_zone):
						# Set the volume to what is use to be
						zone.volume = muted_zone['original_vol']
						print "%s is now back to %s" % (zone.player_name, zone.volume)

		resetFile()

	else:
		print "No zone to unmute."

	return


main()