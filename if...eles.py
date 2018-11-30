height = 1.75
weight = 80.5
BMI = weight/pow(height, 2)

if height < 0 or weight < 0:
    print("参数错误！")
    exit(0)

if BMI < 18.5:
    print('过轻')
elif 18.5 <= BMI <25:
    print('正常')
elif 25 <= BMI < 28:
    print('过重')
elif 28 <= BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')