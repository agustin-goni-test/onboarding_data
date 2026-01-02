from pydantic import BaseModel
from typing import List

class AccountTypeDTO(BaseModel):
    code: int
    name: str


class AccountTypeResponse(BaseModel):
    accountTypes: List[AccountTypeDTO]