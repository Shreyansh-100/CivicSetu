import io
import json
import pickle
from pathlib import Path

import torch


models_dir = Path(__file__).resolve().parent / "secondary_files"


def _load_pickle(filename):
    with open(models_dir / filename, "rb") as file:
        return pickle.load(file)

# if pickle contains gpu tensors then load them onto cpu instead
def _load_sentence_model():
    original_loader = torch.storage._load_from_bytes
    torch.storage._load_from_bytes = lambda data: torch.load(
        io.BytesIO(data),
        map_location="cpu",
        weights_only=False,
    )

    try:
        return _load_pickle("sentence_model.pkl")
    finally:
        #if fails, restore original pytorch loading behavior
        torch.storage._load_from_bytes = original_loader


cat_encoder = _load_pickle("cat_encoded.pkl")
dept_encoder = _load_pickle("Dept_encoded.pkl")
cat_model = _load_pickle("cat_model.pkl")
dept_model = _load_pickle("dept_model.pkl")
sentence_model = _load_sentence_model()


def output(input_string):
    embedding = sentence_model.encode([input_string])

    dept_prediction = dept_model.predict(embedding)
    cat_prediction = cat_model.predict(embedding)

    department = dept_encoder.inverse_transform(dept_prediction)[0]
    category = cat_encoder.inverse_transform(cat_prediction)[0]

    return {
        "input": input_string,
        "department": department,
        "category": category,
    }


if __name__ == "__main__":
    input_string = "traffic lights"
    print(json.dumps(output(input_string), indent=2))
