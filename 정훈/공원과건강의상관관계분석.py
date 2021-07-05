import pandas as pd

data1 = pd.read_csv('../raw/서울시 공원 (1인당 공원면적) 통계(2017).txt', sep ='\t',encoding='UTF8')
data2 = pd.read_csv('../raw/서울시 지역사회 건강통계(건강행태) 통계(2017).txt', sep ='\t',encoding='UTF8')
data3 = pd.read_csv('../raw/서울시 공원 통계(2017).txt', sep ='\t',encoding='UTF8')

df1 = data1.drop([0,1])
df1 = df1.drop(['기간'],axis=1)
index1 = ['자치구','공원 면적', '1인당 공원 면적','도시공원 면적', '1인당 도시공원 면적','생활권 공원 면적', '1인당 생활권 공원 면적']
df1.columns = index1
df1 = df1.set_index("자치구")

df2 = data2.drop([0])
df2 = df2.drop(['기간','흡연','흡연.1','음주','음주.1'],axis=1)
index2=['자치구','증등도 이상 신체활동 실천율','걷기실천율','비만율','스트레스 인지율','우울감 경험률','양호한 주관적 건강수준 인지율']
df2.columns=index2
df2 = df2.set_index("자치구")

df3 = pd.concat([df1,df2],axis=1, join='inner') 

def remove_comma(x):
    return x.replace(',', '')

df3['공원 면적'] = df3['공원 면적'].apply(remove_comma)
df3['도시공원 면적'] = df3['도시공원 면적'].apply(remove_comma)
df3['생활권 공원 면적'] = df3['생활권 공원 면적'].apply(remove_comma)
df3 = df3.astype('float')

import matplotlib as mp
import matplotlib.pyplot as plt
import seaborn as sns
fm = mp.font_manager.FontManager()

plt.rcParams['font.family'] = 'Malgun Gothic'

plt.figure(figsize=(30,30))
plt.xticks(rotation=45)
sns.lineplot(data=df3)

corr = df3.corr()

corr