from pydantic import BaseModel, Field
from typing import List

class AccountTypeDTO(BaseModel):
    code: int
    name: str

class BankCodeDTO(BaseModel):
    code: int
    name: str   


class AccountTypeResponse(BaseModel):
    account_types: List[AccountTypeDTO] = Field(..., alias="accountTypes")


class BankCodeResponse(BaseModel):
    bank_codes: List[BankCodeDTO] = Field(..., alias="banks")