import argparse
from datetime import datetime
from sauvgarde import load_data, save_data


def add_lap(team: str, time_sec: float, filename: str = "data.json"):
    data = load_data(filename)
    if team not in data:
        data[team] = []
    entry = {
        "timestamp": datetime.now().isoformat(),
        "time_sec": time_sec,
    }
    data[team].append(entry)
    save_data(data, filename)


def summary(filename: str = "data.json"):
    data = load_data(filename)
    for team, laps in data.items():
        total = sum(lap["time_sec"] for lap in laps)
        print(f"{team}: {len(laps)} tours, {total:.2f} s au total")


def main():
    parser = argparse.ArgumentParser(description="Gestion des temps pour les 24h vélo")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Ajouter un tour")
    add_parser.add_argument("team", help="Nom de l'equipe")
    add_parser.add_argument("time", type=float, help="Temps du tour en secondes")
    add_parser.add_argument("--file", default="data.json", help="Fichier de sauvegarde")

    sum_parser = subparsers.add_parser("summary", help="Afficher le résumé")
    sum_parser.add_argument("--file", default="data.json", help="Fichier de sauvegarde")

    args = parser.parse_args()
    if args.command == "add":
        add_lap(args.team, args.time, args.file)
    elif args.command == "summary":
        summary(args.file)


if __name__ == "__main__":
    main()

