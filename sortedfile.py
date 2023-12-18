import os


def open_files(files_dir_name):
    base_path = os.getcwd()
    dir_path = os.path.join(base_path, files_dir_name)
    file_names = os.listdir(dir_path)
    result = []
    for file in file_names:
        full_path = os.path.join(base_path, files_dir_name, file)
        with open(full_path, encoding='utf-8') as txt_file:
            tmp_list = txt_file.readlines()
            tmp_list.append(file + '\n')
            tmp_list.append(len(tmp_list) - 1)
            result.append(tmp_list)
    print(result)
    return result


def sort_files(result):
    for i in range(len(result)-1):
        if result[i][-1] > result[i+1][-1]:
            result[i], result[i+1] = result[i+1], result[i]
    print(result)
    return result


def write_files(lead_list):
    result_file = open('merger.txt', 'w+', encoding = 'utf-8')
    lead_list = sort_files(lead_list)
    for i in range(len(lead_list)):
        result_file.write(lead_list[i][-2])
        result_file.write(str(lead_list[i][-1]) + '\n')
        for j in range(len(lead_list[i])-2):
            result_file.write(lead_list[i][j].strip() + '\n')


files_dir_name = 'sorted'       # папка, в которой будут храниться входные файлы

list1 = open_files(files_dir_name)
write_files(list1)