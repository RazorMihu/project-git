nStr = input('请输入字符：')

alpha_count = 0
space_count = 0
digit_count = 0
other_count = 0

for str in nStr:
    if str.isalpha():
        alpha_count += 1
    elif str.isspace():
        space_count += 1
    elif str.isdigit():
        digit_count += 1
    else:
        other_count += 1
print ('英文字母有： %d' %alpha_count)
print ('空格有： %d' %space_count)
print ('数字有： %d' %digit_count)
print ('其他字符有： %d' %other_count)