from tkinter import *

win = Tk()
win.geometry("1000x500")
win.option_add("*Font", "궁서 15")

ent = Entry(win)
ent.pack()


def lotto_p():
    import requests
    from bs4 import BeautifulSoup
    n = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(
        n)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", attrs={"class", "win_result"}).get_text()
    num_list = txt.split("\n")[7:13]
    bonus = txt.split("\n")[-4]
    btn.config(text="{}회차의 로또 당첨 번호는 {}이고 보너스 번호는 {}입니다.".format(
        n, num_list, bonus))


btn = Button(win)
btn.config(text="로또 당첨 번호 확인")
btn.config(command=lotto_p)
btn.pack()
win.mainloop()
