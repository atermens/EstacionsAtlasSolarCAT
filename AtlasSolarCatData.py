#-------------------------------------------------------------------------------
# Name:        AtlasSolarCatData.py
# Purpose:     Merge information about Atlas Solar stations (Taula 1 and Taula 3),
#              only over Catalonia.
#              Output file is a GeoJSON, format to be ready for GIS evaluation.
#
# Author:      a.termens
#
# Created:     08/06/2021
# Copyright:   (c) a.termens 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
#
# Limits Catalunya: bbox = (Xmin,Ymin,Xmax,Ymax)
#
CATBBOX = [257000.0, 4484000.0, 536000.0, 4753000.0]
#
# EQUIPAMENT ESTACIONS:
#
EQUIP = { 1: "Siap\/Kipp-Zonen", 2: "Ph. Schenk", 3: "Campbell", 4: "Kipp-Zonen", 5: "Casella\/Campbell", 6: "Siap", 7: "Fuess\/Kipp-Konen" }
#
# TAULA1 = { "NOM": {"ID","UTMX","UTMY","H","EQUIP","NUM_YEARS","CENTER"}...}
#
TAULA1_KEYS = ["ID","UTMX","UTMY","H","EQUIP","NUM_YEARS","CENTER"]

TAULA1 = {}
TAULA1["AGONCI"] = { "ID":  1, "UTMX":  62000.0, "UTMY": 4714000.0, "H":  352.0, "EQUIP": 1, "NUM_YEARS": 11.4, "CENTER": "INM" }
TAULA1["AGULLA"] = { "ID":  2, "UTMX": 487000.0, "UTMY": 4694000.0, "H":  217.0, "EQUIP": 2, "NUM_YEARS":  4.4, "CENTER": "DMA" }
TAULA1["ALCANA"] = { "ID":  3, "UTMX": 290000.0, "UTMY": 4493000.0, "H":   35.0, "EQUIP": 3, "NUM_YEARS":  6.5, "CENTER": "DARP" }
TAULA1["ALCOVE"] = { "ID":  4, "UTMX": 347000.0, "UTMY": 4570000.0, "H":  246.0, "EQUIP": 2, "NUM_YEARS":  4.6, "CENTER": "DMA" }
TAULA1["ALDEA"]  = { "ID":  5, "UTMX": 299000.0, "UTMY": 4516000.0, "H":   62.0, "EQUIP": 3, "NUM_YEARS":  2.8, "CENTER": "DARP" }
TAULA1["ALFACS"] = { "ID":  6, "UTMX": 302000.0, "UTMY": 4500000.0, "H":    0.5, "EQUIP": 3, "NUM_YEARS":  1.5, "CENTER": "DARP" }
TAULA1["ALP"]    = { "ID":  7, "UTMX": 408000.0, "UTMY": 4692000.0, "H": 1200.0, "EQUIP": 4, "NUM_YEARS":  0.8, "CENTER": "ICAEN" }
TAULA1["AMETLL"] = { "ID":  8, "UTMX": 312000.0, "UTMY": 4531000.0, "H":   95.0, "EQUIP": 3, "NUM_YEARS":  2.3, "CENTER": "DARP" }
TAULA1["AMPOST"] = { "ID":  9, "UTMX": 300000.0, "UTMY": 4509000.0, "H":    3.5, "EQUIP": 3, "NUM_YEARS":  5.0, "CENTER": "DARP" }
TAULA1["ANDORR"] = { "ID": 10, "UTMX": 380000.0, "UTMY": 4708000.0, "H": 1100.0, "EQUIP": 4, "NUM_YEARS":  4.1, "CENTER": "AND" }
TAULA1["AVELLA"] = { "ID": 11, "UTMX":  31000.0, "UTMY": 4639000.0, "H":  580.0, "EQUIP": 3, "NUM_YEARS":  2.3, "CENTER": "DARP" }
TAULA1["BALAGU"] = { "ID": 12, "UTMX": 320000.0, "UTMY": 4628000.0, "H":  245.0, "EQUIP": 3, "NUM_YEARS":  5.8, "CENTER": "DARP" }
TAULA1["BARCEL"] = { "ID": 13, "UTMX": 426000.0, "UTMY": 4582000.0, "H":   99.0, "EQUIP": , 4, "NUM_YEARS": 10.2, "CENTER": "UB\/ICAEN" }
TAULA1["BELLAT"] = { "ID": 14, "UTMX": 423000.0, "UTMY": 4595000.0, "H":  120.0, "EQUIP": 4, "NUM_YEARS":  1.6, "CENTER": "UAB" }
TAULA1["BENISS"] = { "ID": 15, "UTMX": 301000.0, "UTMY": 4549000.0, "H":   30.0, "EQUIP": 3, "NUM_YEARS":  4.0, "CENTER": "DARP" }
TAULA1["BISCAR"] = { "ID": 16, "UTMX": 162000.0, "UTMY": 4929000.0, "H":   48.0, "EQUIP": 4, "NUM_YEARS": 15.7, "CENTER": "MF" }
TAULA1["CABANE"] = { "ID": 17, "UTMX": 496000.0, "UTMY": 4684000.0, "H":   31.0, "EQUIP": 3, "NUM_YEARS":  1.6, "CENTER": "DARP" }
TAULA1["CABRIL"] = { "ID": 18, "UTMX": 448000.0, "UTMY": 4597000.0, "H":   82.0, "EQUIP": 5, "NUM_YEARS":  6.7, "CENTER": "IRTA\/DARP" }
TAULA1["CAMBRI"] = { "ID": 19, "UTMX": 338000.0, "UTMY": 4550000.0, "H":   24.0, "EQUIP": 3, "NUM_YEARS":  3.7, "CENTER": "DARP" }
TAULA1["CARCAS"] = { "ID": 20, "UTMX": 444000.0, "UTMY": 4785000.0, "H":  130.0, "EQUIP": 4, "NUM_YEARS": 15.9, "CENTER": "MF" }
TAULA1["CASES"]  = { "ID": 21, "UTMX": 291000.0, "UTMY": 4492000.0, "H":    4.0, "EQUIP": 4, "NUM_YEARS":  3.8, "CENTER": "DARP" }
TAULA1["CASTEL"] = { "ID": 22, "UTMX": 238000.0, "UTMY": 4427000.0, "H":   35.0, "EQUIP": 4, "NUM_YEARS":  2.0, "CENTER": "INM" }
TAULA1["COMPAN"] = { "ID": 23, "UTMX": 432000.0, "UTMY": 4583000.0, "H":    7.0, "EQUIP": 2, "NUM_YEARS":  1.8, "CENTER": "DMA" }
TAULA1["CORRED"] = { "ID": 24, "UTMX": 454000.0, "UTMY": 4608000.0, "H":  460.0, "EQUIP": 3, "NUM_YEARS":  1.2, "CENTER": "DARP" }
TAULA1["CQUERA"] = { "ID": 25, "UTMX": 364000.0, "UTMY": 4599000.0, "H":  718.0, "EQUIP": 3, "NUM_YEARS":  1.1, "CENTER": "DARP" }
TAULA1["DELTEB"] = { "ID": 26, "UTMX": 310000.0, "UTMY": 4518000.0, "H":    1.5, "EQUIP": 3, "NUM_YEARS":  4.9, "CENTER": "DARP" }
TAULA1["EIVISS"] = { "ID": 27, "UTMX": 360000.0, "UTMY": 4304000.0, "H":   12.0, "EQUIP": 4, "NUM_YEARS":  3.0, "CENTER": "INM" }
TAULA1["EMECA"]  = { "ID": 28, "UTMX": 300000.0, "UTMY": 4612000.0, "H":  190.0, "EQUIP": 3, "NUM_YEARS":  5.2, "CENTER": "DARP" }
TAULA1["ESTMOL"] = { "ID": 29, "UTMX": 413000.0, "UTMY": 4687000.0, "H": 1500.0, "EQUIP": 6, "NUM_YEARS":  5.0, "CENTER": "INM" }
TAULA1["FELIU"]  = { "ID": 30, "UTMX": 503000.0, "UTMY": 4626000.0, "H":   20.0, "EQUIP": 4, "NUM_YEARS":  2.3, "CENTER": "ICAEN" }
TAULA1["FORNEL"] = { "ID": 31, "UTMX": 484000.0, "UTMY": 4642000.0, "H":  101.0, "EQUIP": 2, "NUM_YEARS":  3.6, "CENTER": "DMA" }
TAULA1["GIMENE"] = { "ID": 32, "UTMX": 283000.0, "UTMY": 4615000.0, "H":  248.0, "EQUIP": 3, "NUM_YEARS":  1.0, "CENTER": "DARP" }
TAULA1["GIRONA"] = { "ID": 33, "UTMX": 485000.0, "UTMY": 4647000.0, "H":  100.0, "EQUIP": 4, "NUM_YEARS":  9.1, "CENTER": "ICAEN" }
TAULA1["GORIZ"]  = { "ID": 34, "UTMX": 254000.0, "UTMY": 4726000.0, "H": 2215.0, "EQUIP": 6, "NUM_YEARS":  6.0, "CENTER": "INM" }
TAULA1["GRANAD"] = { "ID": 35, "UTMX": 305000.0, "UTMY": 4582000.0, "H":  490.0, "EQUIP": 3, "NUM_YEARS":  4.7, "CENTER": "DARP" }
TAULA1["IGUALA"] = { "ID": 36, "UTMX": 386000.0, "UTMY": 4604000.0, "H":  309.0, "EQUIP": 2, "NUM_YEARS":  1.0, "CENTER": "DMA" }
TAULA1["JUNEDA"] = { "ID": 37, "UTMX": 318000.0, "UTMY": 4603000.0, "H":  275.0, "EQUIP": 2, "NUM_YEARS":  4.3, "CENTER": "DMA" }
TAULA1["LAQUAR"] = { "ID": 38, "UTMX": 414000.0, "UTMY": 4659000.0, "H":  864.0, "EQUIP": 2, "NUM_YEARS":  1.6, "CENTER": "DMA" }
TAULA1["LLANCA"] = { "ID": 39, "UTMX": 513000.0, "UTMY": 4690000.0, "H":   20.0, "EQUIP": 4, "NUM_YEARS":  5.4, "CENTER": "ICAEN" }
TAULA1["LLEIDA"] = { "ID": 40, "UTMX": 301000.0, "UTMY": 4611000.0, "H":  199.0, "EQUIP": 1, "NUM_YEARS":  4.0, "CENTER": "INM\/ICAEN" }
TAULA1["LOGRON"] = { "ID": 41, "UTMX":  49000.0, "UTMY": 4720000.0, "H":  364.0, "EQUIP": 4, "NUM_YEARS":  5.5, "CENTER": "INM" }
TAULA1["MAHON"]  = { "ID": 42, "UTMX": 607000.0, "UTMY": 4416000.0, "H":   82.0, "EQUIP": 6, "NUM_YEARS": 12.9, "CENTER": "INM" }
TAULA1["MALGRA"] = { "ID": 43, "UTMX": 479000.0, "UTMY": 4611000.0, "H":    4.5, "EQUIP": 3, "NUM_YEARS":  3.8, "CENTER": "DARP" }
TAULA1["MARIGN"] = { "ID": 45, "UTMX": 681000.0, "UTMY": 4813000.0, "H":    8.0, "EQUIP": 4, "NUM_YEARS": 15.4, "CENTER": "MF" }
TAULA1["MARTOR"] = { "ID": 46, "UTMX": 410000.0, "UTMY": 4592000.0, "H":   77.0, "EQUIP": 2, "NUM_YEARS":  2.4, "CENTER": "DMA" }
TAULA1["MASBOV"] = { "ID": 47, "UTMX": 347000.0, "UTMY": 4560000.0, "H":  105.0, "EQUIP": 3, "NUM_YEARS":  6.4, "CENTER": "DARP" }
TAULA1["MJULIA"] = { "ID": 48, "UTMX": 270000.0, "UTMY": 4627000.0, "H":  340.0, "EQUIP": 3, "NUM_YEARS":  3.3, "CENTER": "DARP" }
TAULA1["MOLINA"] = { "ID": 49, "UTMX":  88000.0, "UTMY": 4533000.0, "H": 1063.0, "EQUIP": 6, "NUM_YEARS":  4.0, "CENTER": "INM" }
TAULA1["MONTPE"] = { "ID": 50, "UTMX": 578000.0, "UTMY": 4826000.0, "H":    6.0, "EQUIP": 4, "NUM_YEARS": 14.7, "CENTER": "MF" }
TAULA1["MONTSE"] = { "ID": 51, "UTMX": 442000.0, "UTMY": 4622000.0, "H":  990.0, "EQUIP": 3, "NUM_YEARS":  1.1, "CENTER": "DARP" }
TAULA1["MVECIA"] = { "ID": 52, "UTMX": 370000.0, "UTMY": 4614000.0, "H":  726.0, "EQUIP": 2, "NUM_YEARS":  1.5, "CENTER": "DMA" }
TAULA1["NOAIN"]  = { "ID": 53, "UTMX": 120000.0, "UTMY": 4745000.0, "H":  461.0, "EQUIP": 6, "NUM_YEARS":  3.0, "CENTER": "INM" }
TAULA1["PALAUT"] = { "ID": 55, "UTMX": 454000.0, "UTMY": 4616000.0, "H":  215.0, "EQUIP": 2, "NUM_YEARS":  4.8, "CENTER": "DMA" }
TAULA1["PALMA"]  = { "ID": 56, "UTMX": 478000.0, "UTMY": 4379000.0, "H":    7.0, "EQUIP": 4, "NUM_YEARS": 20.3, "CENTER": "INM" }
TAULA1["PAU"]    = { "ID": 57, "UTMX": 223000.0, "UTMY": 4809000.0, "H":  185.0, "EQUIP": 4, "NUM_YEARS": 15.9, "CENTER": "MF" }
TAULA1["PERAFI"] = { "ID": 58, "UTMX": 427000.0, "UTMY": 4655000.0, "H":  770.0, "EQUIP": 3, "NUM_YEARS":  2.5, "CENTER": "DARP" }
TAULA1["PERPIG"] = { "ID": 59, "UTMX": 489000.0, "UTMY": 4731000.0, "H":   48.0, "EQUIP": 4, "NUM_YEARS": 16.0, "CENTER": "MF" }
TAULA1["PINOS"]  = { "ID": 60, "UTMX": 377000.0, "UTMY": 4628000.0, "H":  650.0, "EQUIP": 3, "NUM_YEARS":  2.5, "CENTER": "DARP" }
TAULA1["PSUERT"] = { "ID": 61, "UTMX": 314000.0, "UTMY": 4697000.0, "H":  824.0, "EQUIP": 2, "NUM_YEARS":  1.0, "CENTER": "DM" }
TAULA1["RAIMAT"] = { "ID": 62, "UTMX": 288000.0, "UTMY": 4618000.0, "H":  290.0, "EQUIP": 3, "NUM_YEARS":  5.1, "CENTER": "DARP" }
TAULA1["ROQUET"] = { "ID": 63, "UTMX": 288000.0, "UTMY": 4522000.0, "H":   50.0, "EQUIP": 4, "NUM_YEARS":  6.3, "CENTER": "INM" }
TAULA1["SABADE"] = { "ID": 64, "UTMX": 425000.0, "UTMY": 4602000.0, "H":  213.0, "EQUIP": 2, "NUM_YEARS":  3.7, "CENTER": "DMA" }
TAULA1["SANPER"] = { "ID": 65, "UTMX": 508000.0, "UTMY": 4670000.0, "H":    5.0, "EQUIP": 3, "NUM_YEARS":  7.4, "CENTER": "DARP" }
TAULA1["SARRIA"] = { "ID": 66, "UTMX": 485000.0, "UTMY": 4652000.0, "H":   65.0, "EQUIP": 2, "NUM_YEARS":  5.4, "CENTER": "DMA" }
TAULA1["SCUGAT"] = { "ID": 67, "UTMX": 424000.0, "UTMY": 4592000.0, "H":  113.0, "EQUIP": 2, "NUM_YEARS":  3.8, "CENTER": "DMA" }
TAULA1["SOR_MA"] = { "ID": 68, "UTMX": 346000.0, "UTMY": 4697000.0, "H":  682.0, "EQUIP": 2, "NUM_YEARS":  3.9, "CENTER": "DMA" }
TAULA1["SORT"]   = { "ID": 69, "UTMX": 346000.0, "UTMY": 4697000.0, "H":  700.0, "EQUIP": 4, "NUM_YEARS":  6.6, "CENTER": "ICAEN" }
TAULA1["STAPAU"] = { "ID": 70, "UTMX": 460000.0, "UTMY": 4666000.0, "H":  569.0, "EQUIP": 2, "NUM_YEARS":  1.9, "CENTER": "DMA" }
TAULA1["STCELO"] = { "ID": 71, "UTMX": 458000.0, "UTMY": 4616000.0, "H":  143.0, "EQUIP": 2, "NUM_YEARS":  3.8, "CENTER": "DMA" }
TAULA1["STFOST"] = { "ID": 72, "UTMX": 435000.0, "UTMY": 4598000.0, "H":   56.0, "EQUIP": 2, "NUM_YEARS":  1.5, "CENTER": "DMA" }
TAULA1["TARRAG"] = { "ID": 73, "UTMX": 349000.0, "UTMY": 4552000.0, "H":    8.0, "EQUIP": 4, "NUM_YEARS":  8.5, "CENTER": "ICAEN" }
TAULA1["TERRAS"] = { "ID": 74, "UTMX": 422000.0, "UTMY": 4601000.0, "H":  224.0, "EQUIP": 4, "NUM_YEARS":  2.9, "CENTER": "ICAEN" }
TAULA1["TORRE"]  = { "ID": 75, "UTMX": 431000.0, "UTMY": 4607000.0, "H":  130.0, "EQUIP": 3, "NUM_YEARS":  3.8, "CENTER": "DARP" }
TAULA1["ULLDEC"] = { "ID": 76, "UTMX": 278000.0, "UTMY": 4501000.0, "H":  225.0, "EQUIP": 3, "NUM_YEARS":  3.0, "CENTER": "DARP" }
TAULA1["V_GELT"] = { "ID": 77, "UTMX": 393000.0, "UTMY": 4564000.0, "H":   14.0, "EQUIP": 2, "NUM_YEARS":  3.4, "CENTER": "DMA" }
TAULA1["VALENC"] = { "ID": 78, "UTMX": 209000.0, "UTMY": 4376000.0, "H":   11.0, "EQUIP": 7, "NUM_YEARS": 11.0, "CENTER": "INM\/UV" }
TAULA1["VANDEL"] = { "ID": 79, "UTMX": 320000.0, "UTMY": 4535000.0, "H":   25.0, "EQUIP": 6, "NUM_YEARS":  7.9, "CENTER": "CNV" }
TAULA1["VECIAN"] = { "ID": 80, "UTMX": 370000.0, "UTMY": 4614000.0, "H":  726.0, "EQUIP": 4, "NUM_YEARS": 10.5, "CENTER": "ICAEN" }
TAULA1["VILADR"] = { "ID": 81, "UTMX": 452000.0, "UTMY": 4633000.0, "H":  860.0, "EQUIP": 3, "NUM_YEARS":  2.2, "CENTER": "DARP" }
TAULA1["VILASE"] = { "ID": 82, "UTMX": 345000.0, "UTMY": 4553000.0, "H":   41.0, "EQUIP": 2, "NUM_YEARS":  1.7, "CENTER": "DMA" }
TAULA1["ZARAGO"] = { "ID": 83, "UTMX": 166000.0, "UTMY": 4620000.0, "H":  240.0, "EQUIP": 6, "NUM_YEARS":  4.0, "CENTER": "UZ" }
#
# TAULA3["NOM"] = rad_glob_list
# where rad_glob_list:
#  0 ... M (MJ/m2), mean irradiation
#  1 ... A (MJ/m2)
#  2 ... B (radians)
#  define the irradiation at D applying the model I = M + cos(w*D+B), where D is Day Of Year (i.e DOY)
#  3 ... I01: January (MJ/m2)
#  4 ... I02: February (MJ/m2)
#  5 ... I03: March (MJ/m2)
#  6 ... I04: April (MJ/m2)
#  7 ... I05: May (MJ/m2)
#  8 ... I06: June (MJ/m2)
#  9 ... I07: July (MJ/m2)
# 10 ... I08: August (MJ/m2)
# 11 ... I09: September (MJ/m2)
# 12 ... I10: October (MJ/m2)
# 13 ... I11: November (MJ/m2)
# 14 ... I12: December (MJ/m2)
#
TAULA3_KEYS = [ "M", "A", "B", "I01","I02","I03","I04","I05","I06","I07","I08","I09","I10","I11","I12" ]

