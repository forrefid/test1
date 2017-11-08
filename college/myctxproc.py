st=None
def set_st(s1):
    global st
    st=s1
def ctxproc(request):
    global st
    return {'student': st}
