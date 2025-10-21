import datetime

def dias_entre(f1,f2):
    d1=datetime.date.fromisoformat(f1)
    d2=datetime.date.fromisoformat(f2)
    return abs((d2-d1).days)

print(dias_entre('2020-01-01','2020-01-10'))
