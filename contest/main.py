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
    """Решение для Задачи 3"""
    pass

# В данной функции определите самостоятельно, что она принимает, а что возвращает
def lazy():
    """Решение для Задачи 4"""
    pass
