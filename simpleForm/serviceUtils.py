def dateConvert(date):
    d = date[0:2]
    m = date[3:5]
    y = date[-4:]
    # print(f"{d}-{m}-{y}")
    newdate = y+"-"+m+"-"+d
    return newdate
    # type :  <class 'str'> value:25/02/2546 err
    # type :  <class 'str'> value:2546-02-25 yes



print(dateConvert('25/02/2546'))