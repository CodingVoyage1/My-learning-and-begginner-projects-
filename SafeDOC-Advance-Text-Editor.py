from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sqlite3 as sql
import bcrypt

# --- Initialize userdata DB on startup ---
conn = sql.connect("userdata.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
""")
conn.commit()
conn.close()


class SinUp(QMainWindow):
    def __init__(self):
        super(SinUp, self).__init__()
        self.ui = uic.loadUi("SinUp_Page.ui", self)
        self.show()
        self.ui.lineEdit.setPlaceholderText("Username")
        self.ui.lineEdit_2.setPlaceholderText("Password")
        self.ui.lineEdit_3.setPlaceholderText("Confirm Password")
        self.ui.label.setStyleSheet("""
            QLabel {
                color: purple;
                font-size: 25px;
            }
        """)
        self.ui.pushButton.setStyleSheet("""
            QPushButton {
                color: white;
                background: purple;
            }
        """)
        self.ui.pushButton.clicked.connect(self.SignUp_btn)
        self.ui.pushButton_2.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                color: purple;
                text-decoration: underline;
            }
            QPushButton:hover {
                color: white;
            }
        """)
        self.ui.pushButton_2.clicked.connect(self.open_login)

    def SignUp_btn(self):
        username = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text()
        password2 = self.ui.lineEdit_3.text()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please fill in all fields")
            return

        if password != password2:
            QMessageBox.warning(self, "Error", "Passwords don't match")
            return

        conn = sql.connect("userdata.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM userdata WHERE username = ?", (username,))
        if cursor.fetchone():
            QMessageBox.warning(self, "Error", "Username already exists")
            conn.close()
            return

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute(
            "INSERT INTO userdata (username, password) VALUES (?, ?)",
            (username, hashed)
        )
        conn.commit()
        conn.close()
        QMessageBox.information(self, "Success", "Account Created!")

    def open_login(self):
        self.login_page = LoginPage()
        self.login_page.show()
        self.close()


class LoginPage(QMainWindow):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.ui = uic.loadUi("Login_Page.ui", self)
        self.show()
        self.ui.lineEdit.setPlaceholderText("Username")
        self.ui.lineEdit_2.setPlaceholderText("Password")
        self.ui.label.setStyleSheet("""
            QLabel {
                qproperty-alignment: AlignTop;
            }
        """)
        self.ui.label_2.setStyleSheet("""
            QLabel {
                color: purple;
                font-size: 20px;
            }
        """)

        pixmap = QPixmap("luffy.png")
        transform = QTransform().rotate(30)
        rotated = pixmap.transformed(transform)
        scaled = rotated.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.label_3.setPixmap(scaled)
        self.ui.label_3.show()

        pixmap2 = QPixmap("luffy.png")
        scaled2 = pixmap2.scaled(200, 200)
        self.ui.label_4.setPixmap(scaled2)

        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton.setStyleSheet("""
            QPushButton {
                color: white;
                background: purple;
            }
        """)

    def login(self):
        username = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter username and password")
            return

        conn = sql.connect("userdata.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM userdata WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result:
            user_id = result[0]
            stored_hash = result[2]

            # FIX 4: ensure stored_hash is bytes for bcrypt
            if isinstance(stored_hash, str):
                stored_hash = stored_hash.encode('utf-8')

            if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                self.text_editor = TextEditor(user_id)
                self.text_editor.show()
                self.close()
            else:
                QMessageBox.warning(self, "Error", "Invalid Username or Password")
        else:
            QMessageBox.warning(self, "Error", "Invalid Username or Password")


class TextEditor(QMainWindow):
    def __init__(self, user_id):
        super(TextEditor, self).__init__()
        self.user_id = user_id
        self.ui = uic.loadUi("SafeDoc.ui", self)

        self.ui.label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 25px;
            }
        """)
        self.ui.lineEdit.setPlaceholderText("Enter the name of file")

        # FIX 1: call ensure_notes_table() properly from __init__
        self.ensure_notes_table()

        # FIX 3: connect buttons AFTER table is guaranteed to exist
        self.ui.pushButton.clicked.connect(self.save)
        self.ui.pushButton_3.clicked.connect(self.load)
        self.ui.listWidget.itemClicked.connect(self.open_note)

        # Safe to call load_notes now — table exists
        self.load_notes()
        self.show()

    def ensure_notes_table(self):
        # FIX 1: removed the recursive self.ensure_notes_table() call that was inside here
        conn = sql.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                title TEXT,
                content TEXT
            )
        """)
        conn.commit()
        cursor.execute("PRAGMA table_info(notes)")
        cols = [r[1] for r in cursor.fetchall()]
        if 'user_id' not in cols:
            cursor.execute("ALTER TABLE notes ADD COLUMN user_id INTEGER")
            conn.commit()
        conn.close()

    def load(self):
        name = self.ui.lineEdit.text()
        conn = sql.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT content FROM notes WHERE title = ? AND user_id = ?",
            (name, self.user_id)
        )
        note = cursor.fetchone()
        conn.close()
        if note:
            self.ui.textEdit.setPlainText(note[0])
        else:
            QMessageBox.warning(self, "Error", "Note not found")

    def load_notes(self):
        conn = sql.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM notes WHERE user_id = ?", (self.user_id,))
        notes = cursor.fetchall()
        self.ui.listWidget.clear()
        for note in notes:
            self.ui.listWidget.addItem(note[0])
        conn.close()

    def open_note(self, item):
        title = item.text()
        conn = sql.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT content FROM notes WHERE title = ? AND user_id = ?",
            (title, self.user_id)
        )
        note = cursor.fetchone()
        conn.close()
        if note:
            self.ui.lineEdit.setText(title)
            self.ui.textEdit.setPlainText(note[0])

    def save(self):
        title = self.ui.lineEdit.text().strip()
        content = self.ui.textEdit.toPlainText()
        if not title:
            QMessageBox.warning(self, "Error", "Please enter a note title")
            return
        conn = sql.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM notes WHERE title = ? AND user_id = ?", (title, self.user_id))
        row = cursor.fetchone()
        if row:
            cursor.execute("UPDATE notes SET content = ? WHERE id = ?", (content, row[0]))
        else:
            cursor.execute(
                "INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)",
                (self.user_id, title, content)
            )
        conn.commit()
        conn.close()
        self.load_notes()
        QMessageBox.information(self, "Saved", "Note saved successfully")


# FIX 2: main2 can't work without a user_id — removed bad call
def main():
    app = QApplication([])
    window = SinUp()
    app.exec_()

if __name__ == '__main__':
    main()