import asyncio
from  httpx import AsyncClient



class NumberService:

    def check_prime(self, number: int) -> bool:
        if number < 2:
            return False
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
    
    def number_sum(self, number: int) -> int | None:
        if number < 0:
            return None
        result = sum(int(i) for i in str(number))
        return result

    def check_armstrong(self, number: int) -> bool:
        if number < 0:
            return False
        number_length = len(str(number))
        result = sum((int(i)**number_length) for i in str(number))
        return result == number
    
    def get_properties(self, number:int):
        properties = []
        if self.check_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 != 0 else "even")
        return properties

    async def get_fun_fact(self, number: int):
        url = f"http://numbersapi.com/{number}/math"
        async with AsyncClient() as client:
            result = await client.get(url)
            return result.text


# async def get_details():
#     service = NumberService()
#     result1 = await service.get_fun_fact(79)
#     result2 = service.number_sum(79)
#     result3 = service.get_properties(371)
#     print(result1)
#     print(result2)
#     print(result3)

# asyncio.run(get_details())