"""xignite security news

Revision ID: 5809f092058
Revises: 243385d2034
Create Date: 2014-12-16 13:04:45.853890

"""

# revision identifiers, used by Alembic.
revision = '5809f092058'
down_revision = '243385d2034'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('xignite_securty',
    sa.Column('symbol', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=20), nullable=False),
    sa.Column('cik', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=10), nullable=True),
    sa.Column('cusip', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=9), nullable=True),
    sa.Column('isin', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=12), nullable=True),
    sa.Column('valoren', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=9), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('market', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('mic', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=4), nullable=True),
    sa.Column('most_liquid_exg', sa.BOOLEAN(), nullable=False),
    sa.Column('industry', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('symbol')
    )
    op.create_table('xignite_security_release',
    sa.Column('symbol', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=20), server_default='', nullable=False),
    sa.Column('title', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('local_pub_date', sa.DATE(), nullable=False),
    sa.Column('utc_offset', sa.FLOAT(), autoincrement=False, nullable=False),
    sa.Column('discovered_at', sa.DATETIME(), nullable=False),
    sa.Column('source', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('url', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=767), nullable=False),
    sa.Column('image_urls', mysql.MEDIUMTEXT(convert_unicode=True), nullable=True),
    sa.Column('tags', sa.TEXT(convert_unicode=True), nullable=True),
    sa.Column('proc_dur', sa.FLOAT(), nullable=False),
    sa.ForeignKeyConstraint(['symbol'], [u'xignite_securty.symbol'], name='xignite_security_release_to_security_fk', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('symbol', 'local_pub_date', 'url', name='xignite_security_release_pk')
    )
    op.create_table('xignite_security_headline',
    sa.Column('symbol', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=20), server_default='', nullable=False),
    sa.Column('title', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('local_pub_date', sa.DATE(), nullable=False),
    sa.Column('utc_offset', sa.FLOAT(), autoincrement=False, nullable=False),
    sa.Column('discovered_at', sa.DATETIME(), nullable=False),
    sa.Column('source', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('url', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=767), nullable=False),
    sa.Column('image_urls', mysql.MEDIUMTEXT(convert_unicode=True), nullable=True),
    sa.Column('tags', sa.TEXT(convert_unicode=True), nullable=True),
    sa.Column('proc_dur', sa.FLOAT(), nullable=False),
    sa.ForeignKeyConstraint(['symbol'], [u'xignite_securty.symbol'], name='xignite_security_headline_to_security_fk', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('symbol', 'local_pub_date', 'url', name='xignite_security_headline_pk')
    )
    ### end Alembic commands ###


def downgrade():
    raise NotImplementedError("Rollback is not supported.")
