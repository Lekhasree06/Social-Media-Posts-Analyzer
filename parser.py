
import json
from pydantic import BaseModel, Field, ValidationError


class PostAnalysis(BaseModel):
    tone: str = Field(description="Tone of the social media post")
    intent: str = Field(description="Intent or purpose of the post")
    communication_style: str = Field(description="Communication style of the post")
    summary: str = Field(description="Short summary of the post")


def parse_response(response_text: str):
    try:
        cleaned_text = response_text.strip()

        if cleaned_text.startswith("```json"):
            cleaned_text = cleaned_text.replace("```json", "").replace("```", "").strip()
        elif cleaned_text.startswith("```"):
            cleaned_text = cleaned_text.replace("```", "").strip()

        data = json.loads(cleaned_text)
        parsed_output = PostAnalysis(**data)
        return parsed_output.model_dump()

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by model",
            "raw_response": response_text
        }

    except ValidationError as e:
        return {
            "error": "Output validation failed",
            "details": str(e),
            "raw_response": response_text
        }
