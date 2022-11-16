import argparse

def init_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    return parser.parse_args()

def main() -> None:
    args = init_args()

if __name__ == "__main__":
    main()