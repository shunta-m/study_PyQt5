def group_box_style() -> str:
    return """
        QGroupBox {
        background-color:#fcc334;
        font:15pt Times;
        color:white;
        border:2px solid gray;
        border-radius:15px;
        }
    """


def progress_bar_style() -> str:
    return """
        QProgressBar {
        border:1px solid #bbb;
        background:white;
        height:10px;
        border-radius:6px;
        }
    """


def play_list_style() -> str:
    return """
        QListWidget {
        background-color:#fff;
        border-radius:10px;
        border:2px solid blue;
        }
    """


def tool_button_style() -> str:
    return """
        QToolButton {
        background-color:#90ee90;
        }
        """
