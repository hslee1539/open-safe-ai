from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from typer import Typer
from pydantic import BaseModel
from mlx_lm import load, stream_generate
from mlx_lm.cache_prompt import make_prompt_cache
from pathlib import Path
from typing import Generator
import os, json

api_app = FastAPI()
cli_app = Typer()


class Query(BaseModel):
    prompt: str
    model: str


class Mlx:
    @staticmethod
    def predict(query: Query):
        model, tokenizer = load("mlx-community/" + query.model)
        messages = [{"role": "user", "content": query.prompt}]
        prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
        return stream_generate(model, tokenizer, prompt=prompt)

    @staticmethod
    def predict_stream(model: str, prompt: Generator[str, None, None]):
        model, tokenizer = load("mlx-community/" + model)
        prompt_cache = make_prompt_cache(model)
        prompt = ([{"role": "user", "content": i}] for i in prompt)
        prompt = (
            tokenizer.apply_chat_template(i, add_generation_prompt=True) for i in prompt
        )
        for i in prompt:
            yield stream_generate(model, tokenizer, i, prompt_cache=prompt_cache)

    @staticmethod
    def list():
        full_name_list = os.listdir(Path.home() / ".cache" / "huggingface" / "hub")
        full_name_list = [i for i in full_name_list if "models--mlx-community" in i]
        return [i.split("--")[-1] for i in full_name_list]


@cli_app.command()
def run(model: str):
    """run model..."""
    import sys

    stream = range(9999)
    stream = (print(f"({model})>>", end="", flush=True) for _ in stream)
    stream = (sys.stdin.readline() for _ in stream)
    stream = (i for i in stream if type(i) is str)
    for stream in Mlx.predict_stream(model, stream):
        for tok in stream:
            print(tok.text, end="", flush=True)
        print("")


@cli_app.command()
def list():
    """get available model list"""
    print(Mlx.list())


@cli_app.command()
def serve():
    import uvicorn

    uvicorn.run(api_app, host="0.0.0.0", port=8000)


@api_app.post("/generate")
def predict(query: Query):
    stream = (
        {"text": i.text, "finish_reason": str(i.finish_reason)}
        for i in Mlx.predict(query)
    )
    stream = (json.dumps(i, separators=(",", ":")) + "\n" for i in stream)
    return StreamingResponse(stream, media_type="application/json")


@api_app.get("/list")
def list():
    return Mlx.list()


def main():
    cli_app()


if __name__ == "__main__":
    main()
