from datetime import datetime, timedelta

import jwt

from core.config import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.AUTH_JWT.PRIVATE_KEY_PATH.read_text(),
    algorithm: str = settings.AUTH_JWT.ALGORITHM,
    expire_minutes: int = 60,
    expire_timedelta: timedelta | None = None,
) -> str:
    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.AUTH_JWT.PUBLIC_KEY_PATH.read_text(),
    algorithm: str = settings.AUTH_JWT.ALGORITHM,
) -> dict:
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=[algorithm],
    )
    return decoded

def verify_access_token(
    token: str
):
    try:
        payload_jwt = decode_jwt(token=token)
        return True, payload_jwt.get("id"), payload_jwt.get("email")
    except Exception:
        return False