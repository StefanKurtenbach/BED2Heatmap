#!/usr/bin/env python
# coding: utf-8

# In[29]:


import os

def write_to_file(row):
    with open("graph_minus1.svg", "a") as f:
        f.write(row)
        f.write("\n")
        
def draw_rect(x_coord, y_0, color, width, hight1, opacity):
    return '''<rect x="''' + str(x_coord) + '''" opacity="''' + str(opacity) + '''" y="''' + str(y_0 - hight1) + '''" fill="''' + color + '''" width="''' + str(width) + '''" height="''' + str(hight1) + '''"/>'''

if os.path.exists("graph_minus1.svg"):
    os.remove("graph_minus1.svg")

chromosomal_length = 3095677412
desired_width = 150
length_factor = float(desired_width)/chromosomal_length
write_to_file('''<svg viewBox="0 0 300 ''' + str(500) + '''" xmlns="http://www.w3.org/2000/svg">''')


# In[30]:


start = 0
for i in chromosome_sizes: 
    write_to_file(draw_rect(start, 0, "#005CFF", float(i[1])*length_factor, 1, 100))
    start += float(i[1]) * length_factor


# In[31]:


group1 = [0, 1, 4, 6, 10, 21, 26, 28, 29, 30, 35, 50, 65, 66, 71, 85, 89, 95, 96, 98, 107, 109, 112, 118, 123, 126, 127, 129, 133, 140, 151, 153, 155, 159, 160, 165, 168, 171, 172, 182, 188, 191, 208, 211, 214, 215, 216, 218, 226, 230, 233, 235, 236, 237, 255, 256, 257, 258, 260, 262, 271, 273, 284, 285, 299, 305, 308, 309, 310, 313, 315, 320, 334, 359, 362, 373, 381, 382, 383, 385, 389, 402, 403, 418, 434, 438, 446, 450, 453, 459, 462, 467, 477, 479, 494, 508, 510, 511, 515, 516, 520, 523, 528, 529, 539, 549, 559, 567, 568, 582, 583, 587, 588, 589, 590, 592, 600, 604, 607, 609, 611, 619, 620, 625, 626, 627, 630, 631, 634, 637, 645, 650, 657, 658, 661, 668, 671, 672, 674, 676, 679, 682, 684, 685, 694, 707, 717, 718, 726, 728, 729, 733, 744, 748, 750, 757, 762, 765, 776, 781, 784, 787, 789, 791, 798, 799, 814, 817, 820, 822, 823, 825, 830, 852, 858, 866, 867, 873, 876, 878, 890, 891, 892, 898, 906, 909, 911, 912, 916, 920, 921, 923, 930, 932, 934, 943, 945, 948, 953, 958, 962, 974, 975, 978, 979, 984, 997, 1001, 1002, 1014, 1017, 1018, 1022, 1023, 1030, 1034, 1036, 1041, 1049, 1051, 1054, 1058, 1060, 1070, 1071, 1074, 1075, 1077, 1081, 1083]
group2 = [2, 3, 5, 7, 9, 15, 16, 17, 22, 24, 31, 32, 33, 38, 41, 47, 48, 52, 60, 61, 63, 68, 77, 81, 82, 88, 91, 100, 101, 102, 105, 108, 111, 113, 114, 116, 128, 132, 137, 141, 143, 146, 156, 177, 183, 186, 194, 196, 201, 209, 219, 220, 222, 223, 224, 225, 234, 238, 249, 251, 252, 253, 261, 263, 267, 269, 275, 279, 283, 288, 291, 294, 298, 302, 316, 322, 325, 327, 338, 341, 343, 345, 348, 350, 352, 353, 355, 361, 363, 365, 367, 369, 375, 384, 409, 410, 414, 415, 429, 430, 431, 437, 443, 447, 448, 451, 454, 468, 469, 472, 473, 481, 484, 500, 505, 507, 512, 514, 522, 535, 537, 542, 562, 563, 565, 573, 575, 576, 579, 585, 612, 641, 648, 651, 652, 654, 656, 659, 660, 662, 669, 673, 690, 691, 706, 710, 712, 723, 736, 738, 741, 743, 747, 753, 759, 760, 763, 770, 778, 788, 794, 795, 797, 800, 801, 811, 815, 816, 819, 821, 832, 833, 836, 843, 846, 849, 851, 854, 855, 860, 870, 877, 883, 884, 889, 894, 902, 907, 913, 915, 922, 924, 928, 931, 937, 939, 941, 942, 957, 959, 965, 981, 990, 991, 992, 993, 998, 1000, 1005, 1011, 1013, 1029, 1040, 1045, 1050, 1052, 1053, 1057, 1061, 1062, 1063, 1067, 1069, 1073, 1078]
gfp = [0, 1, 2, 7, 9, 12, 14, 17, 18, 19, 20, 21, 24, 27, 28, 29, 30, 31, 32, 33, 34, 36, 39, 42, 46, 47, 49, 50, 52, 54, 55, 57, 60, 61, 65, 72, 73, 75, 76, 77, 79, 81, 85, 86, 87, 88, 92, 94, 96, 97, 99, 100, 101, 106, 107, 108, 109, 110, 112, 114, 116, 117, 118, 119, 121, 125, 127, 128, 129, 130, 131, 135, 136, 137, 140, 141, 142, 143, 145, 147, 148, 149, 150, 151, 152, 153, 154, 156, 158, 159, 163, 164, 165, 166, 167, 170, 172, 173, 178, 180, 181, 183, 184, 185, 186, 188, 189, 190, 191, 194, 195, 197, 198, 201, 203, 204, 206, 207, 209, 210, 215, 217, 219, 220, 221, 222, 226, 227, 229, 230, 232, 233, 234, 235, 237, 238, 240, 241, 242, 243, 244, 245, 247, 250, 251, 252, 253, 254, 256, 257, 258, 263, 264, 265, 269, 270, 272, 273, 275, 278, 279, 280, 281, 282, 284, 286, 288, 289, 290, 291, 294, 295, 297, 299, 300, 302, 304, 305, 306, 307, 310, 311, 312, 314, 315, 318, 320, 321, 324, 325, 327, 328, 329, 330, 331, 332, 335, 336, 337, 339, 340, 341, 345, 346, 350, 351, 353, 356, 359, 360, 361, 366, 370, 374, 379, 381, 382, 383, 385, 386, 387, 392, 393, 394, 395, 397, 398, 400, 401, 402, 403, 405, 406, 407, 408, 409, 410, 411, 418, 420, 422, 423, 424, 425, 427, 428, 429, 433, 434, 436, 438, 440, 441, 443, 446, 447, 448, 449, 452, 453, 454, 455, 458, 460, 462, 463, 465, 466, 467, 468, 470, 473, 475, 476, 478, 479, 480, 483, 484, 487, 488, 489, 492, 493, 494, 495, 497, 499, 500, 501, 504, 505, 506, 508, 510, 513, 514, 517, 518, 519, 521, 523, 525, 526, 529, 530, 531, 532, 533, 537, 540, 542, 543, 546, 548, 549, 552, 556, 557, 559, 560, 561, 563, 575, 576, 577, 578, 579, 581, 582, 583, 585, 587, 588, 592, 594, 595, 598, 599, 601, 602, 603, 604, 605, 607, 609, 610, 611, 613, 614, 615, 616, 617, 618, 619, 620, 622, 623, 624, 625, 626, 627, 629, 632, 633, 634, 635, 636, 639, 640, 645, 647, 649, 651, 653, 654, 658, 659, 660, 663, 666, 668, 671, 672, 673, 674, 676, 677, 679, 682, 683, 684, 685, 687, 688, 689, 692, 693, 694, 695, 696, 697, 698, 700, 702, 703, 704, 705, 707, 712, 713, 718, 719, 721, 722, 724, 727, 729, 731, 732, 733, 737, 738, 739, 741, 742, 743, 746, 748, 750, 752, 753, 754, 756, 757, 758, 760, 762, 763, 764, 767, 769, 770, 773, 774, 776, 777, 778, 779, 780, 784, 785, 786, 787, 790, 791, 792, 794, 795, 796, 798, 799, 802, 804, 805, 807, 808, 809, 811, 813, 814, 817, 818, 820, 821, 822, 823, 824, 825, 829, 830, 831, 832, 833, 836, 837, 839, 842, 843, 844, 845, 851, 852, 856, 858, 859, 861, 862, 864, 866, 868, 869, 870, 871, 873, 875, 876, 877, 879, 880, 882, 883, 884, 886, 888, 889, 890, 892, 896, 897, 899, 900, 901, 902, 903, 904, 905, 906, 907, 916, 917, 918, 921, 924, 925, 932, 934, 935, 937, 938, 940, 943, 945, 946, 947, 950, 952, 953, 954, 955, 959, 960, 962, 963, 964, 965, 966, 970, 972, 973, 974, 976, 977, 978, 980, 982, 985, 986, 987, 988, 993, 995, 996, 997, 998, 999]
gfp_samebins = [3, 214, 477, 490, 78]

