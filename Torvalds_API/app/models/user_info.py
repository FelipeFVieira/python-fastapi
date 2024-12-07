from pydantic import BaseModel
from enum import Enum

class TemplateEnum(str, Enum):
    academy = "academy"
    linux_creation = "linux_creation"
    torvalds_biography = "torvalds_biography"

class UserInfo(BaseModel):
    recipient_name: str
    recipient_email: str
    template_type: TemplateEnum  