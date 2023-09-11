# Importar o GTK
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Abrir o arquivo Glade com a interface de usuário
builder = Gtk.Builder()
builder.add_from_file("/usr/share/calc-gtk/calc-gtk.glade")

# ---------------- BOTÕES -------------------------- #

# Obter os botões da calculadora
btn1        = builder.get_object("Btn1")
btn2        = builder.get_object("Btn2")
btn3        = builder.get_object("Btn3")
btn4        = builder.get_object("Btn4")
btn5        = builder.get_object("Btn5")
btn6        = builder.get_object("Btn6")
btn7        = builder.get_object("Btn7")
btn8        = builder.get_object("Btn8")
btn9        = builder.get_object("Btn9")
btn0        = builder.get_object("Btn0")
btn_igual   = builder.get_object("BtnIgual")
btn_apagar  = builder.get_object("BtnApagar")

# Obter o display
display     = builder.get_object("Display")

# Função que atualiza o display com o número
def atualizar_display(button, input):
    if input == "":
        display.set_text(input)

    elif input == "igual":
        num                 = int(display.get_text())
        divisores           = [str(i) for i in range(1, num + 1) if num % i == 0]
        divisores_string    = ", ".join(divisores) + "."
        display             .set_text(divisores_string)

    else:
        display.set_text(display.get_text() + str(input))

# Conectar os botões com a função
btn1        .connect("clicked", atualizar_display, 1)
btn2        .connect("clicked", atualizar_display, 2)
btn3        .connect("clicked", atualizar_display, 3)
btn4        .connect("clicked", atualizar_display, 4)
btn5        .connect("clicked", atualizar_display, 5)
btn6        .connect("clicked", atualizar_display, 6)
btn7        .connect("clicked", atualizar_display, 7)
btn8        .connect("clicked", atualizar_display, 8)
btn9        .connect("clicked", atualizar_display, 9)
btn0        .connect("clicked", atualizar_display, 0)
btn_apagar  .connect("clicked", atualizar_display, "")
btn_igual   .connect("clicked", atualizar_display, "igual")

# Event handlers do display
display     .connect("activate",            atualizar_display, "igual")
display     .connect("backspace",           atualizar_display, "")

def delete_from_cursor(a, b, c, d):
    atualizar_display("", "")

display     .connect("delete-from-cursor",  delete_from_cursor, "")

# ---------------- MENU ----------------------------#

# Obter o botão de menu e o menu
menu_button     = builder.get_object("BtnMenu")
popover_menu    = builder.get_object("Menu")

# Função que abre o menu
def on_menu_button_clicked(button, popover_menu):
    popover_menu.set_relative_to(button)
    popover_menu.show_all()

# Conectar o event handler à função
menu_button.connect("clicked", on_menu_button_clicked, popover_menu)

##### MENU OPTIONS ######

# Obter os botões do menu
btn_apagar_menu     = builder.get_object("BtnApagarMenu")
btn_calcular_menu   = builder.get_object("BtnCalcularMenu")
btn_sair_menu       = builder.get_object("BtnSairMenu")

# Conectar os event handlers
btn_apagar_menu.connect("clicked", atualizar_display, "")
btn_calcular_menu.connect("clicked", atualizar_display, "igual")
btn_sair_menu.connect("clicked", Gtk.main_quit)

# -------------------------------------------------- #

# Abrir e mostrar a janela como um todo
window = builder.get_object("Calculadora")
window.connect("destroy", Gtk.main_quit) # Garantir que o processo seja encerrado ao fechar a janela
window.show_all()

# Mainloop
Gtk.main()
