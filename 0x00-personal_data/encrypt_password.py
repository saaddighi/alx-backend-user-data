#!/usr/bin/env python3
"""A module for encrypting passwords.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """returns a encrypted password"""
    salt = bcrypt.gensalt()
    hashd_pwd = bcrypt.hashpw(password.encode(), salt)
    return hashd_pwd
