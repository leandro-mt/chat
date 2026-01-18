# importa  o flet
import flet as ft
 #criar pagina inical
def main(pagina):
    # criar a pagina princial
    titulo = ft.Text("Hashzap")
    pagina.add(titulo)
    def enviar_mensamge_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensamge_tunel)

    def Enviar_mensagem(evento):
        nome_usario = caixa_nome.value
        texto_campo_usariao = campo_enviar_mensagem.value
        mensagem = f"{nome_usario}: {texto_campo_usariao}"
        pagina.pubsub.send_all(mensagem)
        

        #limpar caixa
        campo_enviar_mensagem.value =""
        pagina.update()


    campo_enviar_mensagem = ft.TextField(label = "Digite sua Mesagem", on_submit= Enviar_mensagem)
    botao_enviar_mengaem = ft.ElevatedButton("Enviar Mensagem", on_click=Enviar_mensagem)

    chat = ft.Column()
    linha_enviar = ft.Row ({campo_enviar_mensagem, botao_enviar_mengaem})
    def entra_no_chat(evento):
        # fecha popup
        popup.open = False
        # sumir o titirulo sumir com botão do chat
        pagina.remove(titulo)
        pagina.remove(botao)

        pagina.add(chat)
       
        #carregar chat

        #carregar o botaão 
        pagina.add(linha_enviar)
        # aviso que esntro no chat
        nome_usario = caixa_nome.value
        mensagem = f"{nome_usario} entrou no Chat"
        pagina.pubsub.send_all(mensagem)
       
        

   
        pagina.update()
    
    # ciari o popup


    titulo_popup = ft.Text("Bem vindo ao Hasdzap")
    caixa_nome = ft.TextField(label="Digita seu nome")
    botao_popup = ft.ElevatedButton("Entra no chat", on_click=entra_no_chat)
    popup = ft.AlertDialog(title=titulo_popup, content= caixa_nome, actions= [botao_popup])

    # botao inicial
    def abrir_popup(evento):
        pagina.dialog =popup
        popup.open = True
        pagina.update()
        print("cliclou no botão")
    botao = ft.ElevatedButton("Incia chat",on_click= abrir_popup)
    pagina.add(botao)

# executar 
if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)

