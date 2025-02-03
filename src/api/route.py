from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from .service import NumberService


number_router = APIRouter()
number_service = NumberService()

@number_router.get("/classify-number", status_code=status.HTTP_200_OK)
async def get_classification(number: str) -> dict:
    try:
        number = int(number)
        property = set()
        armstrong = number_service.check_armstrong(number=int(number))
        if armstrong:
            property.add("armstrong")
        property.add(number_service.check_even_or_odd(number=int(number)))

        return JSONResponse(
            content={
                "number": number,
                "is_prime": number_service.check_prime(int(number)),
                "is_perfect": number_service.check_perfect(int(number)),
                "properties": list(property),
                "digit_sum": number_service.number_sum(int(number)),
                "fun_fact": number_service.get_fun_fact(int(number))
            },
            status_code=status.HTTP_200_OK
        )
    except ValueError:
        return JSONResponse(
            content={
                "number": str(number),
                "error": True
            },
            status_code=status.HTTP_400_BAD_REQUEST
        )

