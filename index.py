from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_contract(nome, cpf, telefone, cep, output_filename):
    
    # Crie um objeto PDF
    c = canvas.Canvas(output_filename, pagesize=letter)

    # Defina a fonte e tamanho do texto
    c.setFont("Helvetica", 12)

    # Adicione o título
    c.drawString(50, 750, "CONTRATO DE SERVIÇOS")

    # Adicione as informações do contrato
    c.drawString(50, 700, f"Nome do Cliente: {nome}")
    c.drawString(50, 680, f"CPF: {cpf}")
    c.drawString(50, 660, f"Telefone: {telefone}")
    c.drawString(50, 640, f"CEP: {cep}")

    # Adicione o corpo do contrato
    texto_contrato = """
    Este é um exemplo simples de contrato de serviços.
    Você pode personalizar o conteúdo do contrato
    de acordo com suas necessidades.
    """
    c.drawString(50, 620, texto_contrato)

    # Assine o contrato
    c.drawString(50, 570, "Assinatura do Cliente: ________________________")

    # Assine o contrato
    c.drawString(50, 570, "Assinatura do Testemeenha1: ________________________")
    
    c.drawString(50, 570, "Assinatura do Testemeenha2: ________________________")
    
    # Adicione uma linha divisória
    c.setLineWidth(1)
    c.line(50, 560, 550, 560)

    # Feche o arquivo PDF
    c.save()

# Exemplo de uso
if __name__ == "__main__":
    
    create_contract(
        nome="Nome do Cliente",
        cpf="123.456.789-00",
        telefone="(11) 1234-5678",
        cep="12345-678",
        output_filename="contrato_exemplo.pdf"
    )