TAULA3 = {}
TAULA3["AGONCI"] = [ 14.82,  9.62, 3.25, 5.95, 8.71,13.04,17.96,22.03,24.17,23.78,20.92,16.44,11.53,7.50,5.45 ]
TAULA3["AGULLA"] = [ 14.09,  8.38, 3.37, 6.77, 9.57,13.52,17.74,20.97,22.36,21.51,18.60,14.52,10.31,7.12,5.82 ]
TAULA3["ALCANA"] = [ 15.03,  8.79, 3.34, 7.23,10.07,14.18,18.63,22.10,23.68,22.92,19.98,15.74,11.30,7.87,6.37 ]
TAULA3["ALCOVE"] = [ 14.14,  8.69, 3.44, 6.85, 9.97,14.15,18.46,21.60,22.73,21.55,18.30,13.98, 9.70,6.61,5.55 ]
TAULA3["ALDEA"]  = [ 15.12,  8.78, 3.36, 7.41,10.31,14.44,18.87,22.28,23.78,22.93,19.92,15.65,11.24,7.87,6.46 ]
TAULA3["ALFACS"] = [ 15.15,  9.68, 3.35, 6.61, 9.77,14.30,19.20,22.99,24.69,23.80,20.52,15.83,10.96,7.21,5.61 ]
TAULA3["ALP"]    = [ 15.06,  9.01, 3.34, 7.07, 9.97,14.18,18.75,22.31,23.93,23.15,20.13,15.78,11.24,7.72,6.18 ]
TAULA3["AMETLL"] = [ 15.21,  9.25, 3.32, 6.93, 9.84,14.13,18.83,22.55,24.30,23.59,20.57,16.14,11.45,7.78,6.11 ]
TAULA3["AMPOST"] = [ 14.78,  8.89, 3.36, 6.97, 9.91,14.09,18.58,22.03,23.55,22.69,19.64,15.32,10.85,7.44,6.01 ]
TAULA3["ANDORR"] = [ 13.77,  8.08, 3.31, 6.50, 9.01,12.75,16.86,20.13,21.70,21.12,18.51,14.66,10.56,7.32,5.83 ]
TAULA3["AVELLA"] = [ 16.10, 10.48, 3.30, 6.63, 9.85,14.67,20.01,24.29,26.37,25.68,22.34,17.35,12.03,7.80,5.81 ]
TAULA3["BALAGU"] = [ 15.12, 10.32, 3.29, 5.75, 8.88,13.61,18.87,23.12,25.22,24.59,21.34,16.46,11.21,7.01,5.00 ]
TAULA3["BARCEL"] = [ 15.04,  9.16, 3.31, 6.80, 9.65,13.88,18.54,22.25,24.03,23.37,20.42,16.05,11.40,7.73,6.04 ]
TAULA3["BELLAT"] = [ 14.93,  8.83, 3.29, 6.92, 9.59,13.64,18.14,21.77,23.57,23.03,20.25,16.07,11.58,7.99,6.27 ]
TAULA3["BENISS"] = [ 15.14,  9.39, 3.35, 6.85, 9.92,14.32,19.07,22.75,24.39,23.53,20.35,15.80,11.07,7.43,5.88 ]
TAULA3["BISCAR"] = [ 13.46,  9.47, 3.29, 4.86, 7.74,12.08,16.90,20.80,22.73,22.15,19.17,14.69, 9.87,6.02,4.18 ]
TAULA3["CABANE"] = [ 13.80,  8.62, 3.35, 6.19, 9.01,13.05,17.40,20.79,22.29,21.50,18.58,14.41,10.07,6.73,5.30 ]
TAULA3["CABRIL"] = [ 15.53,  9.57, 3.28, 6.81, 9.67,14.04,18.92,22.89,24.88,24.34,21.38,16.86,11.99,8.07,6.16 ]
TAULA3["CAMBRI"] = [ 14.60,  8.94, 3.42, 7.01,10.15,14.44,18.89,22.18,23.44,22.31,19.04,14.61,10.18,6.94,5.77 ]
TAULA3["CARCAS"] = [ 13.57,  9.21, 3.26, 5.11, 7.79,11.95,16.66,20.54,22.54,22.12,19.34,15.03,10.33,6.50,4.58 ]
TAULA3["CASES"]  = [ 15.17,  9.15, 3.34, 7.05,10.01,14.28,18.91,22.53,24.18,23.39,20.32,15.91,11.29,7.71,6.15 ]
TAULA3["CASTEL"] = [ 15.95,  8.82, 3.28, 7.91,10.55,14.57,19.08,22.73,24.57,24.07,21.34,17.18,12.69,9.07,7.32 ]
TAULA3["COMPAN"] = [ 15.87,  9.18, 3.39, 7.94,11.07,15.43,20.03,23.51,24.94,23.91,20.66,16.15,11.57,8.14,6.80 ]
TAULA3["CORRED"] = [ 14.95,  9.57, 3.35, 6.50, 9.63,14.11,18.95,22.71,24.38,23.50,20.26,15.62,10.80,7.10,5.51 ]
TAULA3["CQUERA"] = [ 15.48,  9.88, 3.33, 6.67, 9.82,14.42,19.43,23.37,25.20,24.39,21.12,16.37,11.38,7.48,5.75 ]
TAULA3["DELTEB"] = [ 15.13,  9.08, 3.36, 7.16,10.15,14.43,19.01,22.54,24.08,23.21,20.09,15.68,11.12,7.63,6.17 ]
TAULA3["EIVISS"] = [ 16.43,  9.61, 3.35, 7.95,11.08,15.59,20.45,24.22,25.90,25.02,21.76,17.11,12.27,8.54,6.95 ]
TAULA3["EMECA"]  = [ 14.69, 10.65, 3.33, 5.20, 8.59,13.55,18.95,23.20,25.17,24.30,20.77,15.65,10.27,6.07,4.21 ]
TAULA3["ESTMOL"] = [ 14.93,  8.44, 3.20, 7.00, 9.25,12.96,17.29,20.98,23.05,22.92,20.59,16.76,12.44,8.78,6.79 ]
TAULA3["FELIU"]  = [ 14.23,  8.53, 3.27, 6.42, 8.94,12.82,17.17,20.73,22.55,22.12,19.51,15.50,11.15,7.63,5.89 ]
TAULA3["FORNEL"] = [ 14.74,  8.41, 3.37, 7.39,10.20,14.17,18.41,21.65,23.04,22.18,19.27,15.17,10.95,7.75,6.44 ]
TAULA3["GIMENE"] = [ 15.52, 10.57, 3.28, 5.89, 9.05,13.87,19.27,23.65,25.85,25.26,21.98,16.99,11.61,7.28,5.17 ]
TAULA3["GIRONA"] = [ 14.30,  8.47, 3.34, 6.79, 9.52,13.48,17.77,21.12,22.64,21.91,19.07,14.98,10.71,7.40,5.95 ]
TAULA3["GORIZ"]  = [ 16.40,  7.92, 3.40, 9.59,12.32,16.10,20.06,23.03,24.23,23.30,20.47,16.57,12.62,9.69,8.57 ]
TAULA3["GRANAD"] = [ 15.19,  9.59, 3.36, 6.77, 9.93,14.45,19.29,23.02,24.65,23.72,20.43,15.77,10.95,7.27,5.73 ]
TAULA3["IGUALA"] = [ 14.95,  9.18, 3.36, 6.89, 9.92,14.24,18.87,22.44,24.00,23.12,19.97,15.51,10.89,7.37,5.89 ]
TAULA3["JUNEDA"] = [ 16.20, 10.01, 3.34, 7.32,10.55,15.23,20.30,24.25,26.06,25.19,21.84,17.00,11.95,8.04,6.34 ]
TAULA3["LAQUAR"] = [ 14.63,  9.84, 3.37, 6.03, 9.32,13.96,18.92,22.71,24.34,23.34,19.93,15.13,10.19,6.45,4.92 ]
TAULA3["LLANCA"] = [ 13.71,  9.32, 3.34, 5.44, 8.45,12.80,17.52,21.21,22.89,22.08,18.96,14.46, 9.76,6.11,4.53 ]
TAULA3["LLEIDA"] = [ 15.87, 10.60, 3.33, 6.42, 9.80,14.74,20.11,24.34,26.30,25.43,21.93,16.83,11.47,7.29,5.43 ]
TAULA3["LOGRON"] = [ 14.35,  9.36, 3.26, 5.75, 8.48,12.71,17.49,21.43,23.47,23.04,20.21,15.84,11.06,7.16,5.21 ]
TAULA3["MAHON"]  = [ 15.68,  8.63, 3.26, 7.75,10.26,14.17,18.58,22.21,24.09,23.69,21.08,17.05,12.65,9.05,7.26 ]
TAULA3["MALGRA"] = [ 14.08,  8.92, 3.35, 6.21, 9.12,13.30,17.81,21.31,22.87,22.05,19.03,14.71,10.22,6.76,5.29 ]
TAULA3["MANRES"] = [ 14.90,  9.56, 3.32, 6.34, 9.35,13.78,18.64,22.48,24.29,23.56,20.44,15.86,11.02,7.22,5.50 ]
TAULA3["MARIGN"] = [ 14.51,  9.53, 3.29, 5.86, 8.75,13.12,17.98,21.90,23.84,23.25,20.26,15.74,10.90,7.02,5.17 ]
TAULA3["MARTOR"] = [ 14.30,  7.97, 3.31, 7.13, 9.61,13.29,17.34,20.57,22.12,21.55,18.98,15.18,11.13,7.94,6.47 ]
TAULA3["MASBOV"] = [ 14.83,  9.09, 3.36, 6.85, 9.85,14.13,18.71,22.25,23.79,22.92,19.80,15.38,10.81,7.32,5.86 ]
TAULA3["MJULIA"] = [ 14.31, 10.02, 3.25, 5.07, 7.94,12.45,17.58,21.82,24.05,23.64,20.66,16.00,10.88,6.68,4.55 ]
TAULA3["MOLINA"] = [ 16.62,  9.52, 3.20, 7.68,10.22,14.40,19.28,23.44,25.78,25.63,23.01,18.69,13.81,9.68,7.43 ]
TAULA3["MONTPE"] = [ 14.55,  9.80, 3.29, 5.66, 8.63,13.12,18.11,22.15,24.14,23.54,20.46,15.82,10.83,6.85,4.94 ]
TAULA3["MONTSE"] = [ 13.65,  8.00, 3.44, 6.94, 9.81,13.66,17.63,20.51,21.56,20.47,17.48,13.50, 9.56,6.71,5.75 ]
TAULA3["MVECIA"] = [ 15.16,  9.87, 3.31, 6.28, 9.35,13.91,18.93,22.93,24.85,24.14,20.96,16.24,11.24,7.28,5.46 ]
TAULA3["NOAIN"]  = [ 14.44,  9.66, 3.18, 5.31, 7.81,12.00,16.96,21.23,23.69,23.64,21.06,16.72,11.77,7.53,5.16 ]
TAULA3["ODEILL"] = [ 15.88,  8.59, 3.27, 8.02,10.55,14.46,18.84,22.43,24.26,23.82,21.19,17.16,12.78,9.23,7.48 ]
TAULA3["PALAUT"] = [ 14.64,  8.43, 3.36, 7.24,10.02,13.99,18.24,21.52,22.95,22.14,19.25,15.15,10.91,7.68,6.32 ]
TAULA3["PALMA"]  = [ 15.82,  9.37, 3.29, 7.32,10.16,14.45,19.23,23.08,24.99,24.42,21.47,17.03,12.27,8.45,6.64 ]
TAULA3["PAU"]    = [ 12.43,  7.65, 3.29, 5.49, 7.81,11.31,15.21,18.36,19.92,19.45,17.04,13.42, 9.53,6.42,4.93 ]
TAULA3["PERAFI"] = [ 14.75,  9.48, 3.34, 6.34, 9.40,13.83,18.63,22.38,24.08,23.26,20.09,15.51,10.73,7.02,5.41 ]
TAULA3["PERPIG"] = [ 14.22,  8.93, 3.30, 6.15, 8.89,13.00,17.55,21.20,22.97,22.38,19.53,15.29,10.75,7.15,5.46 ]
TAULA3["PINOS"]  = [ 14.55, 10.01, 3.34, 5.67, 8.90,13.58,18.65,22.60,24.41,23.54,20.19,15.35,10.30,6.39,4.69 ]
TAULA3["PSUERT"] = [ 14.97,  7.99, 3.44, 8.27,11.13,14.98,18.94,21.82,22.87,21.78,18.80,14.82,10.89,8.04,7.08 ]
TAULA3["RAIMAT"] = [ 14.47, 10.66, 3.32, 4.92, 8.28,13.22,18.64,22.92,24.94,24.13,20.65,15.54,10.14,5.90,3.99 ]
TAULA3["ROQUET"] = [ 15.05,  8.63, 3.31, 7.29, 9.97,13.96,18.35,21.84,23.52,22.90,20.12,16.00,11.62,8.16,6.57 ]
TAULA3["SABADE"] = [ 13.98,  8.86, 3.33, 6.08, 8.91,13.03,17.52,21.06,22.69,21.97,19.04,14.78,10.30,6.81,5.26 ]
TAULA3["SANPER"] = [ 13.88,  8.66, 3.36, 6.28, 9.13,13.21,17.58,20.95,22.42,21.58,18.62,14.40,10.05,6.73,5.34 ]
TAULA3["SARRIA"] = [ 14.41,  8.03, 3.39, 7.47,10.21,14.02,18.05,21.09,22.34,21.45,18.60,14.66,10.65,7.65,6.48 ]
TAULA3["SCUGAT"] = [ 15.19,  9.14, 3.38, 7.25,10.33,14.66,19.26,22.75,24.22,23.24,20.04,15.56,10.99,7.54,6.16 ]
TAULA3["SOR_MA"] = [ 15.16,  8.50, 3.39, 7.82,10.71,14.75,19.02,22.23,23.56,22.61,19.60,15.42,11.18,8.00,6.76 ]
TAULA3["SORT"]   = [ 14.68,  9.03, 3.34, 6.67, 9.58,13.80,18.37,21.95,23.57,22.79,19.77,15.41,10.85,7.32,5.78 ]
TAULA3["STAPAU"] = [ 14.01,  7.42, 3.39, 7.60,10.13,13.65,17.38,20.19,21.34,20.51,17.88,14.24,10.54,7.76,6.68 ]
TAULA3["STCELO"] = [ 14.61,  8.86, 3.36, 6.83, 9.75,13.92,18.39,21.84,23.35,22.49,19.45,15.15,10.69,7.29,5.87 ]
TAULA3["STFOST"] = [ 15.19,  9.32, 3.34, 6.92, 9.93,14.28,19.00,22.69,24.37,23.56,20.44,15.94,11.24,7.59,6.01 ]
TAULA3["TARRAG"] = [ 15.79,  9.60, 3.34, 7.28,10.37,14.86,19.72,23.51,25.24,24.41,21.20,16.56,11.72,7.97,6.33 ]
TAULA3["TERRAS"] = [ 15.07,  9.10, 3.37, 7.12,10.16,14.45,19.04,22.55,24.05,23.12,19.97,15.53,10.97,7.50,6.09 ]
TAULA3["TORRE"]  = [ 13.45,  7.75, 3.38, 6.72, 9.33,13.00,16.90,19.86,21.10,20.28,17.56,13.77, 9.89,6.96,5.80 ]
TAULA3["ULLDEC"] = [ 14.50,  8.81, 3.27, 6.44, 9.04,13.04,17.54,21.22,23.10,22.65,19.95,15.81,11.32,7.68,5.89 ]
TAULA3["V_GELT"] = [ 15.54,  8.91, 3.40, 7.88,10.96,15.20,19.66,23.00,24.35,23.31,20.11,15.73,11.29,7.99,6.74 ]
TAULA3["VALENC"] = [ 16.17,  8.89, 3.31, 8.17,10.94,15.04,19.57,23.17,24.89,24.26,21.39,17.15,12.64,9.08,7.44 ]
TAULA3["VANDEL"] = [ 15.64,  9.02, 3.26, 7.35, 9.98,14.06,18.67,22.46,24.43,24.01,21.29,17.07,12.47,8.72,6.84 ]
TAULA3["VECIAN"] = [ 15.79,  9.83, 3.35, 7.11,10.32,14.93,19.90,23.76,25.48,24.58,21.25,16.48,11.53,7.72,6.10 ]
TAULA3["VILADR"] = [ 12.66,  8.32, 3.31, 5.18, 7.76,11.61,15.84,19.21,20.82,20.23,17.55,13.57, 9.35,6.02,4.49 ]
TAULA3["VILASE"] = [ 15.52,  8.88, 3.34, 7.64,10.51,14.66,19.15,22.67,24.26,23.49,20.52,16.23,11.75,8.28,6.77 ]
TAULA3["ZARAGO"] = [ 16.55, 10.37, 3.23, 6.91, 9.81,14.43,19.74,24.19,26.59,26.27,23.28,18.50,13.19,8.79,6.48 ]



