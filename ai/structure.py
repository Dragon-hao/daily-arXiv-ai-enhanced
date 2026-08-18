from pydantic import BaseModel, Field, field_validator
import re

class Structure(BaseModel):
    tldr: str = Field(
        description="Provide a concise TL;DR summary of the paper's key idea and contribution"
    )
    motivation: str = Field(
        description="Explain the problem, motivation, and importance of the paper"
    )
    method: str = Field(
        description="Describe the proposed method, architecture, and technical innovations"
    )
    result: str = Field(
        description="Summarize experiments, datasets, metrics, and major results"
    )
    conclusion: str = Field(
        description="Summarize contributions, significance, and limitations"
    )
