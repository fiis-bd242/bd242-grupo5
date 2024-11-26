import reflex as rx
import asyncio
import sqlalchemy

from datetime import datetime, timezone
from sqlmodel import Field

from .. import utils


class ContactEntryModel(rx.Model, table=True):
    user_id: int | None = None
    first_name: str
    last_name: str | None = None
    email: str | None=None #Field(default=None, nullable=True)
    message: str
    created_ad: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )