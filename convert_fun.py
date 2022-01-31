def convert_gamelist(f, dict):
    for row in dict: # 每行
        f.write("REPLACE INTO `GameList`.`GameList` (`GameID`, `GameCode`, `RealCode`, `GameName`, `MenuType`, `OpenGame`, `IsMobile`, `IsWeb`, `Image`, `Currency`, `NewTime`, `UPTime`) VALUES (") # 行首
        f.write(', '.join(map(lambda x:f'\'{x}\'', dict[row])) + ");\n")

def convert_dictionary(f, dict):
    for row in dict: # 每行
        f.write("REPLACE INTO `GameList`.`GameDictionary` (`DictionaryType`, `GameDictionary`, `GameCode`, `GameType`, `GameName`, `NewTime`, `UPTime`) VALUES (") # 行首
        f.write(', '.join(map(lambda x:f'\'{x}\'', dict[row])) + ");\n")

def convert_gamemenu(f, dict, top_user_id):
    for station in top_user_id:
        f.write(f'# {station}\n')
        for row in dict: # 每行
            dict[row][5] = top_user_id[station]
            f.write("REPLACE INTO `GameList`.`GameMenu` (`GameCode`, `MenuType`, `MenuOrder`, `MenuSubOrder`, `MenuName`, `TopUserID`, `NewTime`, `UPTime`) VALUES (") # 行首
            f.write(', '.join(map(lambda x:f'\'{x}\'', dict[row])) + ");\n")
        f.write("\n")
