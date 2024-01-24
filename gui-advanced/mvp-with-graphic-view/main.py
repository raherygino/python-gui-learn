import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene,QGraphicsTextItem, QMenu, QGraphicsPixmapItem, QGraphicsItem, QScrollBar
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QContextMenuEvent,QFont
from PyQt5.QtCore import Qt

class DraggablePixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap,text,  parent=None):
        super(DraggablePixmapItem, self).__init__(pixmap, parent)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        # Create a QGraphicsTextItem and set its text
        self.text_item = QGraphicsTextItem(text, parent=self)
        self.text_item.setPos(63, 14)  # Adjust the position as needed
        self.text_item.setFont(QFont("Arial", 14))  # Customize the font as needed

    def contextMenuEvent(self, event):
        menu = QMenu()
        remove_action = menu.addAction("Remove Item")
        action = menu.exec_(event.screenPos())

        if action == remove_action:
            self.scene().removeItem(self)

class ZoomableGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(ZoomableGraphicsView, self).__init__(scene, parent)
        self.nScene = scene
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


    def mouseDoubleClickEvent(self, event):
        pixmap = QPixmap("resource/img/treasor.png")
        draggable_pixmap_item = DraggablePixmapItem(pixmap, "New")
        
        draggable_pixmap_item.setPos(event.x(), event.x())
        self.nScene.addItem(draggable_pixmap_item)


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
    draggable_pixmap_item = QGraphicsPixmapItem(pixmap)
    draggable_pixmap_item_1 = QGraphicsPixmapItem(pixmap_1)
    # Create a draggable pixmap item
    #draggable_pixmap_item_1 = DraggablePixmapItem(pixmap_1)
    scene.addItem(draggable_pixmap_item)
    scene.addItem(draggable_pixmap_item_1)

    # Create a zoomable graphics view
    view = ZoomableGraphicsView(scene)
    view.setWindowTitle("Zoomable QGraphicsView with Scrollbars Example")
    view.resize(400, 300)
    view.show()

    sys.exit(app.exec_())
