# Contrato de Serviços 

Este é um simples script Python que utiliza a biblioteca ReportLab para criar um contrato de serviços em formato PDF. O contrato gerado por este script inclui informações básicas do cliente, como nome, CPF, telefone e CEP, bem como um espaço para o conteúdo do contrato e assinaturas.

## Pré-requisitos

Antes de utilizar este script, você deve ter o Python instalado no seu sistema. Além disso, é necessário instalar a biblioteca ReportLab, que pode ser instalada utilizando o pip:

```bash
pip install reportlab
```

## Uso

Você pode personalizar o contrato de acordo com suas necessidades, alterando as informações exibidas no contrato ou adicionando/removendo campos. O exemplo abaixo demonstra como usar o script:

```python
if __name__ == "__main__":
    
    create_contract(
        nome="Nome do Cliente",
        cpf="123.456.789-00",
        telefone="(11) 1234-5678",
        cep="12345-678",
        output_filename="contrato_exemplo.pdf"
    )
```

Certifique-se de substituir as informações de exemplo (nome, CPF, telefone e CEP) pelos dados reais do cliente e ajuste o nome do arquivo de saída conforme necessário.

## Personalização

Você pode personalizar o conteúdo do contrato editando a variável `texto_contrato` no script. Adicione ou modifique o texto conforme apropriado para o seu contrato de serviços.

Além disso, você pode ajustar a posição dos elementos no contrato (títulos, informações do cliente, assinaturas) alterando os valores das coordenadas no script.

## Execução

Para gerar o contrato em PDF, basta executar o script Python. O contrato será salvo com o nome especificado na variável `output_filename`.

```bash
python nome_do_script.py
```

Isso criará um arquivo PDF com o contrato de serviços preenchido com as informações fornecidas.

Esperamos que este script seja útil para você na criação de contratos de serviços personalizados em formato PDF. Sinta-se à vontade para adaptá-lo conforme suas necessidades específicas.
