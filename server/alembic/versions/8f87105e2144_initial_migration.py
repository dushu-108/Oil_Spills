"""Initial migration

Revision ID: 8f87105e2144
Revises: 
Create Date: 2024-09-04 17:38:49.007026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8f87105e2144'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Drop existing tables if necessary
    op.drop_table('anomalies', if_exists=True)
    op.drop_table('satellite_data', if_exists=True)
    op.drop_table('alerts', if_exists=True)

    # Create ais_data table
    op.create_table('ais_data',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('mmsi', sa.BigInteger(), nullable=True),
        sa.Column('base_date_time', sa.DateTime(), nullable=True),
        sa.Column('latitude', sa.Float(), nullable=True),
        sa.Column('longitude', sa.Float(), nullable=True),
        sa.Column('sog', sa.Float(), nullable=True),
        sa.Column('cog', sa.Float(), nullable=True),
        sa.Column('heading', sa.Float(), nullable=True),
        sa.Column('vessel_name', sa.String(length=255), nullable=True),
        sa.Column('imo', sa.String(length=50), nullable=True),
        sa.Column('call_sign', sa.String(length=50), nullable=True),
        sa.Column('vessel_type', sa.Integer(), nullable=True),
        sa.Column('status', sa.Integer(), nullable=True),
        sa.Column('length', sa.Float(), nullable=True),
        sa.Column('width', sa.Float(), nullable=True),
        sa.Column('draft', sa.Float(), nullable=True),
        sa.Column('cargo', sa.Float(), nullable=True),
        sa.Column('transceiver_class', sa.String(length=1), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    # Recreate tables if necessary
    op.create_table('ais_data',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('mmsi', sa.BigInteger(), nullable=True),
        sa.Column('base_date_time', sa.DateTime(), nullable=True),
        sa.Column('latitude', sa.Float(), nullable=True),
        sa.Column('longitude', sa.Float(), nullable=True),
        sa.Column('sog', sa.Float(), nullable=True),
        sa.Column('cog', sa.Float(), nullable=True),
        sa.Column('heading', sa.Float(), nullable=True),
        sa.Column('vessel_name', sa.String(length=255), nullable=True),
        sa.Column('imo', sa.String(length=50), nullable=True),
        sa.Column('call_sign', sa.String(length=50), nullable=True),
        sa.Column('vessel_type', sa.Integer(), nullable=True),
        sa.Column('status', sa.Integer(), nullable=True),
        sa.Column('length', sa.Float(), nullable=True),
        sa.Column('width', sa.Float(), nullable=True),
        sa.Column('draft', sa.Float(), nullable=True),
        sa.Column('cargo', sa.Float(), nullable=True),
        sa.Column('transceiver_class', sa.String(length=1), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('alerts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('vessel_id', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('alert_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('alert_type', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='alerts_pkey')
    )
    op.create_table('satellite_data',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('image', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.Column('latitude', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('longitude', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('detected_spill', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='satellite_data_pkey')
    )
    op.create_table('anomalies',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('vessel_id', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('anomaly_type', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('latitude', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('longitude', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='anomalies_pkey')
    )
    # ### end Alembic commands ###
