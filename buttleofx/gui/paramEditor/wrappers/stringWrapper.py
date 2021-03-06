# common
from .paramWrapper import ParamWrapper

from PySide import QtCore


class StringWrapper(ParamWrapper):
    """
        Gui class, which maps a ParamString.
    """

    def __init__(self, param):
        ParamWrapper.__init__(self, param)

    #################### getters ####################

    @QtCore.Slot(result=str)
    def getDefaultValue(self):
        self.setHasChanged(False)
        return self._param.getDefaultValue()

    def getValue(self):
        return self._param.getValue()

    def getStringType(self):
        return self._param.getStringType()

    def getHasChanged(self):
        return self._param.getHasChanged()

    #################### setters ####################

    def setValue(self, value):
        self._param.setValue(value)

    def setHasChanged(self, changed):
        self._param.setHasChanged(changed)

    @QtCore.Slot(str)
    def pushValue(self, value):
        self._param.pushValue(value)

    @QtCore.Signal
    def changed(self):
        pass
    
    ################################################## DATA EXPOSED TO QML ##################################################

    value = QtCore.Property(str, getValue, setValue, notify=changed)
    stringType = QtCore.Property(str, getStringType, constant=True)
    
    hasChanged = QtCore.Property(bool, getHasChanged, setHasChanged, notify=changed)
