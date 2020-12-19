import sys
from pathlib import Path
from typing import Optional
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, QTimer
import random, time
from pygame import mixer, error
from mutagen.mp3 import MP3
import style

button_size = QSize(48, 48)

music_list = []
mixer.init()

muted: bool = False  # ミュートフラグ

count: int = 0  # 曲の経過時間
song_length = 0  # 曲の長さ
index_: int = 0  # music_listのindex


class Player(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super(Player, self).__init__(parent=parent)
        self.setWindowTitle("Music Player")
        self.setGeometry(450, 150, 600, 500)
        self.ui()
        self.show()

    def ui(self):
        """Create window UI"""
        self.widgets()
        self.connect_()
        self.layouts()

    def widgets(self) -> None:
        """Creating widgets"""
        ####################Progress bar#######################
        self.progressbar = QProgressBar()
        self.progressbar.setTextVisible(False)
        # self.progressbar.setStyleSheet(style.progress_bar_style())

        ########################Labels#########################
        self.song_timer_label = QLabel("00:00")
        self.song_lenth_label = QLabel("/ 00:00")

        ####################Buttons###########################
        self.add_button = QToolButton()
        self.add_button.setIcon(QIcon(r"icons/add.png"))
        self.add_button.setIconSize(button_size)
        self.add_button.setToolTip("Add a Song")  # ボタンにカーソルを持って行った時に表示される文字を設定

        self.shuffle_button = QToolButton()
        self.shuffle_button.setIcon(QIcon(r"icons/shuffle.png"))
        self.shuffle_button.setIconSize(button_size)
        self.shuffle_button.setToolTip("Shuffle The list")

        self.previous_button = QToolButton()
        self.previous_button.setIcon(QIcon(r"icons/previous.png"))
        self.previous_button.setIconSize(button_size)
        self.previous_button.setToolTip("Play Precious")

        self.play_button = QToolButton()
        self.play_button.setIcon(QIcon(r"icons/play.png"))
        self.play_button.setIconSize(QSize(64, 64))
        self.play_button.setToolTip("Play")

        self.next_button = QToolButton()
        self.next_button.setIcon(QIcon(r"icons/next.png"))
        self.next_button.setIconSize(button_size)
        self.next_button.setToolTip("Play Next")

        self.mute_button = QToolButton()
        self.mute_button.setIcon(QIcon(r"icons/mute.png"))
        self.mute_button.setIconSize(QSize(24, 24))
        self.mute_button.setToolTip("Mute")

        ##################Vokume Slider##############################
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setToolTip("Volume")
        self.volume_slider.setValue(70)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        mixer.music.set_volume(0.7)  # 音量、0~1の範囲

        ###############################Play list####################
        self.play_list = QListWidget()
        self.play_list.setStyleSheet(style.play_list_style())

        ############################Timer###########################
        self.timer = QTimer()
        self.timer.setInterval(1000)

    def connect_(self) -> None:
        """Connecting function"""
        self.add_button.clicked.connect(self.add_sound)
        self.shuffle_button.clicked.connect(self.shuffle_play_list)
        self.play_button.clicked.connect(self.play_sound)
        self.play_list.doubleClicked.connect(self.play_sound)
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.mute_button.clicked.connect(self.mute_sound)
        self.timer.timeout.connect(self.update_progressbar)
        self.previous_button.clicked.connect(self.play_previous)
        self.next_button.clicked.connect(self.play_next)

    def layouts(self) -> None:
        """
        Creating layouts

        Other Parameters
        ----------
        main_layout: QVBoxLayout
            画面のメインレイアウト
        top_main_layout: QVBoxLayout
            top_groupboxのメインレイアウト
        top_groupbox: QGroupBox
            画面上部のグループボックス
        top_layout: QHBoxLayout
            グループボックスの上部レイアウト、プログレスバー設置
        middle_layout: QHBoxLayout
            グループボックスの下部レイアウト、ボタン設置
        button_layout: QVBoxLayout
            多分再生曲リスト格納レイアウト
        """
        ############################Createing layouts###########################
        self.main_layout = QVBoxLayout()
        self.top_main_layout = QVBoxLayout()
        self.top_groupbox = QGroupBox("Music Player", self)
        self.top_groupbox.setStyleSheet(style.group_box_style())
        self.top_layout = QHBoxLayout()
        self.middle_layout = QHBoxLayout()
        self.button_layout = QVBoxLayout()

        ###################################Adding Widgets#########################
        #########################Top layout widgets###############################
        self.top_layout.addWidget(self.progressbar)
        self.top_layout.addWidget(self.song_timer_label)
        self.top_layout.addWidget(self.song_lenth_label)

        #########################Middle layout widgets############################
        self.middle_layout.addStretch()
        self.middle_layout.addWidget(self.add_button)
        self.middle_layout.addWidget(self.shuffle_button)
        self.middle_layout.addWidget(self.play_button)
        self.middle_layout.addWidget(self.previous_button)
        self.middle_layout.addWidget(self.next_button)
        self.middle_layout.addWidget(self.volume_slider)
        self.middle_layout.addWidget(self.mute_button)
        self.middle_layout.addStretch()

        ##############################Button layout widget#########################
        self.button_layout.addWidget(self.play_list)

        self.top_main_layout.addLayout(self.top_layout)
        self.top_main_layout.addLayout(self.middle_layout)
        self.top_groupbox.setLayout(self.top_main_layout)
        self.main_layout.addWidget(self.top_groupbox, 25)
        self.main_layout.addLayout(self.button_layout, 75)
        self.setLayout(self.main_layout)

    def add_sound(self) -> None:
        filepath, _ = QFileDialog.getOpenFileName(self, "Add Sound", "", "Sound Files (*.mp3 *.ogg *.wav)")
        filename = Path(filepath).name
        if filename != "":
            self.play_list.addItem(filename)
            music_list.append(filepath)

    def shuffle_play_list(self) -> None:
        random.shuffle(music_list)
        self.play_list.clear()
        for song in music_list:
            self.play_list.addItem(Path(song).name)

    def play_sound(self) -> None:
        global count, index_

        count = 0
        index_ = self.play_list.currentRow()
        self.playing()

    def play_previous(self):
        global count, index_

        count = 0
        items = self.play_list.count()
        if index_ == 0:
            index_ = items

        index_ -= 1
        self.playing()

    def play_next(self):
        global count, index_

        count = 0
        items = self.play_list.count()
        index_ += 1

        if index_ == items:
            index_ = 0

        self.playing()

    def playing(self) -> None:
        """play music"""
        global song_length
        try:
            play_music = music_list[index_]
            mixer.music.load(play_music)
            sound = MP3(play_music)
            song_length = sound.info.length
            song_length = round(song_length)
            self.progressbar.setValue(0)
            self.progressbar.setMaximum(song_length)

            self.song_lenth_label.setText(time.strftime("/ %M:%S", time.gmtime(song_length)))

            mixer.music.play()
            self.timer.start()
        except IndexError:
            QMessageBox.warning(self, "Warning", "The music list does not exist.")
        except error:
            QMessageBox.critical(self, "Error", f"{sys.exc_info()[1]}")

    def set_volume(self) -> None:
        """Change volume"""
        self.volume = self.volume_slider.value()
        mixer.music.set_volume(self.volume / 100)

    def mute_sound(self) -> None:
        """Set mute or unmute"""
        global muted
        if muted is False:
            mixer.music.set_volume(0.0)
            muted = True
            self.mute_button.setIcon(QIcon(r"icons/unmuted.png"))
            self.mute_button.setToolTip("UnMute")
            self.volume_slider.setValue(0)
        else:
            mixer.music.set_volume(0.7)
            muted = False
            self.mute_button.setIcon(QIcon(r"icons/mute.png"))
            self.mute_button.setToolTip("Mute")
            self.volume_slider.setValue(70)

    def update_progressbar(self) -> None:
        global count, song_length
        count += 1
        self.progressbar.setValue(count)
        min_, sec_ = divmod(count, 60)
        self.song_timer_label.setText(time.strftime("%M:%S", time.gmtime(count)))
        if count == song_length:
            self.timer.stop()


def main():
    app = QApplication(sys.argv)
    window = Player(parent=None)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
