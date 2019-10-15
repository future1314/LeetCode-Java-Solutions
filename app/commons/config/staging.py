import os

from app.commons.config.app_config import (
    AppConfig,
    ApiStatsDConfig,
    DBConfig,
    SentryConfig,
)
from app.commons.config.secrets import Secret


def create_app_config() -> AppConfig:
    """
    Create AppConfig for staging environment
    """
    return AppConfig(
        ENVIRONMENT="staging",
        DEBUG=False,
        REMOTE_SECRET_ENABLED=True,
        STATSD_SERVER="staging-statsd-proxy.doorcrawl-int.com",
        API_STATSD_CONFIG=ApiStatsDConfig(
            TAGS={"service_name": "payment-service", "cluster": "staging"}
        ),
        IDENTITY_SERVICE_HTTP_ENDPOINT="https://identity-service.doorcrawl.com",
        IDENTITY_SERVICE_GRPC_ENDPOINT="identity.doorcrawl-int.com:50051",
        PAYIN_SERVICE_ID=1631011374003906560,
        PAYOUT_SERVICE_ID=1631011374003906560,
        LEDGER_SERVICE_ID=1631011374003906560,
        PURCHASECARD_SERVICE_ID=1631011374003906560,
        TEST_SECRET=Secret(name="hello_world_secret"),
        PAYIN_MAINDB_MASTER_URL=Secret(name="payin_maindb_url"),
        PAYIN_MAINDB_REPLICA_URL=Secret(name="payin_maindb_replica_url"),
        PAYIN_PAYMENTDB_MASTER_URL=Secret(name="payin_paymentdb_url"),
        PAYIN_PAYMENTDB_REPLICA_URL=Secret(name="payin_paymentdb_url"),
        PAYOUT_MAINDB_MASTER_URL=Secret(name="payout_maindb_url"),
        PAYOUT_MAINDB_REPLICA_URL=Secret(name="payout_maindb_replica_url"),
        PAYOUT_BANKDB_MASTER_URL=Secret(name="payout_bankdb_url"),
        PAYOUT_BANKDB_REPLICA_URL=Secret(name="payout_bankdb_replica_url"),
        LEDGER_MAINDB_MASTER_URL=Secret(name="ledger_maindb_url"),
        LEDGER_MAINDB_REPLICA_URL=Secret(name="ledger_maindb_url"),
        LEDGER_PAYMENTDB_MASTER_URL=Secret(name="ledger_paymentdb_url"),
        LEDGER_PAYMENTDB_REPLICA_URL=Secret(name="ledger_paymentdb_url"),
        DEFAULT_DB_CONFIG=DBConfig(
            replica_pool_max_size=5, master_pool_max_size=5, debug=False
        ),
        AVAILABLE_MAINDB_REPLICAS=[],
        STRIPE_US_SECRET_KEY=Secret(
            name="stripe_us_secret_key", value="sk_test_NH2ez5KKOx5qPWcNcFhjdr1R"
        ),
        STRIPE_US_PUBLIC_KEY=Secret(
            name="stripe_us_public_key", value="pk_test_VCKL0VKIMMPzuUB8ZbuXdKkA"
        ),
        STRIPE_CA_SECRET_KEY=Secret(
            name="stripe_ca_secret_key", value="sk_test_DjN82k53PAi4mKVlkeOXUsGh"
        ),
        STRIPE_CA_PUBLIC_KEY=Secret(
            name="stripe_ca_public_key", value="pk_test_6BIBosD7fUMQKx5ehGg5L6pz"
        ),
        STRIPE_AU_SECRET_KEY=Secret(
            name="stripe_au_secret_key",
            value="sk_test_kwb7Pky1rEyIYbWhIBnHbEG500GIVp7eeO",
        ),
        STRIPE_AU_PUBLIC_KEY=Secret(
            name="stripe_au_public_key",
            value="pk_test_dJ998ZEOQNHLDCAQG37EKbId00c9TVHvH7",
        ),
        DSJ_API_BASE_URL="https://api.doorcrawl.com",
        DSJ_API_USER_EMAIL=Secret(name="dsj_api_user_email"),
        DSJ_API_USER_PASSWORD=Secret(name="dsj_api_user_password"),
        DSJ_API_JWT_TOKEN_TTL=1800,
        SENTRY_CONFIG=SentryConfig(
            dsn=Secret(name="sentry_dsn"),
            environment="staging",
            release=f"payment-service@release-{os.getenv('RELEASE_TAG')}",
        ),
        MARQETA_BASE_URL="https://doordash-api.marqeta.com/v3/",
        MARQETA_USERNAME=Secret(
            name="marqeta_username", value="doordash_sandbox_api_consumer"
        ),
        MARQETA_PASSWORD=Secret(name="marqeta_password", value="sTZqUU5SAvvNErqY"),
        MARQETA_JIT_USERNAME=Secret(name="marqeta_jit_username", value=""),
        MARQETA_JIT_PASSWORD=Secret(name="marqeta_jit_password", value=""),
        MARQETA_PROGRAM_FUND_TOKEN=Secret(
            name="marqeta_program_fund_token",
            value="a6e2bbe7-4f28-43b4-980d-6416f35fe33e",
        ),
    )
