# Título da página : Mensagens
# Botão para inicar o chat
    # Título: Bem vindo ao Zapzapdois
    # Campo com textp: Escreva o nome no chat
    # Botão: Entrar no0 chat
        # Sumir com o Título e o Botão
        # Fechar o Popup
        # Criar o chat com f'{Nome usuário} entrou no site'
        # Embaixo no chat:
            # Campo de texto "Digite sua mensagem"
            # Botão de enviar mensagem
                # Aparece menagem no chat + nome de usuario

import flet as ft

def main(page):
    titulo = ft.Text('Mensagens')

    def enviar_tunel_socket(mensagem):
        chat.controls.append(ft.Text(mensagem))
        page.update()

    page.pubsub.subscribe(enviar_tunel_socket) # Criação do tunel de comunicação

    titulo_janela = ft.Text('Bem vindo ao Mensagens') # Título da página
    campo_nome_usuario = ft.TextField(label = 'Meu nome é... ') # Campo para escrever o nome

    def enviar_mensagem(evento):
        # Como a mensagem vai ser exibida no chat
        texto = f'{campo_nome_usuario.value} : {texto_usuario.value}'
        # Limpar o campo de mensagem
        texto_usuario.value = ''
        page.pubsub.send_all(texto) # Passagem da mensagem pelo tunel

    texto_usuario = ft.TextField(label = 'Digite algo... ', on_submit=enviar_mensagem) # Ação ao apertar tecla enter
    botao_enviar = ft.ElevatedButton('Enviar', on_click = enviar_mensagem)
    
    chat = ft.Column()

    linha_mensagem = ft.Row([texto_usuario, botao_enviar])

    def entrar_chat(evento):
        # remover o Título, Botão e Popup
        page.remove(titulo)
        page.remove(botao_iniciar)
        janela.open = False
        page.add(chat)
        page.add(linha_mensagem)

        # Criar o chat com f'{Nome usuário} entrou no site'
        texto_entrou_chat = ft.Text(f'{campo_nome_usuario.value} entrou no chat') # Como formatar dados flet
        page.pubsub.send_all(texto_entrou_chat.value)

        page.update()

    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click = entrar_chat) # Botao para entrar no chat

    janela = ft.AlertDialog( # Criação de uma janela para entrar no chat
        title = titulo_janela, 
        content = campo_nome_usuario, 
        actions = [botao_entrar]
    )

    def abrir_popup(evento):
        page.dialog = janela
        janela.open = True
        page.update() # Atualiza onde está localizado

    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=abrir_popup)

    page.add(titulo)
    page.add(botao_iniciar)

ft.app(main, view = ft.WEB_BROWSER)
