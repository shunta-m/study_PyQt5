# study_PyQt5

## LineEdit

### プレースホルダーを設定する

```python
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Please Enter your name")
```

<img src="/Users/shiyun/Documents/python_project/study_PyQt5/images/プレースホルダ.png" alt="プレースホルダ" style="zoom:50%;" />

### 入力文字を隠す

```python
        self.passTextBox = QLineEdit(self)
        self.passTextBox.setEchoMode(QLineEdit.Password)
```

<img src="/Users/shiyun/Documents/python_project/study_PyQt5/images/パスワード.png" alt="パスワード" style="zoom:50%;" />

## RadioButton

#### グループ化

```python
				self.male = QRadioButton("Male", self)
        self.female = QRadioButton("Female", self)
    
  			self.group = QButtonGroup()
        self.group.addButton(self.male, 0)
        self.group.addButton(self.female, 1)
```

