from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    """
    The `Hasher` class provides methods for verifying passwords
    and generating password hashes using the `CryptContext` class from the `passlib` library.
    """

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify if the plain password matches the hashed password.

        Args:
            plain_password (str): The plain password to verify.
            hashed_password (str): The hashed password to compare against.

        Returns:
            bool: True if the plain password matches the hashed password, False otherwise.
        """
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def generate_password_hash(password: str) -> str:
        """
        Generate the hashed version of the password.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return pwd_context.hash(password)
