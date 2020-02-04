from PIL import Image
import os, glob
import numpy as np
import random, math

"""
define type number
1:Normal:ノーマル
2:Fire:ほのお
3:Water:みず
4:Electric:でんき
5:Grass:くさ
6:Ice:こおり
7:Fighting:かくとう
8:Poison:どく
9:Ground:じめん
10:Flying:ひこう
11:Psychic:エスパー
12:Bug:むし
13:Rock:いわ
14:Ghost:ゴースト
15:Dragon:ドラゴン
16:Dark:あく
17:Steel:はがね
18:Fairy:フェアリー
"""

img_path = 'data'
def get_image(path,mosa_num,x_start, x_end, y_start, y_end):
    r2=0
    g2=0
    b2=0
    im = Image.open(path)
    rgb_im = im.convert('RGB')
    size = rgb_im.size
    for x in range(int(size[0]/mosa_num)*x_start,int(size[0]/mosa_num)*x_end+1):
        for y in range(int(size[1]/mosa_num)*y_start,int(size[1]/mosa_num)*y_end):
            r1,g1,b1 = rgb_im.getpixel((x,y))
            r2 = r2 + r1
            g2 = g2 + g1
            b2 = b2 + b1
    #print(r2,g2,b2)
    r = int(r2/(int(size[0]/mosa_num)*(x_end-x_start)*int(size[1]/mosa_num)*(y_end-y_start)))
    g = int(g2/(int(size[0]/mosa_num)*(x_end-x_start)*int(size[1]/mosa_num)*(y_end-y_start)))
    b = int(b2/(int(size[0]/mosa_num)*(x_end-x_start)*int(size[1]/mosa_num)*(y_end-y_start)))
    im_data = []
    im_data.append([r,g,b])
    return r,g,b

def get_color(path):
    col_data = []
    for x in range(1,3):
        for y in range(1,3):
            r,g,b = get_image(path,4,x,x+1,y,y+1)
            col_data.append([r,g,b])
    return col_data[0], col_data[1], col_data[2], col_data[3]

def get_type(path):
    type_tmp1 = np.loadtxt(path,delimiter = ',', usecols=2, skiprows = 1, dtype = 'U8')#type1 only get
    type1 = []
    """
    for i in range(len(type_tmp1)):
        if type_tmp1[i] == 'Normal':
            type1.append(1)
        elif type_tmp1[i] == 'Fire':
            type1.append(2)
        elif type_tmp1[i] == 'Water':
            type1.append(3)
        elif type_tmp1[i] == 'Electric':
            type1.append(4)
        elif type_tmp1[i] == 'Grass':
            type1.append(5)
        elif type_tmp1[i] == 'Ice':
            type1.append(6)
        elif type_tmp1[i] == 'Fighting':
            type1.append(7)
        elif type_tmp1[i] == 'Poison':
            type1.append(8)
        elif type_tmp1[i] == 'Ground':
            type1.append(9)
        elif type_tmp1[i] == 'Flying':
            type1.append(10)
        elif type_tmp1[i] == 'Psychic':
            type1.append(11)
        elif type_tmp1[i] == 'Bug':
            type1.append(12)
        elif type_tmp1[i] == 'Rock':
            type1.append(13)
        elif type_tmp1[i] == 'Ghost':
            type1.append(14)
        elif type_tmp1[i] == 'Dragon':
            type1.append(15)
        elif type_tmp1[i] == 'Dark':
            type1.append(16)
        elif type_tmp1[i] == 'Steel':
            type1.append(17)
        elif type_tmp1[i] == 'Fairy':
            type1.append(18)
    """

    type_tmp2 = np.loadtxt(path, delimiter = ',', usecols=3, skiprows=1, dtype='U8')
    type2 = []
    name = np.loadtxt(path, delimiter = ',', usecols=1,skiprows=1, dtype='U8')
    return name, type_tmp1, type_tmp2
    
def Data_set():
    #ex = get_image('data/images/0001.png',4,1,2,1,2)
    #print(ex)
    name,t1,t2 = get_type('data/convert_data/No_Mega_Weight_new2.csv') 
    dict = os.listdir('data/images')
    dict2 = sorted(glob.glob('data/images/*.png'))
    col_list = []
    for i in dict2:
        #print(i)
        m1,m2,m3,m4 = get_color(i)
        col_list.append([m1,m2,m3,m4])
    
    #col = get_color('data/images/0001.png')
    
    n = 0
    for i in col_list:
        print(name[n],t1[n],t2[n],i)
        n += 1

    return col_list, t1, t2
