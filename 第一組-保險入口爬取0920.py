# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:17:31 2021

@author: wgkev
"""
# # In[]
# #!pip install requests
# #!pip install BeautifulSoup4

# import requests
# from bs4 import BeautifulSoup

# url = 'https://finfo.tw/compares/%E5%AE%9A%E6%9C%9F%E5%A3%BD%E9%9A%AA'
# html = requests.get(url)

# print(html.text)

# print(html.encoding)
# # utf-8


# sp = BeautifulSoup(html.text, 'html.parser')
# type(sp)
# # bs4.BeautifulSoup

# sp

# In[]

from selenium.webdriver import Chrome
import time
# 設定exe檔位置
driver = Chrome("C:\\Users\\wgkev\\OneDrive\\桌面\\產業新尖兵-AI大數據企業實務班\\FB與IG爬蟲20210914課程\\chromedriver.exe")

# 設定要開啟的網頁
driver.get("https://finfo.tw/compares/%E5%AE%9A%E6%9C%9F%E5%A3%BD%E9%9A%AA")

# 等待時間
time.sleep(2)

# In[]
# 初始畫面
driver.find_element_by_xpath('//*[@id="call-to-sign-up-popup"]/div/div/div/div/a[1]').click()

# # 註冊
# driver.find_element_by_name("user[email]").send_keys('wgkevinwong@gmail.com')
# driver.find_element_by_name("user[password]").send_keys('12345678')
# driver.find_element_by_xpath('//*[@id="new_user"]/input[2]').click()

# 已註冊
driver.find_element_by_xpath('//*[@id="registration_new"]/div/div[4]/a').click()

# 登入
driver.find_element_by_name("user[email]").send_keys('wgkevinwong@gmail.com')
driver.find_element_by_name("user[password]").send_keys('12345678')
driver.find_element_by_xpath('//*[@id="new_user"]/input[6]').click()


# In[]
# 年紀輸入
userAge = int(input('請輸入使用者年紀: '))
driver.find_element_by_name("recommendation_form[age]").clear()
driver.find_element_by_name("recommendation_form[age]").send_keys(userAge)

# 性別
userGender = eval(input('請輸入1或2來表示性別，1為男生、2為女生: '))
if userGender == 1:
    print('性別: 男')
    driver.find_element_by_xpath('//*[@id="new_recommendation_form"]/div[2]/div[1]/label').click()
elif userGender == 2:
    print('性別: 女')
    driver.find_element_by_xpath('//*[@id="new_recommendation_form"]/div[2]/div[2]/label').click()
else:
    print('輸入錯誤')
    

# 抓取網址
from bs4 import BeautifulSoup
import requests

# 現學現賣BeautifulSoup再次登場
sp = BeautifulSoup(driver.page_source, 'html.parser')

# In[]
# 1.保險合約
contract = sp.find_all('span', class_="main")
contract_list = []

for i in range(len(contract)):
    contract_list.append(contract[i].text)
    print(contract[i].text)

# In[]
# 2.合約超連結
hyperlink = sp.find_all("a", {"target":"_blank"})
hyperlink_list = []

for i in range(len(hyperlink)):
    hyperlink_list.append(hyperlink[i]["href"])

i = 0
while len(hyperlink_list) > len(contract):
    if str(hyperlink_list[i]).startswith('/') == False:
        hyperlink_list.pop(i)
    else: i += 1
for i in range (len(hyperlink_list)):
    print('https://finfo.tw', end ='')
    print(hyperlink_list[i], end = '\n\n')
    
# In[]  
# 3.月排名
rank = sp.find_all('div', class_="rank")
rank_list = []

for i in range(len(rank)):
    rank_list.append(rank[i].text)
    print(rank[i].text)
rank_list.pop(0)

# In[]
# 4.年期
duration = sp.find_all('div', class_="term")
duration_list = []

for i in range(len(duration)):
    duration_list.append(duration[i].text)
    print(duration[i].text)
duration_list.pop(0)

# In[]
# 5-1.保額/計畫(推薦)
plan = sp.find_all('div', class_="hottest-combination-div")
plan_list = []

for i in range(len(plan)):
    plan_list.append(plan[i].text)
    print(plan[i].text)
plan_list.pop(0)

# In[]
# 5-2. 年繳金額
price = sp.find_all('div', class_="price")  # 顯示不出金額數字
price_list = []
for i in range(len(price)):
    price_list.append(price[i].text)
    print(price[i].text)
price_list.pop(0)

# Find element by Xpath
# list_of_price = []
# for i in range(len(price)):
#     factor = driver.find_element_by_xpath('//*[@id="compare"]/section/div[3]/div[i]/div[1]/div[6]/div')
#     list_of_price.append(factor)

# In[]
# 6.保險介紹
intro = sp.find_all('div', class_="features block")
intro_list = []

for i in range(len(intro)):
    intro_list.append(intro[i].text)
    print(intro[i].text)
intro_list.pop(0)

# In[]
# 7.保障項目
benefits = sp.find_all('span', class_="benefit")
temp = []
count = 0
for i in range(len(benefits)):
    temp.append(benefits[i].text)
    print(benefits[i].text)
    
step = 4
benefits_list = [temp[i : i+step] for i in range(0, len(temp), step)]
print(benefits_list)

# In[]
# 8.其他資訊
moreInfo = sp.find_all('div', class_="comments block")
moreInfo_list = []

for i in range(len(moreInfo)):
    moreInfo_list.append(moreInfo[i].text)
    print(moreInfo[1].text)
moreInfo_list.pop(0)

# In[]
# 查詢目錄
for i in range(len(contract)):
    print('%d'%(i+1), end = '. ')
    print(contract[i].text)


num = eval(input('請輸入編號1~%d來查詢對應之保險合約內容: ' %len(contract)))
while (num < 1) or (num > len(contract)) or type(num) != int:
    print('輸入錯誤, 請重新輸入')
    num = eval(input('請輸入編號1~%d來查詢對應之保險合約內容: ' %len(contract)))

print()
print('#查詢結果: ', end = '\n\n')

print('1.合約名稱: ', contract_list[num-1], end = '\n\n')

print('2.商品連結: https://finfo.tw', hyperlink_list[num-1],sep = '', end = '\n\n')

print('3.月排行:', rank_list[num-1], end = '\n\n')

print('4.保險年期: ', duration_list[num-1], end = '\n\n')

print('5.保險計畫: ', plan_list[num-1], end = '\n\n')
print('年繳保費: ', price[num].text, end = '\n')

print('6.保險介紹: ', intro_list[num-1], end = '\n\n')

print('7.保障項目: ', end = '\n\n')
print('一般身故 -> 身故保險金 : ', benefits_list[num-1][0], end = '\n\n')
print('失能 -> 完全失能 : ', benefits_list[num-1][1], end = '\n\n')
print('意外身故 -> 意外身故保險金 : ', benefits_list[num-1][2], end = '\n\n')
print('意外失能 -> 意外完全失能 : ', benefits_list[num-1][3], end = '\n\n')

print('8.其他資訊: ', moreInfo_list[num-1], end = '\n\n')


