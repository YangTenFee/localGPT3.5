import openai
import tkinter as tk

openai.api_key = "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"

window = tk.Tk()
window.title('GPT3查询')
window.geometry('1200x800')

textExample = tk.Text(window, height=10)

textExample.pack()


def str_insert(str_origin, pos, str_add):
    count = 1
    str_out = ''
    while pos * count < str_origin.__len__():
        str_list = list(str_origin)    # 字符串转list
        str_list.insert(pos * count, str_add)  # 在指定位置插入字符串
        str_out = ''.join(str_list)    # 空字符连接
        count += 1
    return str_out


def getTextInput():
    result = textExample.get("1.0", "end")  # 获取文本输入框的内容
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": result}])
    content = response.choices[0].message.content
    print(content)
    if content.__len__() > 50:
        content = str_insert(content, 50, ' \n ')
    res = "{} \n\n {}".format(result, content)
    lb = tk.Label(window, text=res,  # 设置文本内容
                  width=1200,  # 设置label的宽度：30
                  height=5,  # 设置label的高度：10
                  justify='left',  # 设置文本对齐方式：左对齐
                  anchor='nw',  # 设置文本在label的方位：西北方位
                  font=('微软雅黑', 10),  # 设置字体：微软雅黑，字号：18
                  fg='white',  # 设置前景色：白色
                  bg='grey',  # 设置背景色：灰色
                  padx=20,  # 设置x方向内边距：20
                  pady=10)  # 设置y方向内边距：10
    lb.pack(fill='both', expand=True)
    textExample.delete('1.0', 'end')


# lb = tk.Label(window,  # 设置文本内容
#               width=1200,  # 设置label的宽度：30
#               height=5,  # 设置label的高度：10
#               justify='left',  # 设置文本对齐方式：左对齐
#               anchor='nw',  # 设置文本在label的方位：西北方位
#               font=('微软雅黑', 10),  # 设置字体：微软雅黑，字号：18
#               fg='white',  # 设置前景色：白色
#               bg='grey',  # 设置背景色：灰色
#               padx=20,  # 设置x方向内边距：20
#               pady=10)  # 设置y方向内边距：10
# lb.pack(fill='both', expand=True)
btnRead = tk.Button(window, height=1, width=10, text="提问", command=getTextInput)

btnRead.pack()

window.mainloop()
# while True:
#     prompt = input()
#     response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
#
#     # print(response)
#
