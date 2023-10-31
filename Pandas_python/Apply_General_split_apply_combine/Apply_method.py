import pandas as pd 
import numpy as np 

def top1(df, n = 5, column = "tip_pct"):
    return df.sort_values(column, ascending = False)[:n]

def top2(df, n = 7, column = "total_bill"):
    return df.sort_values(column, ascending = True)[:n]

filename = "C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/Data_Aggregation_and_Group_Operations/Column_Wise_and_Multiple_Function_Application/tips.csv"

tips = pd.read_csv(filename) 

tips["tip_pct"] = tips["tip"]/tips["total_bill"]

grouped1 = tips.groupby("smoker").apply(top1)
print(grouped1)

#             total_bill   tip     sex smoker   day    time  size   tip_pct
# smoker                                                                   
# No     232       11.61  3.39    Male     No   Sat  Dinner     2  0.291990
#        149        7.51  2.00    Male     No  Thur   Lunch     2  0.266312
#        51        10.29  2.60  Female     No   Sun  Dinner     2  0.252672
#        185       20.69  5.00    Male     No   Sun  Dinner     5  0.241663
#        88        24.71  5.85    Male     No  Thur   Lunch     2  0.236746
# Yes    172        7.25  5.15    Male    Yes   Sun  Dinner     2  0.710345
#        178        9.60  4.00  Female    Yes   Sun  Dinner     2  0.416667
#        67         3.07  1.00  Female    Yes   Sat  Dinner     1  0.325733
#        183       23.17  6.50    Male    Yes   Sun  Dinner     4  0.280535
#        109       14.31  4.00  Female    Yes   Sat  Dinner     2  0.279525


grouped2 = tips.groupby("day").apply(top2)
print(grouped2)

#           total_bill   tip     sex smoker   day    time  size   tip_pct
# day                                                                    
# Fri  92         5.75  1.00  Female    Yes   Fri  Dinner     2  0.173913
#      222        8.58  1.92    Male    Yes   Fri   Lunch     1  0.223776
#      226       10.09  2.00  Female    Yes   Fri   Lunch     2  0.198216
#      100       11.35  2.50  Female    Yes   Fri  Dinner     2  0.220264
#      97        12.03  1.50    Male    Yes   Fri  Dinner     2  0.124688
#      220       12.16  2.20    Male    Yes   Fri   Lunch     2  0.180921
#      99        12.46  1.50    Male     No   Fri  Dinner     2  0.120385
# Sat  67         3.07  1.00  Female    Yes   Sat  Dinner     1  0.325733
#      111        7.25  1.00  Female     No   Sat  Dinner     1  0.137931
#      218        7.74  1.44    Male    Yes   Sat  Dinner     2  0.186047
#      30         9.55  1.45    Male     No   Sat  Dinner     2  0.151832
#      235       10.07  1.25    Male     No   Sat  Dinner     2  0.124131
#      75        10.51  1.25    Male     No   Sat  Dinner     2  0.118934
#      168       10.59  1.61  Female    Yes   Sat  Dinner     2  0.152030
# Sun  172        7.25  5.15    Male    Yes   Sun  Dinner     2  0.710345
#      6          8.77  2.00    Male     No   Sun  Dinner     2  0.228050
#      178        9.60  4.00  Female    Yes   Sun  Dinner     2  0.416667
#      43         9.68  1.32    Male     No   Sun  Dinner     2  0.136364
#      53         9.94  1.56    Male     No   Sun  Dinner     2  0.156942
#      10        10.27  1.71    Male     No   Sun  Dinner     2  0.166504
#      51        10.29  2.60  Female     No   Sun  Dinner     2  0.252672
# Thur 149        7.51  2.00    Male     No  Thur   Lunch     2  0.266312
#      195        7.56  1.44    Male     No  Thur   Lunch     2  0.190476
#      145        8.35  1.50  Female     No  Thur   Lunch     2  0.179641
#      135        8.51  1.25  Female     No  Thur   Lunch     2  0.146886
#      126        8.52  1.48    Male     No  Thur   Lunch     2  0.173709
#      148        9.78  1.73    Male     No  Thur   Lunch     2  0.176892
#      82        10.07  1.83  Female     No  Thur   Lunch     1  0.181728

