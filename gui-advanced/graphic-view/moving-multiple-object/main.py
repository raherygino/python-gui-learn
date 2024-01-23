import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

class DraggablePixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap, parent=None):
        super(DraggablePixmapItem, self).__init__(pixmap, parent)
        self.setFlag(QGraphicsPixmapItem.ItemIsMovable)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("Pixmap item clicked")

class MyGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(MyGraphicsView, self).__init__(scene, parent)
        self.setRenderHint(QPainter.Antialiasing, True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = QGraphicsScene()

    # Load image files
    pixmap1 = QPixmap("resource/img/map.jpg")
    pixmap2 = QPixmap("resource/img/whatsapp.png")
    pixmap3 = QPixmap("resource/img/whatsapp.png")

    # Create multiple draggable pixmap items
    draggable_pixmap_item1 = DraggablePixmapItem(pixmap1)
    draggable_pixmap_item2 = DraggablePixmapItem(pixmap2)
    draggable_pixmap_item3 = DraggablePixmapItem(pixmap3)

    # Set positions for the items
    draggable_pixmap_item1.setPos(0, 0)
    draggable_pixmap_item2.setPos(100, 100)
    draggable_pixmap_item3.setPos(200, 200)

    # Add items to the scene
    scene.addItem(draggable_pixmap_item1)
    scene.addItem(draggable_pixmap_item2)
    scene.addItem(draggable_pixmap_item3)

    # Create a graphics view
    view = MyGraphicsView(scene)
    view.setWindowTitle("Multiple Draggable Pixmap Items Example")
    view.resize(400, 300)
    view.show()

    sys.exit(app.exec_())
