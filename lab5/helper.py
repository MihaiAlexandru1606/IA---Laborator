class Base(object):

    def __init__(self, name_var, value_var):
        self.name_var = name_var
        self.value_var = value_var

    def get_name(self):
        return self.name_var

    def get_value(self):
        return self.value_var

    def __set_value(self, new_value):
        self.value_var = new_value


class Const(Base):

    def __init__(self, name_var, value_var):
        super().__init__(name_var, value_var)


class Variable(Base):

    def __init__(self, name_var):
        super().__init__(name_var, None)
        self.is_assigment = False