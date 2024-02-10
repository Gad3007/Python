# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.


text1 = 'A, E, I, O, U, L, N, S, T, R'
text2 = 'D, G'
text3 = 'B, C, M, P'
text4 = 'F, H, V, W, Y'
text5 = 'K'
text6 = 'J, X'
text7 = 'Q, Z'
text01 = 'А, В, Е, И, Н, О, Р, С, Т'
text02 = 'Д, К, Л, М, П, У'
text03 = 'Б, Г, Ё, Ь, Я'
text04 = 'Й, Ы'
text05 = 'Ж, З, Х, Ц, Ч'
text06 = 'Ш, Э, Ю'
text07 = 'Ф, Щ, Ъ'

eng_txt = {text1 : 1, text2 : 2, text3 : 3, text4 : 4 , text5 : 5, text6 : 8, text7 : 10}
rus_txt = {text01 : 1, text02 : 2, text03 : 3, text04 : 4 , text05 : 5, text06 : 8, text07 : 10}
print(eng_txt)
print(rus_txt)

char_list = []
count = 0
word = str(input('Введите слово: '))

for c in word :
    char_list.append(c.upper())
print(char_list)
length = len(char_list)
n = 0


# while n < length :
    

# text1_dict_ = eng_txt.split(", ")
# text2_dict_ = dict.fromkeys(text2.split(", "), 2)
# text3_dict_ = dict.fromkeys(text3.split(", "), 3)
# text4_dict_ = dict.fromkeys(text4.split(", "), 4)
# text5_dict_ = dict.fromkeys(text5.split(", "), 5)
# text6_dict_ = dict.fromkeys(text6.split(", "), 8)
# text7_dict_ = dict.fromkeys(text7.split(", "), 10)

# print(text2_dict_)
# print(text3_dict_)
# print(text4_dict_)
# print(text5_dict_)
# print(text6_dict_)
# print(text7_dict_)

# text01_dict_ = dict.fromkeys(text01.split(","), 1)
# text02_dict_ = dict.fromkeys(text02.split(", "), 2)
# text03_dict_ = dict.fromkeys(text03.split(", "), 3)
# text04_dict_ = dict.fromkeys(text04.split(", "), 4)
# text05_dict_ = dict.fromkeys(text05.split(", "), 5)
# text06_dict_ = dict.fromkeys(text06.split(", "), 8)
# text07_dict_ = dict.fromkeys(text07.split(", "), 10)

# print(text01_dict_)
# print(text02_dict_)
# print(text03_dict_)
# print(text04_dict_)
# print(text05_dict_)
# print(text06_dict_)
# print(text07_dict_)