print(tips.groupby(["smoker", "day"]).apply(top1, n = 6, column = "tip_pct"))

#             total_bill   tip     sex smoker   day    time  size   tip_pct
# smoker day                                                                    
# No     Fri  223       15.98  3.00  Female     No   Fri   Lunch     3  0.187735
#             91        22.49  3.50    Male     No   Fri  Dinner     2  0.155625
#             94        22.75  3.25  Female     No   Fri  Dinner     2  0.142857
#             99        12.46  1.50    Male     No   Fri  Dinner     2  0.120385
#        Sat  232       11.61  3.39    Male     No   Sat  Dinner     2  0.291990
#             20        17.92  4.08    Male     No   Sat  Dinner     2  0.227679
#             110       14.00  3.00    Male     No   Sat  Dinner     2  0.214286
#             108       18.24  3.76    Male     No   Sat  Dinner     2  0.206140
#             228       13.28  2.72    Male     No   Sat  Dinner     2  0.204819
#             239       29.03  5.92    Male     No   Sat  Dinner     3  0.203927
#        Sun  51        10.29  2.60  Female     No   Sun  Dinner     2  0.252672
#             185       20.69  5.00    Male     No   Sun  Dinner     5  0.241663
#             6          8.77  2.00    Male     No   Sun  Dinner     2  0.228050
#             17        16.29  3.71    Male     No   Sun  Dinner     3  0.227747
#             46        22.23  5.00    Male     No   Sun  Dinner     2  0.224921
#             42        13.94  3.06    Male     No   Sun  Dinner     2  0.219512
#        Thur 149        7.51  2.00    Male     No  Thur   Lunch     2  0.266312
#             88        24.71  5.85    Male     No  Thur   Lunch     2  0.236746
#             87        18.28  4.00    Male     No  Thur   Lunch     2  0.218818
#             139       13.16  2.75  Female     No  Thur   Lunch     2  0.208967
#             81        16.66  3.40    Male     No  Thur   Lunch     2  0.204082
#             124       12.48  2.52  Female     No  Thur   Lunch     2  0.201923
# Yes    Fri  93        16.32  4.30  Female    Yes   Fri  Dinner     2  0.263480
#             221       13.42  3.48  Female    Yes   Fri   Lunch     2  0.259314
#             222        8.58  1.92    Male    Yes   Fri   Lunch     1  0.223776
#             100       11.35  2.50  Female    Yes   Fri  Dinner     2  0.220264
#             226       10.09  2.00  Female    Yes   Fri   Lunch     2  0.198216
#             101       15.38  3.00  Female    Yes   Fri  Dinner     2  0.195059
#        Sat  67         3.07  1.00  Female    Yes   Sat  Dinner     1  0.325733
#             109       14.31  4.00  Female    Yes   Sat  Dinner     2  0.279525
#             214       28.17  6.50  Female    Yes   Sat  Dinner     3  0.230742
#             63        18.29  3.76    Male    Yes   Sat  Dinner     4  0.205577
#             171       15.81  3.16    Male    Yes   Sat  Dinner     2  0.199873
#             211       25.89  5.16    Male    Yes   Sat  Dinner     4  0.199305
#        Sun  172        7.25  5.15    Male    Yes   Sun  Dinner     2  0.710345
#             178        9.60  4.00  Female    Yes   Sun  Dinner     2  0.416667
#             183       23.17  6.50    Male    Yes   Sun  Dinner     4  0.280535
#             181       23.33  5.65    Male    Yes   Sun  Dinner     2  0.242177
#             174       16.82  4.00    Male    Yes   Sun  Dinner     2  0.237812
#             188       18.15  3.50  Female    Yes   Sun  Dinner     3  0.192837
#        Thur 194       16.58  4.00    Male    Yes  Thur   Lunch     2  0.241255
#             200       18.71  4.00    Male    Yes  Thur   Lunch     3  0.213789
#             191       19.81  4.19  Female    Yes  Thur   Lunch     2  0.211509
#             205       16.47  3.23  Female    Yes  Thur   Lunch     3  0.196114
#             204       20.53  4.00    Male    Yes  Thur   Lunch     4  0.194837
#             196       10.34  2.00    Male    Yes  Thur   Lunch     2  0.193424

