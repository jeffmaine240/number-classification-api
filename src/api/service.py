import requests

class NumberService:

    def check_prime(self, number: int) -> bool:
        if number < 2:
            return False
        print(int(number**0.5 + 1))
        print(number**0.5 + 1)
        for i in range(2, int(number**0.5 + 1)):
            if number % i == 0:
                return False
        return True
    
    def check_perfect(self, number: int) -> bool:
        if number < 2:
            return False

        divisors_sum = 1  
        for i in range(2, int(number**0.5 + 1)):
            if number % i == 0:
                divisors_sum += i
                if i != number // i:  
                    divisors_sum += number // i

        return divisors_sum == number
    
    def number_sum(self, number: int) -> int:
        sum = 0
        for i in str(number):
            sum += int(i)
        return sum

    def check_even_or_odd(self, number: int):
        if number % 2 == 0:
            return "even"
        return "odd"

    def check_armstrong(self, number: int) -> bool:
        number_length = len(str(number))
        sum = 0
        for i in str(number):
            sum += (int(i)**number_length)
        return sum == number

    def get_fun_fact(self, number: int):
        url = f"http://numbersapi.com/{number}"
        result = requests.get(url=url)
        return result.text





service = NumberService()
result =  service.get_fun_fact(7777777)
print(result)