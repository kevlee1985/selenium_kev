import random
import string


class RandomStringGenerator:
    @staticmethod
    def generate_random_string(length=10):
        # Generate a random string of lowercase letters
        lowercase_letters = string.ascii_lowercase
        random_string = ''.join(random.choice(lowercase_letters) for _ in range(length))
        return random_string
