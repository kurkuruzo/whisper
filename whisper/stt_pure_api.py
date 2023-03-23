import asyncio
import os
import pathlib
from typing import BinaryIO, Iterable, Union
import aiohttp
from dotenv import load_dotenv


load_dotenv()


class WhisperAPI:
    API_KEY = os.environ["API_KEY"]

    async def _send_transcription_request(
        self,
        file: Union[pathlib.Path, BinaryIO],
        model: str,
        session: aiohttp.ClientSession,
        response_format: str = "json",
        language: str = "ru",
        prompt: str = "",
        temperature: float = 0.2,
    ):
        headers = {"Authorization": f"Bearer {self.API_KEY}"}
        if isinstance(file, pathlib.Path):
            with file.open("rb") as f:
                file_bytes = f.read()
        else:
            file_bytes = file
        body = aiohttp.FormData(
            {
                "file": file_bytes,
                "model": model,
                "response_format": response_format,
                "language": language,
                "prompt": prompt,
            }
        )

        async with session.post(
            "https://api.openai.com/v1/audio/transcriptions", headers=headers, data=body
        ) as res:
            return await res.json()

    async def _format_transcription(
        self,
        file: pathlib.Path,
        model: str,
        session: aiohttp.ClientSession,
        response_format: str,
        language: str,
        prompt: str,
    ) -> dict[str, dict[str, str]]:
        res = await self._send_transcription_request(
            file, model, session, response_format, language, prompt
        )
        return {file.name: res}

    async def trancribe_file(
        self,
        file_path: pathlib.Path,
        model: str,
        response_format: str = "json",
        language: str = "ru",
        prompt: str = "",
    ):
        async with aiohttp.ClientSession() as session:
            res = await self._format_transcription(
                file_path, model, session, response_format, language, prompt
            )
        return res[file_path.name]

    async def transcribe_files(
        self,
        file_list: Iterable[pathlib.Path],
        model: str,
        response_format: str = "json",
        language: str = "ru",
        prompt: str = "",
    ):
        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(limit=50)
        ) as session:
            tasks = [
                self._format_transcription(
                    file, model, session, response_format, language, prompt
                )
                for file in file_list
            ]
            return await asyncio.gather(*tasks)