print(tips.groupby(["smoker", "day"]).apply(top2, n = 3))

#                  total_bill   tip     sex smoker   day    time  size   tip_pct
# smoker day                                                                    
# No     Fri  99        12.46  1.50    Male     No   Fri  Dinner     2  0.120385
#             223       15.98  3.00  Female     No   Fri   Lunch     3  0.187735
#             91        22.49  3.50    Male     No   Fri  Dinner     2  0.155625
#        Sat  111        7.25  1.00  Female     No   Sat  Dinner     1  0.137931
#             30         9.55  1.45    Male     No   Sat  Dinner     2  0.151832
#             235       10.07  1.25    Male     No   Sat  Dinner     2  0.124131
#        Sun  6          8.77  2.00    Male     No   Sun  Dinner     2  0.228050
#             43         9.68  1.32    Male     No   Sun  Dinner     2  0.136364
#             53         9.94  1.56    Male     No   Sun  Dinner     2  0.156942
#        Thur 149        7.51  2.00    Male     No  Thur   Lunch     2  0.266312
#             195        7.56  1.44    Male     No  Thur   Lunch     2  0.190476
#             145        8.35  1.50  Female     No  Thur   Lunch     2  0.179641
# Yes    Fri  92         5.75  1.00  Female    Yes   Fri  Dinner     2  0.173913
#             222        8.58  1.92    Male    Yes   Fri   Lunch     1  0.223776
#             226       10.09  2.00  Female    Yes   Fri   Lunch     2  0.198216
#        Sat  67         3.07  1.00  Female    Yes   Sat  Dinner     1  0.325733
#             218        7.74  1.44    Male    Yes   Sat  Dinner     2  0.186047
#             168       10.59  1.61  Female    Yes   Sat  Dinner     2  0.152030
#        Sun  172        7.25  5.15    Male    Yes   Sun  Dinner     2  0.710345
#             178        9.60  4.00  Female    Yes   Sun  Dinner     2  0.416667
#             177       14.48  2.00    Male    Yes   Sun  Dinner     2  0.138122
#        Thur 196       10.34  2.00    Male    Yes  Thur   Lunch     2  0.193424
#             201       12.74  2.01  Female    Yes  Thur   Lunch     2  0.157771
#             202       13.00  2.00  Female    Yes  Thur   Lunch     2  0.153846

print(tips.groupby("time").apply(top1, n = 10))

# #             total_bill   tip     sex smoker   day    time  size   tip_pct
# time                                                                     
# Dinner 172        7.25  5.15    Male    Yes   Sun  Dinner     2  0.710345
#        178        9.60  4.00  Female    Yes   Sun  Dinner     2  0.416667
#        67         3.07  1.00  Female    Yes   Sat  Dinner     1  0.325733
#        232       11.61  3.39    Male     No   Sat  Dinner     2  0.291990
#        183       23.17  6.50    Male    Yes   Sun  Dinner     4  0.280535
#        109       14.31  4.00  Female    Yes   Sat  Dinner     2  0.279525
#        93        16.32  4.30  Female    Yes   Fri  Dinner     2  0.263480
#        51        10.29  2.60  Female     No   Sun  Dinner     2  0.252672
#        181       23.33  5.65    Male    Yes   Sun  Dinner     2  0.242177
#        185       20.69  5.00    Male     No   Sun  Dinner     5  0.241663
# Lunch  149        7.51  2.00    Male     No  Thur   Lunch     2  0.266312
#        221       13.42  3.48  Female    Yes   Fri   Lunch     2  0.259314
#        194       16.58  4.00    Male    Yes  Thur   Lunch     2  0.241255
#        88        24.71  5.85    Male     No  Thur   Lunch     2  0.236746
#        222        8.58  1.92    Male    Yes   Fri   Lunch     1  0.223776
#        87        18.28  4.00    Male     No  Thur   Lunch     2  0.218818
#        200       18.71  4.00    Male    Yes  Thur   Lunch     3  0.213789
#        191       19.81  4.19  Female    Yes  Thur   Lunch     2  0.211509
#        139       13.16  2.75  Female     No  Thur   Lunch     2  0.208967
#        81        16.66  3.40    Male     No  Thur   Lunch     2  0.204082

