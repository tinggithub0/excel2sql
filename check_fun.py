import re

def check_gamelist(dict):
    result = True
    for index in dict:
        # game name
        if len(re.findall(r'"[a-z-]{2,5}":', dict[index][3])) != 7:
            print(f'{dict[index][0]} list - game name 異常')
            result = False

        # game name 檢查 '
        if dict[index][3].find("'") > 0:
            dict[index][3] = dict[index][3].replace("'", "\\'")
        
        # image type 全轉小寫
        if dict[index][8] is None:
            pass
        else:
            if "." in dict[index][8]:
                name, suf = dict[index][8].split(".")
                dict[index][8] = f'{name}.{suf.lower()}'
        
        # currency 檢查
        if len(re.findall(r'"[A-Z]{3}"', dict[index][9])) != (len(dict[index][9])-1)/6:
            print(f'{dict[index][0]} list - currency 異常')
            result = False

        # 檢查日期格式
        pattern = r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}'
        if (re.fullmatch(pattern, str(dict[index][10])) is None) or \
            (re.fullmatch(pattern, str(dict[index][11])) is None):
            print(f'{dict[index][0]} list - 日期異常')
            result = False
        
        # 檢查長度
        length = len(dict[index])
        while length > 12:
            for cell in range(length-1, 11, -1):
                del dict[index][cell]
            break
    return result

def check_dictionary(dict):
    result = True
    for index in dict:
        # game name
        if len(re.findall(r'"[a-z-]{2,5}":', dict[index][4])) != 7:
            print(f'{dict[index][4]} dict - game name 異常')
            result = False
        
        # game name 檢查 '
        if dict[index][4].find("'") > 0:
            dict[index][4] = dict[index][4].replace("'", "\\'")

        # 檢查日期格式
        pattern = r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}'
        if (re.fullmatch(pattern, str(dict[index][5])) is None) or \
            (re.fullmatch(pattern, str(dict[index][6])) is None):
            print(f'{dict[index][4]} dict - 日期異常')
            result = False
        
        # 檢查長度
        length = len(dict[index])
        while length > 7:
            for cell in range(length-1, 6, -1):
                del dict[index][cell]
            break
    return result

def check_gamemenu(dict):
    result = True
    for index in dict:
        # menu name
        if len(re.findall(r'"[a-z-]{2,5}":', dict[index][4])) != 7:
            print(f'{dict[index][4]} menu - menu name 異常')
            result = False

        # 檢查日期格式
        pattern = r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}'
        if (re.fullmatch(pattern, str(dict[index][6])) is None) or \
            (re.fullmatch(pattern, str(dict[index][7])) is None):
            print(f'{dict[index][0]} menu - 日期異常')
            result = False

        # 檢查長度
        length = len(dict[index])
        while length > 8:
            for cell in range(length-1, 7, -1):
                del dict[index][cell]
            break
    return result
