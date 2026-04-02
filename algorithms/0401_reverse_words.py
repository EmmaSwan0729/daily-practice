def reverse_words(s:str) -> str:
    '''
    reverse order of words in a string 
    args: s(str), a string includes words
    return: int: a string of words with reversal order
    ''' 
    reverse_order = s.split()
    words_list_rev = reverse_order[::-1]
    return " ".join(words_list_rev)





# [::-1] 是切片语法，步长为 -1，意思是从后往前取所有元素：
# pythonwords = ["the", "sky", "is", "blue"]
# words[::-1]  # ["blue", "is", "sky", "the"]

# join 是字符串方法，把列表里的元素拼成一个字符串，用指定的分隔符连接：
# pythonwords = ["blue", "is", "sky", "the"]
# " ".join(words)   # "blue is sky the"
# ",".join(words)   # "blue,is,sky,the"
# "".join(words)    # "blueisskythe"
# 格式是 "分隔符".join(列表)，分隔符放在前面。0401_climbing_stairs.py