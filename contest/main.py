def array_diff(a: list, b: list) -> list:
    """Решение для Задачи 1
    Реализуйте функцию, которая вычисляет разницу между двумя списками. 
    Функция должна удалять все вхождения элементов из первого списка (a), присутствующие во втором списке (b). 
    Порядок элементов в первом списке должен сохраняться в результате.
    Пример:
    array_diff([1, 2], [1]) # [2]
    array_diff([1, 2, 2, 2, 3], [2]) # [1, 3]
    """
    
    for x in reversed(a):
        if x in b:
            a.remove(x)

    return(a)

def sum_pairs(nums: list, sum: int) -> list:
    """Решение для Задачи 2
    Дан список целых чисел и одно значение суммы. 
    Верните первые два значения (!анализируйте слева направо!) в порядке их появления, сумма которых образует эту сумму.
    Если существует две или более пар с требуемой суммой, то решением является пара, второй элемент которой имеет наименьший индекс.
    """
    
    """ <- there's a list with 10 million items in the tests so rest in peace this solution
    result = None
    lowestSecondIndex = None
    
    for i1,a in enumerate(nums):
        for i2,b in enumerate(nums):
            if i2 > i1:
                if a + b == sum:
                    if not lowestSecondIndex or lowestSecondIndex > i2:
                        result = [a,b]
                        lowestSecondIndex = i2
                        
    return(result)
    """
    
    alreadySeen = set()
    
    for a in nums:
        b = sum - a
        
        if b in alreadySeen:
            return [b, a]
        
        alreadySeen.add(a)
    
    return None

def remove_duplicate_ids(obj: dict) -> dict:
    """Решение для Задачи 3
    Дан словарь, в которой каждый ключ представляет собой строковое число, а каждое соответствующее значение — массив символов.
    Создайте функцию, которая возвращает таблицу с одинаковыми ключами, но каждый символ должен встречаться в массивах значений только один раз
    Примечание:
    Если два ключа содержат один и тот же символ, их следует сравнивать численно, и больший ключ сохранит этот символ. 
    Именно поэтому в приведенном выше примере массив под ключом "2" содержит "A" и "B", поскольку 2 > 1.
    Если в одном и том же массиве обнаружены повторяющиеся символы, следует сохранить первое их появление."""

    finalDict = {}
    
    for key in obj:
        finalDict[key] = []
    
    allUsedLetters = []
    
    itemsList = []
    for key in obj:
        itemsList.append([key, obj[key]])
    
    for i in range(len(itemsList)):
        for j in range(i + 1, len(itemsList)):
            if int(itemsList[i][0]) < int(itemsList[j][0]):
                temp = itemsList[i]
                itemsList[i] = itemsList[j]
                itemsList[j] = temp
    
    for item in itemsList:
        key = item[0]
        letters = item[1]
        
        goodLetters = []
        for letter in letters:
            alreadyUsed = False
            for used in allUsedLetters:
                if letter == used:
                    alreadyUsed = True
                    break
            
            if alreadyUsed == False:
                goodLetters.append(letter)
                allUsedLetters.append(letter)
        
        finalDict[key] = goodLetters
    
    result = {}
    for key in obj:
        result[key] = finalDict[key]
    
    return result

# В данной функции определите самостоятельно, что она принимает, а что возвращает
def lazy(n: int): # -> func:
    """Решение для Задачи 4
    Требуется написать функцию-декоратор @lazy(n), где n — частота «нормальных» запусков. 
    
    Например, если n == 4, то после первого успешного запуска следующие три вызова этой функции ничего не будут делать, 
    а затем 5-й запуск снова будет выполняться нормально. 
    
    (Первый запуск всегда должен быть успешным, за исключением n == -1, который всегда является ленивым). 
    
    Однако, если n — отрицательное число, 
    то частота инвертируется (т.е. @lazy(-4) означает, что только каждый 4-й запуск является ленивым, остальные — нормальными). 
    
    Если n == 1, то функция всегда должна быть нормальной, 
    а если n == -1, то функция всегда должна быть ленивой. 
    
    n == 0 никогда не будет проверяться. 
    
    Примечание: Когда ленивая функция «ничего не делает», это означает, что она немедленно возвращает None. 
    Ни одна строка «обычной» функции не должна выполняться вообще."""
    pass
    
    def decorator(func):
        callCounter = 0
        
        def wrapper(*arguments, **extraArguments):
            nonlocal callCounter
            callCounter = callCounter + 1
            
            if n == 1:
                return func(*arguments, **extraArguments)
            
            if n == -1:
                return None
            
            if n > 0:
                if (callCounter - 1) % n == 0:
                    return func(*arguments, **extraArguments)
                else:
                    return None
            
            if n < 0:
                positiveN = n * -1
                if callCounter % positiveN == 0:
                    return None
                else:
                    return func(*arguments, **extraArguments)
        
        return wrapper
    
    return decorator
