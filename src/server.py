from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_produtos, rotas_pedidos, rotas_auth
from src.jobs.writer_notification import write_notification

#criar_bd()

#Produtos

app = FastAPI()

#CORS
origins = ['http://localhhost:3000',
           'http://myapp.vercel.com']
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Rotas Produtos
app.include_router(rotas_produtos.router)

#Rotas Segurança: Autenticação e Autorização
app.include_router(rotas_auth.router,prefix= "/auth")

#Rotas Pedidos
app.include_router(rotas_pedidos.router)

@app.post('/send_email/{email}')
def send_email(email:str,backgroud:BackgroundTasks):
    backgroud.add_task(write_notification,email,
                       'Ola , Segue abaixo o certificado de conclusão do curso')
    return {"ok": "Mensagem Enviada"}

@app.middleware('http')
async def tempoMiddleware(request:Request,next):
    print('Interceptou a chegada')

    response = await next (request) 

    print('Interceptou a volta')

    return response
