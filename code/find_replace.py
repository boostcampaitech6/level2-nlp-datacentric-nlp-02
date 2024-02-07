import pandas as pd

df1 = pd.read_csv('### original data ###')
df2 = pd.read_csv('### denoised data ###')

different = []

'''
원본은 그대로 두고 노이즈가 발생한 항목에 대해서만 추가로 정제된 데이터를 넣어주는 작업.
'''

for i in range(len(df1)):
    if df1.loc[i, 'text'] != df2.loc[i, 'text']:
        different.append(df2.loc[i])
        
df1 = pd.concat([df1, pd.DataFrame(different)], ignore_index=True)


df1.to_csv("### save ###", index=False)