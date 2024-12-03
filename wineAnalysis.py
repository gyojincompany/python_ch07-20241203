import pandas as pd

# pip install scipy
# pip install statsmodels

from scipy import stats  # T-Test
from statsmodels.formula.api import ols, glm  # 회귀분석


red_df = pd.read_csv("data/winequality-red.csv", sep=";", header=0, engine="python")
white_df = pd.read_csv("data/winequality-white.csv", sep=";", header=0, engine="python")
# print(red_df)
# print(white_df)

red_df.to_csv("data/winequality-red2.csv",index=False)
white_df.to_csv("data/winequality-white2.csv",index=False)

red_df.insert(0, column="type", value="red")
white_df.insert(0, column="type", value="white")
# type 열을 새롭게 삽입하고, 값을 모두 각각 red와 white 로 채움
# print(red_df)
# print(white_df)

wine = pd.concat([red_df, white_df])  # 두 데이터를 병합
# print(wine)
wine.to_csv("data/wine.csv", index=False)
# 두 와인 데이터를 병합한 wine.csv 만들기

print(wine.info())  # 데이터의 기본 정보 확인

wine.columns = wine.columns.str.replace(" ","_")
# 열의 이름에 들어 있는 공백을 모두 '_'로 변경

print(wine.info())  # 데이터의 기본 정보 확인

print(wine.describe())  # 데이터의 기술통계 정보 확인

print(sorted(wine.quality.unique()))  # 등급 값 정렬 출력->3, 4, 5, 6, 7, 8, 9->3~9까지 7개 등급이 존재
print(wine.quality.value_counts())  # 각 등급별 개수

print(wine.groupby("type")["quality"].describe())
# 두 와인 레드, 화이트 별로 각각 그룹으로 묶어 quality 의 요약 통계 출력

print(wine.groupby("type")["quality"].mean())
# 두 와인 레드, 화이트 별로 각각 그룹으로 묶어 quality 의 평균값 들만 따로 출력

print(wine.groupby("type")["quality"].std())
# 두 와인 레드, 화이트 별로 각각 그룹으로 묶어 quality 의 표준편차 들만 따로 출력

print(wine.groupby("type")["quality"].agg(["mean","std"]))
# 두 와인 레드, 화이트 별로 각각 그룹으로 묶어 quality 의 평균과 표준편차 들만 묶어서 한번에 출력

red_wine_quality = wine.loc[wine["type"]=="red","quality"]  # type이 red인 데이터 중에서 quality열만 추출
white_wine_quality = wine.loc[wine["type"]=="white","quality"]  # type이 white인 데이터 중에서 quality열만 추출

print("=====================T-검정=====================")
print(stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var=False))  # T-test 검정

print("=====================회귀분석=====================")
Rformula = "quality ~ fixed_acidity+volatile_acidity+citric_acid+residual_sugar+chlorides+free_sulfur_dioxide+total_sulfur_dioxide+density+pH+sulphates+alcohol"
regression_result = ols(Rformula, data=wine).fit()
print(regression_result.summary())

print("================================================")
sample1 = wine[wine.columns.difference(["quality","type"])]  # quality, type 열을 제외한 열들만 따로 sample1로 저장
print(sample1)
sample1 = sample1[0:5][:]
print(sample1)

sample1_predict = regression_result.predict(sample1)  # sample1의 등급 예측 결과
print(sample1_predict)  # 만들어진 회귀모델이 예측한 결과
print(wine[0:5]["quality"])  # 0~4행까지의 실제 등급

# 새로운 와인 샘플의 성분 데이터
randomData = {"fixed_acidity":[8.5,8.1],"volatile_acidity":[0.8,0.5],"citric_acid":[0.3,0.4],
              "residual_sugar":[6.1,5.8], "chlorides":[0.055,0.04], "free_sulfur_dioxide":[30.0,31.0],
              "total_sulfur_dioxide":[98.0,99],"density":[0.996,0.91],"pH":[3.25,3.01],"sulphates":[0.4,0.35],
              "alcohol":[9.0,0.88]}


sample2 = pd.DataFrame(randomData, columns=sample1.columns)
print(sample2)
sample2_predict = regression_result.predict(sample2)
print(sample2_predict)
