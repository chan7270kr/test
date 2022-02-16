import pyupbit

access = "vZ71xDOAxfbjIgaqouUpWG2ju6dVJP8y6uarXSQO"          # 본인 값으로 변경
secret = "xJm4BdR9PzlOB5YohE7CjJkSVj13BoMpJLV7RxG8"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-STX"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회