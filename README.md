O objetivo dessa integração foi consolidar as informações das três bases de dados da empresa em um arquivo só, corrigindo falhas de preenchimento e inconsistências sistêmicas para permitir análises mais precisas.

Os passos foram:
1. Separação e Estruturação dos Arquivos
- Foi identificado que as planilhas continham os dados salvos em uma única coluna com valores separados por vírgulas, dificultando a leitura direta.
- Com isso, os dados foram desmembrados em colunas individuais e os nomes dos campos foram padronizados, organizando a tabela no formato tradicional.

2. Limpeza e Normalização dos Dados
- Campos com quantidades e valores foram convertidos para números reais, permitindo cálculos.
- As colunas de datas foram ajustadas para um formato padrão, evitando erros de interpretação entre dia e mês.
- Os números apresentavam diferentes formas de preenchimento. Foram mantidos apenas os números válidos para facilitar contato e busca.

3. Tratamento de Duplicidades Sistêmicas
- Clientes repetidos estavam sendo cadastrados com múltiplos identificadores (ID_Cliente), inflando artificialmente o tamanho da base.
- Com isso Realizou-se uma verificação por nome, e-mail e data de nascimento, mantendo apenas o registro mais completo de cada cliente e eliminando as repetições desnecessárias.

4. Integração das Bases (Visão Única do Negócio)
- Os dados foram cruzados horizontalmente para que cada pedido mostre, lado a lado, os detalhes da compra, a navegação no site e as informações de quem comprou:
Pedidos + Sessões: Vinculados pelo código da sessão de navegação (ID_Sessao).
Sessões + Clientes: Vinculados pelo nome do cliente.

Resultado: Uma base única e limpa.