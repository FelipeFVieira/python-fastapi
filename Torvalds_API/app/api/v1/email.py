from fastapi import APIRouter, HTTPException
from app.services.email_service import EmailService
from app.models.user_info import UserInfo

router = APIRouter()

@router.post('/email')
def send_email(user_info: UserInfo):
    try:
        EmailService.send_email(user_info.recipient_name, user_info.recipient_email, user_info.template_type)
        return {"message": "E-mail enviado com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar e-mail: {e}")