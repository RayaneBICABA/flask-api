import bcrypt

def hash_password(plain_password: str) -> str:
    """Hash a password using bcrypt"""
    hashed = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hashed password"""
    return bcrypt.checkpw(plain_password.encode('utf-8'),hashed_password.encode('utf-8'))