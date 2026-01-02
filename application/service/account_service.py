from application.domain.entities import AccountInfo, CommerceAccount
from application.data.unit_of_work import UnitOfWork

class AccountService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def create_account(
            self,
            rut_titular: str,
            nombre_titular: str,
            banco: int,
            tipo_cuenta: int
    ):
        account_info = AccountInfo(
            rut_titular=rut_titular,
            nombre_titular=nombre_titular,
            banco=banco,
            tipo_cuenta=tipo_cuenta
        )

        with self.uow as uow:
            uow.accounts.add(account_info)


class CommerceAccountService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def create_commerce_account_relation(
            self,
            comercio_id: int,
            cuenta_id: int,
            principal: bool
    ) -> None:
        commerce_account = CommerceAccount(
            comercio_id=comercio_id,
            cuenta_id=cuenta_id,
            principal=principal
        )

        with self.uow as uow:
            uow.commerce_accounts.add(commerce_account)

    
    def create_account_for_commerce(
            self,
            rut_comercio: str,
            rut_titular: str,
            nombre_titular: str,
            banco: int,
            tipo_cuenta: int,
            principal: bool = True
    ) -> None:
        with self.uow as uow:
        
            # 1. Create account info
            account_info = AccountInfo(
                rut_titular=rut_titular,
                nombre_titular=nombre_titular,
                banco=banco,
                tipo_cuenta=tipo_cuenta
            )
            account_id = uow.accounts.add(account_info)

            # 2. Get comercio_id by RUT
            commerce_id = uow.commerce_registrations.get_id_by_rut(rut_comercio)

            # 3. Create commerce account link
            commerce_account = CommerceAccount(
                comercio_id=commerce_id,
                cuenta_id=account_id,
                principal=principal
            )

            uow.commerce_accounts.add(commerce_account)