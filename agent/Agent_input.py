import io
import json
import pickle
from pathlib import Path

import torch

class input_agent:
    def _load_pickle(filename):
        models_dir = Path(__file__).resolve().parent / "secondary_files"
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
            return input_agent._load_pickle("sentence_model.pkl")
        finally:
                #if fails, restore original pytorch loading behavior
            torch.storage._load_from_bytes = original_loader


    def output(input_string:str):
        
        cat_encoder = input_agent._load_pickle("cat_encoded.pkl")
        dept_encoder = input_agent._load_pickle("Dept_encoded.pkl")
        cat_model = input_agent._load_pickle("cat_model.pkl")
        dept_model = input_agent._load_pickle("dept_model.pkl")
        sentence_model = input_agent._load_sentence_model()


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


