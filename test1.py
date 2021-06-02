import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import matplotlib
from matplotlib.colors import ListedColormap
from matplotlib import font_manager, rc

#폰트 설정
font_fname = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
font_name = font_manager.FontProperties(fname=font_fname).get_name()
rc('font', family=font_name)

#용천이형 취합
motive=pd.read_csv('범행동기.csv',encoding='cp949')
motive = motive.transpose(copy=True)
motive.rename(columns=motive.iloc[1], inplace=True)
motive.drop(motive.index[0:2], inplace=True)
motive[motive.columns] = motive[motive.columns].apply(pd.to_numeric)
friend_drop = motive.loc[('허영사치심','사행심','호기심','유혹','현실불만','부주의'), : ].sum(axis=0)
friend_drop.name = '경찰청_범죄자_범행동기'
motive = motive.append(friend_drop)
motive.drop(['허영사치심','사행심','호기심','유혹','현실불만','부주의'], axis=0, inplace=True)
empty_drop = motive.loc[('기타', '기타1','미분류') , : ].sum(axis=0)
empty_drop.name = '기타동기'
motive = motive.append(empty_drop)
motive.drop(['기타', '기타1','미분류'], axis=0, inplace=True)
motive.to_csv('space_of_crime.csv',encoding='cp949')
c=pd.read_csv('space_of_crime.csv',encoding='cp949')

#세은이쪽 취합
Place=pd.read_csv('20141231..csv',encoding='cp949')
Place = Place.transpose(copy=True)
Place.rename(columns=Place.iloc[1], inplace=True)
Place.drop(Place.index[0:2], inplace=True)
Place[Place.columns] = Place[Place.columns].apply(pd.to_numeric)
Place.to_csv('space_of_crime.csv',encoding='cp949')
a=pd.read_csv('space_of_crime.csv',encoding='cp949')

#광원이형 취합
accomplice=pd.read_csv('complicity.csv',encoding='utf-8')
accomplice = accomplice.transpose(copy=True)
accomplice.rename(columns=accomplice.iloc[1], inplace=True)
accomplice.drop(accomplice.index[0:2], inplace=True)
accomplice[accomplice.columns] = accomplice[accomplice.columns].apply(pd.to_numeric)
accomplice.to_csv('complicity1.csv',encoding='cp949')
b=pd.read_csv('complicity1.csv',encoding='cp949')


#영완이 코드
complicity = pd.read_csv('/home/aiot110/PycharmProjects/pythonProject/빅데이터/경찰청_범죄자 생활정도, 혼인관계 및 부모관계_20151231.csv',
                         encoding='cp949')
marriage = complicity.transpose(copy=True)
marriage.rename(columns=marriage.iloc[1], inplace=True)
marriage.drop(marriage.index[0:2], inplace=True)
marriage[marriage.columns] = marriage[marriage.columns].apply(pd.to_numeric)
smnomarry = marriage.loc['미혼자부모관계(실(양)부모)':'미상', :].sum(axis=0)
smnomarry.name = '미혼자부모관계(실부모,계부모)'
marriage = marriage.append(smnomarry)
marriage.drop(['미혼자부모관계(실(양)부모)', '미혼자부모관계(계부모)', '미혼자부모관계(실부계모)', '미혼자부모관계(실부무모)', '미혼자부모관계(실모계부)',
                      '미혼자부모관계(실모무부)', '미혼자부모관계(계부무모)', '미혼자부모관계(계모무부)','미혼자부모관계(무부모)','생활정도(미상)','미상'],axis=0,inplace=True)
marriage.to_csv('생활정도와혼인관계.csv',encoding='cp949')

#폰트 설정
plt.rcParams['font.family'] = 'nanummyeongjo'
plt.rcParams['font.size']=10.
plt.rcParams['axes.unicode_minus']=False

#트랜스포스한 파일 취합후 plot.bar에 출력
space_singel_mom=pd.concat([marriage,Place,accomplice,motive])
space_singel_mom.to_csv('너가해라.csv',encoding='cp949')
space_singel_mom.plot.bar(stacked=True,legend='reverse',figsize=(17,15))
plt.legend(bbox_to_anchor=(1,1.15))
plt.show()
