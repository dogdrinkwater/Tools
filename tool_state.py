from clearCache import clearRedis
from modify_Sql import updateSQL


def tool():
    userId = input("输入用户id：")
    updateSQL.modifyState(userId)
    clearRedis.clear_user(userId)

if __name__ == '__main__':
    tool()