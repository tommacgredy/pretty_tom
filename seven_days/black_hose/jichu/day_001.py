import os, shutil


def del_otherdirs(dir_path):
    file_list = os.listdir(dir_path)
    for i in file_list:
        # 获取第一层目录
        file_path_01 = os.path.join(dir_path, i)
        if os.path.isfile(file_path_01):
            os.remove(file_path_01)
            print("===文件已经被删除===")
        else:
            file_list_02 = os.listdir(file_path_01)
            for j in file_list_02:
                # 获取第二层目录
                file_path_02 = os.path.join(file_path_01, j)
                if os.path.isfile(file_path_02):
                    os.remove(file_path_02)
                    print("===文件已经被删除===")
                else:
                    file_list_03 = os.listdir(file_path_02)
                    if os.path.isdir(file_path_02) and j != "ceshi":
                        shutil.rmtree(file_path_02)
                        print("++++文件夹已经被删除++++")
                    elif os.path.isfile(file_path_02):
                        os.remove(file_path_02)
                        print("===文件已经被删除===")
                    elif os.path.isdir(file_path_02) and j == "ceshi":
                        for file in file_list_03:
                            file_path_03 = os.path.join(file_path_02, file)
                            if os.path.isdir(file_path_03):
                                shutil.rmtree(file_path_03)
                                print("++++文件夹已经被删除++++")
                            elif '副本' in file or '.txt' not in file:
                                os.remove(file_path_03)
                                print("===文件已经被删除===")




def paixu():
    lines_01 = []

    while True:
        try:
            N = int(input().strip())
            for i in range(N):
                lines_01.append(int(input()))
            b = sorted(set(lines_01))
            for j in b:
                print(j)
        except:
            break



def qiuyu():
    l_01 = []

    while True:
        try:
            str_01 = input()
            if str_01 == '':
                break
            else:
                l_01.append(str_01)

        except:
            break
    print(l_01)
    for i in l_01:
        a = len(i) // 8
        b = len(i) % 8
        c = a if b == 0 else a + 1
        if len(i) <= 8:
            print(i + (8 - len(i)) * '0')

        else:
            for j in range(c):
                s = i[j * 8 : (j + 1) * 8]
                if len(s) == 8:
                    print(s)
                else:
                    s_02 = s+ (8 - len(s)) * '0'
                    print(s_02)



def erjinzhi():
    # a = input()
    # b = bin(int(a, 10))
    # print(b)
    # s = str(b)
    # print(s)
    # print(s.count('1'))
    m = 'A10;D50;C100'
    l_01 = m.split(';')
    print(l_01)
    for i in l_01:
        print(i[1:])
        print(i[:1])



def zuobiao():
    a = input()
    x = 0
    y = 0
    l_01 = a.split(';')
    for i in l_01:
        try:
            b = int(i[1:])
        except:
            b = 0

        if i[:1] == 'A':
            x -= b
        elif i[:1] == 'D':
            x += b
        elif i[:1] == 'W':
            y += b
        elif i[:1] == 'S':
            y -= b
        else:
            pass

    x_s = str(x)
    y_s = str(y)
    print(x_s + ',' + y_s)




if __name__ == "__main__":
    # dirs_path = r"C:\Users\Administrator\Desktop\123"
    # del_otherdirs(dirs_path)
    zuobiao()