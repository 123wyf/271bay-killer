import cv2

def pos_main(img_name,x_axis_add = 100,y_axis_add = 100,save_file = ""):

    if save_file == "" :

        save_file = "add"+img_name

    else:

        pass


    def pos(img_name, x_axis, y_axis,text):

        x_axis = int(x_axis)

        y_axis = int(y_axis)

        # 加载背景图片
        img = cv2.imread(img_name)

        # 在图片上添加文字信息
        cv2.putText(
            img, text, (x_axis, y_axis), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA
        )

        # 保存图片
        cv2.imwrite(save_file, img)

    x_axis_max = 1920

    y_axis_max = 1080

    x_axis = 0

    y_axis = 0

    test = 0

    while x_axis < x_axis_max:

        x_axis = x_axis+x_axis_add

        x_axis = str(x_axis)

        if test == 1:

            pos(save_file, x_axis, 15,x_axis)

        elif test == 0:

            pos(img_name,x_axis,15,x_axis)

        test = 1

        x_axis = int(x_axis)



    while y_axis < y_axis_max:

        y_axis = y_axis + y_axis_add

        y_axis = str(y_axis)

        pos(save_file,15, y_axis,y_axis)

        y_axis = int(y_axis)

    return save_file






