import yaml
from rich.console import Console

console = Console()

def log_sign_in():
    username_logged = None
    try:
        confirmed = False
        with open("usrdata.yml", "r") as configfile:
            loadconfig = yaml.safe_load
            config = loadconfig(configfile)
            usrn = config["usern"]
            usrp = config["passw"]
            console.rule("Log in")
            input_usrn = console.input("[green]Username: ")
            if not input_usrn == usrn:
                console.print("[red]Wrong!")
                exit()
            input_usrp = console.input("[orange]Password: ")
            if not input_usrp == usrp:
                console.print("[red]Wrong!")
                exit()
            else:
                confirmed = True
            if confirmed:
                username_logged = input_usrn
    except:
        console.rule("Sign in")
        usrnm = console.input("[green]Username: ")
        pass_word = console.input("[orange]Password: ")
        with open("usrdata.yml", "w") as writef:
            usrd = {
                "usern": usrnm,
                "passw": pass_word
            }
            yaml.dump(usrd, writef, default_flow_style=False)
        username_logged = usrnm
    if not username_logged == None:
        return username_logged

print(log_sign_in())