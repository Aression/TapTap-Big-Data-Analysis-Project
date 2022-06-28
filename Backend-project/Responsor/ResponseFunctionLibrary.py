def MakeResponseBase(bSucceed,Message):
    RespCode=404
    if bSucceed:
        RespCode=200
    else:
        RespCode=400

    Resp={'code': RespCode, 'message': Message, 'data': {}}
    return Resp