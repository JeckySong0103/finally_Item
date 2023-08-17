import cv2

for i in range(15):
    person = cv2.imread("E:/photo/test-0005_nsd-00671.png")
    back = cv2.imread("E:/photo/background.jpg")
    # 这里将mask图转化为灰度图
    mask = cv2.imread("E:/photo/masks/"+str(i)+".png", cv2.IMREAD_GRAYSCALE)  # Corrected 'i' to 'str(i)'

    # 将背景图resize到和原图一样的尺寸
    back = cv2.resize(back, (person.shape[1], person.shape[0]))

    # 这一步是将背景图中的人像部分抠出来，也就是人像部分的像素值为0
    scenic_mask = ~mask
    scenic_mask = scenic_mask / 255.0
    back[:, :, 0] = back[:, :, 0] * scenic_mask
    back[:, :, 1] = back[:, :, 1] * scenic_mask
    back[:, :, 2] = back[:, :, 2] * scenic_mask

    # 这部分是将我们的人像抠出来，也就是背景部分的像素值为0
    mask = mask / 255.0
    person[:, :, 0] = person[:, :, 0] * mask
    person[:, :, 1] = person[:, :, 1] * mask
    person[:, :, 2] = person[:, :, 2] * mask

    # 这里做个相加就可以实现合并
    result = cv2.add(back, person)

    cv2.imwrite("E:/photo/hebing/"+str(i)+".jpg", result)  # Corrected 'i' to 'str(i)'

