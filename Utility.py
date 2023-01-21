import os
import shutil
import stat


# 移除夹心文件夹
def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)


def remove_empty_file(path):
    try:
        os.rmdir(path)
    except:
        os.chmod(path, stat.S_IWRITE)
        os.rmdir(path)


def remove_sandwich_fold(path):
    current = os.listdir(path)
    current_path = path + '\\' + current[0]
    for file in os.listdir(path + '\\' + current[0]):
        print(file)
        shutil.move(current_path + '\\' + file, path + '\\' + file)

def file_finishing():
    path = input("address: ")
    loop = True
    print('display order')
    # for root, dirs, files in os.walk(path, topdown=False):
    #     print(f"root: {root}, dir: {dirs}, file: {files}")
    # print("-----------------------------------")
    for root, dirs, files in os.walk(path, topdown=False):
        print(f"root: {root}, dir: {dirs}, file: {files}")
        if len(dirs) == 1 and len(files) == 0 and os.path.isdir(root):
            print(f'remove sandwich _-_ file {root}')
            remove_sandwich_fold(root)
        if len(dirs) == 0 and len(files) == 0:
            print(f'remove empty files {root}')
            remove_empty_file(root)
    for root, dirs, files in os.walk(path, topdown=False):
        print(f"root: {root}, dir: {dirs}, file: {files}")
        if len(dirs) == 1 and len(files) == 0 and os.path.isdir(root):
            print(f'remove sandwich _-_ file {root}')
            remove_sandwich_fold(root)

