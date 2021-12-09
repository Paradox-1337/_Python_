# ### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; *
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
# минута = 60
# час = 3600
# день = 86400

#-------------
# первое решение

user_time = int(input("Enter sec: "))

# найдем чему равняются день, час, минута в секундах
# используем целочисленное деление, чтобы потом не переводить флоат в инт

day = user_time // 86400
hour = user_time // 3600 % 24
minute = user_time // 60 % 60
sec = user_time % 60

# добавим проверку на нулевые дни , часы и минуты, чтобы они не попадали в вывод , как и просит нас условие
# в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.
if day == 0 and hour == 0 and minute == 0:
    print(sec , "Sec")
elif day == 0 and hour == 0 and minute >= 1:
    print (minute , "Min", sec, "sec")
elif day == 0 and hour >= 1:
    print (hour, "hour" ,minute , "min", sec, "sec")
else:
    print (day, "day", hour, "hour" ,minute , "min", sec, "sec")

#-------------

# можно записать код в пару строк, но он не совсем тогда соответсвует условию


# user_time = int(input("Enter sec: "))
#
# day, hour, minute, sec = user_time // 86400, user_time // 3600 % 24, user_time // 60 % 60, user_time % 60
#
# print(day, "day", hour, "hour", minute, "minute", sec, "sec")

#-------------

#-------------

# будет ли тут полезен список?
#даже не знаю, наверное возможно , но выглядит это страшновато и вообще не очень


# user_time = int(input("Enter sec: "))
#
# day = user_time // 86400, "day"
# hour = user_time // 3600 % 24, "hour"
# minute = user_time // 60 % 60, "minute"
# sec = user_time % 60, "sec"
#
# list_time = day, hour, minute, sec
#
# print(list_time)

#-------------