#! /usr/bin/env python
# -*- coding: utf-8 -*-

from obspy import read
from obspy.core import UTCDateTime
from obspy.arclink.client import Client
import matplotlib.pyplot as plt
import numpy as np

client = Client(
    host="eida.resif.fr",
    port=18001,
    user="fabien.engels@unistra.fr",
    institution="EOST"
)

t1 = UTCDateTime("2013-06-01 22:22:06.84")
#client.saveWaveform(
#    "waveforms.mseed",
#    "FR",
#    "OGDI",
#    "00",
#    "*",
#    t1-300,
#    t1+2000
#)

st = read("waveforms.mseed")
print st[0].stats.sampling_rate
st[0].filter('lowpass', freq=2)
st[0].decimate(factor=3, strict_length=False)


d1 = st[0].data
d1 -= d1[0]
t = np.linspace(-900, 1600, len(d1))
plt.figure(figsize=(12, 4))
plt.plot(t, d1, label=str(t1))
plt.show()
