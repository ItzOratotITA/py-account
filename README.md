
# PyAccount: a simple Python account package

With PyAccount you can create a GitHub repository from this repository because of it being a template, so you will have the account package file already included in the file structure, so you can develop a program written in Python and use this open-source account system.

## How to use templates

Click on the following button:
![Image from github docs](https://docs.github.com/assets/cb-77734/mw-1440/images/help/repository/use-this-template-button.webp)
> This image is from [this Github docs page](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template), where you can find a detailed guide for templates

Then you are done.

## Including the package in your code

After having created the repos from the template, you also need to include it in your code. To do so is really easy: first install these packages:

- rich
- pyyaml

then write this at the first line of your file.

```python
from lib.account import *
```

## Variables & functions

- [FUNCTION] log_sign_in(): opens the login dialogue and returns the username variable.

The username and the password are saved locally into usrdata.yml.

DO NOT USE THIS FOR SERIOUS THINGS: THE PASSWORD IS IN usrdata.yml WITHOUT ENCRYPTION, ROT13 OR OTHER STUFF SO IT'S EASILY BREAKABLE! When this announce will be removed that will mean that it will have been made more secure.
