

class user(object):
    def __init__(self,id=None,name='',face=None,birthday='',current_level=None,regtime='',sex='',sign=None):
        '''
        user 对象
        '''
        self.id=id
        self.name=name
        self.face=face
        self.birthday=birthday
        self.current_level=current_level
        self.regtime=regtime
        self.sex=sex
        self.sign=sign

    def __eq__(self,other):
        return self.id==other.id
    
    def __hash__(self):
        return hash(id(self.id))
