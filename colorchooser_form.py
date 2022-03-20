from tkinter import *
from tkinter import colorchooser
from tkinter import simpledialog
import matplotlib.pyplot as plt
import colorsys

def rgb2hex(val):
    """
    Takes tuple and converts to hex value.
    """
    conversion = '#%02x%02x%02x' % val
    return conversion

def hex2rgb(val):
    """
    Takes hex string and converts to rgb tuple.
    """
    hexNum = val.strip('#')
    hexLen = len(hexNum)
    conversion = tuple(int(hexNum[i:i+hexLen//3], 16) for i in range(0, hexLen, hexLen//3))
    return conversion

def complimentary(val):
    """
    Takes rgb tuple and produces complimentary color.
    """
    #value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 150 and 210 degrees
    deg_180_hue = h + (180.0 / 360.0)
    color_180_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_180_hue, l, s)))
    return color_180_rgb

def splitComplimentary(val):
    """
    Takes rgb tuple and produces list of split complimentary colors.
    """
    #value has to be 0 <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>&lt; x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 150 and 210 degrees
    deg_150_hue = h + (150.0 / 360.0)
    deg_210_hue = h + (210.0 / 360.0)
    #convert to rgb
    color_150_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_150_hue, l, s)))
    color_210_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_210_hue, l, s)))
    return [color_150_rgb, color_210_rgb]

def analogous(val, d):
    """
    Takes rgb tuple and angle (out of 100) and produces list of analogous colors)
    """
    analogous_list = []
    #set color wheel angle
    d = d /360.0
    #value has to be 0 <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>&lt; x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #rotate hue by d
    h = [(h+d) % 1 for d in (-d, d)]
    for nh in h:
        new_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(nh, l, s)))
        analogous_list.append(new_rgb)
    return analogous_list

def triadic(val):
    """
    Takes rgb tuple and produces list of triadic colors.
    """
    #value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_120_hue = h + (120.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_120_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_120_hue, l, s)))
    color_240_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_120_rgb, color_240_rgb]

def tetradic(val):
    """
    Takes rgb tuple and produces list of tetradic colors.
    """
    #value has to be 0 <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>&lt; x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_60_hue = h + (60.0 / 360.0)
    deg_180_hue = h + (180.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_60_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_60_hue, l, s)))
    color_180_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_180_hue, l, s)))
    color_240_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_60_rgb, color_180_rgb, color_240_rgb]

def createComplimentary():
    rgb_eden = hex2rgb(cc[1])
    comp_col1 = complimentary(rgb_eden)
    hexVal1 = rgb2hex((comp_col1[0],comp_col1[1],comp_col1[2]))
    edenHex = rgb2hex(rgb_eden)
    #fig = plt.gcf()
    circle = plt.Circle((0, 0), radius=0.75, fc=edenHex)
    circle1 = plt.Circle((1, 1), radius=0.75, fc=hexVal1)
    plt.gca().add_patch(circle)
    plt.gca().add_patch(circle1)
    plt.axis('scaled')
    print("[Комплементарная схема] Основной цвет: ",edenHex,",комплементарный:",hexVal1)
    plt.show()

def createTriadic():
    rgb_eden = hex2rgb(cc[1])
    triadic_col1 = triadic(rgb_eden)[0]
    triadic_col2 = triadic(rgb_eden)[1]
    hexVal1 = rgb2hex((triadic_col1[0],triadic_col1[1],triadic_col1[2]))
    hexVal2 = rgb2hex((triadic_col2[0],triadic_col2[1],triadic_col2[2]))
    edenHex = rgb2hex(rgb_eden)
    #fig = plt.gcf()
    circle = plt.Circle((0, 0), radius=0.75, fc=edenHex)
    circle1 = plt.Circle((0.5, 1), radius=0.75, fc=hexVal1)
    circle2 = plt.Circle((1, 0), radius=0.75, fc=hexVal2)
    plt.gca().add_patch(circle)
    plt.gca().add_patch(circle1)
    plt.gca().add_patch(circle2)
    print("[Триада цветов] Основной цвет: ",edenHex,",сочетания:",hexVal1,hexVal2)
    plt.axis('scaled')
    plt.show()