def mergeTaules():
    FeaturesPropertiesDict = {}
    for ele in TAULA1.keys():
        # ele is the station name ("NOM")
        
        PropertiesDict = { k: TAULA1[ele][k] for k in TAULA1_KEYS }
        # mirem si existeix informacio a la TAULA2
        if ele in TAULA3.keys():
            # carreguem les dades de la TAULA3 (array)
            if len(TAULA3_KEYS) == len(TAULA3[ele]):
                PropertiesDict.update( { TAULA3_KEYS[i]: TAULA3[ele][i] for i in range(len(TAULA3_KEYS)) } )
            else:
                print (ele, "TAULA3_KEYS and TAULA3 has different lengths")
                PropertiesDict.update( { k: 0.0 for k in TAULA3_KEYS } )
        else:
            # no existeix, inicialitzem dades a 0.0
            print ("{} not found in TAULA3".format(ele))
            PropertiesDict.update( { k: 0.0 for k in TAULA3_KEYS } )

        FeaturesPropertiesDict[ele] = PropertiesDict
    return FeaturesPropertiesDict



def IsCatalunya(x,y):
    # CATBBOX = [257000.0,4484000.0,536000.0,4753000.0]
    bX = (CATBBOX[0]<x) and (x<CATBBOX[2])
    bY = (CATBBOX[1]<y) and (y<CATBBOX[3])
    return ( bX and bY )



