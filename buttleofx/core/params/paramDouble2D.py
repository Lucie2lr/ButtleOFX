class ParamDouble2D(object):

    def __init__(self, defaultValue1, defaultValue2, minimum, maximum, text="default"):
        self.paramType = "ParamDouble2D"
        self.defaultValue1 = defaultValue1
        self.defaultValue2 = defaultValue2
        self.minimum = minimum
        self.maximum = maximum
        self.text = text
