from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from MukeshRobot import DB_URI
from MukeshRobot import LOGGER as log

# Correct the DB_URI if it starts with "postgres://"
if DB_URI and DB_URI.startswith("postgres://"):
    DB_URI = DB_URI.replace("postgres://", "postgresql://", 1)

# Declare the base for declarative class definitions
BASE = declarative_base()

def start() -> scoped_session:
    try:
        # Create the engine and bind it to the metadata
        engine = create_engine(DB_URI, client_encoding="utf8")
        log.info("[PostgreSQL] Connecting to database...")
        BASE.metadata.bind = engine
        BASE.metadata.create_all(engine)
        
        # Return the session
        return scoped_session(sessionmaker(bind=engine, autoflush=False))
    except Exception as e:
        log.exception(f"[PostgreSQL] Failed to connect due to: {e}")
        raise

try:
    SESSION = start()
    log.info("[PostgreSQL] Connection successful, session started.")
except Exception as e:
    log.error("[PostgreSQL] Exiting due to failure.")
    exit(1)