def getFeature(ele, dict):
    # dict = FeaturesPropertiesDict[ele]
    sData = '{ "type": "Feature", "properties": { '
    sData += '"NOM": "' + ele + '", '
    for k in TAULA1_KEYS:
        if isinstance(dict[k],str):
            sData += '"{}": "{}", '.format(k,dict[k])
        else:
            sData += '"{}": {}, '.format(k,dict[k])
    for k in TAULA3_KEYS:
        sData += '"{}": {}, '.format(k,dict[k])
    # carreguem la irradiaciacio M en Wh/m2 (M esta en MJ/m2 )
    sData += '"IWHM2": {:8.2f} '.format(dict["M"]*1000.0/3.6)
    sData += '}, "geometry": { "type": "Point", "coordinates": [ '
    sData += '{}, {}, {} '.format(dict["UTMX"], dict["UTMY"], dict["H"])
    sData += '] } },\n'
    return sData



if __name__ == '__main__':
    AtlasData = mergeTaules()
    
    with open("AtlasSolarCATData.geojson", "w") as fout:
        fout.write('{ \n')
        fout.write(' "type": "FeatureCollection", \n')
        fout.write(' "name": "sample",\n')
        fout.write(' "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::25831" } },\n')
        fout.write(' "features": [\n')

        for ele in AtlasData.keys():
            dict = AtlasData[ele]
            x = dict["UTMX"]
            y = dict["UTMY"]
            if IsCatalunya(x,y):
                sData = getFeature(ele, dict)
                fout.write(sData)

        # afegim el Centre Geografic de Catalunya (CGCAT) per tancar be l'arxiu .geojson
        cgx = (CATBBOX[0]+CATBBOX[2])/2.0
        cgy = (CATBBOX[1]+CATBBOX[3])/2.0
        sData = '{ "type": "Feature", "properties": { '
        sData += '"NOM": "CGCAT", "ID": 9999, '
        sData += '"UTMX": {}, "UTMY": {}, "H": {}, '.format(cgx,cgy,0.0)
        sData += '"EQUIP": 0, "NUM_YEARS": 99.99, "CENTER": "ICGC" }, '
        sData += '"M": 0.0, "A": 0.0, "B":0.0, '
        sData += '"I01": 0.0, "I02": 0.0, "I03": 0.0, "I04": 0.0, '
        sData += '"I05": 0.0, "I06": 0.0, "I07": 0.0, "I08": 0.0, '
        sData += '"I09": 0.0, "I10": 0.0, "I11": 0.0, "I12": 0.0, '
        sData += '"IWHM2": 0.0 '
        sData += '}, "geometry": { "type": "Point", "coordinates": [ '
        sData += '62000.0, 4714000.0, 352.0 '
        sData += '] } }\n'
        fout.write(sData)

        fout.write(' ] \n')
        fout.write('} \n')
    
    

