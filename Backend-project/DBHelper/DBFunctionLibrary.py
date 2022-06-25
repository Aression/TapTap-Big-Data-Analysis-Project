#Development!
#ART0189

from AppStartDataBase import HiveDB,HiveConnection

def GenericInsert(TableName,Object):
    try:
        TargetCommand=''
        TableNameStr=str(TableName)
        ObjectStr=Object.Serialize()

        TargetCommand='insert into {} values{}'.format(TableNameStr,ObjectStr)

        HiveDB.execute(TargetCommand)
        HiveConnection.commit()

        return True
    except BaseException:
        print('Invalid TableName/Object')

        return False

def GenericUpdate(TableName,UpdateMethod,Condition):
    try:
        TargetCommand=''
        TableNameStr=str(TableName)
        UpdateMethodStr=str(UpdateMethod)
        ConditionStr=str(Condition)

        TargetCommand='update {} set {} where {}'.format(TableNameStr,UpdateMethodStr,ConditionStr)

        HiveDB.execute(TargetCommand)
        HiveConnection.commit()

        return True
    except BaseException:
        print('Invalid TableName/UpdateMethod/Condition')

        return False

def GenericDelete(TableName,Condition):
    #Use table name and condition to delete data.
    try:
        TargetCommand=''
        TableNameStr=str(TableName)
        ConditionStr=str(Condition)

        TargetCommand='delete from {} where {}'.format(TableNameStr,ConditionStr)

        HiveDB.execute(TargetCommand)
        HiveConnection.commit()

        return True
    except BaseException:
        print('Invalid TableName/Condition')

        return False

