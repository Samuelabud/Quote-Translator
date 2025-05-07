import flet as ft

def main(page: ft.Page):
    title = "Quote Translator"

    quote = "The only thing we have to fear is fear itself. – Franklin D. Roosevelt"z
    translations = {
        "ingles": "The only thing we have to fear is fear itself.",
        "espanish": "Lo único que debemos temer es al miedo mismo.",
        "frances": "La seule chose que nous devons craindre, c'est la peur elle-même.", #tous le meme tous le meme tous le meme
    }

    language = ft.Ref[ft.RadioGroup]()#radio group e pa q lo tiguere no se pongan de 
    #palomo y ten eligiendo 2 o mas vainas al mismo tiempo
    translated_quote = ft.Text(quote, size=20)

    def cambio(e):
        lang = language.current.value
        translated_quote.value = translations.get(lang, quote)
        page.update()

    def exit_app(e):
        page.window_destroy() #yo creo q en el mismo nombre lo dice todo

    page.title = title #esto taba como innecesario pero dejaelo ahi pq corre el codigo

    page.add(
        ft.Column(
            controls=[
                ft.Text(title, size=30),
                translated_quote,
                ft.RadioGroup(
                    ref=language,
                    value="Ingles", 
                    on_change=cambio,
                    content=ft.Column([
                        ft.Radio(value="Ingles", label="English"),
                        ft.Radio(value="espanish", label="Español"),
                        ft.Radio(value="frances", label="Français"),
                    ])
                ),
                ft.ElevatedButton(text="Exit", on_click=exit_app),
            ],
        )
    )
ft.app(target=main)
