# Calculator
PyQt5를 이용한 계산기 구현

## 실행 결과
<img src="https://user-images.githubusercontent.com/68969252/104424392-a9758600-55c2-11eb-93db-e6a3f13095bb.png" width=250>

## 기능
* 계산기 UI
  * 숫자 키패드 버튼
  * [*],[/],[+],[-] : 사칙연산 기호 버튼
  * [.] : 소수점 버튼 
  * [(],[)] 키 : 괄호 버튼
  * [=] 키 : eval() 함수를 이용해서 계산 결과 출력
  * [C] 키 : 계산 창의 내용 모두 지움
  * 상수 입력 버튼
    |상수 버튼 내용|연결된 상수|
    |:---:|:---:|
    |PI|3.141592|
    |빛의 이동 속도 (m/s)|3E+8|
    |소리의 이동 속도 (m/s)|340|
    |태양과의 평균 거리 (km)|1.5E+8|
    
  * 함수 계산 버튼
  
    |함수 버튼 내용|연결된 함수|
    |:---:|:---:|
    |factorial (!)|factorial|
    |-> binary'|decToBin|
    |binary -> dec|binToDec|
    |-> roman|decToRoman|
    |roman -> dec|romanToDec|
   
