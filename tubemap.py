#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mapstations
tubecoordsdict = mapstations.mapcoords()
tubecoords = pd.DataFrame.from_dict(tubecoordsdict)
tcT = tubecoords.T
stations = pd.read_csv('./stations.csv')
linedef = pd.read_csv('./linedef.csv')
routes = pd.read_csv('./routes.csv')
tcx = tcT.x[stations['name']]
tcy = tcT.y[stations['name']]
geolist = []
maplist = []
clist = []
nlist = []
fig = plt.figure()
ax1 = plt.subplot(1,2,1)
ax2 = plt.subplot(1,2,2)
for rn in range(1,14):
    route = routes[routes.line==rn]
    clr = (route['colour'])
    clist.append(clr)
    nlist.append(route['name'])
    slist = linedef[linedef.line==rn]
    geoseg = np.zeros((2,2,slist.shape[0]))
    mapseg = np.zeros((2,2,slist.shape[0]))
    for sn in range(0, slist.shape[0]):
        sids1 = slist['station1']
        sids2 = slist['station2']
        s1 = sids1.iloc[sn]
        s2 = sids2.iloc[sn]
        stat1 = stations[stations.id==s1]
        stat2 = stations[stations.id==s2]
        geoseg[0,0,sn] = stat1['longitude']
        geoseg[0,1,sn] = stat1['latitude']
        geoseg[1,0,sn] = stat2['longitude']
        geoseg[1,1,sn] = stat2['latitude']
        mapseg[0,0,sn] = tcx[stat1['name']]
        mapseg[0,1,sn] = tcy[stat1['name']]
        mapseg[1,0,sn] = tcx[stat2['name']]
        mapseg[1,1,sn] = tcy[stat2['name']]
        ax1.plot(geoseg[:,0,sn], geoseg[:,1,sn], '#'+clr.iloc[0])
        ax2.plot(mapseg[:,0,sn], mapseg[:,1,sn], '#'+clr.iloc[0])
    geolist.append(geoseg)
    maplist.append(mapseg)
ax1.scatter(stations.longitude, stations.latitude)
ax2.scatter(tcT.x, tcT.y)
plt.show()
