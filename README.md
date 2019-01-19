# Check Pwned Passwords

Simple tool to check if any of your passwords in your password database
are known by the [Pwned Passwords](https://haveibeenpwned.com/Passwords)
API.

The passwords aren't actually transmitted, only a part of the SHA-1 hash
is.

Currently supports the password database format for:

 - Dashlane JSON export

Other formats should be easy to add - please send a PR.

# Usage

```bash
pip install -r requirements.txt
python check_pwnedpasswords.py DashlaneExport.json
```

# License

MIT + BSD 3-clause, see [LICENSE.md](LICENSE.md).
