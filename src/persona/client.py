# This file was auto-generated by Fern from our API Definition.

from .environment import PersonaEnvironment
from .resources.accounts.client import AccountsClient, AsyncAccountsClient
from .resources.api_logs.client import ApiLogsClient, AsyncApiLogsClient
from .resources.database_verifications.client import AsyncDatabaseVerificationsClient, DatabaseVerificationsClient
from .resources.document_verifications.client import AsyncDocumentVerificationsClient, DocumentVerificationsClient
from .resources.documents.client import AsyncDocumentsClient, DocumentsClient
from .resources.events.client import AsyncEventsClient, EventsClient
from .resources.government_id_verifications.client import (
    AsyncGovernmentIdVerificationsClient,
    GovernmentIdVerificationsClient,
)
from .resources.importers.client import AsyncImportersClient, ImportersClient
from .resources.inquiries.client import AsyncInquiriesClient, InquiriesClient
from .resources.phone_number_verifications.client import (
    AsyncPhoneNumberVerificationsClient,
    PhoneNumberVerificationsClient,
)
from .resources.reports.client import AsyncReportsClient, ReportsClient
from .resources.verifications.client import AsyncVerificationsClient, VerificationsClient


class Persona:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key
        self.inquiries = InquiriesClient(environment=self._environment, api_key=self.api_key)
        self.reports = ReportsClient(environment=self._environment, api_key=self.api_key)
        self.verifications = VerificationsClient(environment=self._environment, api_key=self.api_key)
        self.accounts = AccountsClient(environment=self._environment, api_key=self.api_key)
        self.api_logs = ApiLogsClient(environment=self._environment, api_key=self.api_key)
        self.documents = DocumentsClient(environment=self._environment, api_key=self.api_key)
        self.database_verifications = DatabaseVerificationsClient(environment=self._environment, api_key=self.api_key)
        self.government_id_verifications = GovernmentIdVerificationsClient(
            environment=self._environment, api_key=self.api_key
        )
        self.phone_number_verifications = PhoneNumberVerificationsClient(
            environment=self._environment, api_key=self.api_key
        )
        self.events = EventsClient(environment=self._environment, api_key=self.api_key)
        self.document_verifications = DocumentVerificationsClient(environment=self._environment, api_key=self.api_key)
        self.importers = ImportersClient(environment=self._environment, api_key=self.api_key)


class AsyncPersona:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key
        self.inquiries = AsyncInquiriesClient(environment=self._environment, api_key=self.api_key)
        self.reports = AsyncReportsClient(environment=self._environment, api_key=self.api_key)
        self.verifications = AsyncVerificationsClient(environment=self._environment, api_key=self.api_key)
        self.accounts = AsyncAccountsClient(environment=self._environment, api_key=self.api_key)
        self.api_logs = AsyncApiLogsClient(environment=self._environment, api_key=self.api_key)
        self.documents = AsyncDocumentsClient(environment=self._environment, api_key=self.api_key)
        self.database_verifications = AsyncDatabaseVerificationsClient(
            environment=self._environment, api_key=self.api_key
        )
        self.government_id_verifications = AsyncGovernmentIdVerificationsClient(
            environment=self._environment, api_key=self.api_key
        )
        self.phone_number_verifications = AsyncPhoneNumberVerificationsClient(
            environment=self._environment, api_key=self.api_key
        )
        self.events = AsyncEventsClient(environment=self._environment, api_key=self.api_key)
        self.document_verifications = AsyncDocumentVerificationsClient(
            environment=self._environment, api_key=self.api_key
        )
        self.importers = AsyncImportersClient(environment=self._environment, api_key=self.api_key)
