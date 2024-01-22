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

    # Load an image file
    pixmap = QPixmap("resource/img/whatsapp.png")  # Replace "image.jpg" with the path to your image file

    # Create a draggable pixmap item
    draggable_pixmap_item = DraggablePixmapItem(pixmap)
    scene.addItem(draggable_pixmap_item)

    # Create a graphics view
    view = MyGraphicsView(scene)
    view.setWindowTitle("Draggable Pixmap Item Example")
    view.resize(400, 300)
    view.show()

    sys.exit(app.exec_())
