import reflex as rx
from datetime import datetime

import sqlalchemy
from sqlmodel import Field

from .. import utils

class BlogPostModel(rx.Model, table=True):
    #user
    #id: int -> primary key
    title: str
    content: str
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )
    update_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )
    publish_active: bool=False
    publish_date: datetime = Field(
        default=None,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={},
        nullable=True
    )
    #created_at
    #update_at
    #publish_date
    #publish_time