import pandas as pd
import random as r
import math as m


df1 = pd.read_csv(r'C:\Users\91730\Downloads\CC GENERAL.csv')
df1.drop('CUST_ID', inplace=True, axis=1)

c1 = r.randint(0, 8949)
c2 = r.randint(0, 8949)
c3 = r.randint(0, 8949)
centroid1 = df1.iloc[c1]
centroid2 = df1.iloc[c2]
centroid3 = df1.iloc[c3]
# print('The selected centroids are:')
    
    # print(centroid1, '\n')
    # print(centroid2, '\n')
    # print(centroid3, '\n')
for i in range(0, 10):
   
    
    
  
    cluster1 = []
    cluster2 = []
    cluster3 = []
    
    
    for j in range(0, 8949):
        if j == c1 or j == c2 or j == c3:
            continue
        
        point = df1.iloc[j]
        temp1=0
        temp2=0
        temp3=0
        for i in range(0,17):
           temp1=temp1+(point.iloc[i]-centroid1.iloc[i])**2
           temp2=temp2+(point.iloc[i]-centroid2.iloc[i])**2
           temp3=temp3+(point.iloc[i]-centroid3.iloc[i])**2
        temp1=m.sqrt(temp1)
        temp2=m.sqrt(temp2)
        temp3=m.sqrt(temp3)
        if temp1 <= temp2 and temp1 <= temp3:
            cluster1.append(j)
        elif temp2 <= temp1 and temp2 <= temp3:
            cluster2.append(j)
        else:
            cluster3.append(j)

    new_centroid1 = df1.iloc[cluster1].mean()
    new_centroid2 = df1.iloc[cluster2].mean()
    new_centroid3 = df1.iloc[cluster3].mean()
    # print('Cluster 1 \n',cluster1)
    # print('cluster 2\n',cluster2)
    # print('cluster 3\n',cluster3)
    
    print('sizes of cluster 1 2 and 3 are respectively ',len(cluster1),len(cluster2),len(cluster3))
    # Check convergence by comparing new centroids with previous centroids
    if (centroid1.equals(new_centroid1) and centroid2.equals(new_centroid2) and centroid3.equals(new_centroid3)):
        break

    centroid1, centroid2, centroid3 = new_centroid1, new_centroid2, new_centroid3        

    # Create DataFrames for each cluster
    cluster1_df = df1.iloc[cluster1]
    cluster2_df = df1.iloc[cluster2]
    cluster3_df = df1.iloc[cluster3]

    # Write each DataFrame to a CSV file
    cluster1_df.to_csv('cluster1.csv', index=False)
    cluster2_df.to_csv('cluster2.csv', index=False)
    cluster3_df.to_csv('cluster3.csv', index=False)
    