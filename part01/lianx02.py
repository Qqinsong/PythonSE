import os
# os.walk() 方法可以创建一个生成器，
# 用以生成所要查找的目录及其子目录下的所有文件
# g = os.walk('E:\\PythonSE\\part01')
for path, dir_list, file_list in os.walk(os.getcwd()):
    # 遍历所有的目录
    for dir_name in dir_list:
        # 把目录和文件夹名合成一个路径
        print("目录:"+os.path.join(path, dir_name))
    # 遍历所有的文件
    for file_name in file_list:
        # 把目录和文件名合成一个路径，打印输出
        print("文件:"+os.path.join(path, file_name))