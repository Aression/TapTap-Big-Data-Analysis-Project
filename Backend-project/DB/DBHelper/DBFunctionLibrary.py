#Development!
#ART0189

from AppStartDataBase import DB,DBS
from sqlalchemy.exc import IntegrityError

global TotalGame
TotalGame=0
global InsertSuccess
InsertSuccess=0
global InsertFailed
InsertFailed=0
global InsertRepeat
InsertRepeat=0

#Other data-write operations are not recommandable.
#Most data-read operation need be implemented manually.

def DebugInsert():
    print("Total insert: {}, Success: {}, Failed: {}, Repeative: {}" \
        .format(TotalGame,InsertSuccess,InsertFailed,InsertRepeat))

def GenericInsert(Object):
    global TotalGame
    global InsertSuccess
    global InsertFailed
    global InsertRepeat

    TotalGame+=1
    try:
        DBS.add(Object)
        DBS.commit()
        InsertSuccess+=1
        return True
    except IntegrityError:
        InsertRepeat+=1
        DBS.rollback()
        return True
    
        print('Invalid or Repeative Object')
        InsertFailed+=1

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
        print('Invalid Class/Condition/VarName/NewValue')

        return False
