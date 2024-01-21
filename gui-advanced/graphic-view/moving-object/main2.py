import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsEllipseItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter

class DraggableItem(QGraphicsEllipseItem):
    def __init__(self, parent=None):
        super(DraggableItem, self).__init__(parent)
        self.setRect(0, 0, 50, 50)
        self.setFlag(QGraphicsItem.ItemIsMovable)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("Item clicked")

class MyGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(MyGraphicsView, self).__init__(scene, parent)
        self.setRenderHint(QPainter.Antialiasing, True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = QGraphicsScene()
    
    # Create a draggable item
    draggable_item = DraggableItem()
    scene.addItem(draggable_item)
    
    # Create a graphics view
    view = MyGraphicsView(scene)
    view.setWindowTitle("Draggable Object Example")
    view.resize(400, 300)
    view.show()

    sys.exit(app.exec_())
