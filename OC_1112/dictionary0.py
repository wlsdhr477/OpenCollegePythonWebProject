#딕셔너리
a = {"김도한" : "010-7178-0000"}
print(a["김도한"])
a["박지영"]="010-9765-1111"
print(a)

#리스트
b = ["010-7178-0000"]
print(b[0])

#딕셔너리-키가 튜플
c={("정유선","성악") : "이태원"}
print(c["정유선","성악"])

#딕셔너리 - get
d={"김도한":"맥주", "이광우":"소주", "정유선":"막걸리"}
print(d.get("김도한"))
print(d["김도한"])

#bool type = trud, false
is_jiyoung_exist = "박지영" in d
print(type(is_jiyoung_exist))
print(type(d))

#element 삭제 딕셔너리 - 삭제
d.pop("김도한")
del d["이광우"]
print(d)