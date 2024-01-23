import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsItem, QScrollBar
from PyQt5.QtGui import QPixmap, QPainter, QBrush
from PyQt5.QtCore import Qt

class DraggablePixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap, parent=None):
        super(DraggablePixmapItem, self).__init__(pixmap, parent)
        self.setFlag(QGraphicsItem.ItemIsMovable)

class ZoomableGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(ZoomableGraphicsView, self).__init__(scene, parent)
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setRenderHint(QPainter.SmoothPixmapTransform, True)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        # Load a background image
        background_pixmap = QPixmap("resource/img/background.jpg")  # Replace with the path to your background image
        self.setBackgroundBrush(QBrush(background_pixmap))

        # Enable scrollbars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.zoom_factor = 1.0

    def wheelEvent(self, event):
        factor = 1.2
        if event.angleDelta().y() < 0:
            factor = 1.0 / factor

        self.zoom_factor *= factor
        self.scale(factor, factor)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = QGraphicsScene()

    # Load an image file
    pixmap = QPixmap("resource/img/land.png")
    # Load an image file
    pixmap_1 = QPixmap("resource/img/land2.png")

    # Create a draggable pixmap item
    draggable_pixmap_item = DraggablePixmapItem(pixmap)
    # Create a draggable pixmap item
    draggable_pixmap_item_1 = DraggablePixmapItem(pixmap_1)
    scene.addItem(draggable_pixmap_item)
    scene.addItem(draggable_pixmap_item_1)

    # Create a zoomable graphics view
    view = ZoomableGraphicsView(scene)
    view.setWindowTitle("Zoomable QGraphicsView with Scrollbars Example")
    view.resize(400, 300)
    view.show()

    sys.exit(app.exec_())
