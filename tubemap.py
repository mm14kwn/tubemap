#! /usr/bin/python

import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
from scipy import misc
import pickle


def main():
    # import matplotlib.colors as colors
    # import mapstations2
    # tubecoordsdict = mapstations2.mapcoords()
    # tubecoords = pd.DataFrame.from_dict(tubecoordsdict)
    # tcT = tubecoords.T
    stations = pd.read_csv('./stations.csv')
    linedef = pd.read_csv('./linedef.csv')
    routes = pd.read_csv('./routes.csv')
    # tcx = tcT.x[stations['name']]
    # tcy = tcT.y[stations['name']]
    geolist = []
    # maplist = []
    clist = []
    nlist = []
    # fig = plt.figure()
    # ax1 = plt.subplot(1, 2, 1)
    # ax2 = plt.subplot(1, 2, 2)
    for rn in range(1, 14):
        route = routes[routes.line == rn]
        clr = (route['colour'])
        clist.append(clr)
        nlist.append(route['name'])
        slist = linedef[linedef.line == rn]
        geoseg = np.zeros((2, 2, slist.shape[0]))
        # mapseg = np.zeros((2, 2, slist.shape[0]))
        for sn in range(0, slist.shape[0]):
            sids1 = slist['station1']
            sids2 = slist['station2']
            s1 = sids1.iloc[sn]
            s2 = sids2.iloc[sn]
            stat1 = stations[stations.id == s1]
            stat2 = stations[stations.id == s2]
            geoseg[0, 0, sn] = stat1['longitude']
            geoseg[0, 1, sn] = stat1['latitude']
            geoseg[1, 0, sn] = stat2['longitude']
            geoseg[1, 1, sn] = stat2['latitude']
            # mapseg[0, 0, sn] = tcx[stat1['name']]
            # mapseg[0, 1, sn] = tcy[stat1['name']]
            # mapseg[1, 0, sn] = tcx[stat2['name']]
            # mapseg[1, 1, sn] = tcy[stat2['name']]
            # plt.plot(geoseg[:, 0, sn], geoseg[:, 1, sn], '#' + clr.iloc[0])
            # ax2.plot(mapseg[:, 0, sn], mapseg[:, 1, sn], '#' + clr.iloc[0])
        geolist.append(geoseg)
        # maplist.append(mapseg)
    # plt.scatter(stations.longitude, stations.latitude)
    # ax2.scatter(tcT.x, tcT.y)
    # plt.show()
    # timg = misc.imread('./lines.png', mode='RGB')
    # xi , yi = np.indices((timg.shape[0], timg.shape[1]))
    # crgb = []
    # for ind in range(0, len(clist)):
    #     cpd = clist[ind]
    #     h = '#' + cpd.iloc[0]
    #     rgb = colors.hex2color(h)
    #     rgbt = tuple([int(255*x) for x in rgb])
    #     crgb.append(rgbt)

    fnlist = [
        'bakerloo', 'central', 'circle', 'district', 'hscity', 'jubilee',
        'metropolitan', 'northern', 'picadilly', 'victoria', 'wlcity', 'dlr'
    ]
    pngdict = {}
    filldict = {}
    for fn in fnlist:
        print(fn)
        lineimage = misc.imread('./' + fn + '.png', mode='L')
        img_nogaps = fillgaps(lineimage, iterations=3, sqsize=81)
        filldict[fn] = img_nogaps
        pngdict[fn] = lineimage
    with open('./savefile.pickle', 'wb') as fp:
        savedict = {
            "pngdict": pngdict,
            "filldict": filldict,
            "fnlist": fnlist,
            "geolist": geolist,
            "clist": clist,
            "nlist": nlist,
            "stations": stations,
            "linedef": linedef,
            "routes": routes
        }
        pickle.dump(savedict, fp)


if __name__ == "__main__":
    main()


def fillgaps(img, iterations=1, mode='closing', sqsize=21):
    """dilation bit is 
    from http://stackoverflow.com/a/28079714
    fills gaps in binary skeleton image
    """
    from skimage import morphology, img_as_bool, segmentation
    from scipy import ndimage as ndi
    if mode is 'dilate':
        image = 1 - img_as_bool(img)
        out = ndi.distance_transform_edt(~image)
        out = out < 0.05 * out.max()
        out = morphology.skeletonize(out)
        out = morphology.binary_dilation(out, morphology.selem.disk(1))
        out = segmentation.clear_border(out)
        out = out | image
    elif mode is 'closing':
        out = 1 - img_as_bool(img)
        while iterations > 0:
            out = morphology.binary_closing(out, morphology.square(sqsize))
            iterations -= 1
    return out


# for line in pngdict:
#     plt.subplot(1,2,1)
#     plt.imshow(pngdict[line])
#     plt.subplot(1,2,2)
#     plt.imshow(filldict[line])
#     plt.show()
