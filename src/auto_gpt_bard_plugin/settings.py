from pydantic import BaseSettings

class Settings(BaseSettings):
    BARD_SESSION_TOKEN: str
    BARD_COMMAND_LABEL: str = "chat_with_bard"
    BARD_COMMAND_NAME: str = "Chat with bard"

    class Config:
        case_sensitive = True
        
    @property
    def __name__(self):
        # here is trick to avoid getting this class as a plugin
        # autogpt/plugins.py, line: 231, if ... and a_module.__name__ != "AutoGPTPluginTemplate"
        return "AutoGPTPluginTemplate"

settings = Settings()
