def list_to_string(s):
    # initialize an empty string and a counter so that you don't add an extra space at the end
    str1 = ""
    counter = 0

    # traverse in the string
    for ele in s:
        counter += 1
        str1 += str(ele)
        if counter < len(s):  # add spaces between all strings and make sure to not add one after last entry
            str1 += ''

        # return string
    return str1


pretext_filename_p = 'K_results_pretext.txt'

pretext = open(pretext_filename_p, 'r')

with open(pretext_filename_p) as myfile:
    head = [next(myfile) for x in range(4)]
# print(list_to_string(head))  # commented out MAR-17-2022

pretext_data = pretext.read()
pretext_data = pretext_data[:-10]  # -3 before
# print(pretext_data)