def createTetradic():
    rgb_eden = hex2rgb(cc[1])
    tetradic_col1 = tetradic(rgb_eden)[0]
    tetradic_col2 = tetradic(rgb_eden)[1]
    tetradic_col3 = tetradic(rgb_eden)[2]
    hexVal1 = rgb2hex((tetradic_col1[0],tetradic_col1[1],tetradic_col1[2]))
    hexVal2 = rgb2hex((tetradic_col2[0],tetradic_col2[1],tetradic_col2[2]))
    hexVal3 = rgb2hex((tetradic_col3[0],tetradic_col3[1],tetradic_col3[2]))
    edenHex = rgb2hex(rgb_eden)
    #fig = plt.gcf()
    circle = plt.Circle((-1, -1), radius=0.75, fc=edenHex)
    circle1 = plt.Circle((-1, 1), radius=0.75, fc=hexVal1)
    circle2 = plt.Circle((1, -1), radius=0.75, fc=hexVal2)
    circle3 = plt.Circle((1, 1), radius=0.75, fc=hexVal3)
    plt.gca().add_patch(circle)
    plt.gca().add_patch(circle1)
    plt.gca().add_patch(circle2)
    plt.gca().add_patch(circle3)
    print("[Тетрада цветов] Основной цвет: ",edenHex,",сочетания:",hexVal1,hexVal2,hexVal3)
    plt.axis('scaled')
    plt.show()

def createSplitComplimetary():
    rgb_eden = hex2rgb(cc[1])
    split_comp_col1 = splitComplimentary(rgb_eden)[0]
    split_comp_col2 = splitComplimentary(rgb_eden)[1]
    #Visualize Colors
    hexVal1 = rgb2hex((split_comp_col1[0],split_comp_col1[1],split_comp_col1[2]))
    hexVal2 = rgb2hex((split_comp_col2[0],split_comp_col2[1],split_comp_col2[2]))
    edenHex = rgb2hex(rgb_eden)
    fig = plt.gcf()
    circle = plt.Circle((0, 0), radius=0.75, fc=edenHex)
    circle1 = plt.Circle((0.5, 1), radius=0.75, fc=hexVal1)
    circle2 = plt.Circle((1, 0), radius=0.75, fc=hexVal2)
    plt.gca().add_patch(circle)
    plt.gca().add_patch(circle1)
    plt.gca().add_patch(circle2)
    print("[Сплит-комплементарная схема] Основной цвет: ",edenHex,",сочетания:",hexVal1,hexVal2)
    plt.axis('scaled')
    plt.show()

def createAnalogous():
    rgb_eden = hex2rgb(cc[1])
    list_of_colors = analogous(rgb_eden,64)
    analog1 = list_of_colors[0]
    analog2 = list_of_colors[1]
    #Visualize Colors
    hexVal1 = rgb2hex((analog1[0],analog1[1],analog1[2]))
    hexVal2 = rgb2hex((analog2[0],analog2[1],analog2[2]))
    edenHex = rgb2hex(rgb_eden)
    fig = plt.gcf()
    circle = plt.Circle((0, 0), radius=0.75, fc=edenHex)
    circle1 = plt.Circle((0.5, 1), radius=0.75, fc=hexVal1)
    circle2 = plt.Circle((1, 0), radius=0.75, fc=hexVal2)
    plt.gca().add_patch(circle)
    plt.gca().add_patch(circle1)
    plt.gca().add_patch(circle2)
    print("[Последовательная схема] Основной цвет: ",edenHex,",сочетания:",hexVal1,hexVal2)
    plt.axis('scaled')
    plt.show()

def pickColor():
    global cc
    cc = colorchooser.askcolor()
    print(cc)

def choose():
    if var.get() == 0:
        plt.clf()
        createComplimentary()
    elif var.get() == 1:
        plt.clf()
        createSplitComplimetary()           
    elif var.get() == 2:
        plt.clf()
        createTriadic()
    elif var.get() == 3:
        plt.clf()
        createTetradic()
    elif var.get() == 4:
        plt.clf()
        createAnalogous()



root = Tk()
var = IntVar()
Button(text="Выбрать цвет",command=pickColor).pack()
Radiobutton(text = "Комплементарная форма", variable=var,value = 0).pack()
Radiobutton(text = "Сплит-комплементарная форма", variable=var, value = 1).pack()
Radiobutton(text = "Триада цветов", variable=var, value = 2).pack()
Radiobutton(text = "Тетрада цветов", variable=var, value = 3).pack()
Radiobutton(text = "Последовательность цветов", variable=var, value = 4).pack()
Button(text="ОК",command=choose).pack()
root.mainloop()



