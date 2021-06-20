# Check Pwned Passwords

![Build status](https://travis-ci.org/lietu/check-pwnedpasswords.svg?branch=master)

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


# Financial support

This project has been made possible thanks to [Cocreators](https://cocreators.ee) and [Lietu](https://lietu.net). You can help us continue our open source work by supporting us on [Buy me a coffee](https://www.buymeacoffee.com/cocreators).

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/cocreators)
