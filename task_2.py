numb = int(input ("Enter the time of seconds: "))
if numb < 60:
    print(f"00:00:{numb:02}"
elif number < 3600:
    print(f"00:{numb // 60:02}: {numb % 60:02}")
else:
    print({number // 3600:02}:{(number % 3600)// 60:02}:{numb % 60:02})