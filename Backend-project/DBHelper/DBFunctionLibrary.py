#Development!
#ART0189

def GenericBase():
    return

def GenericCreate(TableName,TableStoreDir):
    #GenericCreate(NewTable,/root)
    '''
    try:
        TargetCommand=''
        TableNameStr=str(TableName)
        TableDirStr=str(TableStoreDir)

        TargetCommand=\
            'create database if not exists {}'.format(TableNameStr)\
            +' location \'{}\''.format(TableDirStr)+';'

        exec(TargetCommand)

        return True
    except BaseException:
        print('Invalid DataBaseModel/ParameterName/Value')

        return False
    '''

    print('Reject dynamic table operations!')
    return False


def GenericRemove(TableName):
    try:
        TargetCommand=''
        TableNameStr=str(TableName)
        TableDirStr=str(TableStoreDir)

        TargetCommand=\
            'create database if not exists {}'.format(TableNameStr)\
            +' location \'{}\''.format(TableDirStr)+';'

        exec(TargetCommand)

        return True
    except BaseException:
        print('Invalid DataBaseModel/ParameterName/Value')

        return False

def GenericUpdate():
    return

def GenericDelete():
    return