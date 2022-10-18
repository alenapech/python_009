# 1. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый
# элемент списка является и ключом и значением. Предполагается, что элементы списка будут соответствовать правилам
# задания ключей в словарях.
# def to_dict(lst):
#     result = {}
#     for item in lst:
#         result[item] = item
#     return result


# source = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']

# print(to_dict(source))

# 2. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), которая
# принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict,
# состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.
# def biggest_dict(**kwargs):
#     my_dic.update(kwargs)


# my_dic = {'fist_one': "we can do it"}
# biggest_dict(second='second', third='third')

# print(my_dic)

# 3. Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать словарь, который в качестве
# ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в
# имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
# def count_it(sequence):
#     seq_list = list(sequence)
#     result = {}
#     answer_dic = {}
#     for item in seq_list:
#         cnt = seq_list.count(item)
#         result[int(item)] = cnt

#     for _ in range(3):
#         max_val = max(result.values())
#         final_dict = {k: v for k, v in result.items() if v == max_val}
#         answer_dic.update(final_dict)
#         tmp = final_dict.keys()
#         tnp_int = list(tmp)
#         result.pop(tnp_int[0])
#     return answer_dic


# raw = '123111333332222234564444566665444'
# print(count_it(raw))

# 4.* (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего
# задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
#  Например:
#  >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
#  {  "А": { "П": ["Петр Алексеев"] },
#     "И": { "И": ["Илья Иванов"] },
#     "С": { "И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"] }
#  }
def thesaurus_adv(*args):
    dict_by_name = {}
    dict_by_last_name = {}
    save_list = []
    i = 0
    for item in args:
        i += 1
        tmp_list = item.split()
        key_by_last_name = tmp_list[1][0][0]
        key_by_name = tmp_list[0][0][0]
        if key_by_last_name not in dict_by_last_name.keys():
            dict_by_name[key_by_name] = item
            dict_by_last_name[key_by_last_name] = dict_by_name
            dict_by_name = {}
        else:
            if key_by_name in dict_by_name.keys() or key_by_name == previous_key_by_name:
                save_list.append(item)
                save_list.append(previous_item)
                dict_by_name[key_by_name] = save_list
                dict_by_last_name[key_by_last_name] = dict_by_name
                dict_by_name = {}
            else:
                tmp_dict = dict_by_last_name[key_by_last_name]
                tmp_dict[key_by_name] = item
                dict_by_last_name[key_by_last_name] = tmp_dict
        previous_key_by_name = key_by_name
        previous_item = item

        save_list = []
    print(dict_by_last_name)

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")