import pandas as pd

# pip install scipy
# pip install statsmodels


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



