import sys
from pathlib import Path

def read_entry(path):
    parts = path.read_text(encoding="utf-8").split("---")
    if len(parts) < 3:
        return None
    data = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().lower()
    return data

def average(numbers):
    return round(sum(numbers) / len(numbers), 1) if numbers else None

folder = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
entries = []
for p in sorted(folder.glob("*.md")):
    e = read_entry(p)
    if e:
        entries.append(e)

def conf(e):
    try:
        return float(e.get("confidence", ""))
    except ValueError:
        return None

wins = [conf(e) for e in entries if e.get("outcome") == "win" and conf(e) is not None]
losses = [conf(e) for e in entries if e.get("outcome") == "loss" and conf(e) is not None]
high_conf_losses = [e for e in entries if e.get("outcome") == "loss" and (conf(e) or 0) >= 8]
with_kill = [e for e in entries if e.get("kill_criteria_set") == "yes"]
followed = [e for e in with_kill if e.get("kill_criteria_followed") == "yes"]
urgent = [e for e in entries if e.get("urgency_cue") == "yes"]
urgent_losses = [e for e in urgent if e.get("outcome") == "loss"]

print("Entries read:", len(entries))
print("Avg confidence on wins:", average(wins))
print("Avg confidence on losses:", average(losses))
print("High-confidence (8+) losses:", len(high_conf_losses))
print("Entries with kill criteria:", len(with_kill))
print("Kill criteria followed:", len(followed), "of", len(with_kill))
print("Entries with an urgency cue:", len(urgent))
print("Urgency-cue entries that ended in a loss:", len(urgent_losses))
