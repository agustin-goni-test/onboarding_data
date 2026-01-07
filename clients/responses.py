from pydantic import BaseModel, Field
from typing import List, Optional

class AccountTypeDTO(BaseModel):
    code: int
    name: str

class BankCodeDTO(BaseModel):
    code: int
    name: str

class RegionCodeDTO(BaseModel):
    code: int
    name: str

class DistrictCodeDTO(BaseModel):
    code: int
    name: str
    codigo_region: Optional[int] = None


class AccountTypeResponse(BaseModel):
    account_types: List[AccountTypeDTO] = Field(..., alias="accountTypes")


class BankCodeResponse(BaseModel):
    bank_codes: List[BankCodeDTO] = Field(..., alias="banks")

class RegionCodeResponse(BaseModel):
    regions: List[RegionCodeDTO] = Field(..., alias="regions")

class DistrictCodeReponse(BaseModel):
    districts: List[DistrictCodeDTO] = Field(..., alias="districts")