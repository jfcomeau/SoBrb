#!/usr/bin/env python
# -*- coding: utf-8 -*-

import soco, pickle


ROOT = '~/Documents/scripts/SoBrb/'
MUTED_VOLUME_LEVEL = 6

uri_signature = '7QMTL0.akacast.akamaistream.net'
muted_zones = []


def isPlaying(zone):
	state = zone.get_current_transport_info().get(u'current_transport_state')
	if state == 'PLAYING':
		return True

	return False


def isUriToMute(zone):
	uri = zone.get_current_track_info().get(u'uri')
	if uri_signature in uri:
		return True

	return False


def muteZone(zone):
	if zone.is_coordinator:
		for member in zone.group.members:
			if member.is_visible:
				appendZone(member)
				member.volume = MUTED_VOLUME_LEVEL
				print "%s is now muted." % (member.player_name)
	
	else:
		appendZone(zone)
		zone.volume = MUTED_VOLUME_LEVEL
		print "%s is now muted." % (member.player_name)

	return


def appendZone(zone) :
	muted_zones.append({
		'player_name': zone.player_name,
		'ip': zone.ip_address,
		'original_vol': zone.volume,
		'muted_vol': MUTED_VOLUME_LEVEL,
		'uri_signature': zone.get_current_track_info().get(u'uri') })

	return


def serializeToFile():
	output = open(ROOT + 'data.pkl', 'wb')
	pickle.dump(muted_zones, output)
	output.close()

	return


def main():
	sd = soco.discover()
	for zone in sd:
		if isPlaying(zone):
			if isUriToMute(zone):
				muteZone(zone)

	if not muted_zones:
		print "No zone to mute."
	else:
		serializeToFile()


main()