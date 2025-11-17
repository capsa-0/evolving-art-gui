from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QFrame
from PySide6.QtCore import Signal, Qt

from .common import StyledScreen, build_outline_button_style


class MenuScreen(StyledScreen):
    """Main menu screen styled after a modern video game."""
                                
    populations_requested = Signal()              
    quit_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

                             
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 200, 50, 50)
        main_layout.setSpacing(20)

                                                        

        title = QLabel("EVOLVING ART")
        title.setStyleSheet(f"""
            font-size: 120px; 
            font-weight: 900; 
            color: {self.palette.accent}; 
            margin-bottom: 10px;
            background-color: transparent;
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        subtitle = QLabel("Interactive Genetic Art Studio")
        subtitle.setStyleSheet(f"""
            font-size: 20px; 
            color: {self.palette.primary_text}; 
            margin-bottom: 30px;
            font-weight: 300; 
            background-color: transparent;
        """)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

                                                             
        content_frame = QFrame(self)
        content_frame.setMaximumWidth(600)
        content_frame.setMinimumHeight(310)                     
        content_frame.setStyleSheet("background-color: transparent; border: none;")
        
                                                 
        layout = QVBoxLayout(content_frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)
                                                                 

        description = QLabel("A tool to evolve artwork through guided selection.")
        description.setStyleSheet(f"""
            font-size: 16px; 
            color: {self.palette.tertiary_text}; 
            margin-bottom: 40px;
        """)
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description.setWordWrap(True)

                                                      
        button_style = build_outline_button_style(
            self.palette,
            font_size="20px",
            font_weight="700",
            padding="10px",
            radius=8,
        )

                         
        
        self.btn_manage = QPushButton("POPULATIONS")
        self.btn_manage.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_manage.setStyleSheet(button_style)
        
        self.btn_quit = QPushButton("QUIT")
        self.btn_quit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_quit.setStyleSheet(button_style)

                                     

                                
        main_layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(subtitle, alignment=Qt.AlignmentFlag.AlignCenter)

                                      
        layout.addWidget(description)
        layout.addWidget(self.btn_manage)
        layout.addSpacing(10)
        layout.addWidget(self.btn_quit)

                                    
        main_layout.addWidget(content_frame, alignment=Qt.AlignmentFlag.AlignCenter)

                                       
        main_layout.addStretch(1)

        self.btn_manage.clicked.connect(self.populations_requested.emit)
        self.btn_quit.clicked.connect(self.quit_requested.emit)