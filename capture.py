from compress import compress

from pos import pos_main

import win32gui, win32ui, win32con, win32api

import datetime

import re

import os


def capture_and_handle(file_kb = 1000):

    #获取时间，命名截图
    now_time = datetime.datetime.now()
    now_time = datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
    now_time = re.sub(":","",now_time)
    now_time = re.sub(" ", "", now_time)
    filename = now_time+".jpg"

    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口

    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)

    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)

    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()

    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()

    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)

    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小

    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)

    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

    #运行pos_main函数,传入img_name和可选x_axis_add,y_axis_add,save_file参数
    pos_main(filename)

    savefile = pos_main(filename)

    #运行compress函数,传入outfile kb参数
    compress(savefile,file_kb)

    #删除原截图
    os.remove(filename)

    return savefile
