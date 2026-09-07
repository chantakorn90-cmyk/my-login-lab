# นำเข้า PasswordHasher สำหรับสร้างและตรวจสอบ Password Hash
from argon2 import PasswordHasher

# นำเข้า Type สำหรับระบุให้ใช้อัลกอริทึม Argon2id โดยตรง
from argon2.low_level import Type

# นำเข้า VerifyMismatchError สำหรับจัดการกรณี Password ไม่ตรงกับ Hash
from argon2.exceptions import VerifyMismatchError

_hasher = PasswordHasher(
    time_cost=3,
    memory_cost=64 * 1024,
    parallelism=4,
    hash_len=32,
    salt_len=16,
    type=Type.ID
)

def hash_password(password: str) -> str:
    return _hasher.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    try:
        return _hasher.verify(hashed_password, password)
    except VerifyMismatchError:
        return False