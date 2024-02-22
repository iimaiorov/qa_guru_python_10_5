from typing import Literal
import pydantic

BrowserType = Literal['chrome', 'firefox', 'edge']


class Config(pydantic.BaseSettings):

    base_url: str = 'https://demoqa.com/automation-practice-form'
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 5
    driver_name: BrowserType = 'chrome'
