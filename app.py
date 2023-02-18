import pyautogui  # mouse movement, keyboard and typing
from time import sleep

# 1 - Clicar e escrever o nome
pyautogui.click(700, 389)
pyautogui.write('jhonatan')
# 2 - Clicar e escrever a senha
pyautogui.click(709, 412)
pyautogui.write('123456')
# 3 - Clicar em entrar
pyautogui.click(597, 441)
# 4 - Extrair cada informação do produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #   1 - Clicar e digitar o produto
        pyautogui.click(465, 378, duration=1)
        pyautogui.write(produto)

        #   2 - Clicar e digitar a quantidade
        pyautogui.click(488, 402, duration=1)
        pyautogui.write(quantidade)

        #   3 - Clicar e digitar o preço
        pyautogui.click(488, 423, duration=1)
        pyautogui.write(preco)

        #   4 - Clicar no botão registrar
        pyautogui.click(319, 578, duration=1)
        sleep(1)
