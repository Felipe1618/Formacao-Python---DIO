from datetime import datetime, timedelta, timezone
import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
print(data)

#trabalhando com a função 'tz' -> mais coverboso e menos usado
data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sao_paulo)