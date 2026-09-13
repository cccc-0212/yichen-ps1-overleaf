"""Write the deterministic PS1 validation record to standard output."""
import json
from .games import one_shot_benchmark, preset_results


if __name__ == "__main__":
    record = {
        "model": "adaptive-tax repeated game",
        "evidence_class": "programmed demonstration",
        "one_shot_benchmark": one_shot_benchmark(),
        "preset_results": preset_results(),
    }
    print(json.dumps(record, indent=2, sort_keys=True))
