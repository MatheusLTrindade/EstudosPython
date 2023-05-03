# Projeto de Automação de Criação de Instâncias EC2 na AWS com Python

Este é um projeto de automação de criação de instâncias EC2 na AWS usando Python. Ele utiliza o serviço de computação em nuvem Amazon Elastic Compute Cloud (EC2) para criar instâncias virtuais utilizando a linguagem de programação Python.

O projeto contém os seguintes arquivos:

- `iam_role.json`: Este arquivo contém a política do IAM que permite que o código Python crie instâncias EC2.
- `lambda_function.py`: Este arquivo contém o código Python que cria instâncias EC2.
- `README.md`: Este arquivo fornece informações sobre como configurar e executar o projeto.

## Pré-requisitos
Antes de executar o projeto, você precisa ter os seguintes requisitos:

- Uma conta AWS com permissões para criar instâncias EC2 e funções IAM.
- O acesso às chaves de acesso da sua conta AWS.
- O Python 3 instalado em seu sistema.

## Configuração Inicial

Para configurar o projeto, siga as etapas abaixo:

1. Crie uma função do AWS Lambda no console da AWS:

```python
import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)
```

2. Certifique-se de que a função esteja associada a um papel com a política IAM a seguir:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:RunInstances"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

Também é necessário criar uma role IAM com permissões para executar a ação de criar instâncias EC2, além de .

## Execução
Para executar o projeto, siga as etapas abaixo:

1. Abra o console do AWS Lambda e selecione a função que você criou.
2. Clique em "Teste" e, em seguida, em "Criar novo teste".
3. Defina o nome do teste e clique em "Criar".
4. Clique em "Teste" novamente para executar a função.
5. Acesse a seção "Logs" para ver o registro da criação da instância EC2.

## Variáveis de Ambiente

As variáveis de ambiente que devem ser configuradas são:

- `AMI`: O ID da imagem da máquina Amazon Machine Image (AMI) que você deseja usar para criar a instância. Por exemplo, `ami-0c55b159cbfafe1f0`.

- `INSTANCE_TYPE`: O tipo de instância que você deseja criar. Por exemplo, `t2.micro`.

- `KEY_NAME`: O nome da chave SSH que você usará para se conectar à instância. Por exemplo, `my-key-pair`.

- `SUBNET_ID`: O ID da sub-rede em que você deseja que a instância seja criada. Por exemplo, `subnet-0bb1c79de3EXAMPLE`.

## Conclusão
Este projeto é uma maneira fácil de criar instâncias EC2 na AWS usando Python. Ele automatiza o processo de criação de instâncias e ajuda a reduzir a carga de trabalho manual. Com as configurações corretas, você pode executar a função Lambda sempre que precisar criar uma nova instância EC2.