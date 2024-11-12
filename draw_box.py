import cv2

if __name__ == '__main__':

    # 读取原始图像
    ori_path = 'compare_rgb/nv3d/virg-peel-banana_ours_00010.png'

    dst_path = ori_path.replace('experiment_rgb', 'experiment_box').replace('.png', '_box.png')
    # dst_red_path = ori_path.replace('experiment_rgb', 'experiment_box').replace('.png', '_red_box.png')
    # dst_green_path = ori_path.replace('experiment_rgb', 'experiment_box').replace('.png', '_green_box.png')


    image = cv2.imread(ori_path)


    # 定义两组box的范围
    red_center = (300, 380)
    green_center = (1020, 900)

    red_w = 150
    red_h = 150

    green_w = 50
    green_h = 80

    box_size = 2

    red_box = (red_center[0] - red_w, red_center[1]-red_h, red_center[0] + red_w, red_center[1] + red_h)  # (x1, y1, x2, y2)
    green_box = (green_center[0] - green_w, green_center[1]-green_h, green_center[0] + green_w, green_center[1] + green_h)  # (x1, y1, x2, y2)

    # 在原始图像上绘制红色和绿色框
    image_with_boxes = image.copy()
    cv2.rectangle(image_with_boxes, (red_box[0], red_box[1]), (red_box[2], red_box[3]), (0, 0, 255), box_size)  # 红色框
    # cv2.rectangle(image_with_boxes, (green_box[0], green_box[1]), (green_box[2], green_box[3]), (0, 255, 0), box_size)  # 绿色框

    # 保存带有框的图像
    cv2.imwrite(dst_path, image_with_boxes)

    # 截取红色框的部分
    # red_roi = image_with_boxes[red_box[1]:red_box[3], red_box[0]:red_box[2]]
    # cv2.imwrite(dst_red_path, red_roi)

    # 截取绿色框的部分
    # green_roi = image_with_boxes[green_box[1]:green_box[3], green_box[0]:green_box[2]]
    # cv2.imwrite(dst_green_path, green_roi)