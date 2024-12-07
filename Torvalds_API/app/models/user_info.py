from pydantic import BaseModel
from enum import Enum

class TemplateEnum(str, Enum):
    academy: str = "academy"
    linux_creation: str = "linux_creation"
    torvalds_biography: str = "torvalds_biography"

class UserInfo(BaseModel):
    recipient_name: str
    recipient_email: str
    template_type: TemplateEnum  