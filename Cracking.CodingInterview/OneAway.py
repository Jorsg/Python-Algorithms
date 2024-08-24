# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
# Give two string, write a function to check if they are one edit(or zero edit) away




def one_edit_away(s1, s2):
    if len(s1) == len(s2):

        return on_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    return False




def on_edit_replace(s1, s2):

    found_difference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_difference:
                return False
        found_difference = True
    return True



def one_edit_insert(s1, s2):
    index_1 = 0
    index_2 = 0
    while index_2 < len(s2) and index_1 < len(s1):
        if(s1[index_1] != s2[index_2]):
            if index_1 != index_2:
                return False
            index_2 += 1
        else:
            index_1 +=1
            index_2 += 1
    return True






print(one_edit_away("pale","ple"))







