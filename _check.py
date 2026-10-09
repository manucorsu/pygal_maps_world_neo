import subprocess
import sys

COMMANDS = [
    ["pytest"],
    ["ruff", "check", "--fix", "--show-fixes"],
    ["ruff", "format", "."],
]
commands_count = len(COMMANDS)


def main():
    for i, cmd in enumerate(COMMANDS):
        pretty_command = " ".join(cmd)
        print(f"\n({i + 1}/{commands_count}) Running `{pretty_command}`...")
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError:
            print(f"\n`{pretty_command}` failed.")
            sys.exit(1)

    print("\nAll checks passed.")
