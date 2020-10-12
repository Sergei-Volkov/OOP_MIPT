def create_simple_forest_of_folders(depth=5, width=6, root=""): #в root находится путь до корня дерева. 
                                                                #Вдруг ваша структура лежит не в папке с этим ноутбуком
    #ваш код здесь
    import os 
    if depth == 0:
        return
    else:
        os.chdir(root)
        for i in range(width):
            new_root = root + '/' + str(i + 1)
            if not os.path.exists(new_root):
                os.mkdir(new_root) 
            if depth > 1:
                create_simple_forest_of_folders(depth=depth - 1, width=width, root=new_root)


def myHash(string, base=91, mod=1000000321):
    """
    Function calculating hash-function of string with certain base by mod.
    """
    value = 0
    for pos, elem in enumerate(string[::-1]):  # считаем значение полинома
        value += ord(elem) * base**pos         # в последней задаче сделано с помощью массива (динамика)
    return value % mod


def calculate_saving_directory(file_name, depth, root):
    hashValue = myHash(file_name) % (10 ** depth)
    folders = [digit for digit in str(hashValue)]
    saving_dir = root + '/' + '/'.join(folders)
    return folders, saving_dir


def save_file_hash_table(file_name, depth=5, root=""):
    folders, saving_dir = calculate_saving_directory(file_name.split('.')[0], depth, root)
    create_simple_forest_of_folders(depth=depth, width=max(map(int, folders)), root=root)
    import os, shutil
    os.chdir(root)
    new_path = shutil.move(file_name, saving_dir)
    return new_path


class NoFileInMyLibrary(Exception):
    pass


def find_file_hash_table(file_name, depth, root=""):
    _, saving_dir = calculate_saving_directory(file_name.split('.')[0], depth, root)
    import os
    try:
        if os.path.exists(saving_dir + '/' + file_name):
            return saving_dir
        else:
            raise NoFileInMyLibrary()
    except NoFileInMyLibrary: 
        print('Такого файла нет')


if __name__ == '__main__':
    command = input()
    while command not in ['save', 'open']:
        print('Эта программа умеет только сохранять ("save") файлы и открывать их ("open")')
        print('Введите команду еще раз')
        command = input()
    else:
        file = input()
        import os
        if command == 'save':
            save_file_hash_table(file, depth=2, root=os.getcwd())
        elif command == 'open':
            find_file_hash_table(file, depth=2, root=os.getcwd())
