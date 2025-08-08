import json
from dataclasses import dataclass
import sys
import pdb
sys.path.append('/home/engs2575/project/unified-model-editing')

@dataclass
class HyperParams:
    """
    Simple wrapper to store hyperparameters for Python-based rewriting methods.
    """

    @classmethod
    def from_json(cls, fpath):
        pdb.set_trace()
        with open(fpath, "r") as f:
            data = json.load(f)

        return cls(**data)
