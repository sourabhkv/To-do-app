from PySide6.QtWidgets import QApplication, QMainWindow,QWidget,QVBoxLayout, QPushButton , QListWidget,QLineEdit
import sys
class ToDoApp(QMainWindow):
    def __init__(self):
        super(ToDoApp, self).__init__()

        self.tasks = []
        self.completed_tasks = []

        self.setWindowTitle("To-Do App developed by sourabhkv")
        self.setGeometry(800,400, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter task description")

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)

        self.task_list = QListWidget(self)
        self.task_list.itemDoubleClicked.connect(self.complete_task)
        self.edit_button = QPushButton("Edit Task")
        self.edit_button.clicked.connect(self.edit_task)
        self.remove_button = QPushButton("Remove Task")
        self.remove_button.clicked.connect(self.remove_task)

        self.layout.addWidget(self.task_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.remove_button)

        self.central_widget.setLayout(self.layout)

    def add_task(self):
        description = self.task_input.text()
        if description:
            self.tasks.append(description)
            self.task_list.addItem(description)
            self.task_input.clear()

    def complete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_description = selected_item.text()
            self.completed_tasks.append(task_description)
            self.tasks.remove(task_description)
            self.update_task_list()

    def edit_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_description = selected_item.text()
            new_description, ok = QLineEdit.getText(self, "Edit Task", "Edit task description:", text=task_description)
            if ok and new_description:
                self.tasks.remove(task_description)
                self.tasks.append(new_description)
                self.update_task_list()

    def remove_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_description = selected_item.text()
            self.tasks.remove(task_description)
            self.update_task_list()

    def update_task_list(self):
        self.task_list.clear()
        for task in self.tasks:
            self.task_list.addItem(task)

def main():
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
