def all_cyclic_shifts(text):
    final_list = []

    final_list.append(text)
    flag = True
    while flag:
        text += text[0]
        new_text=text[1:]
        text=new_text

        if new_text not in final_list:
            final_list.append(new_text)
        else:
            flag = False
    return final_list

print(all_cyclic_shifts('hello'))
