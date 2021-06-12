import random
import string
from typing import Sequence


def generate_random_string(
    size: int = 3, chars: Sequence = string.ascii_lowercase + string.digits
) -> str:
    return "".join(random.choice(chars) for _ in range(size))
