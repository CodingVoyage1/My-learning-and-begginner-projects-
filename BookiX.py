import sys
import requests
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, QMessageBox, QApplication, QVBoxLayout, QToolTip, QWidget
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5 import uic

class Worker(QThread):
    finished = pyqtSignal(list)

    def __init__(self, query):
        super().__init__()
        self.query = query

    def run(self):
        url = f"https://openlibrary.org/search.json?q={self.query}"
        response = requests.get(url)
        data = response.json()

        books = data["docs"][:9]

        image_urls = []

        for book in books:
            if 'cover_i' in book:
                cover_id = book['cover_i']
                image_url =  f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"
                title = book.get("title", "No Title")
                author = ", ".join(book.get("author_name", ["Unknown"]))
                year = book.get("first_publish_year", "N/A")
                image_urls.append({
                    "image": image_url,
                    "title": title,
                    "author": author,
                    "year": year,
                })

        self.finished.emit(image_urls)

class HoverLabel(QLabel):
    def __init__(self, pixmap, title, author, year):
        super().__init__()

        self.pixmap_original = pixmap
        self.setPixmap(pixmap.scaled(90, 130, Qt.KeepAspectRatio))
        self.setAlignment(Qt.AlignCenter)

        self.tooltip = QLabel(f"""
        <b>{title}</b>
        Author: {author}
        Year : {year}
          """)
        self.tooltip.setWindowFlags(Qt.ToolTip)
        self.tooltip.setStyleSheet("""
        QLabel{
        background-color : white;
        color : black;
        padding : 8px;
        border-radius : 10px ;
        font-size : 12px;
        }
        
        }
        """)
    def enterEvent(self, event):
        self.setPixmap(self.pixmap_original.scaled(90, 130, Qt.KeepAspectRatio))
        self.tooltip.move(QCursor.pos())
        self.tooltip.show()

    def leaveEvent(self, event):
        self.setPixmap(self.pixmap_original.scaled(90, 130, Qt.KeepAspectRatio))
        self.tooltip.hide()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("BookiXWindow.ui", self)
        if self.ui.frame.layout() is not None:
            self.layout = self.ui.frame.layout()
        else:
            self.layout = QGridLayout()
            self.ui.frame.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)
        self.ui.lineEdit.setPlaceholderText("Enter Book Title to search")
        self.ui.pushButton.clicked.connect(self.start_search)
        self.ui.pushButton.setStyleSheet("""
        QPushButton {
        border:2px solid black;
        border-radius: 10px;
        }
        QPushButton:hover {
        background-color: lightblue;
        }
        QPushButton:pressed {
        background-color: blue;
        color:white;
        }
        """)
        self.ui.label.setStyleSheet("""
        QLabel {
        font-size : 20px;
        color : #588157;
        font-weight : bold;
        }
        """)
        self.ui.label_2.setStyleSheet("""
        QLabel {
        font-size : 24px;
        color : #d4a373;
        background-color : #faedcd ;
        font-weight: bold;
        border : 2px solid black;
        border-radius : 20px ;
        margin-top : 20px;
        margin-bottom : 20px;
        font-family : monospace;
        }
        """)
        self.ui.lineEdit.setStyleSheet("""
        QLineEdit {
        border : 2px solid black;    
        }
        """)
        self.show()
    def start_search(self):
        query = self.ui.lineEdit.text()

        if not query:
            query = "how to type "

        self.worker = Worker(query)
        self.worker.finished.connect(self.display_books)
        self.worker.start()

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def display_books(self, books):
        self.clear_layout()

        row = 0
        col = 0

        for book in books:
            img_data = requests.get(book["image"]).content

            pixmap = QPixmap()
            pixmap.loadFromData(img_data)

            label = HoverLabel(
                pixmap,
                book["title"],
                book["author"],
                book["year"]
            )
            label.setFixedSize(100, 150)

            card = QWidget()
            card_layout = QVBoxLayout()

            card_layout.addWidget(label)
            card_layout.setContentsMargins(0, 0, 0, 0)

            card.setLayout(card_layout)
            card.setStyleSheet("""
            QWidget{
            background-color : white;
            border : 2px solid black;
            
            }
            QWidget : hover {
            background-color : lightblue;
            }
            
            """)
            self.layout.addWidget(label, row, col)

            col += 1
            if col == 3:
                col = 0
                row += 1





def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()