import enum


def find(list_dicari, kata):
    for ea, value in enumerate(list_dicari):
        if value == kata:
            return ea
    return "gak ada"

#list1 = ['mobil' ,'rumah', 'hp']
#print(find(list1,'hp'))

