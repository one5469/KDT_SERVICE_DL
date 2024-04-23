"""empty message

Revision ID: 15f507463eae
Revises: 
Create Date: 2024-04-18 15:34:45.526329

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '15f507463eae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('favorite_food')
    op.drop_table('persen')
    op.drop_table('제조업_생산능력_및_가동률지수')
    op.drop_table('user_table')
    op.drop_table('string_tbl')
    op.drop_table('person')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('person_id', mysql.SMALLINT(unsigned=True), autoincrement=True, nullable=False),
    sa.Column('fname', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('lname', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('eye_color', mysql.ENUM('BR', 'BL', 'GR'), nullable=True),
    sa.Column('birth_date', sa.DATE(), nullable=True),
    sa.Column('street', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('city', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('state', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('country', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('postal_code', mysql.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('person_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('string_tbl',
    sa.Column('char_fld', mysql.CHAR(length=30), nullable=True),
    sa.Column('vchar_fld', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=100), nullable=True),
    sa.Column('text_fld', mysql.TEXT(), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('user_table',
    sa.Column('userID', mysql.CHAR(length=8), nullable=False),
    sa.Column('userName', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('birthYear', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('addr', mysql.CHAR(length=2), nullable=False),
    sa.Column('mobile1', mysql.CHAR(length=3), nullable=True),
    sa.Column('mobile2', mysql.CHAR(length=8), nullable=True),
    sa.Column('height', mysql.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('mDate', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('userID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('제조업_생산능력_및_가동률지수',
    sa.Column('산업별', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('시점', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('생산능력지수', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('가동률지수(원지수)', mysql.DOUBLE(asdecimal=True), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('persen',
    sa.Column('person_id', mysql.SMALLINT(unsigned=True), autoincrement=False, nullable=False),
    sa.Column('fname', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('lname', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('eye_color', mysql.ENUM('BR', 'BL', 'GR'), nullable=True),
    sa.Column('birth_date', sa.DATE(), nullable=True),
    sa.Column('strett', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('city', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('state', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('country', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('postal_code', mysql.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('person_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('favorite_food',
    sa.Column('person_id', mysql.SMALLINT(unsigned=True), autoincrement=False, nullable=False),
    sa.Column('food', mysql.VARCHAR(length=20), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.person_id'], name='fk_fav_food_person_id'),
    sa.PrimaryKeyConstraint('person_id', 'food'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('answer')
    op.drop_table('question')
    # ### end Alembic commands ###
