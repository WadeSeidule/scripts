# type: ignore

import argparse
import subprocess


def main(args):
    codespaces_list_cmd = "gh codespace list | awk '{print $1}'"
    codespaces_code_cmd = "gh codespace {action} -c {codespace_name}"
    github_auth_cmd = "gh auth login"

    if args.auth:
        subprocess.call(github_auth_cmd, shell=True)

    if args.ssh:
        action = "ssh"
    else:
        action = "code"

    output = subprocess.check_output(
        codespaces_list_cmd, universal_newlines=True, shell=True
    )
    codespace_names = output.splitlines()

    input_str = "\n".join([f"{i} {name}" for i, name in enumerate(codespace_names)])
    choice = input(input_str + "\nChoice: ")

    if not choice.isdigit():
        raise TypeError("Must be an int")

    choice = int(choice)

    if choice not in list(range(len(codespace_names))):
        raise ValueError("Pick a correct number")

    subprocess.call(
        codespaces_code_cmd.format(
            action=action, codespace_name=codespace_names[choice]
        ),
        shell=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--auth", action="store_true")
    parser.add_argument("--ssh", action="store_true")
    main(parser.parse_args())
