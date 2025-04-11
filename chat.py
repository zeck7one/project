import flet as ft


def main(pagina):
    texto = ft.Text('weBZep')


   
    chat = ft.Column()

    
    def enviar_mensagem_tunel(mensagem):
        print(mensagem)

        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print(enviar_mensagem)
        pagina.pubsub.send_all(f'{nome_usuario.value}:{campo_mensagem.value}')
        campo_mensagem.value = ''


        pagina.update()

    

    campo_mensagem  = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton(text='Enviar', on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        pagina.add(chat)
        pagina.pubsub.send_all(f'{nome_usuario.value} Entrou no chat')
        pagina.add(linha_enviar)




        pagina.update()



    titulo_popup = ft.Text('bem vindo ao zep')
    nome_usuario = ft.TextField(label='Escreva seu nome no chat')
    botao__entrar = ft.ElevatedButton('Entrar', on_click=entrar_chat)
    popup =ft.AlertDialog(
        open= False,
        modal= True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao__entrar]
        
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True

        pagina.update()
    
    botao_iniciar = ft.ElevatedButton('iniciar chat', on_click=abrir_popup)
    pagina.add(texto)
    pagina.add(botao_iniciar)


    




ft.app(target=main, view=ft.WEB_BROWSER)    
