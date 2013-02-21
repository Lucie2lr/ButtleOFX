from PySide import QtCore
# core
from buttleofx.core.params import ParamInt, ParamInt2D, ParamInt3D, ParamString, ParamBoolean, ParamDouble, ParamDouble2D, ParamDouble3D, ParamChoice, ParamPushButton, ParamRGBA, ParamRGB, ParamGroup, ParamPage
# gui
from buttleofx.gui.paramEditor.wrappers import IntWrapper, Int2DWrapper, Int3DWrapper, StringWrapper, BooleanWrapper, DoubleWrapper, Double2DWrapper, Double3DWrapper, ChoiceWrapper, PushButtonWrapper, RGBAWrapper, RGBWrapper, GroupWrapper, PageWrapper
#quickmamba
from quickmamba.models import QObjectListModel


class ParamEditorWrapper(QtCore.QObject):
    def __init__(self, parent, paramList):
        super(ParamEditorWrapper, self).__init__(parent)
        # QtCore.QObject.__init__(self)
        self._paramElmts = QObjectListModel(self)

        self.mapTypeToWrapper = {
            ParamInt: IntWrapper,
            ParamInt2D: Int2DWrapper,
            ParamInt3D: Int3DWrapper,
            ParamString: StringWrapper,
            ParamDouble: DoubleWrapper,
            ParamDouble2D: Double2DWrapper,
            ParamDouble3D: Double3DWrapper,
            ParamBoolean: BooleanWrapper,
            ParamChoice: ChoiceWrapper,
            ParamPushButton: PushButtonWrapper,
            ParamRGBA: RGBAWrapper,
            ParamRGB: RGBWrapper,
            ParamGroup: GroupWrapper,
            ParamPage: PageWrapper,
        }

        paramListModel = [self.mapTypeToWrapper[paramElt.__class__](paramElt) for paramElt in paramList if not paramElt.isSecret()]
        #paramListModel = [self.mapTypeToWrapper[paramElt.__class__](paramElt) for paramElt in paramList]
        
        self._paramElmts.setObjectList(paramListModel)

        #print "EDITOR WRAPPER CREATED"

    def getParamElts(self):
        return self._paramElmts

    def setNodeForParam(self, node):
        self._paramElmts = node._params
        self.modelChanged.emit()

    modelChanged = QtCore.Signal()
    paramElmts = QtCore.Property("QVariant", getParamElts, notify=modelChanged)
