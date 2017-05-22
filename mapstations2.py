#! python
def mapcoords():
    tubestations = {
        "Amersham": {
            "x": 117.5674,
            "y": 193.3823
        },
        "Chorleywood": {
            "x": 285.0654,
            "y": 207.4351
        },
        "Mill Hill East": {
            "x": 1316.9741,
            "y": 261.0347
        },
        "Rickmansworth": {
            "x": 306.2056,
            "y": 236.7271
        },
        "Perivale": {
            "x": 340.7793,
            "y": 712.6431
        },
        "Kentish Town West": {
            "x": 1342.5054,
            "y": 526.9585
        },
        "Camden Road": {
            "x": 1415.4062,
            "y": 604.6323
        },
        "Dalston Kingsland": {
            "x": 1861.8066,
            "y": 628.8521
        },
        "Hackney Central": {
            "x": 1892.168,
            "y": 661.3706
        },
        "Wanstead Park": {
            "x": 2157.4961,
            "y": 640.8804
        },
        "Vauxhall": {
            "x": 1111.8071,
            "y": 1357.4546
        },
        "Hanger Lane": {
            "x": 368.2026,
            "y": 767.9116
        },
        "Edgware": {
            "x": 991.7798,
            "y": 284.6177
        },
        "Burnt Oak": {
            "x": 1021.0874,
            "y": 324.522
        },
        "Colindale": {
            "x": 1055.2778,
            "y": 355.0181
        },
        "Hendon Central": {
            "x": 1063.6187,
            "y": 385.522
        },
        "Brent Cross": {
            "x": 1103.6987,
            "y": 416.0181
        },
        "Golders Green": {
            "x": 1115.1084,
            "y": 446.522
        },
        "West Silvertown": {
            "x": 2141.3574,
            "y": 1055.1245
        },
        "Pontoon Dock": {
            "x": 2206.127,
            "y": 1108.2144
        },
        "London City Airport": {
            "x": 2224.0293,
            "y": 1161.3159
        },
        "Woolwich Arsenal": {
            "x": 2417.8086,
            "y": 1325.146
        },
        "King George V": {
            "x": 2310.2383,
            "y": 1214.4058
        },
        "Hampstead": {
            "x": 1165.8394,
            "y": 477.019
        },
        "Belsize Park": {
            "x": 1229.2896,
            "y": 542.9644
        },
        "Chalk Farm": {
            "x": 1264.0894,
            "y": 573.4683
        },
        "Chalfont & Latimer": {
            "x": 247.9302,
            "y": 152.8804
        },
        "Chesham": {
            "x": 116.1196,
            "y": 127.7349
        },
        "New Cross Gate": {
            "x": 1636.1035,
            "y": 1362.4956
        },
        "Moor Park": {
            "x": 438.9243,
            "y": 238.3599
        },
        "Northwood": {
            "x": 468.7925,
            "y": 268.2222
        },
        "Northwood Hills": {
            "x": 488.6553,
            "y": 294.7935
        },
        "Pinner": {
            "x": 538.1606,
            "y": 333.7427
        },
        "North Harrow": {
            "x": 564.1733,
            "y": 363.606
        },
        "Custom House for ExCeL": {
            "x": 2363.0723,
            "y": 994.1479
        },
        "Prince Regent": {
            "x": 2312.9336,
            "y": 1024.0054
        },
        "Royal Albert": {
            "x": 2342.8027,
            "y": 1053.8745
        },
        "Beckton Park": {
            "x": 2372.6621,
            "y": 1083.7437
        },
        "Cyprus": {
            "x": 2401.0918,
            "y": 1112.8745
        },
        "Gallions Reach": {
            "x": 2432.4023,
            "y": 1143.4741
        },
        "Beckton": {
            "x": 2462.2617,
            "y": 1173.3335
        },
        "Watford": {
            "x": 431.3545,
            "y": 173.4819
        },
        "Croxley": {
            "x": 431.3545,
            "y": 205.9526
        },
        "Fulham Broadway": {
            "x": 761.2056,
            "y": 1240.4937
        },
        "Lambeth North": {
            "x": 1345.2729,
            "y": 1287.644
        },
        "Heathrow Terminal 4": {
            "x": 242.9331,
            "y": 1360.6343
        },
        "Harrow- on-the-Hill": {
            "x": 606.5137,
            "y": 390.772
        },
        "Kensal Rise": {
            "x": 802.646,
            "y": 573.103
        },
        "Canonbury": {
            "x": 1771.9922,
            "y": 594.4956
        },
        "Bethnal Green": {
            "x": 1862.1719,
            "y": 776.5474
        },
        "Westferry": {
            "x": 1922.2227,
            "y": 974.7241
        },
        "Seven Sisters": {
            "x": 1803.2344,
            "y": 417.7808
        },
        "Blackwall": {
            "x": 2027.9238,
            "y": 974.7241
        },
        "Brondesbury Park": {
            "x": 866.6123,
            "y": 573.105
        },
        "Hampstead Heath": {
            "x": 1275.1948,
            "y": 477.0347
        },
        "Harringay Green Lanes": {
            "x": 1777.125,
            "y": 362.2554
        },
        "Leytonstone High Road": {
            "x": 2149.6152,
            "y": 584.3921
        },
        "Leyton Midland Road": {
            "x": 2036.1348,
            "y": 584.3921
        },
        "Northwick Park": {
            "x": 691.3706,
            "y": 392.7593
        },
        "Preston Road": {
            "x": 772.5488,
            "y": 402.7593
        },
        "Royal Victoria": {
            "x": 2212.375,
            "y": 971.2974
        },
        "Wembley Park": {
            "x": 796.0166,
            "y": 492.3188
        },
        "Rayners Lane": {
            "x": 371.3237,
            "y": 414.7515
        },
        "Watford High Street": {
            "x": 656.0542,
            "y": 160.4019
        },
        "Ruislip Gardens": {
            "x": 266.1401,
            "y": 419.728
        },
        "South Ruislip": {
            "x": 235.0088,
            "y": 482.0806
        },
        "Greenford": {
            "x": 274.6743,
            "y": 663.9878
        },
        "Northolt": {
            "x": 263.0361,
            "y": 552.1714
        },
        "South Harrow": {
            "x": 376.6934,
            "y": 466.6831
        },
        "Sudbury Hill": {
            "x": 385.4927,
            "y": 521.2056
        },
        "Sudbury Town": {
            "x": 371.2832,
            "y": 575.7378
        },
        "Alperton": {
            "x": 406.4478,
            "y": 630.2632
        },
        "Pimlico": {
            "x": 1093.0737,
            "y": 1225.6343
        },
        "Park Royal": {
            "x": 398.0054,
            "y": 814.3159
        },
        "North Ealing": {
            "x": 384.5913,
            "y": 859.5952
        },
        "Acton Central": {
            "x": 515.064,
            "y": 975.5601
        },
        "South Acton": {
            "x": 524.4834,
            "y": 1020.7847
        },
        "Ealing Broadway": {
            "x": 313.6519,
            "y": 904.103
        },
        "Watford Junction": {
            "x": 648.8213,
            "y": 127.4448
        },
        "West Ruislip": {
            "x": 239.1929,
            "y": 283.9585
        },
        "Bushey": {
            "x": 712.4722,
            "y": 193.3589
        },
        "Carpenders Park": {
            "x": 656.2129,
            "y": 226.3228
        },
        "Hatch End": {
            "x": 695.4165,
            "y": 259.2788
        },
        "North Wembley": {
            "x": 653.6592,
            "y": 470.312
        },
        "West Brompton": {
            "x": 753.1689,
            "y": 1173.8452
        },
        "Ealing Common": {
            "x": 360.0073,
            "y": 995.7065
        },
        "South Kenton": {
            "x": 667.2158,
            "y": 442.5347
        },
        "Kenton": {
            "x": 780.0566,
            "y": 366.1753
        },
        "Wembley Central": {
            "x": 645.8408,
            "y": 498.0952
        },
        "Kensal Green": {
            "x": 790.0239,
            "y": 618.4448
        },
        "Queen's Park": {
            "x": 788.7378,
            "y": 646.231
        },
        "Gunnersbury": {
            "x": 564.814,
            "y": 1200.5776
        },
        "Kew Gardens": {
            "x": 564.8823,
            "y": 1247.1675
        },
        "Richmond": {
            "x": 565.0415,
            "y": 1287.2769
        },
        "Stockwell": {
            "x": 1287.519,
            "y": 1444.0483
        },
        "Bow Church": {
            "x": 1906.4785,
            "y": 857.5288
        },
        "Stonebridge Park": {
            "x": 647.9375,
            "y": 525.8804
        },
        "Harlesden": {
            "x": 689.2012,
            "y": 553.6646
        },
        "Camden Town": {
            "x": 1272.0806,
            "y": 611.1694
        },
        "Willesden Junction": {
            "x": 656.5298,
            "y": 581.4468
        },
        "Headstone Lane": {
            "x": 659.5938,
            "y": 292.2456
        },
        "Parsons Green": {
            "x": 782.8408,
            "y": 1273.5679
        },
        "Putney Bridge": {
            "x": 785.9897,
            "y": 1306.5288
        },
        "East Putney": {
            "x": 798.1631,
            "y": 1352.6069
        },
        "Southfields": {
            "x": 800.6025,
            "y": 1385.5679
        },
        "Wimbledon Park": {
            "x": 769.9717,
            "y": 1418.5269
        },
        "Wimbledon": {
            "x": 797.3892,
            "y": 1451.4976
        },
        "Island Gardens": {
            "x": 1888.0508,
            "y": 1274.3979
        },
        "Greenwich": {
            "x": 2006.3203,
            "y": 1366.5874
        },
        "Deptford Bridge": {
            "x": 2006.3203,
            "y": 1398.5269
        },
        "South Quay": {
            "x": 1906.4199,
            "y": 1175.5269
        },
        "Crossharbour": {
            "x": 1896.1191,
            "y": 1208.4761
        },
        "Mudchute": {
            "x": 1916.3203,
            "y": 1241.437
        },
        "Heron Quays": {
            "x": 1898.9102,
            "y": 1142.5659
        },
        "West India Quay": {
            "x": 2006.4805,
            "y": 1051.1265
        },
        "Elverson Road": {
            "x": 2006.3203,
            "y": 1430.4565
        },
        "Oakwood": {
            "x": 1751.2188,
            "y": 205.2515
        },
        "Cockfosters": {
            "x": 1749.9004,
            "y": 172.2935
        },
        "Southgate": {
            "x": 1665.5898,
            "y": 238.2144
        },
        "Arnos Grove": {
            "x": 1652.4785,
            "y": 271.1714
        },
        "Bounds Green": {
            "x": 1652.5586,
            "y": 304.1265
        },
        "Theydon Bois": {
            "x": 2046.0586,
            "y": 146.9888
        },
        "Epping": {
            "x": 2084.668,
            "y": 119.1733
        },
        "Debden": {
            "x": 2080.3086,
            "y": 174.8042
        },
        "Loughton": {
            "x": 2069.5195,
            "y": 202.6138
        },
        "Buckhurst Hill": {
            "x": 2042.4395,
            "y": 240.7241
        },
        "Walthamstow Queen's Road": {
            "x": 1965.6602,
            "y": 509.5054
        },
        "Woodgrange Park": {
            "x": 2153.1504,
            "y": 675.1167
        },
        "Leytonstone": {
            "x": 2050.9316,
            "y": 548.8267
        },
        "Leyton": {
            "x": 2085.6211,
            "y": 630.5366
        },
        "Wood Green": {
            "x": 1651.4512,
            "y": 337.0913
        },
        "Turnpike Lane": {
            "x": 1642.6699,
            "y": 370.0483
        },
        "Manor House": {
            "x": 1647.3594,
            "y": 418.6685
        },
        "Stanmore": {
            "x": 876.4678,
            "y": 305.6138
        },
        "Canons Park": {
            "x": 873.9639,
            "y": 338.5728
        },
        "Queensbury": {
            "x": 873.9639,
            "y": 371.5327
        },
        "Kingsbury": {
            "x": 873.9639,
            "y": 404.4878
        },
        "High Barnet": {
            "x": 1459.811,
            "y": 165.3237
        },
        "Totteridge & Whetstone": {
            "x": 1487.6206,
            "y": 198.2866
        },
        "Woodside Park": {
            "x": 1459.3911,
            "y": 231.2437
        },
        "West Finchley": {
            "x": 1459.3701,
            "y": 264.2007
        },
        "Finchley Central": {
            "x": 1459.3701,
            "y": 314.1177
        },
        "Woodford": {
            "x": 2062.7715,
            "y": 360.4351
        },
        "South Woodford": {
            "x": 2026.8594,
            "y": 392.519
        },
        "Snaresbrook": {
            "x": 2052.9102,
            "y": 425.48
        },
        "Hainault": {
            "x": 2227.3398,
            "y": 346.2017
        },
        "Fairlop": {
            "x": 2240.4609,
            "y": 379.1646
        },
        "Barkingside": {
            "x": 2212.1992,
            "y": 412.1226
        },
        "Newbury Park": {
            "x": 2196.6895,
            "y": 445.0835
        },
        "East Finchley": {
            "x": 1457.6196,
            "y": 347.0806
        },
        "Highgate": {
            "x": 1457.6196,
            "y": 380.0386
        },
        "Archway": {
            "x": 1447.6196,
            "y": 419.5015
        },
        "Devons Road": {
            "x": 2006.3691,
            "y": 885.9429
        },
        "Langdon Park": {
            "x": 2006.3691,
            "y": 918.9019
        },
        "All Saints": {
            "x": 2006.3691,
            "y": 951.8628
        },
        "Tufnell Park": {
            "x": 1457.6196,
            "y": 458.9702
        },
        "Kentish Town": {
            "x": 1459.5898,
            "y": 497.1685
        },
        "Neasden": {
            "x": 906.0229,
            "y": 465.0327
        },
        "Dollis Hill": {
            "x": 934.6426,
            "y": 493.644
        },
        "Willesden Green": {
            "x": 983.2671,
            "y": 522.2642
        },
        "South Tottenham": {
            "x": 1894.8691,
            "y": 395.1685
        },
        "Swiss Cottage": {
            "x": 884.8198,
            "y": 436.8257
        },
        "Imperial Wharf": {
            "x": 946.6265,
            "y": 1246.5972
        },
        "Brixton": {
            "x": 1334.1997,
            "y": 1507.0483
        },
        "Kilburn": {
            "x": 995.8633,
            "y": 550.8853
        },
        "West Hampstead": {
            "x": 1023.9546,
            "y": 579.4995
        },
        "Blackhorse Road": {
            "x": 1939.2441,
            "y": 421.8726
        },
        "Acton Town": {
            "x": 489.7124,
            "y": 1069.9565
        },
        "Canning Town": {
            "x": 2133.5137,
            "y": 975.7046
        },
        "Finchley Road": {
            "x": 1052.564,
            "y": 607.6616
        },
        "Highbury & Islington": {
            "x": 1684.7031,
            "y": 594.5562
        },
        "Canary Wharf": {
            "x": 1896.6738,
            "y": 1099.0972
        },
        "Stratford": {
            "x": 2034.9629,
            "y": 675.9019
        },
        "Finsbury Park": {
            "x": 1734.3223,
            "y": 495.9556
        },
        "Elephant & Castle": {
            "x": 1402.6128,
            "y": 1360.1479
        },
        "Stepney Green": {
            "x": 1879.832,
            "y": 891.3706
        },
        "Barking": {
            "x": 2278.3125,
            "y": 731.9741
        },
        "East Ham": {
            "x": 2248.9727,
            "y": 762.0503
        },
        "Upton Park": {
            "x": 2141.1035,
            "y": 753.6792
        },
        "Plaistow": {
            "x": 2202.1621,
            "y": 809.4253
        },
        "Poplar": {
            "x": 2001.5938,
            "y": 1007.3198
        },
        "West Ham": {
            "x": 2144.0742,
            "y": 844.1226
        },
        "Upper Holloway": {
            "x": 1580.0645,
            "y": 473.2856
        },
        "Pudding Mill Lane": {
            "x": 2069.4531,
            "y": 751.3784
        },
        "Kennington": {
            "x": 1325.7524,
            "y": 1411.2085
        },
        "Borough": {
            "x": 1461.9922,
            "y": 1274.9585
        },
        "Elm Park": {
            "x": 2434.8926,
            "y": 579.7964
        },
        "Dagenham East": {
            "x": 2324.1211,
            "y": 571.2642
        },
        "Dagenham Heathway": {
            "x": 2381.5625,
            "y": 633.1245
        },
        "Becontree": {
            "x": 2341.5117,
            "y": 668.4644
        },
        "Upney": {
            "x": 2312.332,
            "y": 702.3628
        },
        "Heathrow Terminal 5": {
            "x": 148.6274,
            "y": 1412.9702
        },
        "Finchley Road & Frognal": {
            "x": 1127.7417,
            "y": 522.8823
        },
        "Crouch Hill": {
            "x": 1538.7129,
            "y": 396.8179
        },
        "Northfields": {
            "x": 338.6743,
            "y": 1113.0405
        },
        "Boston Manor": {
            "x": 294.937,
            "y": 1141.6206
        },
        "South Ealing": {
            "x": 360.5566,
            "y": 1084.4702
        },
        "Osterley": {
            "x": 298.7939,
            "y": 1170.1909
        },
        "Hounslow Central": {
            "x": 307.7993,
            "y": 1251.7104
        },
        "Hounslow East": {
            "x": 339.229,
            "y": 1223.1714
        },
        "Clapham North": {
            "x": 1150.272,
            "y": 1457.3101
        },
        "Oval": {
            "x": 1264.3823,
            "y": 1408.8413
        },
        "Clapham Common": {
            "x": 1100.4219,
            "y": 1487.4312
        },
        "Clapham South": {
            "x": 1090.3613,
            "y": 1517.5405
        },
        "Balham": {
            "x": 1105.4712,
            "y": 1547.6616
        },
        "Tooting Bec": {
            "x": 1051.8105,
            "y": 1577.771
        },
        "Tooting Broadway": {
            "x": 984.4414,
            "y": 1607.8804
        },
        "Colliers Wood": {
            "x": 976.9155,
            "y": 1637.9897
        },
        "South Wimbledon": {
            "x": 942.9585,
            "y": 1668.1108
        },
        "Arsenal": {
            "x": 1603.8711,
            "y": 504.2095
        },
        "Holloway Road": {
            "x": 1529.041,
            "y": 534.3267
        },
        "Caledonian Road": {
            "x": 1493.7808,
            "y": 564.439
        },
        "Morden": {
            "x": 952.478,
            "y": 1698.2104
        },
        "West Croydon": {
            "x": 1750.9004,
            "y": 1706.8198
        },
        "Hounslow West": {
            "x": 206.1875,
            "y": 1235.8101
        },
        "Hatton Cross": {
            "x": 162.3843,
            "y": 1278.6108
        },
        "Heathrow Terminals 1, 2, 3": {
            "x": 109.5649,
            "y": 1315.1401
        },
        "Clapham Junction": {
            "x": 1059.582,
            "y": 1419.2808
        },
        "West Harrow": {
            "x": 540.7104,
            "y": 438.9976
        },
        "Brondesbury": {
            "x": 905.7534,
            "y": 609.3413
        },
        "Caledonian Road & Barnsbury": {
            "x": 1589.9336,
            "y": 647.9351
        },
        "Tottenham Hale": {
            "x": 1843.582,
            "y": 467.9146
        },
        "Walthamstow Central": {
            "x": 1981.4219,
            "y": 467.9146
        },
        "Hackney Wick": {
            "x": 1982.0508,
            "y": 712.6685
        },
        "Homerton": {
            "x": 1900.041,
            "y": 712.6685
        },
        "West Acton": {
            "x": 511.376,
            "y": 927.5483
        },
        "Limehouse": {
            "x": 1880.0195,
            "y": 1010.6206
        },
        "East India": {
            "x": 2085.0898,
            "y": 1011.271
        },
        "Crystal Palace": {
            "x": 1579.25,
            "y": 1671.3726
        },
        "Chiswick Park": {
            "x": 487.4385,
            "y": 1119.2222
        },
        "Roding Valley": {
            "x": 2155.5508,
            "y": 275.7749
        },
        "Grange Hill": {
            "x": 2231.9902,
            "y": 277.8813
        },
        "Chigwell": {
            "x": 2189.2207,
            "y": 323.6401
        },
        "Redbridge": {
            "x": 2187.0801,
            "y": 474.3931
        },
        "Gants Hill": {
            "x": 2238.7793,
            "y": 507.2983
        },
        "Wanstead": {
            "x": 2147.8906,
            "y": 507.2983
        },
        "North Greenwich": {
            "x": 2083.8887,
            "y": 1114.8628
        },
        "Ickenham": {
            "x": 246.3052,
            "y": 353.0347
        },
        "Turnham Green": {
            "x": 563.1265,
            "y": 1119.4038
        },
        "Uxbridge": {
            "x": 121.7422,
            "y": 351.9683
        },
        "Hillingdon": {
            "x": 187.9614,
            "y": 313.814
        },
        "Ruislip": {
            "x": 341.0063,
            "y": 312.5845
        },
        "Gospel Oak": {
            "x": 1343.7539,
            "y": 455.6245
        },
        "Mile End": {
            "x": 1926.7949,
            "y": 787.1558
        },
        "Bow Road": {
            "x": 2026.4863,
            "y": 812.7515
        },
        "Bromley-by-Bow": {
            "x": 2070.6953,
            "y": 848.8599
        },
        "Upminster": {
            "x": 2432.8242,
            "y": 473.8101
        },
        "Upminster Bridge": {
            "x": 2364.5547,
            "y": 503.9224
        },
        "Hornchurch": {
            "x": 2368.6152,
            "y": 534.0347
        },
        "Norwood Junction": {
            "x": 1750.5039,
            "y": 1674.0249
        },
        "Sydenham": {
            "x": 1661.4141,
            "y": 1569.3452
        },
        "Forest Hill": {
            "x": 1662.0645,
            "y": 1536.5444
        },
        "Anerley": {
            "x": 1752.0352,
            "y": 1641.2144
        },
        "Penge West": {
            "x": 1748.9062,
            "y": 1608.4038
        },
        "Honor Oak Park": {
            "x": 1631.0449,
            "y": 1503.7437
        },
        "Brockely": {
            "x": 1674.3262,
            "y": 1430.3647
        },
        "Harrow & Wealdstone": {
            "x": 675.8022,
            "y": 333.3228
        },
        "Cutty Sark for Maritime Greenwich": {
            "x": 2026.2637,
            "y": 1335.6655
        },
        "Ruislip Manor": {
            "x": 400.0464,
            "y": 327.7349
        },
        "Eastcote": {
            "x": 442.6572,
            "y": 363.8276
        },
        "Wapping": {
            "x": 1851.2539,
            "y": 1043.0249
        },
        "Shadwell": {
            "x": 1849.4434,
            "y": 963.98
        },
        "New Cross": {
            "x": 1854.4238,
            "y": 1362.4956
        },
        "Canada Water": {
            "x": 1786.1836,
            "y": 1125.855
        },
        "Surrey Quays": {
            "x": 1748.8125,
            "y": 1195.3452
        },
        "Whitechapel": {
            "x": 1850.2324,
            "y": 924.064
        },
        "Lewisham": {
            "x": 2006.3242,
            "y": 1461.8843
        },
        "Kilburn Park": {
            "x": 690.1104,
            "y": 692.1724
        },
        "Regent's Park": {
            "x": 1178.4048,
            "y": 815.0806
        },
        "Kilburn High Road": {
            "x": 875.3823,
            "y": 656.2827
        },
        "Edgware Road": {
            "x": 949.6655,
            "y": 704.1421
        },
        "South Hampstead": {
            "x": 963.9385,
            "y": 656.2827
        },
        "Goodge Street": {
            "x": 1256.3745,
            "y": 860.6538
        },
        "Shepherd's Bush Market": {
            "x": 650.2266,
            "y": 986.1851
        },
        "Goldhawk Road": {
            "x": 654.7407,
            "y": 1032.564
        },
        "Hammersmith": {
            "x": 664.9448,
            "y": 1070.6655
        },
        "Bayswater": {
            "x": 942.4321,
            "y": 835.2202
        },
        "Warren Street": {
            "x": 1225.9844,
            "y": 783.2974
        },
        "Aldgate": {
            "x": 1688.1445,
            "y": 944.3999
        },
        "Euston": {
            "x": 1272.7637,
            "y": 723.3599
        },
        "Farringdon": {
            "x": 1440.563,
            "y": 806.8198
        },
        "Barbican": {
            "x": 1487.6138,
            "y": 844.2349
        },
        "Russell Square": {
            "x": 1350.1533,
            "y": 829.396
        },
        "Kensington (Olympia)": {
            "x": 781.6841,
            "y": 1008.1948
        },
        "Mornington Crescent": {
            "x": 1285.8237,
            "y": 659.3452
        },
        "High Street Kensington": {
            "x": 942.0439,
            "y": 963.7896
        },
        "Old Street": {
            "x": 1601.6152,
            "y": 777.5737
        },
        "St. John's Wood": {
            "x": 1107.8843,
            "y": 656.855
        },
        "Green Park": {
            "x": 1164.9937,
            "y": 967.7651
        },
        "Baker Street": {
            "x": 1144.4443,
            "y": 736.3452
        },
        "Notting Hill Gate": {
            "x": 928.293,
            "y": 883.9458
        },
        "Victoria": {
            "x": 1092.4854,
            "y": 1084.4663
        },
        "Aldgate East": {
            "x": 1758.6113,
            "y": 901.8062
        },
        "Blackfriars": {
            "x": 1419.1143,
            "y": 1056.4956
        },
        "Mansion House": {
            "x": 1415.5142,
            "y": 1030.3452
        },
        "Cannon Street": {
            "x": 1448.7437,
            "y": 1004.187
        },
        "Oxford Circus": {
            "x": 1144.5732,
            "y": 883.9604
        },
        "Bond Street": {
            "x": 1069.5327,
            "y": 883.8521
        },
        "Tower Hill": {
            "x": 1670.1426,
            "y": 1025.0171
        },
        "Westminster": {
            "x": 1192.2622,
            "y": 1118.5874
        },
        "Tottenham Court Road": {
            "x": 1248.1416,
            "y": 926.3384
        },
        "Piccadilly Circus": {
            "x": 1205.0015,
            "y": 999.6538
        },
        "Charing Cross": {
            "x": 1263.7915,
            "y": 1045.7769
        },
        "Holborn": {
            "x": 1395.2007,
            "y": 916.3384
        },
        "Tower Gateway": {
            "x": 1755.4414,
            "y": 1037.7866
        },
        "Monument": {
            "x": 1594.9004,
            "y": 1016.647
        },
        "Moorgate": {
            "x": 1595.4512,
            "y": 867.396
        },
        "Leicester Square": {
            "x": 1345.042,
            "y": 975.1226
        },
        "London Bridge": {
            "x": 1587.3027,
            "y": 1138.4468
        },
        "St. Paul's": {
            "x": 1500.2715,
            "y": 907.8823
        },
        "Hyde Park Corner": {
            "x": 989.2388,
            "y": 1000.3374
        },
        "Knightsbridge": {
            "x": 984.6001,
            "y": 1026.8179
        },
        "Stamford Brook": {
            "x": 622.8711,
            "y": 1119.2085
        },
        "Ravenscourt Park": {
            "x": 683.3662,
            "y": 1119.2085
        },
        "West Kensington": {
            "x": 823.3809,
            "y": 1119.2085
        },
        "North Acton": {
            "x": 610.9263,
            "y": 927.5464
        },
        "Holland Park": {
            "x": 852.1147,
            "y": 917.5464
        },
        "Marylebone": {
            "x": 1011.0435,
            "y": 714.5503
        },
        "Angel": {
            "x": 1503.7129,
            "y": 753.1284
        },
        "Queensway": {
            "x": 954.1445,
            "y": 917.062
        },
        "South Kensington": {
            "x": 982.71,
            "y": 1121.3687
        },
        "Earl's Court": {
            "x": 893.5273,
            "y": 1121.3687
        },
        "Sloane Square": {
            "x": 1060.3921,
            "y": 1119.2476
        },
        "Covent Garden": {
            "x": 1370.1011,
            "y": 945.7612
        },
        "Liverpool Street": {
            "x": 1665.5508,
            "y": 816.6724
        },
        "Great Portland Street": {
            "x": 1211.1016,
            "y": 728.4517
        },
        "Bank": {
            "x": 1552.5215,
            "y": 928.5767
        },
        "East Acton": {
            "x": 668.5234,
            "y": 871.3335
        },
        "Chancery Lane": {
            "x": 1427.1406,
            "y": 876.7554
        },
        "Lancaster Gate": {
            "x": 1007.6011,
            "y": 881.8813
        },
        "Warwick Avenue": {
            "x": 699.9922,
            "y": 730.1206
        },
        "Maida Vale": {
            "x": 716.6992,
            "y": 711.3062
        },
        "Paddington": {
            "x": 853.8096,
            "y": 714.7612
        },
        "Baron's Court": {
            "x": 789.8198,
            "y": 1056.9448
        },
        "Gloucester Road": {
            "x": 937.4785,
            "y": 1056.7358
        },
        "St. James's Park": {
            "x": 1156.6636,
            "y": 1067.3745
        },
        "Temple": {
            "x": 1381.4531,
            "y": 1080.6851
        },
        "Latimer Road": {
            "x": 780.8276,
            "y": 847.687
        },
        "Ladbroke Grove": {
            "x": 803.417,
            "y": 825.0913
        },
        "Royal Oak": {
            "x": 765.9268,
            "y": 755.6851
        },
        "Westbourne Park": {
            "x": 697.8228,
            "y": 780.3599
        },
        "Bermondsey": {
            "x": 1681.9141,
            "y": 1131.605
        },
        "Rotherhithe": {
            "x": 1756.2051,
            "y": 1090.3745
        },
        "Shoreditch High Street": {
            "x": 1761.4844,
            "y": 822.4253
        },
        "Dalston Junction": {
            "x": 1722.6758,
            "y": 659.7378
        },
        "Haggerston": {
            "x": 1757.4453,
            "y": 709.1558
        },
        "Hoxton": {
            "x": 1781.666,
            "y": 758.5698
        },
        "Wood Lane": {
            "x": 685.4492,
            "y": 940.5767
        },
        "Shepherd's Bush": {
            "x": 791.8657,
            "y": 879.4976
        },
        "White City": {
            "x": 715.8872,
            "y": 869.7573
        },
        "King's Cross St. Pancras": {
            "x": 1398.7744,
            "y": 682.6167
        },
        "Euston Square": {
            "x": 1349.8145,
            "y": 780.5767
        },
        "Edgware Road": {
            "x": 982.7212,
            "y": 789.978
        },
        "Waterloo": {
            "x": 1233.7144,
            "y": 1167.7651
        },
        "Southwark": {
            "x": 1371.5142,
            "y": 1222.0054
        },
        "Embankment": {
            "x": 1356.7544,
            "y": 1120.8647
        },
        "Marble Arch": {
            "x": 1073.6084,
            "y": 916.062
        }
    }
    return tubestations
