<h4>
<a target="_blank" href="https://eminent-pruner-9ad.notion.site/1ed29d1da6df464390c238ddd6adfb99">
   [배운것 & 트러블 슈팅]
</a>
</h4>

# 1. 소개

멜론 차트 정보를 원하는 형태로 DB에 저장하는 과정의 미니 프로젝트 입니다.
   
### 🎯목표


<h4>진행 과정</h4>

-   BeautifulSoup & Selenium 사용하여 멜론 홈페이지에 있는 TOP100 정보를 가져온다.<br>
-   vscode + python : 정제 후 원하는 데이터 추출<br>
-   vscode와 MySQL 연결 (Pymysql) 및 데이터 입력<br>

<br>

# 2. 결과🖼

#### CODE
<div align=center>
  <img width="750" alt="" src="https://user-images.githubusercontent.com/76522430/212733750-da7dfa7a-06f2-464b-a42d-ffec70f4cb11.png">
</div>

#### CREATE TABLE melon_top_100
<div align=center>
  <img width="750" alt="" src="https://user-images.githubusercontent.com/76522430/212734583-82c3a9f1-c116-4145-88d5-2a0e5f381e20.png">
</div>

#### SELECT * FROM mydatabase.melon_top_100;
<div align=center>
  <img width="750" alt="" src="https://user-images.githubusercontent.com/76522430/212734666-b2c6d534-08e2-4c6a-9116-c382134d19d9.png">
</div>

#### SELECT singer, sum(likes) FROM melon_top_100 GROUP BY singer LIMIT 10;
<div align=center>
  <img  alt="" src="https://user-images.githubusercontent.com/76522430/212734862-0dbc887f-6abe-45db-a515-21768926747d.png">
</div>

#### SELECT id, singer, likes FROM mydatabase.melon_top_100 ORDER BY likes DESC LIMIT 20;
<div align=center>
  <img alt="" src="https://user-images.githubusercontent.com/76522430/212734886-6c0ddcf7-7f7e-48fb-b733-f294678aa2f4.png">
</div>
