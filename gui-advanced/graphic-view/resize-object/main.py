import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsItem
from PyQt5.QtGui import QPixmap, QPainter, QBrush
from PyQt5.QtCore import Qt, QPointF

class ResizablePixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap, parent=None):
        super(ResizablePixmapItem, self).__init__(pixmap, parent)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setAcceptHoverEvents(True)

        # Variables for resizing
        self.resizing = False
        self.resize_start_pos = QPointF()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.resizing = True
            self.resize_start_pos = event.scenePos()

    def mouseMoveEvent(self, event):
        if self.resizing:
            new_width = abs(event.scenePos().x() - self.resize_start_pos.x())
            new_height = abs(event.scenePos().y() - self.resize_start_pos.y())
        # Set the initial size of the item
            self.setPixmap(pixmap.scaled(new_width, new_height))

            #self.setRect(0, 0, new_width, new_height)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.resizing = False

class CustomScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(CustomScene, self).__init__(parent)

        # Load a background image
        background_pixmap = QPixmap("resource/img/map.jpg")  # Replace with the path to your background image
        self.setBackgroundBrush(QBrush(background_pixmap))

class ZoomableGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(ZoomableGraphicsView, self).__init__(scene, parent)
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setRenderHint(QPainter.SmoothPixmapTransform, True)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = CustomScene()

    # Load an image file
    pixmap = QPixmap("resource/img/whatsapp.png")

    # Create a resizable pixmap item
    resizable_pixmap_item = ResizablePixmapItem(pixmap)
    scene.addItem(resizable_pixmap_item)

    # Create a zoomable graphics view
    view = ZoomableGraphicsView(scene)
    view.setWindowTitle("Resizable QGraphicsPixmapItem Example")
    view.resize(400, 300)
    view.show()

    sys.exit(app.exec_())
