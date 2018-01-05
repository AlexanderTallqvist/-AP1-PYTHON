# -*- coding: cp1252 -*-
# Övning 7 | Uppg. 1, 2, 3, 4, 5
# Alexander Tallqvist

import random

# Uppg. 1

# namn =  raw_input("Ange dit namn: ")
# namn_lista = []
#
#
# for x in range(0, len(namn)):
#     namn_lista.append(namn[x])
#
#
# print namn_lista
#
#
# for x in range(0, len(namn_lista)):
#     print namn_lista[x]



# Uppg. 2

# i = 10;
# number_list = []
#
# while i > 0:
#     number_list.append(random.randrange(1, 10))
#     i -=1
#
# print "The original list:", number_list
#
#
# for x in range(0, len(number_list)):
#     number_list[x] = number_list[x] * 2
#
# print "The multiplyed list:", number_list


# Uppg. 3

# vote_list = [0,0,0,0,0,0,0,0]
# i = 0
#
# while i < 10 :
#     vote = input("Vem vill du rosta for (2-7)? ")
#     if vote <= 7 and vote >= 2:
#         vote_list[vote] = vote_list[vote] + 1
#
#     i += 1
#     print "Tack for rosten."
#
#
# for x in range(2, 8):
#     print "Kandidat nummer", x, "fick", vote_list[x], "antal roster."


# Uppg. 4

# vote_list = [0,0,0,0,0,0,0,0]
# i = 0
#
# while i < 1000 :
#     random_vote = random.randrange(2, 8)
#     vote_list[random_vote] = vote_list[random_vote] + 1
#     i += 1
#
#
# for x in range(2, 8):
#     print "Kandidat nummer", x, "fick", vote_list[x], "antal roster."


# Uppg. 5

# vote_list = [0,0,0,0,0,0,0,0]
# i = 0
#
# while i < 10 :
#     random_vote = random.randrange(2, 8)
#     vote_list[random_vote] = vote_list[random_vote] + 1
#     i += 1
#
#
# for x in range(2, 8):
#     print "Kandidat nummer", x, "fick", vote_list[x], "antal roster."
#
# max_value = max(vote_list)
# winners =  [j for j, value in enumerate(vote_list) if value == max_value]
#
# print "Vinnaren ar kandidat nummer" , winners
