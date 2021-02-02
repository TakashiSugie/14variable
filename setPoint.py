import numpy as np


def main():
    # np.zeros()
    # arr =np.random.randint(1,10)
    # arr =np.random.randint(1,10)
    np.random.seed(1)
    arr = np.random.randint(1, 10, (15, 3)).T
    theta_x, theta_y, theta_z = 0.1, 0.1, 0.1
    tx, ty, tz = 1, 1, 1
    rot = np.array(
        [[1, -theta_z, theta_y], [theta_z, 1, -theta_x], [-theta_y, theta_x, 1]]
    )
    traEle = np.array([[tx, ty, tz]]).T
    tra = np.tile(traEle, (1, arr.shape[1]))

    print(arr.shape, rot.shape, tra.shape)
    dst = np.dot(rot, arr) + tra
    # print(dst.shape)
    print(arr)
    print(dst)


main()
