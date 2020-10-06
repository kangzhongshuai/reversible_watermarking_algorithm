def capacity_calculating(img):
    # 转化为灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

    width = len(img)
    height = len(img[0])
    frequency = list()
    # 计算灰度值的频率
    maxp = 0
    for i in range(256):
        frequency.append(0)
    for i in range(height):
        for j in range(width):
            frequency[img[i, j]] += 1
    for i in range(256):
        if (frequency[i] > frequency[maxp]):
            maxp = i
    #得到容量
    capacity = frequency[maxp]
