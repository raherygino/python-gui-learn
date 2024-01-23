import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsItem, QMenu
from PyQt5.QtGui import QPixmap, QPainter, QBrush
from PyQt5.QtCore import Qt

class DraggablePixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap, text, z_value, parent=None):
        super(DraggablePixmapItem, self).__init__(pixmap, parent)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.text = text
        self.setZValue(z_value)  # Set the initial z-value

    def contextMenuEvent(self, event):
        menu = QMenu()
        bring_to_front_action = menu.addAction("Bring to Front")
        bring_to_back_action = menu.addAction("Send to Back")
        action = menu.exec_(event.screenPos())

        if action == bring_to_front_action:
            self.setZValue(self.zValue() + 1)  # Increase the z-value to bring to front
        elif action == bring_to_back_action:
            self.setZValue(self.zValue() - 1)  # Decrease the z-value to send to back

class CustomScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(CustomScene, self).__init__(parent)

        # Load a background image
        background_pixmap = QPixmap("resource/img/world-map.gif")  # Replace with the path to your background image
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

    # Load image files
    pixmap1 = QPixmap("resource/img/treasor.png")
    pixmap2 = QPixmap("resource/img/treasor.png")
    pixmap3 = QPixmap("resource/img/treasor.png")

    # Create multiple draggable pixmap items with associated text and z-values
    draggable_pixmap_item1 = DraggablePixmapItem(pixmap1, "Item 1", 1)
    draggable_pixmap_item2 = DraggablePixmapItem(pixmap2, "Item 2", 2)
    draggable_pixmap_item3 = DraggablePixmapItem(pixmap3, "Item 3", 3)

    # Set positions for the items
    draggable_pixmap_item1.setPos(0, 0)
    draggable_pixmap_item2.setPos(100, 100)
    draggable_pixmap_item3.setPos(200, 200)

    # Add items to the scene
    scene.addItem(draggable_pixmap_item1)
    scene.addItem(draggable_pixmap_item2)
    scene.addItem(draggable_pixmap_item3)

    # Create a zoomable graphics view
    view = ZoomableGraphicsView(scene)
    view.setWindowTitle("QGraphicsScene with Background Image, Text, and Z-Order Example")
    view.resize(400, 300)
    view.show()

    sys.exit(app.exec_())
