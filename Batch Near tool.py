# 检查线是否有重复
# 按字段批量导出各线至单独的shp文件
# 按字段批量导出各线的点至单独的shp文件
# Python版本-ArcGIS自带

import arcpy
import os.path

path1 = 'stops' #存储点的路径
path2 = 'lines' #存储路的路径

path_stop = []
path_line = []
f1 = os.listdir(path1)
f2 = os.listdir(path2)

for i in f1:
    if i[-3:] == 'shp':
        path_stop.append(path1 + '/' + i) #确定点shp格式的文件存储位置
for j in f2:
    if j[-3:] == 'shp':
        path_line.append(path2 + '/' + j) #确定线shp格式的文件存储位置

for n in range(0,190): #若有190条线
    infc = path_stop[n]
    line = path_line[n]
    arcpy.Near_analysis(infc, line, "", "true") #生成线上距离最近的点（原点shp文件属性表增加字段"NEAR_X", "NEAR_Y"）
