 # class Class_a():
# def aa(self):
                # print("我手机是多少说的都是")
           # def bb(self):
           #     print("大帅哥")
     #   def div(a,b):
         #   try:
           #     c = a/b
          #  except:
            #    print("初设不能为零")
       #         return
         #   return c

   # print(div(10,0))

def ww():
    try:
        open("wen","r")
       # g = open("wen_jian.txt","w")
       # g.read()
       # g.close()


    except FileNotFoundError :
        print("没有找到文件")

    except ValueError :
        print("我也不知道是啥子错误")
ww()

