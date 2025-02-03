from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from typing import Optional

from .service import NumberService


number_router = APIRouter()
number_service = NumberService()

@number_router.get("/classify-number", status_code=status.HTTP_200_OK)
async def get_classification(number: Optional[str]=None) -> dict:
    if number is None:
        return JSONResponse(
        content={
            "message": "Query not provided",
            "error": True
        },
        status_code=status.HTTP_400_BAD_REQUEST
    )

    try:
        number: int = int(number)
        return JSONResponse(
            content={
                "number": number,
                "is_prime": number_service.check_prime(number),
                "is_perfect": number_service.check_perfect(number),
                "properties": number_service.get_properties(number),
                "digit_sum": number_service.number_sum(number),
                "fun_fact": await number_service.get_fun_fact(number)
            },
            status_code=status.HTTP_200_OK
        )
    except ValueError:
        return JSONResponse(
            content={
                "number": number,
                "error": True
            },
            status_code=status.HTTP_400_BAD_REQUEST
        )