print(tips.groupby(["smoker", "day", "time"]).apply(top1, n = 3))

#                         total_bill   tip     sex  ...    time size   tip_pct
# smoker day  time                                  ...                       
# No     Fri  Dinner 99        12.46  1.50    Male  ...  Dinner    2  0.120385
#                    91        22.49  3.50    Male  ...  Dinner    2  0.155625
#                    94        22.75  3.25  Female  ...  Dinner    2  0.142857
#             Lunch  223       15.98  3.00  Female  ...   Lunch    3  0.187735
#        Sat  Dinner 111        7.25  1.00  Female  ...  Dinner    1  0.137931
#                    30         9.55  1.45    Male  ...  Dinner    2  0.151832
#                    235       10.07  1.25    Male  ...  Dinner    2  0.124131
#                    75        10.51  1.25    Male  ...  Dinner    2  0.118934
#                    233       10.77  1.47    Male  ...  Dinner    2  0.136490
#                    232       11.61  3.39    Male  ...  Dinner    2  0.291990
#                    70        12.02  1.97    Male  ...  Dinner    2  0.163894
#        Sun  Dinner 6          8.77  2.00    Male  ...  Dinner    2  0.228050
#                    43         9.68  1.32    Male  ...  Dinner    2  0.136364
#                    53         9.94  1.56    Male  ...  Dinner    2  0.156942
#                    10        10.27  1.71    Male  ...  Dinner    2  0.166504
#                    51        10.29  2.60  Female  ...  Dinner    2  0.252672
#                    16        10.33  1.67  Female  ...  Dinner    3  0.161665
#                    1         10.34  1.66    Male  ...  Dinner    3  0.160542
#        Thur Dinner 243       18.78  3.00  Female  ...  Dinner    2  0.159744
#             Lunch  149        7.51  2.00    Male  ...   Lunch    2  0.266312
#                    195        7.56  1.44    Male  ...   Lunch    2  0.190476
#                    145        8.35  1.50  Female  ...   Lunch    2  0.179641
#                    135        8.51  1.25  Female  ...   Lunch    2  0.146886
#                    126        8.52  1.48    Male  ...   Lunch    2  0.173709
#                    148        9.78  1.73    Male  ...   Lunch    2  0.176892
#                    82        10.07  1.83  Female  ...   Lunch    1  0.181728
# Yes    Fri  Dinner 92         5.75  1.00  Female  ...  Dinner    2  0.173913
#                    100       11.35  2.50  Female  ...  Dinner    2  0.220264
#                    97        12.03  1.50    Male  ...  Dinner    2  0.124688
#                    101       15.38  3.00  Female  ...  Dinner    2  0.195059
#                    93        16.32  4.30  Female  ...  Dinner    2  0.263480
#                    98        21.01  3.00    Male  ...  Dinner    2  0.142789
#                    96        27.28  4.00    Male  ...  Dinner    2  0.146628
#             Lunch  222        8.58  1.92    Male  ...   Lunch    1  0.223776
#                    226       10.09  2.00  Female  ...   Lunch    2  0.198216
#                    220       12.16  2.20    Male  ...   Lunch    2  0.180921
#                    221       13.42  3.48  Female  ...   Lunch    2  0.259314
#                    224       13.42  1.58    Male  ...   Lunch    2  0.117735
#                    225       16.27  2.50  Female  ...   Lunch    2  0.153657
#        Sat  Dinner 67         3.07  1.00  Female  ...  Dinner    1  0.325733
#                    218        7.74  1.44    Male  ...  Dinner    2  0.186047
#                    168       10.59  1.61  Female  ...  Dinner    2  0.152030
#                    169       10.63  2.00  Female  ...  Dinner    2  0.188147
#                    62        11.02  1.98    Male  ...  Dinner    2  0.179673
#                    58        11.24  1.76    Male  ...  Dinner    2  0.156584
#                    217       11.59  1.50    Male  ...  Dinner    2  0.129422
#        Sun  Dinner 172        7.25  5.15    Male  ...  Dinner    2  0.710345
#                    178        9.60  4.00  Female  ...  Dinner    2  0.416667
#                    177       14.48  2.00    Male  ...  Dinner    2  0.138122
#                    190       15.69  1.50    Male  ...  Dinner    2  0.095602
#                    174       16.82  4.00    Male  ...  Dinner    2  0.237812
#                    164       17.51  3.00  Female  ...  Dinner    2  0.171331
#                    176       17.89  2.00    Male  ...  Dinner    2  0.111794
#        Thur Lunch  196       10.34  2.00    Male  ...   Lunch    2  0.193424
#                    201       12.74  2.01  Female  ...   Lunch    2  0.157771
#                    202       13.00  2.00  Female  ...   Lunch    2  0.153846
#                    198       13.00  2.00  Female  ...   Lunch    2  0.153846
#                    199       13.51  2.00    Male  ...   Lunch    2  0.148038
#                    193       15.48  2.02    Male  ...   Lunch    2  0.130491
#                    138       16.00  2.00    Male  ...   Lunch    2  0.125000


