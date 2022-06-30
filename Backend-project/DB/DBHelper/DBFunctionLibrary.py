#Development!
#ART0189

from AppStartDataBase import DB,DBS

#Other data-write operations are not recommandable.
#Most data-read operation need be implemented manually.

def GenericInsert(Object):
    try:
        DBS.add(Object)
        DBS.commit()

        return True
    except BaseException:
        print('Invalid TableName/Object')

        return False

def GenericUpdate(Class,Condition,VarName,NewValue):
    try:
        TargetCommand=''
        ClassStr=str(Class)
        ConditionStr=str(Condition)
        VarNameStr=str(VarName)
        NewValueStr=str(NewValue)
        
        TargetCommand='TpRs={}.query.filter_by({})'.format(ClassStr,ConditionStr) \
            +'\n'+'TpRs.{}={}'.format(VarNameStr,NewValueStr) \
            +'\n'+'DBS.merge(TpRs)'

        exec(TargetCommand)
        DBS.commit()

        return True
    except BaseException:
        print('Invalid TableName/UpdateMethod/Condition')

        return False
