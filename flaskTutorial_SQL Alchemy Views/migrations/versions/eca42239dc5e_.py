"""empty message

Revision ID: eca42239dc5e
Revises: 
Create Date: 2019-02-07 10:05:30.529073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eca42239dc5e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Employee')
    op.drop_table('Departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Departments',
    sa.Column('department_id', sa.INTEGER(), nullable=False),
    sa.Column('department_name', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('department_id')
    )
    op.create_table('Employee',
    sa.Column('employee_id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.TEXT(), nullable=True),
    sa.Column('last_name', sa.TEXT(), nullable=True),
    sa.Column('dob', sa.TEXT(), nullable=True),
    sa.Column('cnic', sa.TEXT(), nullable=True),
    sa.Column('qualification', sa.TEXT(), nullable=True),
    sa.Column('department_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['Departments.department_id'], ),
    sa.PrimaryKeyConstraint('employee_id')
    )
    # ### end Alembic commands ###