from sqlalchemy import Column, VARCHAR, CHAR, Boolean, ForeignKey, TIMESTAMP
from base import Base
from sqlalchemy.dialects.postgresql import UUID 
import uuid

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column("nome", VARCHAR(150), nullable=False)
    email = Column("email", VARCHAR(255), nullable=False, unique=True)
    senha_hash = Column("senha_hash", VARCHAR(255), nullable=False)
    telefone = Column("telefone", VARCHAR(30), nullable=True)
    fuso_horario = Column("fuso_horario", VARCHAR(80), nullable=False)
    moeda_padrao = Column("moeda_padrao", CHAR(3), nullable=False)
    ativo = Column("ativo", Boolean(), default=True, nullable=False)
    criado_em = Column("criado_em", TIMESTAMP, nullable=False)
    atualizado_em = Column("atualizado_em", TIMESTAMP, nullable=False)
    ultimo_acesso_em = Column("ultimo_acesso_em", TIMESTAMP, nullable=True)
