
def len_of_list(inp_list,len_list = 0): # третье задание
    if inp_list != []:
        inp_list.pop(0)
    else:
        return len_list
    return len_of_list(inp_list, len_list + 1)

def IsPalindrom(inp_str,start = 0, end = -1):# четвертое задание
    no_space_str = inp_str.replace(" ", "")
    if no_space_str[start] != no_space_str[end]:
        return False
    if inp_str == '' or start == (len(no_space_str)/2):
        return True
    return IsPalindrom(inp_str,start + 1, end - 1)
