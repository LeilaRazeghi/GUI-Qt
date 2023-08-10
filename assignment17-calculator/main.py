import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def zero():
   main_window.txtbox.setText(main_window.txtbox.text()+"0")

def one():
   main_window.txtbox.setText(main_window.txtbox.text()+"1")

def two():
   main_window.txtbox.setText(main_window.txtbox.text()+"2")

def three():
   main_window.txtbox.setText(main_window.txtbox.text()+"3")

def four():
   main_window.txtbox.setText(main_window.txtbox.text()+"4")

def five():
   main_window.txtbox.setText(main_window.txtbox.text()+"5")

def six():
   main_window.txtbox.setText(main_window.txtbox.text()+"6")

def seven():
   main_window.txtbox.setText(main_window.txtbox.text()+"7")

def eight():
   main_window.txtbox.setText(main_window.txtbox.text()+"8")

def nine():
   main_window.txtbox.setText(main_window.txtbox.text()+"9")

def AC():
   main_window.txtbox.setText("")

def percentage():
   main_window.txtbox.setText(str(float(main_window.txtbox.text())/100))

def point():
   main_window.txtbox.setText(main_window.txtbox.text()+".")

def reverse():
   main_window.txtbox.setText(str(1/float(main_window.txtbox.text()+"+/-")))

def sin():
   main_window.txtbox.setText(str(math.sin(float(main_window.txtbox.text()))))

def cos():
   main_window.txtbox.setText(str(math.cos(float(main_window.txtbox.text()))))

def tan():
   main_window.txtbox.setText(str(math.tan(float(main_window.txtbox.text()))))

def cot():
   main_window.txtbox.setText(str(1/math.tan((float(main_window.txtbox.text())))))

def log():
   main_window.txtbox.setText(str(math.log(float(main_window.txtbox.text()))))

def sqrt():
   main_window.txtbox.setText(str(math.sqrt(float(main_window.txtbox.text()))))

def sub():
   global a
   global oprt
   oprt="-"
   a = float(main_window.txtbox.text())
   main_window.txtbox.setText("")

def sum():
   global a
   global oprt
   oprt="+"
   a = float(main_window.txtbox.text())
   main_window.txtbox.setText("")

def mul():
   global a
   global oprt
   oprt= "*"
   a = float(main_window.txtbox.text())
   main_window.txtbox.setText("")

def div():
   global a
   global oprt
   oprt ="/"
   a = float(main_window.txtbox.text())
   main_window.txtbox.setText("")

def result():
   b =float(main_window.txtbox.text())
   if oprt =="-":
      c = a - b 
      main_window.txtbox.setText(str(c))
   elif oprt =="+":
      c = a + b
      main_window.txtbox.setText(str(c))
   elif oprt =="*":
      c = a * b
      main_window.txtbox.setText(str(c))
   elif oprt =="/":
      if b!=0:
         c = a /b
      else:
         c= "error! Division by zero!"
      main_window.txtbox.setText(str(c))

app = QApplication([])

loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()

main_window.btn_zero.clicked.connect(zero)
main_window.btn_one.clicked.connect(one)
main_window.btn_two.clicked.connect(two)
main_window.btn_three.clicked.connect(three)
main_window.btn_four.clicked.connect(four)
main_window.btn_five.clicked.connect(five)
main_window.btn_six.clicked.connect(six)
main_window.btn_seven.clicked.connect(seven)
main_window.btn_eight.clicked.connect(eight)
main_window.btn_nine.clicked.connect(nine)
main_window.btn_ac.clicked.connect(AC)
main_window.btn_point.clicked.connect(point)
main_window.btn_percentage.clicked.connect(percentage)
main_window.btn_reverse.clicked.connect(reverse)

main_window.btn_sub.clicked.connect(sub)
main_window.btn_sum.clicked.connect(sum)
main_window.btn_mul.clicked.connect(mul)
main_window.btn_div.clicked.connect(div)

main_window.btn_sin.clicked.connect(sin)
main_window.btn_cos.clicked.connect(cos)
main_window.btn_tan.clicked.connect(tan)
main_window.btn_cot.clicked.connect(cot)
main_window.btn_log.clicked.connect(log)
main_window.btn_sqrt.clicked.connect(sqrt)

main_window.btn_equal.clicked.connect(result)

app.exec()