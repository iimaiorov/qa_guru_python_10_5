from typing import Literal
import pydantic

BrowserType = Literal['chrome', 'firefox', 'edge']
BrowserVersion = Literal['100.0', '99.0']


class Config(pydantic.BaseSettings):
    base_url: str = 'https://demoqa.com/automation-practice-form'
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 5
    driver_name: BrowserType = 'chrome'
    browser_version = BrowserVersion = '100.0'
