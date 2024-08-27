
import pyautogui as auto
import time

auto.PAUSE = 0.5

# Abrir o menu iniciar
auto.press('win')
auto.write('vscode')
auto.press('enter')

# Aguardar o Visual Studio Code abrir
time.sleep(5)  # Ajuste o tempo conforme necessário

# Abrir o terminal integrado no VSCode (Ctrl + j)
auto.hotkey('ctrl', 'j')

# Aguardar o terminal abrir
time.sleep(1.2)

# Executar comandos Git no terminal
auto.write('git init')
auto.press('enter')
auto.write('git add .')
auto.press('enter')
auto.write('git commit -m "  "')





        















