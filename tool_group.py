from clearCache import clearRedis
from Tools.modify_Sql import updateSQL


def tool():
    userId = input("输入用户id：")
    updateSQL.modifyGroup(userId)
    clearRedis.clear_usergroup(userId)



if __name__ == '__main__':
    tool()