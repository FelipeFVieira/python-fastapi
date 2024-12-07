from fastapi.middleware.cors import CORSMiddleware

class CorsConfig:
    @staticmethod
    def add_cors(app):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Ou os domínios específicos
            allow_credentials=True,
            allow_methods=["*"],  # Permite todos os métodos HTTP
            allow_headers=["*"],  # Permite todos os cabeçalhos
        )