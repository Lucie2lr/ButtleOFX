import QtQuick 1.1

Item {
    implicitWidth: 100
    implicitHeight: 30

    Row {
        spacing: 10
        Rectangle {
            width: 100
            height: 1
            color: "grey"
            y: 8
        }

        /*Title of the param*/
        Text {
            id: paramGroupTitle
            text: object.label
            color: "white"
            font.pointSize: 11
        }

        Rectangle {
            width: 100
            height: 1
            color: "grey"
            y: 8
        }
    }
}
