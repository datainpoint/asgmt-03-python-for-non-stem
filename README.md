# asgmt-03-python-for-non-stem
Assignment 03: Python for Non-STEM.

## 練習題指引

- 將練習題的 GitHub Repository 下載到自己的電腦，解壓縮後以 VS Code 開啟專案資料夾。
- 先閱讀 `README.md`，再將答案寫在 `answers.py`
- 練習題共分為三種：
  - 是非題：預設答案 `answer_01 = None`，請以布林型別宣告答案，若覺得是非題的敘述**不正確**，就宣告 `answer_01 = False`，若覺得是非題的敘述**正確**則宣告 `answer_01 = True`
  - 單選題：預設答案 `answer_02 = None`，請以整數型別宣告答案，若覺得單選題的第一個選項**正確**宣告為 `answer_02 = 1`，若覺得單選題的第二個選項**正確**則宣告 `answer_02 = 2`，若覺得單選題的第三個選項**正確**則宣告 `answer_02 = 3`，若覺得單選題的第四個選項**正確**則宣告 `answer_02 = 4`
  - 程式題：以函數/類別宣告答案，函數/類別名稱下的長字串（docstring）會描述測試資料與預期輸出，能夠讓我們充分暸解預期輸入以及預期輸出之間的對應關係，寫作完畢後要記得輸出答案的變數 `return your_answer_variable`
- 如果練習題需要載入檔案，檔案會與練習題存放在同個資料夾中，這時可以運用工作目錄的相對路徑直接指定檔案名稱載入。
- 寫作完成後將 `answers.py` 存檔，再執行專案資料夾中的 `test_runner.py` 進行測試，再依照測試結果修正答案或截圖測試結果繳交作業。

## 01.（是非題）布林 `False` 可以轉換為整數 `0`，布林 `True` 可以轉換為整數 `1`。

```python
answer_01 = None
```

## 02.（單選題）當函數沒有寫作 `return` 的時候，該函數的輸出（回傳值）其實是哪個資料類別？

1. `Null`
2. `Nan`
3. `False`
4. `NoneType`

```python
answer_02 = None
```

## 03.（程式題）定義函數 `answer_03()` 能夠將以公里（km）為單位的距離轉換為以英里（mile）為單位的距離。

$$
1 \; \text{km} = 0.62137 \; \text{mile}
$$

```python
def answer_03(km: float) -> float:
    """
    >>> answer_03(1.61)
    1.0004057
    >>> answer_03(21.095)
    13.10780015
    >>> answer_03(42.195)
    26.21870715
    """
```

## 04.（程式題）定義函數 `answer_04()` 能夠將以英里（mile）為單位的距離轉換為以公里（km）為單位的距離。

$$
1 \; \text{km} = 0.62137 \; \text{mile}
$$

```python
def answer_04(mile: float) -> float:
    """
    >>> answer_04(1.0)
    1.6093470878864444
    >>> answer_04(13.1)
    21.082446851312422
    >>> answer_04(26.2)
    42.164893702624845
    """
```

## 05.（程式題）定義函數 `answer_05()` 能夠將以華氏為單位的溫度轉換為以攝氏為單位的溫度。

$$
\text{Celsius}(^{\circ} \text{C}) = (\text{Fahrenheit}(^{\circ} \text{F}) - 32) \times \frac{5}{9}
$$

```python
def answer_05(fahrenheit: int) -> float:
    """
    >>> answer_05(212)
    100.0
    >>> answer_05(32)
    0.0
    """
```

## 06.（程式題）定義函數 `answer_06()` 能夠將以攝氏為單位的溫度轉換為以華氏為單位的溫度。

$$
\text{Celsius}(^{\circ} \text{C}) = (\text{Fahrenheit}(^{\circ} \text{F}) - 32) \times \frac{5}{9}
$$

```python
def answer_06(celsius: int) -> float:
    """
    >>> answer_06(100)
    212.0
    >>> answer_06(0)
    32.0
    """
```

## 07.（程式題）定義函數 `answer_07()` 能夠對輸入的人名說「哈囉」。

```python
def answer_07(name: str) -> str:
    """
    >>> answer_07("world")
    'Hello, world!'
    >>> answer_07("Python")
    'Hello, Python!'
    >>> answer_07("Skywalker")
    'Hello, Skywalker!'
    """
```

## 08.（程式題）定義函數 `answer_08()` 能夠將整數以千分位逗號格式的文字顯示。

```python
def answer_08(x: int) -> str:
    """
    >>> answer_08(1000)
    '1,000'
    >>> answer_08(10000)
    '10,000'
    >>> answer_08(100000)
    '100,000'
    """
```

## 09.（程式題）定義函數 `answer_09()` 能夠判斷輸入的整數是否為偶數。

```python
def answer_09(x: int) -> bool:
    """
    >>> answer_09(0)
    True
    >>> answer_09(1)
    False
    >>> answer_09(2)
    True
    >>> answer_09(3)
    False
    """
```

## 10.（程式題）定義函數 `answer_10()` 能夠判斷除數 `x` 是否能為被除數 `y` 整除。

```python
def answer_10(x: int, y: int) -> bool:
    """
    >>> answer_10(5, 1)
    True
    >>> answer_10(5, 2)
    False
    >>> answer_10(5, 3)
    False
    >>> answer_10(5, 4)
    False
    >>> answer_10(5, 5)
    True
    """
```