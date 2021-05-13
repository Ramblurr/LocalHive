from local_hive import LocalHiveListener


def get_listener(port=6989):
    return LocalHiveListener(port=port)


if __name__ == "__main__":
    localmind = get_listener()
    localmind.listen()
