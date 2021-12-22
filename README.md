# Web_crawler
# 何為爬蟲
- 簡單的來說，就是把網站上面的資料複製下來，一筆資料很容易複製，那一千筆呢?更不要說是圖片，所以這就需要網路爬蟲來幫我們完成，這隻程式可以幫我們把網站資料爬(下載)下來，不管是圖片還是文字資料，這就是爬蟲，而我們這邊選擇以Python來撰寫，因為Python具有幾個特色:可讀性與簡潔性，如果是有寫過其他程式語言的就知道，這兩點在語言中很重要，對於一個工程師撰寫一個可讀性的程式碼超級難，而且用Python來實作爬蟲程式碼其實沒幾行很簡潔，非常適合初學者學習。

### 1.Python Request套件
- 對網路發動請求的套件，可實作對網頁做get、post等HTTP協定的行為，以後會有詳細的介紹。
    ```javascript
    pip install requests
    ```
### 2.Python Beautifulsoup4套件
- 借助網頁的結構特性來解析網頁的工具，只需要簡單的幾條指令就可以提取HTML標籤裡的元素。
    ```javascript
    pip install beautifulsoup4
    ```
##  Jupyter notebook
- CMD中輸入
    ```javascript
    jupyter notebook
    ```
- 於瀏覽器中自動開啟Jupyter notebook的頁面
    - 點選右上角的python3新建檔案
- 到這裡就是正式的進入到可撰寫Python code(Ctrl + Enter編譯)
- 學習輸出Hello world!

##  實作演練
- Python套件import進來
    ```javascript
    import requests
    from bs4 import BeautifulSoup 
    ```
- 將網頁GET
    ```javascript
    import requests
    from bs4 import BeautifulSoup

    r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將此頁面的HTML GET下來
    print(r.text) #印出HTML
    ```
- 將抓下來的資料用Beautifulsoup4轉為HTML的parse
    ```javascript
        import requests
        from bs4 import BeautifulSoup

        r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將網頁資料GET下來
        soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
        sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
    ```




