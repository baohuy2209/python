# 

# As you may recall from Chapter 8, pandas has some tools, in particular pandas.cut
# and pandas.qcut, for slicing data up into buckets with bins of your choosing, or by
# sample quantiles. Combining these functions with groupby makes it convenient to
# perform bucket or quantile analysis on a dataset. Consider a simple random dataset
# and an equal-length bucket categorization using pandas.cut


# Như bạn có thể nhớ lại ở Chương 8, pandas có một số công cụ, đặc biệt là pandas.cut
# và pandas.qcut, để chia dữ liệu thành các nhóm với các thùng bạn chọn hoặc bằng cách
# lượng tử mẫu. Việc kết hợp các chức năng này với groupby sẽ thuận tiện hơn cho việc
# thực hiện phân tích nhóm hoặc lượng tử trên một tập dữ liệu. Hãy xem xét một tập dữ liệu ngẫu nhiên đơn giản
# và phân loại nhóm có độ dài bằng nhau bằng pandas.cut

import pandas as pd 
import numpy as np 

def get_stats(group):
    return pd.DataFrame(
        {"min": group.min(), "max" : group.max(),
         "count" : group.count(), "mean" : group.mean()}
    )

frame = pd.DataFrame({"data1" : [12,2,3,21,234,2,1], 
                      "data2" : [1,2,3,12,10,45,22,]})

quartiles = pd.cut(frame["data1"], 4)
print(quartiles) 
print("=================================")

grouped = frame.groupby(quartiles).apply(get_stats)

print(grouped) 
print(grouped.unstack())


