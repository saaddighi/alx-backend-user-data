#!/usr/bin/env python3
"""A module for encrypting passwords.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """returns a encrypted password"""
    salt = bcrypt.gensalt()
    hashd_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashd_pwd


def is_valid(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