print(tips.groupby(["smoker", "day", "time"]).apply(top2))

#                         total_bill   tip     sex  ...    time size   tip_pct
# smoker day  time                                  ...                       
# No     Fri  Dinner 91        22.49  3.50    Male  ...  Dinner    2  0.155625
#                    94        22.75  3.25  Female  ...  Dinner    2  0.142857
#                    99        12.46  1.50    Male  ...  Dinner    2  0.120385
#             Lunch  223       15.98  3.00  Female  ...   Lunch    3  0.187735
#        Sat  Dinner 232       11.61  3.39    Male  ...  Dinner    2  0.291990
#                    20        17.92  4.08    Male  ...  Dinner    2  0.227679
#                    110       14.00  3.00    Male  ...  Dinner    2  0.214286
#        Sun  Dinner 51        10.29  2.60  Female  ...  Dinner    2  0.252672
#                    185       20.69  5.00    Male  ...  Dinner    5  0.241663
#                    6          8.77  2.00    Male  ...  Dinner    2  0.228050
#        Thur Dinner 243       18.78  3.00  Female  ...  Dinner    2  0.159744
#             Lunch  149        7.51  2.00    Male  ...   Lunch    2  0.266312
#                    88        24.71  5.85    Male  ...   Lunch    2  0.236746
#                    87        18.28  4.00    Male  ...   Lunch    2  0.218818
# Yes    Fri  Dinner 93        16.32  4.30  Female  ...  Dinner    2  0.263480
#                    100       11.35  2.50  Female  ...  Dinner    2  0.220264
#                    101       15.38  3.00  Female  ...  Dinner    2  0.195059
#             Lunch  221       13.42  3.48  Female  ...   Lunch    2  0.259314
#                    222        8.58  1.92    Male  ...   Lunch    1  0.223776
#                    226       10.09  2.00  Female  ...   Lunch    2  0.198216
#        Sat  Dinner 67         3.07  1.00  Female  ...  Dinner    1  0.325733
#                    109       14.31  4.00  Female  ...  Dinner    2  0.279525
#                    214       28.17  6.50  Female  ...  Dinner    3  0.230742
#        Sun  Dinner 172        7.25  5.15    Male  ...  Dinner    2  0.710345
#                    178        9.60  4.00  Female  ...  Dinner    2  0.416667
#                    183       23.17  6.50    Male  ...  Dinner    4  0.280535
#        Thur Lunch  194       16.58  4.00    Male  ...   Lunch    2  0.241255
#                    200       18.71  4.00    Male  ...   Lunch    3  0.213789
#                    191       19.81  4.19  Female  ...   Lunch    2  0.211509


