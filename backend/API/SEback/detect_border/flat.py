import cv2
import numpy as np


# 判断两条直线是否平行
def are_lines_parallel(line1, line2, angle_threshold=3.0):
    # angle_threshold: 允许的方向向量之间的角度误差阈值（以度为单位）
    angle_rad1 = np.arctan2(line1[1], line1[0])
    angle_rad2 = np.arctan2(line2[1], line2[0])

    angle_deg1 = np.degrees(angle_rad1)
    angle_deg2 = np.degrees(angle_rad2)

    angle_diff = abs(angle_deg1 - angle_deg2)

    if angle_diff > 90:
        angle_diff = 180 - angle_diff

    return angle_diff < angle_threshold


def detect(original_path, result_path):
    # 读取原始图像和检测结果图像
    original_image = cv2.imread(original_path)
    result_image = cv2.imread(result_path)

    # 将图像转换为HSV颜色空间
    hsv = cv2.cvtColor(result_image, cv2.COLOR_BGR2HSV)

    # 设定绿色的HSV范围
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    # 根据阈值获取绿色区域的掩码
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # 找到绿色区域的轮廓
    contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 创建新图像，将检测结果覆盖在原始图像上
    overlay_result_on_original = np.copy(original_image)
    overlay_result_on_original[result_image[:, :, 1] > 0] = result_image[result_image[:, :, 1] > 0]

    # 显示检测结果
    # cv2.namedWindow('detected image', cv2.WINDOW_NORMAL)
    # cv2.imshow("detected image", overlay_result_on_original)
    # cv2.waitKey(0)

    # 创建一张空白图像，用于标记线条和聚类点
    marked_image = np.copy(original_image)

    # 存储所有边缘点
    all_edge_points = []

    # 遍历轮廓
    for contour in contours:
        # 将轮廓转换为边缘点
        edge_points = np.squeeze(contour, axis=1)
        all_edge_points.extend(edge_points)

    # 将所有边缘点绘制到图像上
    for point in all_edge_points:
        cv2.circle(marked_image, tuple(point), 2, (0, 0, 255), -1)

    # 显示边缘点化后的图像
    # cv2.namedWindow('pointed image', cv2.WINDOW_NORMAL)
    # cv2.imshow("pointed image", marked_image)
    # cv2.waitKey(0)

    # 分组，每200个点为一组
    group_size = 200
    grouped_points = [all_edge_points[i:i + group_size] for i in range(0, len(all_edge_points), group_size)]

    # 遍历每个分组进行直线拟合
    filtered_lines = []

    for group in grouped_points:

        # 将该分组所有点绘制到图像上
        for point in group:
            cv2.circle(marked_image, tuple(point), 2, (0, 255, 255), -1)

        if len(group) < 200:
            continue

        # 将点坐标转换为二维数组
        points_array = np.array(group)

        # 拟合直线
        [vx, vy, x, y] = cv2.fitLine(points_array, cv2.DIST_L2, 0, 0.01, 0.01)

        # 计算点到直线的距离
        distances = np.abs((vx * (points_array[:, 1] - y) - vy * (points_array[:, 0] - x)) /
                           np.sqrt(vx**2 + vy**2))

        # 判断是否符合条件，保留98%的点
        inliers = distances < 4  # 可以根据实际情况调整距离阈值
        inlier_ratio = np.sum(inliers) / len(inliers)
        # print(inlier_ratio)

        if inlier_ratio > 0.98:
            # 符合条件，将直线信息保存
            filtered_lines.append((vx, vy, x, y))

    # 绘制筛选后的直线到图像上
    for line in filtered_lines:
        vx, vy, x, y = line
        cv2.line(marked_image, (int(x[0] - vx[0] * 1000), int(y[0] - vy[0] * 1000)),
                 (int(x[0] + vx[0] * 1000), int(y[0] + vy[0] * 1000)), (0, 255, 0), 2)

    # 显示边缘点直线拟合后的图像
    # cv2.namedWindow('lined image', cv2.WINDOW_NORMAL)
    # cv2.imshow("lined image", marked_image)
    # cv2.waitKey(0)

    # 划分横向线条和竖向直线
    horizontal_lines = []
    vertical_lines = []

    for line in filtered_lines:
        vx, vy, x, y = line

        # 横向直线
        if abs(vx) > 0.9:
            horizontal_lines.append((vx, vy, x, y))
            cv2.line(marked_image, (int(x[0] - vx[0] * 1000), int(y[0] - vy[0] * 1000)),
                     (int(x[0] + vx[0] * 1000), int(y[0] + vy[0] * 1000)), (255, 255, 0), 2)

        # 竖向直线
        if abs(vy) > 0.9:
            vertical_lines.append((vx, vy, x, y))
            cv2.line(marked_image, (int(x[0] - vx[0] * 1000), int(y[0] - vy[0] * 1000)),
                     (int(x[0] + vx[0] * 1000), int(y[0] + vy[0] * 1000)), (255, 0, 255), 2)

    # 显示区分横向和纵向后的图像
    # cv2.namedWindow('lined plus image', cv2.WINDOW_NORMAL)
    # cv2.imshow("lined plus image", marked_image)
    # cv2.waitKey(0)

    # 比较横向直线和竖向直线是否都平行
    horizontal_parallel = True
    vertical_parallel = True

    # 比较横向直线之间的平行关系
    for i in range(len(horizontal_lines)):
        for j in range(i + 1, len(horizontal_lines)):
            line1 = horizontal_lines[i][:2]
            line2 = horizontal_lines[j][:2]

            if not are_lines_parallel(line1, line2):
                horizontal_parallel = False

                # 标记出来不平行的直线
                vx, vy, x, y = horizontal_lines[i]
                cv2.line(marked_image, (int(x[0] - vx[0] * 1000), int(y[0] - vy[0] * 1000)),
                         (int(x[0] + vx[0] * 1000), int(y[0] + vy[0] * 1000)), (0, 0, 255), 4)

                vx, vy, x, y = horizontal_lines[j]
                cv2.line(marked_image, (int(x[0] - vx[0] * 1000), int(y[0] - vy[0] * 1000)),
                         (int(x[0] + vx[0] * 1000), int(y[0] + vy[0] * 1000)), (0, 0, 255), 4)

    # 比较竖向直线之间的平行关系
    for i in range(len(vertical_lines)):
        for j in range(i + 1, len(vertical_lines)):
            line1 = vertical_lines[i][:2]
            line2 = vertical_lines[j][:2]

            if not are_lines_parallel(line1, line2):
                vertical_parallel = False

                # 标记出来不平行的直线
                vx, vy, x, y = vertical_lines[i]
                cv2.line(marked_image, (int(x[0] - vx[0] * 1000), int(y[0] - vy[0] * 1000)),
                         (int(x[0] + vx[0] * 1000), int(y[0] + vy[0] * 1000)), (0, 0, 255), 4)

                vx, vy, x, y = vertical_lines[j]
                cv2.line(marked_image, (int(x[0] - vx[0] * 1000), int(y[0] - vy[0] * 1000)),
                         (int(x[0] + vx[0] * 1000), int(y[0] + vy[0] * 1000)), (0, 0, 255), 4)

    # 显示平行检测后的图像
    # cv2.namedWindow('marked image', cv2.WINDOW_NORMAL)
    # cv2.imshow("marked image", marked_image)
    # cv2.waitKey(0)

    # 返回原始图像，结构胶检测图像，边缘拟合后的图像
    return original_image, overlay_result_on_original, marked_image, horizontal_parallel, vertical_parallel

