# 정렬 알고리즘

1. 선택 정렬

정렬이 되지 않은 숫자들 중에서 최소값을 선택하여 배열의 첫번째 요소와 교환하는 정렬 알고리즘
- 첫번째 자료를 두번째 자료부터 마지막 자료까지 차례대로 비교해서 가장 작은 값을 찾아 첫번째로 놓고, 두번째 자료를 세번째 자료부터 마지막 자료까지와 차례대로 비교해서 그 중 가장 작은 값을 찾아 두번째 위치에 놓는 과정을 반복하는 알고리즘
ex) 
![image](https://user-images.githubusercontent.com/47842737/224904686-4bd9c337-82ed-431c-8380-dcd57632520d.png)
(출처 : [알고리즘] 선택정렬(selection sort)이란, https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html)

2. 삽입 정렬

두번째 원소부터 시작해서 그 앞에 존재하는 원소들과 비교해서 삽입할 위치를 찾아 삽입하는 정렬 알고리즘
- 손 안의 원카드를 정렬하는 방식과 유사.
  - 새로운 카드를 기존의 정렬된 카드 사이에 올바른 자리에 삽입
  - 새로 삽입될 카드의 수만큼 반복하게 되면 전체 카드가 정렬됨.
- ex)![image](https://user-images.githubusercontent.com/47842737/224905479-c77b6e96-dc1f-4caf-a79b-be9e57aec7e6.png)
(출처 : [알고리즘] 삽입정렬(insertion sort)이란, https://gmlwjd9405.github.io/2018/05/06/algorithm-insertion-sort.html)

3. 버블 정렬

서로 인접한 두 원소를 비교하여 정렬하는 알고리즘
- 인접한 2개의 레코드를 비교하여 크기가 순서대로 되어 있지 않으면 서로 교환한다.
- 1회전을 수행하고 나면 가장 큰 자료가 맨 뒤로 이동하므로 2회전에서는 맨 끝에 있는 자료가 정렬에서 제외되고 2회전을 수행하고 나면 끝에서 두 번째 자료까지가 정렬에서 제외된다.
- ex)![image](https://user-images.githubusercontent.com/47842737/224905948-21ceb663-f3e1-4f20-a3ed-be7bebed1484.png)
(출처 : [알고리즘] 버블정렬(bubble sort)이란, https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html)


4. Merge Sort

주어진 배열을 크기가 1인 배열로 분할하고 합병하면서 정렬을 진행하는 분할정복 알고리즘
- 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 전략
- 주로 순환 호출을 이용하여 구현함.
  1. 리스트의 길이가 0 또는 1이면 이미 정렬된 것으로 본다.
  2. 그렇지 않으면 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분으로 나눈다.
  3. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
  4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.

- ex)
![image](https://user-images.githubusercontent.com/47842737/224906371-93d7fcb4-2252-422b-897d-9df761418cc6.png)
![image](https://user-images.githubusercontent.com/47842737/224906393-e91e3475-d974-4450-a053-bc00dc7db469.png)
(출처 : [알고리즘] 합병정렬(merge sort)이란, [https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html](https://gmlwjd9405.github.io/2018/05/08/algorithm-merge-sort.html))

5. Quick Sort

Merge sort와 다르게 리스트를 비균등하게 분할
Pivot을 설정하고 Pivot보다 큰 값, 작은 값으로 분할하여 정렬

- 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 전략
- 주로 순환 호출을 이용하여 구현함.
  1. 리스트 안에 있는 한 요소를 선택한다. 이렇게 고른 요소를 pivot이라고 함.
  2. pivot을 기준으로 pivot보다 작은 요소들은 모두 pivot의 왼쪽으로 옮겨지고 pivot보다 큰 요소들은 모두 pivot의 오른쪽으로 옮겨진다.
  3. pivot을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬한다.
  4. 부분 리스트들이 더 이상 분할이 불가능할 때까지 반복한다.

