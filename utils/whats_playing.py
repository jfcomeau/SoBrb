#!/usr/bin/env python
# -*- coding: utf-8 -*-

import soco

sd = soco.discover()

for zone in sd:
	print "Currently playing in %s: %s" % (zone.player_name,
		zone.get_current_track_info().get(u'uri'))