colors = ["#4D80FF", "#6CA8FF", "#E2E2E2", "#FFDBA1", "#FFC373", "#FFAC33", "#FF9700", "#FF8500", "#FF5500", "#FF1E00"]
chromosome_sizes = chromosome_sizes = [["1", 249250621],["2", 243199373],["3", 198022430],["4", 191154276],["5", 180915260],["6", 171115067],["7", 159138663], ["8", 146364022],["9", 141213431],["10", 135534747],["11", 135006516],["12", 133851895],["13", 115169878],["14", 107349540],["15", 102531392],["16", 90354753],["17", 81195210],["18", 78077248], ["19", 59128983],[" 20", 63025520], ["21", 48129895],["22", 51304566], ["X", 155270560], ["Y", 59373566]]


# In[32]:


cells = len(group1) + len(group2)
all_cells = group1 + group2
with open("node_cnv_calls.bed") as f:
#with open("node_cnv_calls_gfp.bed") as f:
    for x, line in enumerate(f):
        if x > 2: # get rid of headers
            line_split = line.split("\t")
            if int(line_split[3]) in all_cells:
                line_split[4] = int(line_split[4]) - 1
                if int(line_split[4]) > 9:
                    color = colors[-1]
                else:
                    color = colors[int(line_split[4])]
                start_pos = 0    
                for i in chromosome_sizes:
                    if i[0] != line_split[0]:
                        start_pos += i[1]
                    else:
                        start_pos += int(line_split[1])
                        start_pos = start_pos * length_factor
                        break
                #y_pos = int(line_split[3])
                y_pos = all_cells.index(int(line_split[3]))
                write_to_file(draw_rect(start_pos, y_pos + 5, color, (int(line_split[2])-int(line_split[1]))*length_factor, 1, 100))


# In[33]:


write_to_file("</svg>")


# In[ ]:





# In[ ]:




