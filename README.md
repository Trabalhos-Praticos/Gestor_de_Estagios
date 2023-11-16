# Gestor_de_Estagios
# **Introdução**
Este é um projeto que pode vir a ajudar muitas escolas que ainda não tenham esta implementação, nada mais é que uma aplicação onde possam ser geridos os estágios dos alunos.
# Indice
- [Framework](#Framework)
     - [Django](#Django)
- [Dependencias](#dependências)
- [API](#API)
# Framework
## Django
   Django é uma framework de desenvolvimento web em Python que facilita a criação de sites e aplicações web. Ele fornece um conjunto de ferramentas e funcionalidades pré-construídas para ajudar o processo de desenvolvimento, incluindo gestão de bases de dados, autenticação de utilizadores e criação de interfaces de administração.
 - **Vantagens**
    - Produtividade: O Django fornece uma série de componentes pré-construídos e funcionalidades comuns, o que acelera o desenvolvimento de aplicações web. Isso permite que os desenvolvedores se concentrem mais na lógica específica da aplicação em vez de reinventar a roda.
      
    - Segurança: O Django possui medidas de segurança integradas para proteger contra vulnerabilidades comuns, como a injeção de SQL, cross-site scripting (XSS) e cross-site request forgery (CSRF). Isso ajuda a desenvolver aplicações mais seguras por padrão.
      
    - Administração automática: O Django inclui uma interface de administração pronta para uso, que permite aos desenvolvedores criar, ler, atualizar e excluir dados da aplicação sem escrever código personalizado. Isso é útil para a administração e manutenção de sistemas.
    
    - Arquitetura baseada em padrões: O Django segue o padrão de arquitetura Modelo-Visão-Template (MVT), que promove a organização limpa do código e a separação de preocupações.
    
    - Documentação abrangente: O Django possui uma documentação extensa e uma comunidade ativa, o que facilita o aprendizado e o suporte contínuo.
    
    - Reutilização de código: O framework encoraja a reutilização de componentes e bibliotecas, economizando tempo e esforço na criação de funcionalidades comuns.
    
    - Escalabilidade: O Django é escalável e pode ser usado para criar aplicações pequenas ou grandes. É utilizado por muitos sites e serviços populares, demonstrando sua capacidade de escala.
    
    - Comunidade ativa: Há uma comunidade de desenvolvedores ativos e uma ampla variedade de pacotes de terceiros disponíveis, facilitando a extensão e personalização de aplicações.
    
    - Flexibilidade: Embora siga convenções, o Django permite a personalização, permitindo que os desenvolvedores adaptem o framework às necessidades específicas de seus projetos.
    
    - Gratuito e de código aberto: O Django é de código aberto e gratuito, tornando-o uma escolha económica para muitos projetos.

# Api
APIs são regras que permitem que programas diferentes comuniquem e partilhem informações de forma padronizada, facilitando a integração entre aplicações e a partilha de dados.
# Firebase

# Dependências
## Node.js
**Node.js** é um ambiente de execução de código JavaScript no lado do servidor, construído no motor V8 do Google Chrome. Permite executar JavaScript no servidor, oferecendo uma maneira eficiente de criar aplicativos da web escaláveis e em tempo real.

## Principais Características

1. **JavaScript no Lado do Servidor:** O Node.js permite usar JavaScript no servidor, unificando o desenvolvimento da linguagem em todo o aplicativo, desde o front-end até o back-end.

2. **Assíncrono e Orientado a Eventos:** O Node.js é projetado para ser não bloqueante e assíncrono. Utiliza um modelo de E/S não bloqueante e é orientado a eventos, o que o torna eficiente para operações intensivas de I/O.

3. **Desempenho Rápido:** O motor V8 do Google Chrome é altamente otimizado para executar JavaScript de maneira eficiente, proporcionando um desempenho rápido ao Node.js, especialmente em aplicativos que exigem manipulação rápida de eventos em tempo real.

4. **Módulos e Pacotes:** O Node.js segue o modelo CommonJS para modularização, permitindo dividir o código em módulos reutilizáveis. O npm (Node Package Manager) é um sistema de gerenciamento de pacotes que facilita a instalação e distribuição de bibliotecas e ferramentas adicionais.

5. **Comunidade Ativa:** O Node.js possui uma comunidade grande e ativa, com uma ampla variedade de módulos disponíveis no repositório npm. Isso facilita a construção de aplicativos poderosos usando bibliotecas prontamente disponíveis.

6. **Suporte para Programação em Tempo Real:** O Node.js é amplamente utilizado para aplicativos que requerem comunicação em tempo real, como chat em tempo real, jogos online, colaboração em documentos, entre outros.

O Node.js é uma escolha popular para desenvolvedores que desejam usar JavaScript para construir aplicativos escaláveis e eficientes no lado do servidor. Ele tem sido bem-sucedido em diversos casos de uso, desde APIs RESTful até aplicativos da web em tempo real.

## Instalação

### Linux
1. deixar o teminal em  modo sudo:
```bash
sudo su
```
2. Dar update aos pacotes linux
```bash
apt-get update
```
3. Instalar o node.js e o npm
```bash
apt-get install nodejs npm
```
### Windows
#### Passo 1: Baixar o Instalador

- Acesse o site oficial do Node.js em [nodejs.org](https://nodejs.org/).
- Clique em "Downloads" no menu superior.

#### Passo 2: Escolher a Versão LTS (Recomendado)

- Na página de downloads, é recomendável escolher a versão LTS (Long Term Support) para obter uma versão estável e suportada a longo prazo. Clique no botão "LTS" para baixar a versão recomendada.

#### Passo 3: Baixar o Instalador do Node.js

- Após selecionar a versão LTS, o download do instalador começará automaticamente. Espere o download ser concluído.

### Passo 4: Executar o Instalador

- Após o download, execute o arquivo do instalador (normalmente um arquivo `.msi`, como `node-v14.x.x-x64.msi`). Dê um clique duplo para iniciar a instalação.

#### Passo 5: Configurar o Instalador

- Na janela de instalação, clique em "Next" (Próximo).
- Aceite os termos do contrato de licença e clique em "Next" novamente.
- Escolha o diretório de instalação ou deixe o padrão e clique em "Next".
- Selecione os recursos adicionais, se necessário, e clique em "Next".
- Clique em "Install" para iniciar o processo de instalação.

#### Passo 6: Aguardar a Instalação

- Aguarde enquanto o instalador do Node.js configura o Node.js e o npm (gerenciador de pacotes do Node.js) no seu sistema.

#### Passo 7: Verificar a Instalação

- Após a instalação, abra o Prompt de Comando (cmd) ou o PowerShell.
- Digite os seguintes comandos para verificar se o Node.js e o npm foram instalados corretamente:

  ```bash
  node --version
  npm --version

## Python

**Python** é uma linguagem de programação de alto nível, interpretada, orientada a objetos e de propósito geral. Criada por Guido van Rossum e lançada pela primeira vez em 1991, Python destaca-se pela sua simplicidade e legibilidade de código.

## Características Principais

1. **Sintaxe Simples e Clara:** A sintaxe de Python é projetada para ser fácil de ler e escrever, enfatizando a legibilidade do código.

2. **Multiplataforma:** Python é compatível com várias plataformas, incluindo Windows, macOS e Linux, tornando-o altamente portátil.

3. **Ampla Biblioteca Padrão:** Python possui uma biblioteca padrão extensa, fornecendo módulos e pacotes para realizar diversas tarefas, desde manipulação de arquivos até desenvolvimento web.

4. **Interpretada e Compilada Just-In-Time:** Python é uma linguagem interpretada, mas utiliza compilação just-in-time para melhorar o desempenho em tempo de execução.

5. **Comunidade Ativa:** A comunidade Python é vasta e ativa, com suporte e contribuições contínuas. O gerenciador de pacotes `pip` facilita a instalação e compartilhamento de bibliotecas.

6. **Versatilidade:** Python é utilizado em diversas áreas, incluindo desenvolvimento web, automação, ciência de dados, inteligência artificial, aprendizado de máquina, entre outras.

## Exemplo Simples

Aqui está um exemplo simples de código Python que imprime "Olá, Mundo!":

```python
print("Olá, mundo)
```
## Linux
#### Passo 1: Verificar a Versão do Python Pré-instalada
Abre um terminal e verifica se o Python já está instalado e a sua versão com o comando:
  ```bash
  python --version
  ```
  ou
  ```bash
  python3 --version
  ```
  Se o Python já estiver instalado, o comando mostrará a versão. Caso contrário, continua para o próximo passo.

#### Passo 2: Atualizar o Gestor de Pacotes
Antes de instalar o Python, é sempre uma boa prática atualizar o gestor de pacotes do teu sistema. Utiliza o seguinte comando, dependendo do teu sistema:

Para sistemas baseados no Debian (Ubuntu, Debian, etc.):
```bash
sudo apt-get update
```
Para sistemas baseados no Red Hat (Fedora, CentOS, etc.):
```bash
sudo yum update
```
#### Passo 3: Instalar o Python
Agora podes instalar o Python utilizando o gestor de pacotes do teu sistema. Utiliza os comandos apropriados conforme o teu sistema:

Para sistemas baseados no Debian:
```bash
sudo apt-get install python3
```
Para sistemas baseados no Red Hat:
```bash
sudo yum install python3
```
#### Passo 4: Verificar a Instalação
Depois de instalado, verifica a versão do Python utilizando:
```bash
python3 --version
```
Se a instalação foi bem-sucedida, deverá mostrar a versão do Python.

Lembra-te de que, em alguns sistemas, o comando python pode ser usado em vez de python3. Certifica-te de ajustar conforme necessário.

## Windows
#### Passo 1: Descarregar o Python

- Visita o site oficial do Python em [python.org](https://www.python.org/).
- Clica em "Downloads" no menu superior.

#### Passo 2: Descarregar o Instalador

- Desce até à secção "Looking for a specific release?" e escolhe a versão desejada.
- Clica no link para descarregar o instalador (normalmente um ficheiro `.exe`, como `python-3.x.x.exe`).

#### Passo 3: Executar o Instalador

- Após o download, executa o ficheiro `.exe` que descarregaste.

#### Passo 4: Configurar o Instalador

- Na janela de instalação, assinala a opção "Add Python to PATH" (Adicionar Python ao PATH).
- Clica em "Install Now" (Instalar Agora).

#### Passo 5: Aguardar a Instalação

- Aguarda enquanto o instalador configura o Python no teu sistema.

#### Passo 6: Verificar a Instalação

- Abre o Prompt de Comando (cmd) ou o PowerShell.
- Digita `python --version` ou `python -V` e pressiona Enter. Deve mostrar a versão do Python instalada.

#### Passo 7: Instalação Bem-Sucedida

- Se vires a versão do Python, a instalação foi bem-sucedida.
