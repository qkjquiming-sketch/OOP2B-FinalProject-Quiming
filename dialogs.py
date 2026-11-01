from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
    QComboBox, QFrame, QFormLayout
)

from config import Statuses

class ConfirmOrderDialog(QDialog):
    
    def __init__(self, customer_name: str, phone: str, source: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirm Order Submission")
        self.setMinimumWidth(360)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        title = QLabel("Confirm Your Order")
        title.setObjectName("dialogTitle")
        layout.addWidget(title)
        
        card = QFrame()
        card.setProperty("class", "card")
        card_layout = QFormLayout(card)
        card_layout.setContentsMargins(14, 12, 14, 12)
        card_layout.setSpacing(8)
        
        card_layout.addRow(self._label("Customer Name:"), QLabel(customer_name))
        card_layout.addRow(self._label("Contact Number:"), QLabel(phone))
        card_layout.addRow(self._label("File Source:"), QLabel(source))
        
        layout.addWidget(card)
        
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(8)
        
        btn_cancel = QPushButton("Cancel")
        btn_cancel.setProperty("class", "secondaryButton")
        btn_cancel.clicked.connect(self.reject)
        
        btn_confirm = QPushButton("Confirm & Submit")
        btn_confirm.clicked.connect(self.accept)
        btn_confirm.setDefault(True)
        
        btn_layout.addWidget(btn_cancel)
        btn_layout.addWidget(btn_confirm)
        layout.addLayout(btn_layout)

    def _label(self, text: str) -> QLabel:
        lbl = QLabel(text)
        lbl.setProperty("class", "field-label")
        return lbl


class CustomAlertDialog(QDialog):
    
    def __init__(self, title_text: str, message_text: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title_text)
        self.setMinimumWidth(300)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        lbl_title = QLabel(title_text)
        lbl_title.setObjectName("dialogTitle")
        layout.addWidget(lbl_title)
        
        lbl_msg = QLabel(message_text)
        lbl_msg.setWordWrap(True)
        layout.addWidget(lbl_msg)
        
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.accept)
        btn_ok.setDefault(True)
        layout.addWidget(btn_ok)


class UpdateStatusDialog(QDialog):
    
    def __init__(self, order_id: str, current_status: str = "Pending", parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Update Order {order_id}")
        self.setMinimumWidth(320)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        title = QLabel(f"Order #{order_id}")
        title.setObjectName("dialogTitle")
        layout.addWidget(title)
        
        form = QFormLayout()
        lbl_status = QLabel("Set Status:")
        lbl_status.setProperty("class", "field-label")
        
        self.combo_status = QComboBox()
        self.combo_status.addItems(Statuses)
        self.combo_status.setCurrentText(current_status)
        
        form.addRow(lbl_status, self.combo_status)
        layout.addLayout(form)
        
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(8)
        
        btn_cancel = QPushButton("Cancel")
        btn_cancel.setProperty("class", "secondaryButton")
        btn_cancel.clicked.connect(self.reject)
        
        btn_save = QPushButton("Save")
        btn_save.clicked.connect(self.accept)
        btn_save.setDefault(True)
        
        btn_layout.addWidget(btn_cancel)
        btn_layout.addWidget(btn_save)
        layout.addLayout(btn_layout)

    def get_selected_status(self) -> str:
        return self.combo_status.currentText()