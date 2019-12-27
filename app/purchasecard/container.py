from fastapi import Depends

from app.commons.context.app_context import AppContext, get_global_app_context
from app.commons.context.req_context import ReqContext, get_context_from_req
from app.purchasecard.core.card.processor import CardProcessor
from app.purchasecard.core.jit_funding.processor import CardPaymentMetadataProcessor
from app.purchasecard.core.user.processor import UserProcessor
from app.purchasecard.core.webhook.processor import WebhookProcessor
from app.purchasecard.core.transaction.processor import TransactionProcessor
from app.purchasecard.marqeta_external.marqeta_provider_client import (
    MarqetaProviderClient,
)
from structlog.stdlib import BoundLogger

from app.purchasecard.repository.delivery_funding import DeliveryFundingRepository
from app.purchasecard.repository.marqeta_card import MarqetaCardRepository
from app.purchasecard.repository.marqeta_transaction import MarqetaTransactionRepository
from app.purchasecard.repository.marqeta_card_ownership import (
    MarqetaCardOwnershipRepository,
)
from app.purchasecard.repository.marqeta_card_transition import (
    MarqetaCardTransitionRepository,
)
from app.commons.providers.dsj_client import DSJClient
from app.purchasecard.repository.store_mastercard_data import (
    StoreMastercardDataRepository,
)


class PurchaseCardContainer:

    app_context: AppContext
    req_context: ReqContext

    def __init__(
        self,
        req_context: ReqContext = Depends(get_context_from_req),
        app_context: AppContext = Depends(get_global_app_context),
    ):
        self.app_context = app_context
        self.req_context = req_context

    @property
    def marqeta_client(self) -> MarqetaProviderClient:
        return self.app_context.marqeta_client

    @property
    def logger(self) -> BoundLogger:
        return self.req_context.log

    @property
    def dsj_client(self) -> DSJClient:
        return self.app_context.dsj_client

    @property
    def user_processor(self) -> UserProcessor:
        return UserProcessor(marqeta_client=self.marqeta_client, logger=self.logger)

    @property
    def card_processor(self) -> CardProcessor:
        return CardProcessor(
            marqeta_client=self.marqeta_client,
            card_repo=self.marqeta_card_repository,
            card_ownership_repo=self.marqeta_card_ownership_repository,
            card_transition_repo=self.marqeta_card_transition_repository,
            logger=self.logger,
        )

    @property
    def webhook_processor(self) -> WebhookProcessor:
        return WebhookProcessor(
            logger=self.logger,
            repository=self.marqeta_transaction_repository,
            dsj_client=self.dsj_client,
        )

    @property
    def card_payment_metadata_processor(self) -> CardPaymentMetadataProcessor:
        return CardPaymentMetadataProcessor(
            store_mastercard_data_repo=self.store_mastercard_data_repository
        )

    @property
    def transaction_processor(self) -> TransactionProcessor:
        return TransactionProcessor(
            logger=self.logger,
            marqeta_repository=self.marqeta_transaction_repository,
            delivery_funding_repository=self.delivery_funding_repository,
        )

    @property
    def marqeta_transaction_repository(self) -> MarqetaTransactionRepository:
        return MarqetaTransactionRepository(
            database=self.app_context.purchasecard_maindb
        )

    @property
    def delivery_funding_repository(self) -> DeliveryFundingRepository:
        return DeliveryFundingRepository(database=self.app_context.purchasecard_maindb)

    @property
    def marqeta_card_repository(self) -> MarqetaCardRepository:
        return MarqetaCardRepository(database=self.app_context.purchasecard_maindb)

    @property
    def marqeta_card_ownership_repository(self) -> MarqetaCardOwnershipRepository:
        return MarqetaCardOwnershipRepository(
            database=self.app_context.purchasecard_maindb
        )

    @property
    def marqeta_card_transition_repository(self) -> MarqetaCardTransitionRepository:
        return MarqetaCardTransitionRepository(
            database=self.app_context.purchasecard_maindb
        )

    @property
    def store_mastercard_data_repository(self) -> StoreMastercardDataRepository:
        return StoreMastercardDataRepository(
            database=self.app_context.purchasecard_maindb
        )