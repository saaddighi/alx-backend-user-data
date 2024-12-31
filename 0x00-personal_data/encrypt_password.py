#!/usr/bin/env python3
"""A module for encrypting passwords.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """returns a encrypted password"""
    hashd_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashd_pwd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """check if hashed password is valid"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
