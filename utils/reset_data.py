#!/usr/bin/env python

import pickle

muted_zones = []

output = open('data/data.pkl', 'wb')
pickle.dump(diskVar, output)
output.close()